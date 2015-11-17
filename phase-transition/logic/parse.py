'''
Created on Nov 14, 2014
@author: camilo
'''

#===================#
#===================#
#
# Class likelihoods
#   (ENG + DEU)
#
#===================#
#===================#


# python
from __future__ import division
from operator import attrgetter
#from math import ceil


# my plotting + test classes
from corpuspkg.statsplot import MyPlot
from corpuspkg.statstests import STest


# nltk
from nltk.corpus import PlaintextCorpusReader


# my classes
#from proporclasses import MyClass2, MyPatts2, MyClassStats2
#from savestats import SaveStats
from sentence import *


####################################################################
#################################################################### 

s0 = ".*"        # anything!

####################################################################
####################################################################
# A. simple classes
####################################################################
####################################################################

# # exists
# 
# s10 = " someone/nn"
# s12 = " somebody/nn"
# s12a = " anybody/nn"
# s14 = " something/nn"
# s16 = " some/dt"
# s18 = " a/dt"
# s20 = " many/dt "
# s21 = " many/jj */nns"
# s22 = " there/ex"
# 
# ds10 = " pis/jemand "
# ds14 = " pis/etwas "
# ds15 = " piat/etwas "
# ds16 = " ne/irgendetwas "
# ds17 = " art/ein "
# ds18 = " pper/es vvfnn/gibt "
# ds20 = " pis/manch "
# ds21 = " piat/manch "
# ds22 = " piat/viel "
# 
# some = [s10,s12,s12a,s14,s16,s18,s20,s21,s22,
#         ds10,ds14,ds15,ds16,ds17,ds18,ds20,ds21,ds22]
# 
# ####################################################################
# 
# # all
# 
# s40 = " every/dt "
# s42 = " all/dt "
# s44 = " the/dt .*/nns "
# s46 = " everything/nn "
# s48 = " everyone/nn " 
# s4a = " everybody/nn " 
# s4c = " each/dt "
# s4e = " no/dt "
# 
# ds40 = " piat/alle "
# ds41 = " pis/alle "
# ds42 = " piat/kein "
# ds46 = " piat/jed "
# 
# all = [s40,s42,s44,s46,s48,s4a,s4c,s4e,
#        ds40,ds41,ds42,ds46]
# 
# ####################################################################
# 
# # exactly one
# 
# s74 = " the/dt "
# 
# ds74 = " art/d "
# 
# the = [s74,
#        ds74]
# 
# ####################################################################
# ####################################################################
# 
# # at most k, less than k (k integer)
# 
# s60 = " at/in most/jjs .*/cd "
# s20b = " less/jjr than/in .*/cd "
# s20bb = " fewer/jjr than/in .*/at .*/cd "
# s22b = " less/jjr than/in .*/at .*/cd "
# s22bb = " fewer/jjr than/in .*/at .*/cd "
# 
# ds60 = " adv/h\p{L}chstens card/@card@ "
# ds20b = " piat/weniger kokom/als card/@card@ "
# 
# lessk = [s20b,s22b,s20bb,s22bb,
#          ds60,ds20b]
# 
# ####################################################################
# 
# # at least k, more than k (k integer)
# 
# s60b = " at/in least/jjs .*/cd "
# s20 = " more/jjr than/in .*/cd "
# s22 = " more/jjr than/in .*/at .*/cd "
# 
# ds60b = " adv/mindestens card/@card@ "
# ds20 = " piat/mehr kokom/als card/@card@ "
# 
# morek = [s20,s22,s60b,
#          ds60b,ds20]
# 
# ####################################################################
# 
# # exactly k (k integer)
# 
# s70 = " .*/cd .*/nns "
# s71 = " exactly/rb .*/cd "
# 
# ds70 = " card/@card@ nn/.* "
# 
# exactlyk = [s70,s71,
#             ds70]
# 
# ####################################################################
# ####################################################################
# 
# # more than p/k (p, k integers)
# 
# s80 = " more/ap than/in half/abn "
# s82 = " more/ap than/in .*/cd of/in "
# 
# ds80 = " piat/mehr kokom/als adjd/halb "
# ds82 = " appr/\p{L}ber adjd/halb "
# ds80a = " piat/mehr kokom/als card/@card@ appr/von"
# ds82a = " appr/\p{L}ber card/@card@ appr/von "
# 
# morethanpro = [s80,s82,
#                ds80,ds82,ds80a,ds82a]
# 
# ####################################################################
# 
# # less than p/k (p, k integers)
# 
# s80b = " less/jjr than/in half/nn "
# s80bb = " fewer/jjr than/in half/nn "
# s82b = " less/jjr than/in .*/cd of/in "
# s82bb = " fewer/jjr than/in .*/cd of/in "
# 
# ds80b = " piat/weniger kokom/als adjd/halb "
# ds80bb = " piat/weniger kokom/als card/@card@ appr/von "
# ds80bbb = " appr/unter card/@card@ appr/von "
# ds80bbbb = " appr/unter adjd/halb "
# 
# lessthanpro = [s80b,s80bb,s82b,s82bb,
#                ds80b,ds80bb,ds80bbb,ds80bbbb]
# 
# ####################################################################
# 
# # p/k (p, k integers)
# 
# s80c = " half/dt "
# s80d = " half/pdt "
# s80c = " half/nn of/in"
# s81c = " .*/nns of/in "
# s81d = " .*/nn of/in "
# 
# ds80c = " adja/halb "
# ds80d = " adja/halb appr/von "
# ds80e = " card/@card@ appr/von "
# 
# pro = [s80c,s80d,
#        ds80c,ds80d,ds80e]
# 
# ####################################################################
# 
# # more than k% (k a percentage)
# 
# s30 = " more/jjr than/in .*/cd percent/nn "
# s30a = " more/jjr than/in %/cd "
# 
# ds30 = " appr/uber card/@card@ nn/%"
# ds30a = " piat/mehr kokom/als card/@card@ nn/% "
# 
# morekper = [s30,s30a,
#             ds30,ds30a]
# 
# ####################################################################
# 
# # less than k% (k a percentage)
# 
# s30b = " less/jjr than/in .*/cd percent/nn "
# s30bb = " less/jjr than/in %/cd "
# 
# ds30b = " appr/unter card/@card@ nn/%"
# ds30bb = " piat/weniger kokom/als card/@card@ nn/% "
# 
# lesskper = [s30b,s30bb,
#             ds30b,ds30bb]
# 
# ####################################################################
# 
# # k% (k a percentage)
# 
# s30c = " ./cd percent/nn "
# s30d = " %/cd "
# 
# ds30d = " nn/% "
# 
# kper = [s30c,s30d,ds30d,
#         ds30d]
# 
# ####################################################################
# 
# # most, more than half
# 
# s51 = " most/jjs "
# s51a = " most/dt "
# s53 = " more/jjr than/in half/nn "
# 
# ds51 = " adv/fast piat/jed "
# ds51a = " piat/mehr kokom/als adjd/halb "
# ds53 = " appr/\p{L}ber adjd/halb "
# 
# most = [s51,s51a,s53,
#         ds51,ds51a,ds53]
# 
# ####################################################################
# 
# # few, less than half, fewer than half
# 
# s51b = " few/jj "
# s51bb = " few/dt "
# s53b = " less/jj than/in half/nn "
# s53bb = " fewer/jj than/in half/nn "
# 
# ds51b = " piat/wenig "
# ds53b = " piat/wenig kokom/als adjd/halb "
# ds53bb = " appr/unter adjd/halb "
# 
# few = [s51b,s51bb,s53b,s53bb,
#        ds51b,ds53b,ds53bb]


