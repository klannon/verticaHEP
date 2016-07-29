#!/usr/bin/env python

#include "Rtypes.h"
#include "TColor.h"

import ROOT
ROOT.gSystem.Load('libttH-13TeVMultiLeptonsTemplateMakers.so')

import os
import time

startTime = time.time()

#chain for ttH
ch_ttH = ROOT.TChain('OSTwoLepAna/summaryTree')
for rootFile in os.listdir('/hadoop/users/klannon/ttHTrees/ttH125powheg/'):
   ch_ttH.Add('/hadoop/users/klannon/ttHTrees/ttH125powheg/'+rootFile)b

#chain for lep from T
ch_ttJetT = ROOT.TChain('OSTwoLepAna/summaryTree')
for rootFile in os.listdir('/hadoop/users/klannon/ttHTrees/TTJets_split_1lepFromT'):
   ch_ttJetT.Add('/hadoop/users/klannon/ttHTrees/TTJets_split_1lepFromT/'+rootFile)
   

#chain for lep from TBar
ch_ttJetTBar = ROOT.TChain('OSTwoLepAna/summaryTree')
for rootFile in os.listdir('/hadoop/users/klannon/ttHTrees/TTJets_split_1lepFromTBar'):
   ch_ttJetTBar.Add('/hadoop/users/klannon/ttHTrees/TTJets_split_1lepFromTBar/'+rootFile)

print('chains done')
chainTime = time.time() - startTime

ch_ttJetT.SetFillColor(ROOT.kRed)
ch_ttJetTBar.SetFillColor(ROOT.kRed)
ch_ttH.SetFillColor(ROOT.kBlue)

#scale factor 
#what units do we have?
ttbarCross = 182.7
ttHCross = 0.212
luminosity = 2500
nTotSig = 3991615 #signalTree.GetEntries()
nTotBar = 61614751 #backgroundTree.GetEntries()
nTotT = 61374841

scaleFactorH = luminosity*ttHCross/nTotSig
scaleFactorT = luminosity*ttbarCross/nTotT
scaleFactorBar = luminosity*ttbarCross/nTotBar

#set color options
backCol = ROOT.kRed
sigCol = ROOT.kBlue

startHistTime = time.time()

#define cuts
cut = "@tightMvaBased_leptons.size()==2&&tightMvaBased_leptons[0].charge*tightMvaBased_leptons[1].charge>0&&@preselected_jets.size()>2"

#signal
#pt
ch_ttH.Project('lepPtHistSig(100,0,200)','preselected_leptons.obj.Pt()', cut)
lepPtHistSig = ROOT.gDirectory.Get('lepPtHistSig')
lepPtHistSig.Scale(scaleFactorH)
ch_ttJetT.Project('lepPtBackSig(100,0,200)', 'preselected_leptons.obj.Pt()',cut)
lepPtBackSig = ROOT.gDirectory.Get('lepPtBackSig')
ch_ttJetTBar.Project('lepPtBackSigBar(100,0,200)', 'preselected_leptons.obj.Pt()', cut)
lepPtBackSigBar = ROOT.gDirectory.Get('lepPtBackSigBar')
lepPtBackSig.Scale(scaleFactorT)
lepPtBackSigBar.Scale(scaleFactorBar)
lepPtBackSig.Add(lepPtBackSig,lepPtBackSigBar)

print('pt done')

#eta - need to fix selection statements for projections
ch_ttH.Project('lepEtaHistSig(100,-2,2)','preselected_leptons.obj.Eta()','preselected_leptons.obj.Pt() > 35 &&'+cut)
lepEtaHistSig = ROOT.gDirectory.Get('lepEtaHistSig')
lepEtaHistSig.Scale(scaleFactorH)
ch_ttJetT.Project('lepEtaBackSig(100,-2,2)', 'preselected_leptons.obj.Eta()','preselected_leptons.obj.Pt() > 35 &&'+cut)
lepEtaBackSig = ROOT.gDirectory.Get('lepEtaBackSig')
lepEtaBackSig.Scale(scaleFactorT)
ch_ttJetTBar.Project('lepEtaBackSigBar(100,-2,2)', 'preselected_leptons.obj.Eta()','preselected_leptons.obj.Pt() > 35 &&'+cut)
lepEtaBackSigBar = ROOT.gDirectory.Get('lepEtaBackSigBar')
lepEtaBackSigBar.Scale(scaleFactorBar)
lepEtaBackSig.Add(lepEtaBackSig,lepEtaBackSigBar)

