#!/usr/bin/env python

import ROOT
import time
import os
#ROOT.gSystem.Load('../CMSSW_7_6_3/lib/slc6_amd64_gcc493/libttH-13TeVMultiLeptonsTemplateMakers.so')

startTime = time.time()

ch_all = ROOT.TChain('OSTwoLepAna/summaryTree')
for rootFile in os.listdir('/data3/tth'):
   if rootFile != 'dummy.txt':
      ch_all.Add('/data3/tth/'+rootFile)
      #print(rootFile)

for rootFile in os.listdir('/data3/ttjet'):
   #if os.path.getsize('/hadoop/store/user/lannon/bdtreco_v0/ttjets_semilep/'+rootFile) > 1000000000:
   ch_all.Add('/hadoop/store/user/lannon/bdtreco_v0/ttjets_semilep/'+rootFile)
   #print(rootFile)

chainTime = time.time() - startTime
startLoop = time.time()
numEntries = 0
numMu = 0
numElec = 0

for entry in ch_all:
   
   for muon in entry.preselected_muons:
      if muon.validFrac >= 0.8 and muon.lepMVA > 0.75:
         if muon.isGlobalMuon and muon.normalizedChi2 < 3 and muon.localChi2 < 12 and muon.trKink < 20:
	    segCom = 0.303
	 else:
	    segCom = 0.451
         if muon.segCompatibility > segCom:
	    numMu += 1
	    numEntries += 1

   for elec in entry.preselected_electrons:
      if elec.lepMVA > 0.75: #and elec.numMissingInnerHits == 0 and elec.passConversioVeto:
	 numElec += 1
         numEntries += 1

loopTime = time.time() - startLoop
totalTime = time.time() - startTime

print('numEntries: {}'.format(numEntries))

print('numEntries: {}\nChain time: {}\nLoop time: {}\ntotal time: {}'.format(numEntries, chainTime, loopTime, totalTime))
#verticaInput = temp.replace('*','|')
#f.write('verticaInput2.txt','w')