####################################################################
####################################################################


# Class encoding the plot(s) + test(s)


class ProporStatsF:
   
    
    # corpus            : path to corpora
    # format            : format of corpora (e.g. .txt files)
    # stats             : hash table with class stats of each corpus
    # classstats        : list with global stats (mean frequency) 
    # list              : list of legends in figure
    # plotting          : directory of compiled report

    
    # object constructor
    def __init__(self,path,myformat,mylist,plotting):
        self.stats = {} # stats
        self.classstats = [] # classes
        self.path = path # path of corpus
        self.format = myformat # format of file(s)
        self.list = mylist        
        #self.occStats(path,myformat,self.list,plotting) # collects stats + plots them
        self.statTestB(self.classstats) # runs the stat tests
        self.plotting = plotting    

    
    #############################################################
    #############################################################
        
    
    # collecting statistics
    def occStats(self,path,format,list,plotting):
        wordlists = PlaintextCorpusReader(path,format)
        fileids = wordlists.fileids()
        k = len(fileids)
        
        # computing rel frequencies
        self.fileStats(path,fileids)
        
        
    #############################################################
    #############################################################        
 
            
    # creating the classes
    def fileStats(self,path,fileids):  
        
        print "###################################################"
        print "Phase stats"
        print "###################################################"
        
        # computing the stats
        for idf in fileids:
                        
            ####################################################################
            
            filestats = []
            mydata = OpenFile(path+'/'+idf)
            mydata.lines = mydata.myread()
            
            ####################################################################
            
            print "==================================================="
            print idf
            print "==================================================="
                        
            ####################################################################  
            ####################################################################            
            
            # examine only k chunks of the big file at a time
            while mydata.lines:
                
                i = 0
                my_max = len(mydata.lines)
                
                # loop over chunk
                while i  <  my_max:
            
                    # parse the chunk
                    lines = mydata.lines
                    line = mydata.lines[i]
                    
                    # build sentence            
                    sen = MySen()
                    sen.buildSen(i,lines,my_max)
                
                    # if sentence built, apply patterns       
                    if sen.end == True:
                        
                        # retrieve POS tagged sentence
                        myline = sen.sen   
                    
                    # if a sentence is found, skip the lines it
                    # covers in the loop, otherwise move to the
                    # next line
                    if sen.len > 0:
                        i = i + sen.len
                        print 'senlen=', sen.len, '\n'
                        print 'sen= ', sen.sen, '\n'
                    else:    
                        i = i + 1
                    print 'explore at line= ', i, '\n'
                
                # move to new chunk
                mydata.lines = mydata.myread()
            
            ####################################################################
            ####################################################################
            
            self.stats[idf] = filestats
            
            ####################################################################  
            
            for cla in self.classstats:
                for thiscls in filestats:
                    if (thiscls.tag == cla.tag):
                        cla.classes.append(thiscls)

            ####################################################################  
                                
        # updating the distribution 
        self.classAvg(self.classstats)
        self.classAvg2(self.classstats)
        sort = self.sortClass(self.classstats)
        self.classstats = sort
        print "###################################################"
        #self.printClasses(self.classstats)
    

    ############################################################# 
    #############################################################     
        
                
    # sorts stats classes
    def sortClass(self,classlist):
        sort = sorted(classlist,key=attrgetter('avg'))
        return sort
    
    
    #############################################################
    #############################################################
    

    def testSAT(self,sentence):
        return ""


    #############################################################
    #############################################################

        
    # prints the stats
    def printClasses(self,classstats):
        for cla in classstats:
            print cla.tag
            print "---------------------------------------------------"            
            print `cla.avg` + ": avg rel. freq"
            print "---------------------------------------------------"
            for idf in cla.classes:
                print `idf.freq` + ": rel. freq "+ idf.fileid
                print `idf.count` + ": freq "+ idf.fileid              
            print "###################################################"


    #############################################################
    #############################################################

        
    # statistical tests
    def statTestB(self,classstats):
        
        s = STest()
           
        # simple samples:   
             
        # freqs (cross corpus, per corpus)     
        sample1 = [] 
        for cla in classstats:
            sample1.append(sum([cl.count for cl in cla.classes]))
                                
        # rel. freqs (cross-corpus, per class)
        sample2 = []
        for cla in classstats:
            sample2.append(round(cla.avg,2))                
            
        # simple stats methods
        print "###################################################"        
        print "Simple statistical tests:"
        print "---------------------------------------------------"
        print "sam1 = ", sample1,"(GQ freqs per class)"
        print "sam2 = ", sample2,"(GQ rel freqs per class)"  
        ##########################################################
        s.mySkew(sample1)                       # skewness     
        s.myEntropy(sample2)                    # entropy
        s.myChiTest(sample1,s.uniFor(sample1))  # X^2 test   