print('eta done')

#added by Matthew Link
#px
ch_ttH.Project('lepPxHistSig(100,0,200)','preselected_leptons.obj.Px()',cut)
lepPxHistSig = ROOT.gDirectory.Get('lepPxHistSig')
lepPxHistSig.Scale(scaleFactorH)
ch_ttJetT.Project('lepPxBackSig(100,0,200)','preselected_leptons.obj.Px()',cut)
lepPxBackSig = ROOT.gDirectory.Get('lepPxBackSig')
lepPxBackSig.Scale(scaleFactorT)
ch_ttJetTBar.Project('lepPxBackSigBar(100,0,200)','preselected_leptons.obj.Px()',cut)
lepPxBackSigBar =  ROOT.gDirectory.Get('lepPxBackSigBar')
lepPxBackSigBar.Scale(scaleFactorBar)
lepPxBackSig.Add(lepPxBackSig,lepPxBackSigBar)

ch_ttH.Project('lepRhoHistSig(100,0,10)','preselected_leptons.rho',cut)
lepRhoHistSig = ROOT.gDirectory.Get('lepRhoHistSig')
lepRhoHistSig.Scale(scaleFactorH)
ch_ttJetT.Project('lepRhoBackSig(100,0,10)','preselected_leptons.rho',cut)
lepRhoBackSig = ROOT.gDirectory.Get('lepRhoBackSig')
lepRhoBackSig.Scale(scaleFactorT)
ch_ttJetTBar.Project('lepRhoBackSigBar(100,0,10)','preselected_leptons.rho',cut)
lepRhoBackSigBar = ROOT.gDirectory.Get('lepRhoBackSigBar')
lepRhoBackSigBar.Scale(scaleFactorBar)
lepRhoBackSig.Add(lepRhoBackSig,lepRhoBackSigBar)

print('rho done')

ch_ttH.Project('jetChargeHistSig(100,-2,2)','preselected_jets.charge',cut)
jetChargeHistSig = ROOT.gDirectory.Get('jetChargeHistSig')
jetChargeHistSig.Scale(scaleFactorH)
ch_ttJetT.Project('jetChargeBackSig(100,-2,2)','preselected_jets.charge',cut)
jetChargeBackSig = ROOT.gDirectory.Get('jetChargeBackSig')
jetChargeBackSig.Scale(scaleFactorT)
ch_ttJetTBar.Project('jetChargeBackSigBar(100,-2,2)','preselected_jets.charge',cut)
jetChargeBackSigBar = ROOT.gDirectory.Get('jetChargeBackSigBar')
jetChargeBackSigBar.Scale(scaleFactorBar)
jetChargeBackSig.Add(jetChargeBackSig,jetChargeBackSigBar)

#jet charge 2 - need to fix selections
ch_ttH.Project('jetChargeHistSig2(100,-2,2)','preselected_jets.charge','preselected_jets.obj.Pt() > 42 &&'+cut)
jetChargeHistSig2 = ROOT.gDirectory.Get('jetChargeHistSig2')
jetChargeHistSig2.Scale(scaleFactorH)
ch_ttJetT.Project('jetChargeBackSig2(100,-2,2)','preselected_jets.charge','preselected_jets.obj.Pt() > 42 &&'+cut)
jetChargeBackSig2 = ROOT.gDirectory.Get('jetChargeBackSig2')
jetChargeBackSig2.Scale(scaleFactorT)
ch_ttJetTBar.Project('jetChargeBackSig2Bar(100,-2,2)','preselected_jets.charge','preselected_jets.obj.Pt() > 42 &&'+cut)
jetChargeBackSig2Bar = ROOT.gDirectory.Get('jetChargeBackSig2Bar')
jetChargeBackSig2Bar.Scale(scaleFactorBar)
jetChargeBackSig2.Add(jetChargeBackSig2,jetChargeBackSig2Bar)

