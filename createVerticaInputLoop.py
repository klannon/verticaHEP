#!/usr/bin/env python

import ROOT
import os
ROOT.gSystem.Load('CMSSW_7_6_3/lib/slc6_amd64_gcc493/libttH-13TeVMultiLeptonsTemplateMakers.so')


fLep = open('lep.txt', 'w')
fJet = open('jet.txt', 'w')
fEvent = open('event.txt','w')

fLep.write('Run | Lumi | Event | Pt | Eta | Phi | Charge\n')
fJet.write('Run | Lumi | Event | Pt | Eta | Phi\n')
fEvent.write('Run | Lumi | Event\n')

inFile = ROOT.TFile.Open('ttH_forKevin.root')
inTree = inFile.Get('OSTwoLepAna/summaryTree')


for entry in inTree:
   #print('work')
   fEvent.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '\n' )

   for lep in entry.preselected_leptons:
	fLep.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + str(lep.obj.Pt()) + '|' + str(lep.obj.Eta()) + '|' + str(lep.obj.Phi()) + '|' + str(lep.charge) + '\n' )

   for jet in entry.preselected_jets:
	fJet.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + str(jet.obj.Pt()) + '|' + str(jet.obj.Eta()) + '|' + str(jet.obj.Phi()) + '|' + str(jet.charge) + '\n')

fLep.close()
fJet.close()
fEvent.close()
	

