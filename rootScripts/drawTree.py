#!/usr/bin/env python

#include "Rtypes.h"
#include "TColor.h"

import ROOT
ROOT.gSystem.Load('libttH-13TeVMultiLeptonsTemplateMakers.so')

import os
#test addition
#signal
signalFile = ROOT.TFile.Open('ttH_forKevin.root')
signalTree = signalFile.Get('OSTwoLepAna/summaryTree')

chain = TChain('chain')
for rootFile in os.listdir('/hadoop/users/klannon/ttHTrees/ttH125powheg/'):
   sigFile = ROOT.TFile.Open(rootFile)

#background signal
backgroundFile = ROOT.TFile.Open('ttbar_forKevin.root')
backgroundTree = backgroundFile.Get('OSTwoLepAna/summaryTree')

backgroundTree.SetFillColor(ROOT.kRed)
signalTree.SetFillColor(ROOT.kBlue)

#scale factor 
#what units do we have?
ttbarCross = 182.7
ttHCross = 0.212
luminosity = 2500
nTotSig = 2600389.15887 #signalTree.GetEntries()
nTotBack = 25446993.0 #backgroundTree.GetEntries()

scaleFactorH = luminosity*ttHCross/nTotSig
scaleFactorBar = luminosity*ttbarCross/nTotBack

#set color options
backCol = ROOT.kRed
sigCol = ROOT.kBlue

#print "H: %f" % scaleFactorH
#print "Bar: %f" % scaleFactorBar

#creat TCanvas to explore draw
#c1 = ROOT.TCanvas("c1","test",400,400)

#try to change the directory
#where = ROOT.TDirectory()
#where.cd()
#outfile = ROOT.TFile.Open('drawTree_output.root','RECREATE')
#outfile.cd()

#put all background Hists under Signal hist

#lepPtHistSig = ROOT.TH1F('lepPtHistSig','Lepton p_{T}',100,0,200)
signalTree.Project('lepPtHistSig(100,0,200)','preselected_leptons.obj.Pt()')
#signalTree.Draw('preselected_leptons.obj.Pt()>>lepPtHistSig(100,0,200)')
lepPtHistSig = ROOT.gDirectory.Get('lepPtHistSig')
#ROOT.gROOT.Get('lepPtHistSig').Draw()
#lepPtHistSig.Draw()
lepPtHistSig.Scale(scaleFactorH)
#lepPtBackSig = ROOT.TH1F('lepPtBackSig', 'Lepton p_{T}',100,0,200)
backgroundTree.Project('lepPtBackSig(100,0,200)', 'preselected_leptons.obj.Pt()')
lepPtBackSig = ROOT.gDirectory.Get('lepPtBackSig')
lepPtBackSig.Scale(scaleFactorBar)

#c1.WaitPrimitive()

#lepEtaHistSig = ROOT.TH1F('lepEtaHistSig','Lepton #eta',100,-2,2)
signalTree.Project('lepEtaHistSig(100,-2,2)','preselected_leptons.obj.Eta()','preselected_leptons.obj.Pt() > 35')
lepEtaHistSig = ROOT.gDirectory.Get('lepEtaHistSig')
lepEtaHistSig.Scale(scaleFactorH)
#lepEtaBackSig = ROOT.TH1F('lepEtaBackSig','Lepton #eta',100,-2,2)
backgroundTree.Project('lepEtaBackSig(100,-2,2)', 'preselected_leptons.obj.Eta()','preselected_leptons.obj.Pt() > 35')
lepEtaBackSig = ROOT.gDirectory.Get('lepEtaBackSig')
lepEtaBackSig.Scale(scaleFactorBar)


#added by Matthew Link
#lepPxHistSig = ROOT.TH1F('lepPxHistSig','Lepton p_{x}',100,0,200)
signalTree.Project('lepPxHistSig(100,0,200)','preselected_leptons.obj.Px()')
lepPxHistSig = ROOT.gDirectory.Get('lepPxHistSig')
lepPxHistSig.Scale(scaleFactorH)
#lepPxBackSig = ROOT.TH1F('lepPxBackSig', 'Lepton p_{x}',100,0,200)
backgroundTree.Project('lepPxBackSig(100,0,200)','preselected_leptons.obj.Px()')
lepPxBackSig = ROOT.gDirectory.Get('lepPxBackSig')
lepPxBackSig.Scale(scaleFactorBar)