print('charge done')

#jetCSVHistSig = ROOT.TH1F('jetCSVHistSig', 'Jet csv',100,-10,2)
ch_ttH.Project('jetCSVHistSig(100,-10,2)','preselected_jets.csv',cut)
jetCSVHistSig = ROOT.gDirectory.Get('jetCSVHistSig')
jetCSVHistSig.Scale(scaleFactorH)
ch_ttJetT.Project('jetCSVBackSig(100,-10,2)','preselected_jets.csv',cut)
jetCSVBackSig = ROOT.gDirectory.Get('jetCSVBackSig')
jetCSVBackSig.Scale(scaleFactorT)
ch_ttJetTBar.Project('jetCSVBackSigBar(100,-10,2)','preselected_jets.csv',cut)
jetCSVBackSigBar = ROOT.gDirectory.Get('jetCSVBackSigBar')
jetCSVBackSigBar.Scale(scaleFactorBar)
jetCSVBackSig.Add(jetCSVBackSig,jetCSVBackSigBar)

#end time for histograms
endHistTime = time.time() - startHistTime

#create THStack - need to switch back and sig s.t. back 1st
lepPtStack = ROOT.THStack('lepPtStack','Lepton p_{T}')
lepPtStack.Add(lepPtBackSig)
lepPtStack.Add(lepPtHistSig)

lepEtaStack = ROOT.THStack('lepEtaStack', 'Lepton #eta')
lepEtaStack.Add(lepEtaBackSig)
lepEtaStack.Add(lepEtaHistSig)

lepPxStack = ROOT.THStack('lepPxStack', 'Lepton p_{x}')
lepPxStack.Add(lepPxBackSig)
lepPxStack.Add(lepPxHistSig)

lepRhoStack = ROOT.THStack('lepRhoStack', 'Lepton #rho')
lepRhoStack.Add(lepRhoBackSig)
lepRhoStack.Add(lepRhoHistSig)

jetChargeStack = ROOT.THStack('jetChargeStack', 'Jet Charge')
jetChargeStack.Add(jetChargeBackSig)
jetChargeStack.Add(jetChargeHistSig)

jetChargeStack2 = ROOT.THStack('jetChargeStack2', 'Jet Charge2')
jetChargeStack2.Add(jetChargeBackSig2)
jetChargeStack2.Add(jetChargeHistSig2)

jetCSVStack = ROOT.THStack('jetCSVStack', 'Jet csv')
jetCSVStack.Add(jetCSVBackSig)
jetCSVStack.Add(jetCSVHistSig)

#write files
outfile = ROOT.TFile.Open('drawChain_output.root','RECREATE')
outfile.cd()

lepPtHistSig.Write()
lepEtaHistSig.Write()

lepPxHistSig.Write()
lepRhoHistSig.Write()
jetChargeHistSig.Write()
jetChargeHistSig2.Write()
jetCSVHistSig.Write()

#write background hists
lepPtBackSig.Write()
lepEtaBackSig.Write()

lepPxBackSig.Write()
lepRhoBackSig.Write()
jetChargeBackSig.Write()
jetChargeBackSig2.Write()
jetCSVHistSig.Write()

#write THStack hists
lepPtStack.Write()
lepEtaStack.Write()
lepPxStack.Write()
lepRhoStack.Write()
jetChargeStack.Write()
jetChargeStack2.Write()
jetCSVStack.Write()

totalTime = time.time() - startTime
print('drawChain\n fill chain: {}\nhistograms: {}\nTotal: {}'.format( chainTime, endHistTime, totalTime))
outfile.Close()

