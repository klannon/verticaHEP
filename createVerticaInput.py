#!/usr/bin/env python

import ROOT
import time
import os
ROOT.gSystem.Load('CMSSW_7_6_3/lib/slc6_amd64_gcc493/libttH-13TeVMultiLeptonsTemplateMakers.so')

'''
#inFile = ROOT.TFile.Open('ttH_flat.root')
inFile = ROOT.TFile.Open('ttH_forKevin.root')
#inTree = inFile.Get('flatTree')
inTree = inFile.Get('OSTwoLepAna/summaryTree')
'''

numFiles = 0

ch_ttJetT = ROOT.TChain('OSTwoLepAna/summaryTree')
for rootFile in os.listdir('/hadoop/users/klannon/ttHTrees/TTJets_split_1lepFromT/'):
   if numFiles == 2:
	break
   ch_ttJetT.Add('/hadoop/users/klannon/ttHTrees/TTJets_split_1lepFromT/'+rootFile)
   numFiles += 1

ch_ttJetT.GetPlayer().SetScanRedirect(ROOT.kTRUE)
ch_ttJetT.GetPlayer().SetScanFileName('flatOutput1.txt')
startScan = time.time()
ch_ttJetT.Scan("runNumber:lumiBlock:eventnum:preselected_leptons.obj.Pt():preselected_leptons.obj.Eta():preselected_leptons.obj.Phi()","","colsize=30")
scanTime = time.time() - startScan

'''
inTree.GetPlayer().SetScanRedirect(ROOT.kTRUE)
inTree.GetPlayer().SetScanFileName('flatOutput1.txt')
inTree.Scan("preselected_leptons.obj.Pt():preselected_leptons.obj.Eta()", "","colsize=30")
'''

f = open('flatOutput1.txt','r')
f2 = open('verticaInputTest.txt','w')
#temp = f.read()
lineCount = 0
'''
f.next()
temp = f.readline()
temp.replace('*','|')
f2.write(temp)
f.next()
temp = f.read()
temp.replace('*','|')
f2.write(temp)
'''

'''
with open('flatOutput1.txt') as fp:
   for i, line in enumerate(fp):
	if i == 0 or 2:
	   temp = line.replace('*','|')
	   f2.write(temp)
'''

'''
for line in f:
 
   if lineCount == 1:
	f.next()
   temp = line.replace('*','|')
   f2.write(temp)
   
   #temp = line.replace('*','|')
   #f2.write(temp)
   lineCount += 1

'''

for line in f:
   ''' 
   if lineCount == 1:
      #temp = line.replace('*','|')
      #f2.write(temp)
      header = line.split()
      for word in header:
         if word.endswith(".Pt()"):
            word = 'Pt'
      header.reverse()   
      line = "".join(header)
   '''
   if lineCount != 0:
      #temp = line.replace('*','|')
      if lineCount == 1:
        string = []
	header = line.split()
	for word in header:
           if word.endswith(".Pt()"):
              word = 'Pt'
	   if word.endswith(".Eta()"):
	      word = 'Eta'
           if word.endswith(".Phi()"):
	      word = 'Phi'
           string.append(word)
        line = "".join(string)
	line = line +'\n'
      temp = line.replace('*','|')      
      f2.write(temp)
   if lineCount == 1:
      #temp = line.replace('*','|')
      #f2.write(temp)
      f.next()      
   
   #temp = line.replace('*','|')
   #f2.write(temp)
   lineCount += 1

totalTime = time.time() - startScan
#verticaInput = temp.replace('*','|')
#f.write('verticaInput2.txt','w')

#f2.write(verticaInput)
f.close()
f2.close()

print('Scan time: {}\nTotal: {}'.format(scanTime, totalTime) )