#lepRhoHistSig = ROOT.TH1F('lepRhoHistSig','Lepton #rho', 100,0,10)
signalTree.Project('lepRhoHistSig(100,0,10)','preselected_leptons.rho')
lepRhoHistSig = ROOT.gDirectory.Get('lepRhoHistSig')
lepRhoHistSig.Scale(scaleFactorH)
#lepRhoBackSig = ROOT.TH1F('lepRhoBackSig', 'Lepton #rho Background',100,0,10)
backgroundTree.Project('lepRhoBackSig(100,0,10)','preselected_leptons.rho')
lepRhoBackSig = ROOT.gDirectory.Get('lepRhoBackSig')
lepRhoBackSig.Scale(scaleFactorBar)

#jetChargeHistSig = ROOT.TH1F('jetChargeHistSig', 'Jet Charge',100,-2,2)
signalTree.Project('jetChargeHistSig(100,-2,2)','preselected_jets.charge')
jetChargeHistSig = ROOT.gDirectory.Get('jetChargeHistSig')
jetChargeHistSig.Scale(scaleFactorH)
#jetChargeBackSig = ROOT.TH1F('jetChargeBackSig', 'Jet Charge Background',100,-2,2)
backgroundTree.Project('jetChargeBackSig(100,-2,2)','preselected_jets.charge')
jetChargeBackSig = ROOT.gDirectory.Get('jetChargeBackSig')
jetChargeBackSig.Scale(scaleFactorBar)

#jetChargeHistSig2 = ROOT.TH1F('jetChargeHistSig2', 'Jet Charge Pt>42',100,-2,2)
signalTree.Project('jetChargeHistSig2(100,-2,2)','preselected_jets.charge','preselected_jets.obj.Pt() > 42')
jetChargeHistSig2 = ROOT.gDirectory.Get('jetChargeHistSig2')
jetChargeHistSig2.Scale(scaleFactorH)
#jetChargeBackSig2 = ROOT.TH1F('jetChargeBackSig2', 'Jet Charge Pt>42 Background',100,-2,2)
backgroundTree.Project('jetChargeBackSig2(100,-2,2)','preselected_jets.charge','preselected_jets.obj.Pt() > 42')
jetChargeBackSig2 = ROOT.gDirectory.Get('jetChargeBackSig2')
jetChargeBackSig2.Scale(scaleFactorBar)

#jetCSVHistSig = ROOT.TH1F('jetCSVHistSig', 'Jet csv',100,-10,2)
signalTree.Project('jetCSVHistSig(100,-10,2)','preselected_jets.csv')
jetCSVHistSig = ROOT.gDirectory.Get('jetCSVHistSig')
jetCSVHistSig.Scale(scaleFactorH)
#jetCSVBackSig = ROOT.TH1F('jetCSVBackSig', 'Jet csv background',100,-10,2)
backgroundTree.Project('jetCSVBackSig(100,-10,2)','preselected_jets.csv')
jetCSVBackSig = ROOT.gDirectory.Get('jetCSVBackSig')
jetCSVBackSig.Scale(scaleFactorBar)

#create THStack - need to switch back and sig s.t. back 1st
lepPtStack = ROOT.THStack('lepPtStack','Lepton p_{T}')
lepPtStack.Add(lepPtBackSig)
lepPtStack.Add(lepPtHistSig)

lepPtStack2 = ROOT.THStack('lepPtStack2','Lept p_{T}')
lepPtStack2.Add(lepPtBackSig)
lepPtStack2.Add(lepPtHistSig)

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
outfile = ROOT.TFile.Open('drawTree_output.root','RECREATE')
outfile.cd()
#lepPtTest.Write()
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
lepPtStack2.Write()
lepEtaStack.Write()
lepPxStack.Write()
lepRhoStack.Write()
jetChargeStack.Write()
jetChargeStack2.Write()
jetCSVStack.Write()

outfile.Close()

