#!/usr/bin/env python

import math

import ROOT
ROOT.gSystem.Load('CMSSW_7_6_3/lib/slc6_amd64_gcc493/libttH-13TeVMultiLeptonsTemplateMakers.so')

signalFile = ROOT.TFile.Open('ttH_forKevin.root')
signalTree = signalFile.Get('OSTwoLepAna/summaryTree')

jetCosPhi = ROOT.TH1F('jetCosPhi','CosPhi - ROOT',100,-2,2)
jets2Pt40 = ROOT.TH1F('jets2Pt40', 'nJets >=2 Pt>40 - ROOT',100,0,200)
events = ROOT.TH1F('events', 'nJets >=2 Pt>40',100,0,1000)

numEnt = 0
for entry in signalTree:
       
    # Fill jet plots
    nJet = 0
    nJet50 = 0
    cosPhi = 1
    jetsPt40 = 0
    for jet in entry.preselected_jets:
	cosPhi = math.cos(jet.obj.Phi()) * cosPhi
	if jet.obj.Pt() > 40:
	   jetsPt40 += 1

    if jetsPt40 >= 2:
	
	for jet in entry.preselected_jets:
	   jets2Pt40.Fill(jet.obj.Pt())
    
    if entry.preselected_jets.size() != 0:   
    	jetCosPhi.Fill(cosPhi)
    	numEnt += 1

print(str(numEnt))
	

	

	

    
        
   





outfile = ROOT.TFile.Open('evtLoop_verticaTest_output.root','RECREATE')
outfile.cd()

#write the signals

jets2Pt40.Write()
jetCosPhi.Write()

outfile.Close()


