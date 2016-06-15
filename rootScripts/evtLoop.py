#!/usr/bin/env python

#include "Rtypes.h"
#include "TColor.h"

import ROOT
ROOT.gSystem.Load('CMSSW_7_6_3/lib/slc6_amd64_gcc493/libttH-13TeVMultiLeptonsTemplateMakers.so')

signalFile = ROOT.TFile.Open('ttH_forKevin.root')
signalTree = signalFile.Get('OSTwoLepAna/summaryTree')

backFile = ROOT.TFile.Open('ttbar_forKevin.root')
backTree = backFile.Get('OSTwoLepAna/summaryTree')

#scale factor
ttbarCross = 182.7
ttHCross = 0.212
luminosity = 2500
nTotSig = 2600389.15887
nTotBack = 25446993.0

scaleFactorH = luminosity*ttHCross/nTotSig
scaleFactorBar = luminosity*ttbarCross/nTotBack

#set color options
backTree.SetFillColor(ROOT.kRed)
signalTree.SetFillColor(ROOT.kBlue)

#set the style
style = ROOT.TStyle('style','style')
style.SetHistFillColor(ROOT.kBlue)
ROOT.gROOT.SetStyle('style')

#add background histograms under signal histogram
#also add THStack hists
lepPtHistSig = ROOT.TH1F('lepPtHistSig','Lepton p_{T}',100,0,200)
lepPtHistBack = ROOT.TH1F('lepPtHistBack','Lepton p_{T} Background',100,0,200)
lepPtStack = ROOT.THStack('lepPtStack','lepton p_{T}')

lepEtaHistSig = ROOT.TH1F('lepEtaHistSig','Lepton #eta',100,-2,2)
lepEtaHistBack = ROOT.TH1F('lepEtaHistBack','Lepton #eta Background',100,-2,2)
lepEtaStack = ROOT.THStack('lepEtaStack', 'Lepton #eta')

nJetsHistSig = ROOT.TH1F('nJetsHistSig','N_{Jets}',10,0,10)
nJetsHistBack = ROOT.TH1F('nJetsHistBack','N_{Jets} back',10,0,10)
nJetsStack = ROOT.THStack('nJetsStack','N_{Jets}')

nJets50HistSig = ROOT.TH1F('nJets50HistSig','N_{Jets}',10,0,10)
nJets50HistBack = ROOT.TH1F('nJets50HistBack','N_{Jets} back',10,0,10)
nJets50Stack = ROOT.THStack('nJets50Stack','N_{Jets}')

#added by Matthew Link
lepPtHistSig2 = ROOT.TH1F('lepPtHistSig2', 'Lepton p_{T}2',100,0,200)
lepPtHistBack2 = ROOT.TH1F('lepPtHistBack2','Lepton p_{T}2',100,0,200)
lepPtStack2 = ROOT.THStack('lepPtStack2', 'Lepton p_{T}2')

lepPxHistSig = ROOT.TH1F('lepPxHistSig', 'Lepton p_{X}', 100,0,200)
lepPxHistBack = ROOT.TH1F('lepPxHistBack','Lepton p_{X}',100,0,200)
lepPxStack = ROOT.THStack('lepPxStack','Lepton p_{X}')

lepRhoHistSig = ROOT.TH1F('lepRhoHistSig', 'Lepton #rho', 100,0,10)
lepRhoHistBack = ROOT.TH1F('lepRhoHistBack', 'Lepton #rho',100,0,10)
lepRhoStack = ROOT.THStack('lepRhoStack', 'Lepton #rho')

jetChargeHistSig = ROOT.TH1F('jetChargeHistSig', 'Jet Charge', 100, -2,2)
jetChargeHistBack = ROOT.TH1F('jetChargeHistBack','Jet Charge',100,-2,2)
jetChargeStack = ROOT.THStack('jetChargeStack', 'Jet Charge')

#have not created stack plots for charge2 or csv
jetChargeHistSig2 = ROOT.TH1F('jetChargeHistSig2', 'Jet Charge Pt>42',100,-2,2)
jetCSVHistSig = ROOT.TH1F('jetCSVHistSig', 'Jet csv',100,-10,2)


