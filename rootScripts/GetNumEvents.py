#!/usr/bin/env python

import os
import ROOT
ROOT.gSystem.Load('CMSSW_7_6_3/lib/slc6_amd64_gcc493/libttH-13TeVMultiLeptonsTemplateMakers.so')

ttH_nevents = 0
ttJetT_nevents = 0
ttJetTBar_nevents = 0

#chain for ttH
ch_ttH = ROOT.TChain('OSTwoLepAna/summaryTree')
for rootFile in os.listdir('/hadoop/users/klannon/ttHTrees/ttH125powheg/'):
   tempFile = ROOT.TFile('/hadoop/users/klannon/ttHTrees/ttH125powheg/'+rootFile)
   h1 = tempFile.Get('OSTwoLepAna/numInitialWeightedMCevents')
   ttH_nevents += h1.Integral()


#chain for lep from T
ch_ttJetT = ROOT.TChain('OSTwoLepAna/summaryTree')
for rootFile in os.listdir('/hadoop/users/klannon/ttHTrees/TTJets_split_1lepFromT'):
   tempFile = ROOT.TFile('/hadoop/users/klannon/ttHTrees/TTJets_split_1lepFromT/'+rootFile)
   h2 = tempFile.Get('OSTwoLepAna/numInitialWeightedMCevents')
   ttJetT_nevents += h2.Integral()
   
#chain for lep from TBar
ch_ttJetTBar = ROOT.TChain('OSTwoLepAna/summaryTree')
for rootFile in os.listdir('/hadoop/users/klannon/ttHTrees/TTJets_split_1lepFromTBar'):
   if rootFile != '50.root':
      tempFile = ROOT.TFile('/hadoop/users/klannon/ttHTrees/TTJets_split_1lepFromTBar/'+rootFile)
      h3 = tempFile.Get('OSTwoLepAna/numInitialWeightedMCevents')
      ttJetTBar_nevents += h3.Integral()

print('ttH Events: {}'.format(ttH_nevents))
print('ttJetT Events: {}'.format(ttJetT_nevents))
print('ttJetTBar Events: {}'.format(ttJetTBar_nevents))
   

