'''
Created on Nov 17, 2015
@author: Camilo Thorne
'''


from boxer.fol2tptp import *
from subprocess import call


# class
class SatFor(object):


    # constructor
    def __init__(self):
        
        # start boxer server
        call(["soap_server", "--models /home/camilo/nlp-frameworks/models-boxer/boxer", 
              "--server localhost:9000", "--candc-printer boxer"], 
             shell=True)
       
       
    # return MR in NNF
    def returnFOL(self, sentence):
        
        fol = ""
        
        call(["echo", "'"+sentence+"'", "| soap_client", 
              "--url localhost:9000", "> /home/camilo/boxer-parses/wacky.ccg"
              ])
        
        call(["boxer", "--input /home/camilo/boxer-parses/wacky.ccg",
              "--semantics fol", "> /home/camilo/boxer-parses/wacky.fol"])
         
        return fol
    
    
    # check for proof/refutation using bliksem
    def isSATBlik(self,path):
        file = open(path)
        if "found a saturation!" not in file:
            return False
        else:
            return True
        
        
    # check for proof/refutation using SPASS
    def isSATSpass(self,path):
        file = open(path)
        if "proof found!" not in file:
            return False
        else:
            return True        
          