for entry in signalTree:

    # Fill the lepton plots
    for lep in entry.preselected_leptons:
        lepPtHistSig.Fill(lep.obj.Pt())
	lepPxHistSig.Fill(lep.obj.Px())
	lepRhoHistSig.Fill(lep.rho)

        if lep.obj.Pt() > 35:
            lepEtaHistSig.Fill(lep.obj.Eta())

	# Not in drawTree. testing more complicate if
        if lep.obj.Px() + lep.obj.Py() > 42:
	    lepPtHistSig2.Fill(lep.obj.Pt())

    # Fill jet plots
    nJet = 0
    nJet50 = 0
    for jet in entry.preselected_jets:

        nJet += 1
        if jet.obj.Pt() > 50:
            nJet50 += 1
	
	jetChargeHistSig.Fill(jet.charge)

	if jet.obj.Pt() > 42:
	    jetChargeHistSig2.Fill(jet.charge)

	jetCSVHistSig.Fill(jet.csv)

    nJetsHistSig.Fill(nJet)
    nJets50HistSig.Fill(nJet50)
        
   
#Fill the background plots
for entry in backTree:

    # Fill the lepton plots
    for lep in entry.preselected_leptons:
        lepPtHistBack.Fill(lep.obj.Pt()) 
	lepPxHistBack.Fill(lep.obj.Px())
	lepRhoHistBack.Fill(lep.rho)

	if lep.obj.Pt() > 35:
            lepEtaHistBack.Fill(lep.obj.Eta()) 
	
	if lep.obj.Px() + lep.obj.Py() > 42:
	    lepPtHistBack2.Fill(lep.obj.Pt())

    # Fill jet plots
    nJet = 0
    nJet50 = 0
    for jet in entry.preselected_jets:

        nJet += 1
        if jet.obj.Pt() > 50:
            nJet50 += 1  

	jetChargeHistBack.Fill(jet.charge)
 
    nJetsHistBack.Fill(nJet)
    nJets50HistBack.Fill(nJet50)

#scale the signals and background
lepPtHistSig.Scale(scaleFactorH)
lepPtHistBack.Scale(scaleFactorBar)

lepEtaHistSig.Scale(scaleFactorH)
lepEtaHistBack.Scale(scaleFactorBar)

nJetsHistSig.Scale(scaleFactorH)
nJetsHistBack.Scale(scaleFactorBar)

nJets50HistSig.Scale(scaleFactorH)
nJets50HistBack.Scale(scaleFactorBar)

lepPtHistSig2.Scale(scaleFactorH)
lepPtHistBack2.Scale(scaleFactorBar)

lepPxHistSig.Scale(scaleFactorH)
lepPxHistBack.Scale(scaleFactorBar)

lepRhoHistSig.Scale(scaleFactorH)
lepRhoHistBack.Scale(scaleFactorBar)

jetChargeHistSig.Scale(scaleFactorH)
jetChargeHistBack.Scale(scaleFactorBar)

#Fill THStack - make sure back is 1st
lepPtStack.Add(lepPtHistBack)
lepPtStack.Add(lepPtHistSig)

lepEtaStack.Add(lepEtaHistBack)
lepEtaStack.Add(lepEtaHistSig)

nJetsStack.Add(nJetsHistBack)
nJetsStack.Add(nJetsHistSig)

nJets50Stack.Add(nJets50HistBack)
nJets50Stack.Add(nJets50HistSig)

lepPtStack2.Add(lepPtHistBack2)
lepPtStack2.Add(lepPtHistSig2)

lepPxStack.Add(lepPxHistBack)
lepPxStack.Add(lepPxHistSig)

lepRhoStack.Add(lepRhoHistBack)
lepRhoStack.Add(lepRhoHistSig)

jetChargeStack.Add(jetChargeHistBack)
jetChargeStack.Add(jetChargeHistSig)

backTree.SetFillColor(ROOT.kRed)
signalTree.SetFillColor(ROOT.kBlue)

outfile = ROOT.TFile.Open('evtLoop_output.root','RECREATE')
outfile.cd()

#write the signals
lepPtHistSig.Write()
lepEtaHistSig.Write()
nJetsHistSig.Write()
nJets50HistSig.Write()
lepPtHistSig2.Write()
lepPxHistSig.Write()
lepRhoHistSig.Write()
jetChargeHistSig.Write()
jetChargeHistSig2.Write()
jetCSVHistSig.Write()

#write the backgrounds
lepPtHistBack.Write()
lepEtaHistBack.Write()
nJets50HistBack.Write()
nJetsHistBack.Write()
lepPtHistBack2.Write()
lepPxHistBack.Write()
lepRhoHistBack.Write()
jetChargeHistBack.Write()

#write the THStack
lepPtStack.Write()
lepEtaStack.Write()
nJetsStack.Write()
nJets50Stack.Write()
lepPtStack2.Write()
lepPxStack.Write()
lepRhoStack.Write()
jetChargeStack.Write()

outfile.Close()


