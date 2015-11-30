'''
Created on Nov 19, 2015

@author: camilo
'''

from __future__ import division


from satisfiable import SatFor
from fol2tptp.wrapper import makeWrapper
from fol2tptp.lextab import *
from fol2tptp.parsetab import *


# test if MRs are satisfiable
class TestSAT(object):
    '''
    classdocs
    '''

    #constructor
    def __init__(self, path):
        '''
        Constructor
        '''
        sat = SatFor()
        self.returnStatus(path,sat)
    
        
    # check for satisfiability
    def returnStatus(self,path,sat):
        fol = open(path, 'r')
        count = 0
        consistent = 0
        fail = 0
        for line in fol:
            #print line
            form = makeWrapper(line,"axiom")
            if form != "":
                count = count + 1 
                file = open('/home/camilo/boxer-parses/temp-for.fol','w')
                file.write(form)
                file.close()
                if sat.isSATSpass('/home/camilo/boxer-parses/temp-for.fol'):
                    #print "satisfiable"
                    consistent = consistent + 1 
                else:
                    print "unsatisfiable"
            else:
                print line
                print "wrapper error"
                fail = fail + 1
        print "sat = ", consistent
        print "tot = ", count
        print "fail = ", fail        
        print "sat ratio = ", consistent/count
            
#run class
TestSAT("/home/camilo/nlp-corpora/wacky-corpus/wacky-simple/wacky-post.fol") 
             