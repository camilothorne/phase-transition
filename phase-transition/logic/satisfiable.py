'''
Created on Nov 17, 2015
@author: Camilo Thorne
'''

# custom libraries
import sys
sys.path.append(u'../../../boxer-nnf/')


from fol2tptp.wrapper import *
from subprocess import call


# class
class SatFor(object):


    # constructor
    def __init__(self):
        
        # start boxer server
        call("soap_server --models /home/camilo/nlp-frameworks/models-boxer/boxer " + 
               "--server localhost:9000 --candc-printer boxer",
               shell=True)
       
       
    # return MR in Boxer format
    def returnFOL(self, sentence):
        fol = ""
        call("echo '" + sentence + "' | soap_client " + 
              "--url localhost:9000 > /home/camilo/boxer-parses/wacky.ccg",
              shell=True)
        call("boxer --input /home/camilo/boxer-parses/wacky.ccg " +
              "--semantics fol > /home/camilo/boxer-parses/wacky.fol",
              shell=True)
        file.open("/home/camilo/boxer-parses/wacky.fol", 'r')
        for line in file:
            if line.startswith('fol'):
                fol = line
        return fol
    
    
    # check for proof/refutation using bliksem
    def isSATBlik(self,path):
        call("bliksem " + path + 
              " > /home/camilo/boxer-parses/temp-proof.blik",
              shell=True)
        file = open("/home/camilo/boxer-parses/temp-proof.blik", 'r')          
        if "found a saturation!" not in file:
            file.close()
            return False
        else:
            file.close()
            return True
        
        
    # check for proof/refutation using SPASS
    def isSATSpass(self,path):        
        call("SPASS -TPTP " + path + 
              " > /home/camilo/boxer-parses/temp-proof.spass",
              shell=True)
        file = open("/home/camilo/boxer-parses/temp-proof.spass", 'r')        
        if "Proof found." in file:
            file.close()
            return False
        else:
            file.close()
            return True        
          