#!/usr/bin/env python

import ROOT
import os
import time
ROOT.gSystem.Load('../CMSSW_7_6_3/lib/slc6_amd64_gcc493/libttH-13TeVMultiLeptonsTemplateMakers.so')

startTime = time.time()

#chain for ttH
ttHChain = ROOT.TChain('OSTwoLepAna/summaryTree')
for rootFile in os.listdir('/hadoop/store/user/lannon/bdtreco_v0/tth_nonbb/'):
   ttHChain.Add('/hadoop/store/user/lannon/bdtreco_v0/tth_nonbb/'+rootFile)

#chain for ttJet
ttJetChain = ROOT.TChain('OSTwoLepAna/summaryTree')
for rootFile in os.listdir('/hadoop/store/user/lannon/bdtreco_v0/ttjets_semilep/'):
   if os.path.getsize('/hadoop/store/user/lannon/bdtreco_v0/ttjets_semilep/'+rootFile) > 1000000000:
      ttJetChain.Add('/hadoop/store/user/lannon/bdtreco_v0/ttjets_semilep/'+rootFile)
   

fPreLep = open('verticaInput/preLep.txt', 'w')
fPreElec = open('verticaInput/preElec.txt', 'w')
fPreMuon = open('verticaInput/preMuon.txt', 'w')
fPreTau = open('verticaInput/preTau.txt', 'w')
fPreJet = open('verticaInput/preJet.txt', 'w')
fPrunedGenPart = open('verticaInput/prunedGenPart.txt', 'w')
fPackGenPart = open('verticaInput/packGenPart.txt', 'w')
fMatchJet = open('verticaInput/matchJet.txt', 'w')
fMatchJetTruth = open('verticaInput/matchJetTruth.txt', 'w')
fLepHiggsBDT = open('verticaInput/lepHiggsBDT.txt', 'w')
fLepTopBDT = open('verticaInput/lepTopBDT.txt', 'w')
fLepTopTruth = open('verticaInput/lepTopTruth.txt', 'w')
fLepHiggsTruth = open('verticaInput/lepHiggsBDT.txt', 'w')
fEvent = open('verticaInput/event.txt','w')
#tlv files
fLepTopBDT_tlv = open('verticaInput/lepTopBDT_tlv.txt','w')
fLepHiggsBDT_tlv = open('verticaInput/lepHiggsBDT_tlv.txt','w')
fLepTopBDT_tlv = open('verticaInput/lepTopBDT_tlv.txt','w')
fBJetHadTopBDT_tlv = open('verticaInput/bJetHadTopBDT_tlv.txt','w')
fBJetLepTopBDT_tlv = open('verticaInput/bJetLepTopBDT_tlv.txt','w')
fWJet1HadTopBDT_tlv = open('verticaInput/wJet1HadTopBDT_tlv.txt','w')
fWJet2HadTopBDT_tlv = open('verticaInput/wJet2HadTopBDT_tlv.txt','w')
fWJet1HiggsBDT_tlv = open('verticaInput/wJet1HiggsBDT_tlv.txt','w')
fWJet2HiggsBDT_tlv = open('verticaInput/wJet2HiggsBDT_tlv.txt','w')
fWHadTopBDT_tlv = open('verticaInput/wHadTopBDT_tlv.txt','w')
fWHiggsBDT_tlv = open('verticaInput/wHiggsBDT_tlv.txt','w')
fHiggsBDT_tlv = open('verticaInput/higgsBDT_tlv.txt','w')
fHadTopBDT_tlv = open('verticaInput/hadTopBDT_tlv.txt','w')
fLepTopBDT_tlv = open('verticaInput/lepTopBDT_tlv.txt','w')
fLepTopHiggsBDT_tlv = open('verticaInput/lepTopHiggsBDT_tlv.txt','w')
fHadTopHiggsBDT_tlv = open('verticaInput/hadTopHiggsBDT_tlv.txt','w')
fLepTopHadTopBDT_tlv = open('verticaInput/lepTopHadTopBDT_tlv.txt','w')
ftthBDT_tlv = open('verticaInput/tthBDT_tlv.txt','w')


fPreLep.write('Run | Lumi | Event | SampleID | Pt | Eta | Phi | pdgID | dxy | dz | charge | relIso | miniIso | genPdgID | isPromptFinalState | isDirectPromptTauDecayProductFinalState | genMotherPdgID | genGrandMotherPdgID | lepMVA | miniIsoCharged | miniIsoNeutral | jetPtRatio | jetPtRel | csv | sip3D | jet_nCharged_tracks | miniAbsIsoCharged | miniAbsIsoNeutral | rho | effArea | miniIsoR | miniAbsIsoNeutralcorr\n')

fPreElec.write('Run | Lumi | Event | SampleID | Pt | Eta | Phi | pdgID | dxy | dz | charge | relIso | miniIso | genPdgID | isPromptFinalState | isDirectPromptTauDecayProductFinalState | genMotherPdgID | genGrandMotherPdgID | lepMVA | miniIsoCharged | miniIsoNeutral | jetPtRatio | jetPtRel | csv | sip3D | jet_nCharged_tracks | miniAbsIsoCharged | miniAbsIsoNeutral | rho | effArea | miniIsoR | miniAbsIsoNeutralcorr | SCeta | isGsfCtfScPixChargeConsistent\n')

fPreMuon.write('Run | Lumi | Event | SampleID | Pt | Eta | Phi | pdgID | dxy | dz | charge | relIso | miniIso | genPdgID | isPromptFinalState | isDirectPromptTauDecayProductFinalState | genMotherPdgID | genGrandMotherPdgID | lepMVA | miniIsoCharged | miniIsoNeutral | jetPtRatio | jetPtRel | csv | sip3D | jet_nCharged_tracks | miniAbsIsoCharged | miniAbsIsoNeutral | rho | effArea | miniIsoR | miniAbsIsoNeutralcorr | chargeFlip | isPFMuon | isTrackerMuon | isGlobalMuon | normalizedChi2 | numberOfValidMuonHits | numberOfMatchedStations | numberOfValidPixelHits | trackerLayersWithMeasurement | localChi2 | trKink | validFrac | segCompatibility\n')

fPreTau.write('Run | Lumi | Event | SampleID | Pt | Eta | Phi | charge | genPdgID | genMotherPdgID | genGrandMotherPdgID | dxy | dz | decayModeFinding | mvaID\n')

fPreJet.write('Run | Lumi | Event | SampleID | Pt | Eta | Phi | Mass | charge | genPdgID | genMotherPdgID | genGrandMotherPdgID | csv | qgid | pdgID\n')

fPrunedGenPart.write('Run | Lumi | Event | SampleID | Pt | Eta | Phi | Mass | pdgID | status | isPromptFinalState | isPromptDecayed | isDirectPromptTauDecayProductFinalState | child0 | child1 | mother | grandmother\n')

fPackGenPart.write('Run | Lumi | Event | SampleID | Pt | Eta | Phi | Mass | pdgID | status | isPromptFinalState | isPromptDecayed | isDirectPromptTauDecayProductFinalState | child0 | child1 | mother | grandmother\n')

fMatchJet.write('Run | Lumi | Event | SampleID | Pt | Eta | Phi | Mass | charge | genPdgID | genMotherPdgID | genGrandMotherPdgID | csv | qgid | pdgID\n')
 
fMatchJetTruth.write('Run | Lumi | Event | SampleID | Pt | Eta | Phi | Mass | charge | genPdgID | genMotherPdgID | genGrandMotherPdgID | csv | qgid | pdgID\n')
 
fLepHiggsBDT.write('Run | Lumi | Event | SampleID | Pt | Eta | Phi | pdgID | dxy | dz | charge | relIso | miniIso | genPdgID | isPromptFinalState | isDirectPromptTauDecayProductFinalState | genMotherPdgID | genGrandMotherPdgID | lepMVA | miniIsoCharged | miniIsoNeutral | jetPtRatio | jetPtRel | csv | sip3D | jet_nCharged_tracks | miniAbsIsoCharged | miniAbsIsoNeutral | rho | effArea | miniIsoR | miniAbsIsoNeutralcorr\n')
 
fLepTopBDT.write('Run | Lumi | Event | SampleID | Pt | Eta | Phi | pdgID | dxy | dz | charge | relIso | minilso | genPdgID | isPromptFinalState | isDirectPromptTauDecayProductFinalState | genMotherPdgID | genGrandMotherPdgID | lepMVA | miniIsoCharged | miniIsoNeutral | jetPtRatio | jetPtRel | csv | sip3D | jet_nCharged_tracks | miniAbsIsoCharged | miniAbsIsoNeutral | rho | effArea | miniIsoR | miniAbsIsoNeutralcorr\n')

fLepTopTruth.write('Run | Lumi | Event | SampleID | Pt | Eta | Phi | pdgID | dxy | dz | charge | relIso | minilso | genPdgID | isPromptFinalState | isDirectPromptTauDecayProductFinalState | genMotherPdgID | genGrandMotherPdgID | lepMVA | miniIsoCharged | miniIsoNeutral | jetPtRatio | jetPtRel | csv | sip3D | jet_nCharged_tracks | miniAbsIsoCharged | miniAbsIsoNeutral | rho | effArea | miniIsoR | miniAbsIsoNeutralcorr\n')
 
fLepHiggsTruth.write('Run | Lumi | Event | SampleID | Pt | Eta | Phi | pdgID | dxy | dz | charge | rellso | miniIso | genPdgID | isPromptFinalState | isDirectPromptTauDecayProductFinalState | genMotherPdgID | genGrandMotherPdgID | lepMVA | miniIsoCharged | miniIsoNeutral | jetPtRatio | jetPtRel | csv | sip3D | jet_nCharged_tracks | miniAbsIsoCharged | miniAbsIsoNeutral | rho | effArea | miniIsoR | miniAbsIsoNeutralcorr\n') 

fEvent.write('Run | Lumi | Event | SampleID | mcwgt | wgt | higgs_decay | passTrigger| reco_score | norm_score_sum | num_real_jets_bdt | num_jet_matches_truth | matching_results | metPt | metPhi\n')

fLepTopBDT_tlv.write('Run | Lumi | Event | SampleID | Pt | Eta | Phi | Mass\n')
fLepHiggsBDT_tlv.write('Run | Lumi | Event | SampleID | Pt | Eta | Phi | Mass\n')
fLepTopBDT_tlv.write('Run | Lumi | Event | SampleID | Pt | Eta | Phi | Mass\n')
fBJetHadTopBDT_tlv.write('Run | Lumi | Event | SampleID | Pt | Eta | Phi | Mass\n')
fBJetLepTopBDT_tlv.write('Run | Lumi | Event | SampleID | Pt | Eta | Phi | Mass\n')
fWJet1HadTopBDT_tlv.write('Run | Lumi | Event | SampleID | Pt | Eta | Phi | Mass\n')
fWJet2HadTopBDT_tlv.write('Run | Lumi | Event | SampleID | Pt | Eta | Phi | Mass\n')
fWJet1HiggsBDT_tlv.write('Run | Lumi | Event | SampleID | Pt | Eta | Phi | Mass\n')
fWJet2HiggsBDT_tlv.write('Run | Lumi | Event | SampleID | Pt | Eta | Phi | Mass\n')
fWHadTopBDT_tlv.write('Run | Lumi | Event | SampleID | Pt | Eta | Phi | Mass\n')
fWHiggsBDT_tlv.write('Run | Lumi | Event | SampleID | Pt | Eta | Phi | Mass\n')
fHiggsBDT_tlv.write('Run | Lumi | Event | SampleID | Pt | Eta | Phi | Mass\n')
fHadTopBDT_tlv.write('Run | Lumi | Event | SampleID | Pt | Eta | Phi | Mass\n')
fLepTopBDT_tlv.write('Run | Lumi | Event | SampleID | Pt | Eta | Phi | Mass\n')
fLepTopHiggsBDT_tlv.write('Run | Lumi | Event | SampleID | Pt | Eta | Phi | Mass\n')
fHadTopHiggsBDT_tlv.write('Run | Lumi | Event | SampleID | Pt | Eta | Phi | Mass\n')
fLepTopHadTopBDT_tlv.write('Run | Lumi | Event | SampleID | Pt | Eta | Phi | Mass\n')
ftthBDT_tlv.write('Run | Lumi | Event | SampleID | Pt | Eta | Phi | Mass\n')

SampleID = '1'
for entry in ttHChain:
   #print('work')
   #event
   fEvent.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(entry.mcwgt) + '|' + str(entry.wgt) + '|' + str(entry.higgs_decay) + '|' + str(entry.passTrigger) + '|' + str(entry.reco_score) + '|' + str(entry.norm_score_sum) + '|' + str(entry.num_real_jets_bdt) +  '|' + str(entry.num_jet_matches_truth) + '|' + str(entry.matching_results) + '|' + str(entry.met[0].obj.Pt()) + '|' + str(entry.met[0].obj.Phi()) + '\n' )

   #preselected leptons
   for lep in entry.preselected_leptons:
	fPreLep.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(lep.obj.Pt()) + '|' + str(lep.obj.Eta()) + '|' + str(lep.obj.Phi()) + '|' + str(lep.pdgID) + '|' + str(lep.dxy) + '|' + str(lep.dz) + '|' + str(lep.charge) + '|' + str(lep.relIso) + '|' + str(lep.miniIso) + '|' + str(lep.genPdgID) + '|' + str(lep.isPromptFinalState) + '|' + str(lep.isDirectPromptTauDecayProductFinalState) + '|' + str(lep.genMotherPdgID) + '|' + str(lep.genGrandMotherPdgID) + '|' + str(lep.lepMVA) + '|' + str(lep.miniIsoCharged) + '|' + str(lep.miniIsoNeutral) + '|' + str(lep.jetPtRatio) + '|' + str(lep.jetPtRel) + '|' + str(lep.csv) + '|' + str(lep.sip3D) + '|' + str(lep.jet_nCharged_tracks) + '|' + str(lep.miniAbsIsoCharged) + '|' + str(lep.miniAbsIsoNeutral) + '|' + str(lep.rho) + '|' + str(lep.effArea) + '|' + str(lep.miniIsoR) + '|' + str(lep.miniAbsIsoNeutralcorr) + '\n' )

   #preselected electrons
   for elec in entry.preselected_electrons:
	fPreElec.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(elec.obj.Pt()) + '|' + str(elec.obj.Eta()) + '|' + str(elec.obj.Phi()) + '|' + str(elec.pdgID) + '|' + str(elec.dxy) + '|' + str(elec.dz) + '|' + str(elec.charge) + '|' +  str(elec.relIso) + '|' + str(elec.miniIso) + '|'  + str(elec.genPdgID) + '|'  + str(elec.isPromptFinalState) + '|' + str(elec.isDirectPromptTauDecayProductFinalState) + '|' + str(elec.genMotherPdgID) + '|' + str(elec.genGrandMotherPdgID) + '|' + str(elec.lepMVA) + '|' + str(elec.miniIsoCharged) + '|' + str(elec.miniIsoNeutral) + '|' + str(elec.jetPtRatio) + '|' + str(elec.jetPtRel) + '|' +  str(elec.csv) + '|' + str(elec.sip3D) + '|' + str(elec.jet_nCharged_tracks) + '|' + str(elec.miniAbsIsoCharged) + '|' + str(elec.miniAbsIsoNeutral) + '|' + str(elec.rho) + '|' + str(elec.effArea) + '|' +  str(elec.miniIsoR) + '|' +  str(elec.miniAbsIsoNeutralcorr) + '|'  + str(elec.SCeta) + '|' + str(elec.isGsfCtfScPixChargeConsistent) + '\n')

   #preselected muons
   for muon in entry.preselected_muons:
	fPreMuon.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(muon.obj.Pt()) + '|' + str(muon.obj.Eta()) + '|' + str(muon.obj.Phi()) + '|'  + str(muon.pdgID) + '|' + str(muon.dxy) + '|' + str(muon.dz) + '|' + str(muon.charge) + '|' + str(muon.relIso) + '|' + str(muon.miniIso) + '|' + str(muon.genPdgID) + '|' + str(muon.isPromptFinalState) + '|' + str(muon.isDirectPromptTauDecayProductFinalState) + '|' + str(muon.genMotherPdgID) + '|' + str(muon.genGrandMotherPdgID) + '|' + str(muon.lepMVA) + '|' + str(muon.miniIsoCharged) + '|' + str(muon.miniIsoNeutral) + '|' + str(muon.jetPtRatio) + '|' + str(muon.jetPtRel) + '|' + str(muon.csv) + '|' +  str(muon.sip3D) + '|' + str(muon.jet_nCharged_tracks) + '|' + str(muon.miniAbsIsoCharged) + '|' + str(muon.miniAbsIsoNeutral) + '|' + str(muon.rho) + '|' + str(muon.effArea) + '|' + str(muon.miniIsoR) + '|' + str(muon.miniAbsIsoNeutralcorr) + '|' + str(muon.chargeFlip) + '|' + str(muon.isPFMuon) + '|' + str(muon.isTrackerMuon) + '|' + str(muon.isGlobalMuon) + '|' + str(muon.normalizedChi2) + '|' + str(muon.numberOfValidMuonHits) + '|' + str(muon.numberOfMatchedStations) + '|' + str(muon.numberOfValidPixelHits)  + '|' + str(muon.trackerLayersWithMeasurement) + '|' + str(muon.localChi2) + '|' + str(muon.trKink) + '|' + str(muon.validFrac) + '|'  + str(muon.segCompatibility)+ '\n')

   #preselected taus
   for tau in entry.preselected_taus:
	fPreTau.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(tau.obj.Pt()) + '|' + str(tau.obj.Eta()) + '|' + str(tau.obj.Phi()) + '|'  + str(tau.charge) + '|' + str(tau.genPdgID) + '|' + str(tau.genMotherPdgID) + '|' + str(tau.genGrandMotherPdgID) + '|' + str(tau.dxy) + '|' + str(tau.dz) + '|' + str(tau.decayModeFinding) + '|' + str(tau.mvaID) + '\n')

   #preselected jets
   for jet in entry.preselected_jets:
	fPreJet.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(jet.obj.Pt()) + '|' + str(jet.obj.Eta()) + '|' + str(jet.obj.Phi()) + '|' + str(jet.obj.M()) + '|' + str(jet.charge) + '|' +  str(jet.genPdgID) + '|' + str(jet.genMotherPdgID) + '|' + str(jet.genGrandMotherPdgID) + '|' + str(jet.csv) + '|' + str(jet.qgid) + '|' + str(jet.pdgID) +'\n')

   #pruned genParticles
   for genPart in entry.pruned_genParticles:
	fPrunedGenPart.write(str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(genPart.obj.Pt()) + '|' + str(genPart.obj.Eta()) + '|' + str(genPart.obj.Phi()) + '|' + str(genPart.obj.M()) + '|' + str(genPart.pdgID) + '|' + str(genPart.status) + '|' + str(genPart.isPromptFinalState) + '|' + str(genPart.isPromptDecayed) + '|' + str(genPart.isDirectPromptTauDecayProductFinalState) + '|' + str(genPart.child0) + '|' + str(genPart.child1) + '|' + str(genPart.mother) + '|' + str(genPart.grandmother) + '\n')

   #packed genParticles
   for genPart in entry.packed_genParticles:
	fPackGenPart.write(str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(genPart.obj.Pt()) + '|' + str(genPart.obj.Eta()) + '|' + str(genPart.obj.Phi()) + '|' + str(genPart.obj.M()) + '|' + str(genPart.pdgID) + '|' + str(genPart.status) + '|' + str(genPart.isPromptFinalState) + '|' + str(genPart.isPromptDecayed) + '|' + str(genPart.isDirectPromptTauDecayProductFinalState) + '|' + str(genPart.child0) + '|' + str(genPart.child1) + '|' + str(genPart.mother) + '|' + str(genPart.grandmother) + '\n')
	
   #matched jets
   for jet in entry.matched_jets:
	fMatchJet.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(jet.obj.Pt()) + '|' + str(jet.obj.Eta()) + '|' + str(jet.obj.Phi()) + '|' + str(jet.obj.M()) + '|' + str(jet.charge) + '|' +  str(jet.genPdgID) + '|' + str(jet.genMotherPdgID) + '|' + str(jet.genGrandMotherPdgID) + '|' + str(jet.csv) + '|' + str(jet.qgid) + '|' + str(jet.pdgID) +'\n')

   #matched jets truth
   for jet in entry.matched_jets_truth:
	fMatchJetTruth.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(jet.obj.Pt()) + '|' + str(jet.obj.Eta()) + '|' + str(jet.obj.Phi()) + '|' + str(jet.obj.M()) + '|' + str(jet.charge) + '|' +  str(jet.genPdgID) + '|' + str(jet.genMotherPdgID) + '|' + str(jet.genGrandMotherPdgID) + '|' + str(jet.csv) + '|' + str(jet.qgid) + '|' + str(jet.pdgID) +'\n')

   #leptons from Higgs bdt
   #for lep in entry.lep_fromHiggs_bdt:
   fLepHiggsBDT.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(entry.lep_fromHiggs_bdt.obj.Pt()) + '|' + str(entry.lep_fromHiggs_bdt.obj.Eta()) + '|' + str(entry.lep_fromHiggs_bdt.obj.Phi()) + '|' + str(entry.lep_fromHiggs_bdt.pdgID) + '|' + str(entry.lep_fromHiggs_bdt.dxy) + '|' + str(entry.lep_fromHiggs_bdt.dz) + '|' + str(entry.lep_fromHiggs_bdt.charge) + '|' + str(entry.lep_fromHiggs_bdt.relIso) + '|' + str(entry.lep_fromHiggs_bdt.miniIso) + '|' + str(entry.lep_fromHiggs_bdt.genPdgID) + '|' + str(entry.lep_fromHiggs_bdt.isPromptFinalState) + '|' + str(entry.lep_fromHiggs_bdt.isDirectPromptTauDecayProductFinalState) + '|' + str(entry.lep_fromHiggs_bdt.genMotherPdgID) + '|' + str(entry.lep_fromHiggs_bdt.genGrandMotherPdgID) + '|' + str(entry.lep_fromHiggs_bdt.lepMVA) + '|' + str(entry.lep_fromHiggs_bdt.miniIsoCharged) + '|' + str(entry.lep_fromHiggs_bdt.miniIsoNeutral) + '|' + str(entry.lep_fromHiggs_bdt.jetPtRatio) + '|' + str(entry.lep_fromHiggs_bdt.jetPtRel) + '|' + str(entry.lep_fromHiggs_bdt.csv) + '|' + str(entry.lep_fromHiggs_bdt.sip3D) + '|' + str(entry.lep_fromHiggs_bdt.jet_nCharged_tracks) + '|' + str(entry.lep_fromHiggs_bdt.miniAbsIsoCharged) + '|' + str(entry.lep_fromHiggs_bdt.miniAbsIsoNeutral) + '|' + str(entry.lep_fromHiggs_bdt.rho) + '|' + str(entry.lep_fromHiggs_bdt.effArea) + '|' + str(entry.lep_fromHiggs_bdt.miniIsoR) + '|' + str(entry.lep_fromHiggs_bdt.miniAbsIsoNeutralcorr) + '\n' )

   #leptons from Top bdt
   #for lep in entry.lep_fromTop_bdt:
   fLepTopBDT.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(entry.lep_fromTop_bdt.obj.Pt()) + '|' + str(entry.lep_fromTop_bdt.obj.Eta()) + '|' + str(entry.lep_fromTop_bdt.obj.Phi()) + '|' + str(entry.lep_fromTop_bdt.pdgID) + '|' + str(entry.lep_fromTop_bdt.dxy) + '|' + str(entry.lep_fromTop_bdt.dz) + '|' + str(entry.lep_fromTop_bdt.charge) + '|' + str(entry.lep_fromTop_bdt.relIso) + '|' + str(entry.lep_fromTop_bdt.miniIso) + '|' + str(entry.lep_fromTop_bdt.genPdgID) + '|' + str(entry.lep_fromTop_bdt.isPromptFinalState) + '|' + str(entry.lep_fromTop_bdt.isDirectPromptTauDecayProductFinalState) + '|' + str(entry.lep_fromTop_bdt.genMotherPdgID) + '|' + str(entry.lep_fromTop_bdt.genGrandMotherPdgID) + '|' + str(entry.lep_fromTop_bdt.lepMVA) + '|' + str(entry.lep_fromTop_bdt.miniIsoCharged) + '|' + str(entry.lep_fromTop_bdt.miniIsoNeutral) + '|' + str(entry.lep_fromTop_bdt.jetPtRatio) + '|' + str(entry.lep_fromTop_bdt.jetPtRel) + '|' + str(entry.lep_fromTop_bdt.csv) + '|' + str(entry.lep_fromTop_bdt.sip3D) + '|' + str(entry.lep_fromTop_bdt.jet_nCharged_tracks) + '|' + str(entry.lep_fromTop_bdt.miniAbsIsoCharged) + '|' + str(entry.lep_fromTop_bdt.miniAbsIsoNeutral) + '|' + str(entry.lep_fromTop_bdt.rho) + '|' + str(entry.lep_fromTop_bdt.effArea) + '|' + str(entry.lep_fromTop_bdt.miniIsoR) + '|' + str(entry.lep_fromTop_bdt.miniAbsIsoNeutralcorr) + '\n' )

   #leptons from top truth
   #for lep in entry.lep_fromTop_truth:
   fLepTopTruth.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(entry.lep_fromTop_truth.obj.Pt()) + '|' + str(entry.lep_fromTop_truth.obj.Eta()) + '|' + str(entry.lep_fromTop_truth.obj.Phi()) + '|' + str(entry.lep_fromTop_truth.pdgID) + '|' + str(entry.lep_fromTop_truth.dxy) + '|' + str(entry.lep_fromTop_truth.dz) + '|' + str(entry.lep_fromTop_truth.charge) + '|' + str(entry.lep_fromTop_truth.relIso) + '|' + str(entry.lep_fromTop_truth.miniIso) + '|' + str(entry.lep_fromTop_truth.genPdgID) + '|' + str(entry.lep_fromTop_truth.isPromptFinalState) + '|' + str(entry.lep_fromTop_truth.isDirectPromptTauDecayProductFinalState) + '|' + str(entry.lep_fromTop_truth.genMotherPdgID) + '|' + str(entry.lep_fromTop_truth.genGrandMotherPdgID) + '|' + str(entry.lep_fromTop_truth.lepMVA) + '|' + str(entry.lep_fromTop_truth.miniIsoCharged) + '|' + str(entry.lep_fromTop_truth.miniIsoNeutral) + '|' + str(entry.lep_fromTop_truth.jetPtRatio) + '|' + str(entry.lep_fromTop_truth.jetPtRel) + '|' + str(entry.lep_fromTop_truth.csv) + '|' + str(entry.lep_fromTop_truth.sip3D) + '|' + str(entry.lep_fromTop_truth.jet_nCharged_tracks) + '|' + str(entry.lep_fromTop_truth.miniAbsIsoCharged) + '|' + str(entry.lep_fromTop_truth.miniAbsIsoNeutral) + '|' + str(entry.lep_fromTop_truth.rho) + '|' + str(entry.lep_fromTop_truth.effArea) + '|' + str(entry.lep_fromTop_truth.miniIsoR) + '|' + str(entry.lep_fromTop_truth.miniAbsIsoNeutralcorr) + '\n' )

   #leptons from Higgs truth
   #for lep in entry.lep_fromHiggs_truth:
   fLepHiggsTruth.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(entry.lep_fromHiggs_truth.obj.Pt()) + '|' + str(entry.lep_fromHiggs_truth.obj.Eta()) + '|' + str(entry.lep_fromHiggs_truth.obj.Phi()) + '|' + str(entry.lep_fromHiggs_truth.pdgID) + '|' + str(entry.lep_fromHiggs_truth.dxy) + '|' + str(entry.lep_fromHiggs_truth.dz) + '|' + str(entry.lep_fromHiggs_truth.charge) + '|' + str(entry.lep_fromHiggs_truth.relIso) + '|' + str(entry.lep_fromHiggs_truth.miniIso) + '|' + str(entry.lep_fromHiggs_truth.genPdgID) + '|' + str(entry.lep_fromHiggs_truth.isPromptFinalState) + '|' + str(entry.lep_fromHiggs_truth.isDirectPromptTauDecayProductFinalState) + '|' + str(entry.lep_fromHiggs_truth.genMotherPdgID) + '|' + str(entry.lep_fromHiggs_truth.genGrandMotherPdgID) + '|' + str(entry.lep_fromHiggs_truth.lepMVA) + '|' + str(entry.lep_fromHiggs_truth.miniIsoCharged) + '|' + str(entry.lep_fromHiggs_truth.miniIsoNeutral) + '|' + str(entry.lep_fromHiggs_truth.jetPtRatio) + '|' + str(entry.lep_fromHiggs_truth.jetPtRel) + '|' + str(entry.lep_fromHiggs_truth.csv) + '|' + str(entry.lep_fromHiggs_truth.sip3D) + '|' + str(entry.lep_fromHiggs_truth.jet_nCharged_tracks) + '|' + str(entry.lep_fromHiggs_truth.miniAbsIsoCharged) + '|' + str(entry.lep_fromHiggs_truth.miniAbsIsoNeutral) + '|' + str(entry.lep_fromHiggs_truth.rho) + '|' + str(entry.lep_fromHiggs_truth.effArea) + '|' + str(entry.lep_fromHiggs_truth.miniIsoR) + '|' + str(entry.lep_fromHiggs_truth.miniAbsIsoNeutralcorr) + '\n' )

   #Leptons from Top BDT tlv
   #for tlv in entry.lep_fromTop_bdt_tlv:
   fLepTopBDT_tlv.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(entry.lep_fromTop_bdt_tlv.Pt()) + '|' + str(entry.lep_fromTop_bdt_tlv.Eta()) + '|' + str(entry.lep_fromTop_bdt_tlv.Phi()) + '|' + str(entry.lep_fromTop_bdt_tlv.M())+'\n')

   #Leptons from Higgs BDT tlv
   #for tlv in entry.lep_fromHiggs_bdt_tlv:
   fLepHiggsBDT_tlv.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(entry.lep_fromHiggs_bdt_tlv.Pt()) + '|' + str(entry.lep_fromHiggs_bdt_tlv.Eta()) + '|' + str(entry.lep_fromHiggs_bdt_tlv.Phi()) + '|' + str(entry.lep_fromHiggs_bdt_tlv.M())+'\n')

   #bJet from Had Top BDT tlv
   #for tlv in entry.bjet_fromHadTop_bdt_tlv:
   fBJetHadTopBDT_tlv.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(entry.bjet_fromHadTop_bdt_tlv.Pt()) + '|' + str(entry.bjet_fromHadTop_bdt_tlv.Eta()) + '|' + str(entry.bjet_fromHadTop_bdt_tlv.Phi()) + '|' + str(entry.bjet_fromHadTop_bdt_tlv.M())+'\n')

   #bJet from Lep Top BDT tlv
   #for tlv in entry.bjet_fromLepTop_bdt_tlv:
   fBJetLepTopBDT_tlv.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(entry.bjet_fromLepTop_bdt_tlv.Pt()) + '|' + str(entry.bjet_fromLepTop_bdt_tlv.Eta()) + '|' + str(entry.bjet_fromLepTop_bdt_tlv.Phi()) + '|' + str(entry.bjet_fromLepTop_bdt_tlv.M())+'\n')

   #wJet 1 from Had Top BDT tlv
   #for tlv in entry.wjet1_fromHadTop_bdt_tlv:
   fWJet1HadTopBDT_tlv.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(entry.wjet1_fromHadTop_bdt_tlv.Pt()) + '|' + str(entry.wjet1_fromHadTop_bdt_tlv.Eta()) + '|' + str(entry.wjet1_fromHadTop_bdt_tlv.Phi()) + '|' + str(entry.wjet1_fromHadTop_bdt_tlv.M())+'\n')

   #wJet 1 from Had Top BDT tlv
   #for tlv in entry.wjet2_fromHadTop_bdt_tlv:
   fWJet2HadTopBDT_tlv.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(entry.wjet2_fromHadTop_bdt_tlv.Pt()) + '|' + str(entry.wjet2_fromHadTop_bdt_tlv.Eta()) + '|' + str(entry.wjet2_fromHadTop_bdt_tlv.Phi()) + '|' + str(entry.wjet2_fromHadTop_bdt_tlv.M())+'\n')

   #wJet 1 from Higgs BDT tlv
   #for tlv in entry.wjet1_fromHiggs_bdt_tlv:
   fWJet1HiggsBDT_tlv.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(entry.wjet1_fromHiggs_bdt_tlv.Pt()) + '|' + str(entry.wjet1_fromHiggs_bdt_tlv.Eta()) + '|' + str(entry.wjet1_fromHiggs_bdt_tlv.Phi()) + '|' + str(entry.wjet1_fromHiggs_bdt_tlv.M())+'\n')

   #wJet 2 from Higgs BDT tlv
   #for tlv in entry.wjet2_fromHiggs_bdt_tlv:
   fWJet2HiggsBDT_tlv.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(entry.wjet2_fromHiggs_bdt_tlv.Pt()) + '|' + str(entry.wjet2_fromHiggs_bdt_tlv.Eta()) + '|' + str(entry.wjet2_fromHiggs_bdt_tlv.Phi()) + '|' + str(entry.wjet2_fromHiggs_bdt_tlv.M())+'\n')

   #w from Had Top BDT tlv
   #for tlv in entry.w_fromHadTop_bdt_tlv:
   fWHadTopBDT_tlv.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(entry.w_fromHadTop_bdt_tlv.Pt()) + '|' + str(entry.w_fromHadTop_bdt_tlv.Eta()) + '|' + str(entry.w_fromHadTop_bdt_tlv.Phi()) + '|' + str(entry.w_fromHadTop_bdt_tlv.M())+'\n')

   #w from Higgs BDT tlv
   #for tlv in entry.w_fromHiggs_bdt_tlv:
   fWHiggsBDT_tlv.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(entry.w_fromHiggs_bdt_tlv.Pt()) + '|' + str(entry.w_fromHiggs_bdt_tlv.Eta()) + '|' + str(entry.w_fromHiggs_bdt_tlv.Phi()) + '|' + str(entry.w_fromHiggs_bdt_tlv.M())+'\n')

   #Higgs BDT tlv
   #for tlv in entry.higgs_bdt_tlv:
   fHiggsBDT_tlv.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(entry.higgs_bdt_tlv.Pt()) + '|' + str(entry.higgs_bdt_tlv.Eta()) + '|' + str(entry.higgs_bdt_tlv.Phi()) + '|' + str(entry.higgs_bdt_tlv.M())+'\n')

   #Had top BDT tlv
   #for tlv in entry.hadTop_bdt_tlv:
   fHadTopBDT_tlv.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(entry.hadTop_bdt_tlv.Pt()) + '|' + str(entry.hadTop_bdt_tlv.Eta()) + '|' + str(entry.hadTop_bdt_tlv.Phi()) + '|' + str(entry.hadTop_bdt_tlv.M())+'\n')

   #Lep top BDT tlv
   #for tlv in entry.lepTop_bdt_tlv:
   fLepTopBDT_tlv.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(entry.lepTop_bdt_tlv.Pt()) + '|' + str(entry.lepTop_bdt_tlv.Eta()) + '|' + str(entry.lepTop_bdt_tlv.Phi()) + '|' + str(entry.lepTop_bdt_tlv.M())+'\n')

   #Lep top Higgs BDT tlv
   #for tlv in entry.lepTop_higgs_bdt_tlv:
   fLepTopHiggsBDT_tlv.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(entry.lepTop_higgs_bdt_tlv.Pt()) + '|' + str(entry.lepTop_higgs_bdt_tlv.Eta()) + '|' + str(entry.lepTop_higgs_bdt_tlv.Phi()) + '|' + str(entry.lepTop_higgs_bdt_tlv.M())+'\n')

   #Had top higgs BDT tlv
   #for tlv in entry.hadTop_higgs_bdt_tlv:
   fHadTopHiggsBDT_tlv.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(entry.hadTop_higgs_bdt_tlv.Pt()) + '|' + str(entry.hadTop_higgs_bdt_tlv.Eta()) + '|' + str(entry.hadTop_higgs_bdt_tlv.Phi()) + '|' + str(entry.hadTop_higgs_bdt_tlv.M())+'\n')

   #Lep top Had top BDT tlv
   #for tlv in entry.lepTop_hadTop_bdt_tlv:
   fLepTopHadTopBDT_tlv.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(entry.lepTop_hadTop_bdt_tlv.Pt()) + '|' + str(entry.lepTop_hadTop_bdt_tlv.Eta()) + '|' + str(entry.lepTop_hadTop_bdt_tlv.Phi()) + '|' + str(entry.lepTop_hadTop_bdt_tlv.M())+'\n')

   #tth BDT tlv
   #for tlv in entry.tth_bdt_tlv:
   ftthBDT_tlv.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(entry.tth_bdt_tlv.Pt()) + '|' + str(entry.tth_bdt_tlv.Eta()) + '|' + str(entry.tth_bdt_tlv.Phi()) + '|' + str(entry.tth_bdt_tlv.M())+'\n')


SampleID = '2'
for entry in ttJetChain:
   #print('work')
   #event
   fEvent.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(entry.mcwgt) + '|' + str(entry.wgt) + '|' + str(entry.higgs_decay) + '|' + str(entry.passTrigger) + '|' + str(entry.reco_score) + '|' + str(entry.norm_score_sum) + '|' + str(entry.num_real_jets_bdt) +  '|' + str(entry.num_jet_matches_truth) + '|' + str(entry.matching_results) + '|' + str(entry.met[0].obj.Pt()) + '|' + str(entry.met[0].obj.Phi()) + '\n' )

   #preselected leptons
   for lep in entry.preselected_leptons:
	fPreLep.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(lep.obj.Pt()) + '|' + str(lep.obj.Eta()) + '|' + str(lep.obj.Phi()) + '|' + str(lep.pdgID) + '|' + str(lep.dxy) + '|' + str(lep.dz) + '|' + str(lep.charge) + '|' + str(lep.relIso) + '|' + str(lep.miniIso) + '|' + str(lep.genPdgID) + '|' + str(lep.isPromptFinalState) + '|' + str(lep.isDirectPromptTauDecayProductFinalState) + '|' + str(lep.genMotherPdgID) + '|' + str(lep.genGrandMotherPdgID) + '|' + str(lep.lepMVA) + '|' + str(lep.miniIsoCharged) + '|' + str(lep.miniIsoNeutral) + '|' + str(lep.jetPtRatio) + '|' + str(lep.jetPtRel) + '|' + str(lep.csv) + '|' + str(lep.sip3D) + '|' + str(lep.jet_nCharged_tracks) + '|' + str(lep.miniAbsIsoCharged) + '|' + str(lep.miniAbsIsoNeutral) + '|' + str(lep.rho) + '|' + str(lep.effArea) + '|' + str(lep.miniIsoR) + '|' + str(lep.miniAbsIsoNeutralcorr) + '\n' )

   #preselected electrons
   for elec in entry.preselected_electrons:
	fPreElec.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(elec.obj.Pt()) + '|' + str(elec.obj.Eta()) + '|' + str(elec.obj.Phi()) + '|' + str(elec.pdgID) + '|' + str(elec.dxy) + '|' + str(elec.dz) + '|' + str(elec.charge) + '|' +  str(elec.relIso) + '|' + str(elec.miniIso) + '|'  + str(elec.genPdgID) + '|'  + str(elec.isPromptFinalState) + '|' + str(elec.isDirectPromptTauDecayProductFinalState) + '|' + str(elec.genMotherPdgID) + '|' + str(elec.genGrandMotherPdgID) + '|' + str(elec.lepMVA) + '|' + str(elec.miniIsoCharged) + '|' + str(elec.miniIsoNeutral) + '|' + str(elec.jetPtRatio) + '|' + str(elec.jetPtRel) + '|' +  str(elec.csv) + '|' + str(elec.sip3D) + '|' + str(elec.jet_nCharged_tracks) + '|' + str(elec.miniAbsIsoCharged) + '|' + str(elec.miniAbsIsoNeutral) + '|' + str(elec.rho) + '|' + str(elec.effArea) + '|' +  str(elec.miniIsoR) + '|' +  str(elec.miniAbsIsoNeutralcorr) + '|'  + str(elec.SCeta) + '|' + str(elec.isGsfCtfScPixChargeConsistent) + '\n')

   #preselected muons
   for muon in entry.preselected_muons:
	fPreMuon.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(muon.obj.Pt()) + '|' + str(muon.obj.Eta()) + '|' + str(muon.obj.Phi()) + '|'  + str(muon.pdgID) + '|' + str(muon.dxy) + '|' + str(muon.dz) + '|' + str(muon.charge) + '|' + str(muon.relIso) + '|' + str(muon.miniIso) + '|' + str(muon.genPdgID) + '|' + str(muon.isPromptFinalState) + '|' + str(muon.isDirectPromptTauDecayProductFinalState) + '|' + str(muon.genMotherPdgID) + '|' + str(muon.genGrandMotherPdgID) + '|' + str(muon.lepMVA) + '|' + str(muon.miniIsoCharged) + '|' + str(muon.miniIsoNeutral) + '|' + str(muon.jetPtRatio) + '|' + str(muon.jetPtRel) + '|' + str(muon.csv) + '|' +  str(muon.sip3D) + '|' + str(muon.jet_nCharged_tracks) + '|' + str(muon.miniAbsIsoCharged) + '|' + str(muon.miniAbsIsoNeutral) + '|' + str(muon.rho) + '|' + str(muon.effArea) + '|' + str(muon.miniIsoR) + '|' + str(muon.miniAbsIsoNeutralcorr) + '|' + str(muon.chargeFlip) + '|' + str(muon.isPFMuon) + '|' + str(muon.isTrackerMuon) + '|' + str(muon.isGlobalMuon) + '|' + str(muon.normalizedChi2) + '|' + str(muon.numberOfValidMuonHits) + '|' + str(muon.numberOfMatchedStations) + '|' + str(muon.numberOfValidPixelHits)  + '|' + str(muon.trackerLayersWithMeasurement) + '|' + str(muon.localChi2) + '|' + str(muon.trKink) + '|' + str(muon.validFrac) + '|'  + str(muon.segCompatibility)+ '\n')

   #preselected taus
   for tau in entry.preselected_taus:
	fPreTau.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(tau.obj.Pt()) + '|' + str(tau.obj.Eta()) + '|' + str(tau.obj.Phi()) + '|'  + str(tau.charge) + '|' + str(tau.genPdgID) + '|' + str(tau.genMotherPdgID) + '|' + str(tau.genGrandMotherPdgID) + '|' + str(tau.dxy) + '|' + str(tau.dz) + '|' + str(tau.decayModeFinding) + '|' + str(tau.mvaID) + '\n')

   #preselected jets
   for jet in entry.preselected_jets:
	fPreJet.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(jet.obj.Pt()) + '|' + str(jet.obj.Eta()) + '|' + str(jet.obj.Phi()) + '|' + str(jet.obj.M()) + '|' + str(jet.charge) + '|' +  str(jet.genPdgID) + '|' + str(jet.genMotherPdgID) + '|' + str(jet.genGrandMotherPdgID) + '|' + str(jet.csv) + '|' + str(jet.qgid) + '|' + str(jet.pdgID) +'\n')

   #pruned genParticles
   for genPart in entry.pruned_genParticles:
	fPrunedGenPart.write(str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(genPart.obj.Pt()) + '|' + str(genPart.obj.Eta()) + '|' + str(genPart.obj.Phi()) + '|' + str(genPart.obj.M()) + '|' + str(genPart.pdgID) + '|' + str(genPart.status) + '|' + str(genPart.isPromptFinalState) + '|' + str(genPart.isPromptDecayed) + '|' + str(genPart.isDirectPromptTauDecayProductFinalState) + '|' + str(genPart.child0) + '|' + str(genPart.child1) + '|' + str(genPart.mother) + '|' + str(genPart.grandmother) + '\n')

   #packed genParticles
   for genPart in entry.packed_genParticles:
	fPackGenPart.write(str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(genPart.obj.Pt()) + '|' + str(genPart.obj.Eta()) + '|' + str(genPart.obj.Phi()) + '|' + str(genPart.obj.M()) + '|' + str(genPart.pdgID) + '|' + str(genPart.status) + '|' + str(genPart.isPromptFinalState) + '|' + str(genPart.isPromptDecayed) + '|' + str(genPart.isDirectPromptTauDecayProductFinalState) + '|' + str(genPart.child0) + '|' + str(genPart.child1) + '|' + str(genPart.mother) + '|' + str(genPart.grandmother) + '\n')
	
   #matched jets
   for jet in entry.matched_jets:
	fMatchJet.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(jet.obj.Pt()) + '|' + str(jet.obj.Eta()) + '|' + str(jet.obj.Phi()) + '|' + str(jet.obj.M()) + '|' + str(jet.charge) + '|' +  str(jet.genPdgID) + '|' + str(jet.genMotherPdgID) + '|' + str(jet.genGrandMotherPdgID) + '|' + str(jet.csv) + '|' + str(jet.qgid) + '|' + str(jet.pdgID) +'\n')

   #matched jets truth
   for jet in entry.matched_jets_truth:
	fMatchJetTruth.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(jet.obj.Pt()) + '|' + str(jet.obj.Eta()) + '|' + str(jet.obj.Phi()) + '|' + str(jet.obj.M()) + '|' + str(jet.charge) + '|' +  str(jet.genPdgID) + '|' + str(jet.genMotherPdgID) + '|' + str(jet.genGrandMotherPdgID) + '|' + str(jet.csv) + '|' + str(jet.qgid) + '|' + str(jet.pdgID) +'\n')

   #leptons from Higgs bdt
   #for lep in entry.lep_fromHiggs_bdt:
   fLepHiggsBDT.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(entry.lep_fromHiggs_bdt.obj.Pt()) + '|' + str(entry.lep_fromHiggs_bdt.obj.Eta()) + '|' + str(entry.lep_fromHiggs_bdt.obj.Phi()) + '|' + str(entry.lep_fromHiggs_bdt.pdgID) + '|' + str(entry.lep_fromHiggs_bdt.dxy) + '|' + str(entry.lep_fromHiggs_bdt.dz) + '|' + str(entry.lep_fromHiggs_bdt.charge) + '|' + str(entry.lep_fromHiggs_bdt.relIso) + '|' + str(entry.lep_fromHiggs_bdt.miniIso) + '|' + str(entry.lep_fromHiggs_bdt.genPdgID) + '|' + str(entry.lep_fromHiggs_bdt.isPromptFinalState) + '|' + str(entry.lep_fromHiggs_bdt.isDirectPromptTauDecayProductFinalState) + '|' + str(entry.lep_fromHiggs_bdt.genMotherPdgID) + '|' + str(entry.lep_fromHiggs_bdt.genGrandMotherPdgID) + '|' + str(entry.lep_fromHiggs_bdt.lepMVA) + '|' + str(entry.lep_fromHiggs_bdt.miniIsoCharged) + '|' + str(entry.lep_fromHiggs_bdt.miniIsoNeutral) + '|' + str(entry.lep_fromHiggs_bdt.jetPtRatio) + '|' + str(entry.lep_fromHiggs_bdt.jetPtRel) + '|' + str(entry.lep_fromHiggs_bdt.csv) + '|' + str(entry.lep_fromHiggs_bdt.sip3D) + '|' + str(entry.lep_fromHiggs_bdt.jet_nCharged_tracks) + '|' + str(entry.lep_fromHiggs_bdt.miniAbsIsoCharged) + '|' + str(entry.lep_fromHiggs_bdt.miniAbsIsoNeutral) + '|' + str(entry.lep_fromHiggs_bdt.rho) + '|' + str(entry.lep_fromHiggs_bdt.effArea) + '|' + str(entry.lep_fromHiggs_bdt.miniIsoR) + '|' + str(entry.lep_fromHiggs_bdt.miniAbsIsoNeutralcorr) + '\n' )

   #leptons from Top bdt
   #for lep in entry.lep_fromTop_bdt:
   fLepTopBDT.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(entry.lep_fromTop_bdt.obj.Pt()) + '|' + str(entry.lep_fromTop_bdt.obj.Eta()) + '|' + str(entry.lep_fromTop_bdt.obj.Phi()) + '|' + str(entry.lep_fromTop_bdt.pdgID) + '|' + str(entry.lep_fromTop_bdt.dxy) + '|' + str(entry.lep_fromTop_bdt.dz) + '|' + str(entry.lep_fromTop_bdt.charge) + '|' + str(entry.lep_fromTop_bdt.relIso) + '|' + str(entry.lep_fromTop_bdt.miniIso) + '|' + str(entry.lep_fromTop_bdt.genPdgID) + '|' + str(entry.lep_fromTop_bdt.isPromptFinalState) + '|' + str(entry.lep_fromTop_bdt.isDirectPromptTauDecayProductFinalState) + '|' + str(entry.lep_fromTop_bdt.genMotherPdgID) + '|' + str(entry.lep_fromTop_bdt.genGrandMotherPdgID) + '|' + str(entry.lep_fromTop_bdt.lepMVA) + '|' + str(entry.lep_fromTop_bdt.miniIsoCharged) + '|' + str(entry.lep_fromTop_bdt.miniIsoNeutral) + '|' + str(entry.lep_fromTop_bdt.jetPtRatio) + '|' + str(entry.lep_fromTop_bdt.jetPtRel) + '|' + str(entry.lep_fromTop_bdt.csv) + '|' + str(entry.lep_fromTop_bdt.sip3D) + '|' + str(entry.lep_fromTop_bdt.jet_nCharged_tracks) + '|' + str(entry.lep_fromTop_bdt.miniAbsIsoCharged) + '|' + str(entry.lep_fromTop_bdt.miniAbsIsoNeutral) + '|' + str(entry.lep_fromTop_bdt.rho) + '|' + str(entry.lep_fromTop_bdt.effArea) + '|' + str(entry.lep_fromTop_bdt.miniIsoR) + '|' + str(entry.lep_fromTop_bdt.miniAbsIsoNeutralcorr) + '\n' )

   #leptons from top truth
   #for lep in entry.lep_fromTop_truth:
   fLepTopTruth.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(entry.lep_fromTop_truth.obj.Pt()) + '|' + str(entry.lep_fromTop_truth.obj.Eta()) + '|' + str(entry.lep_fromTop_truth.obj.Phi()) + '|' + str(entry.lep_fromTop_truth.pdgID) + '|' + str(entry.lep_fromTop_truth.dxy) + '|' + str(entry.lep_fromTop_truth.dz) + '|' + str(entry.lep_fromTop_truth.charge) + '|' + str(entry.lep_fromTop_truth.relIso) + '|' + str(entry.lep_fromTop_truth.miniIso) + '|' + str(entry.lep_fromTop_truth.genPdgID) + '|' + str(entry.lep_fromTop_truth.isPromptFinalState) + '|' + str(entry.lep_fromTop_truth.isDirectPromptTauDecayProductFinalState) + '|' + str(entry.lep_fromTop_truth.genMotherPdgID) + '|' + str(entry.lep_fromTop_truth.genGrandMotherPdgID) + '|' + str(entry.lep_fromTop_truth.lepMVA) + '|' + str(entry.lep_fromTop_truth.miniIsoCharged) + '|' + str(entry.lep_fromTop_truth.miniIsoNeutral) + '|' + str(entry.lep_fromTop_truth.jetPtRatio) + '|' + str(entry.lep_fromTop_truth.jetPtRel) + '|' + str(entry.lep_fromTop_truth.csv) + '|' + str(entry.lep_fromTop_truth.sip3D) + '|' + str(entry.lep_fromTop_truth.jet_nCharged_tracks) + '|' + str(entry.lep_fromTop_truth.miniAbsIsoCharged) + '|' + str(entry.lep_fromTop_truth.miniAbsIsoNeutral) + '|' + str(entry.lep_fromTop_truth.rho) + '|' + str(entry.lep_fromTop_truth.effArea) + '|' + str(entry.lep_fromTop_truth.miniIsoR) + '|' + str(entry.lep_fromTop_truth.miniAbsIsoNeutralcorr) + '\n' )

   #leptons from Higgs truth
   #for lep in entry.lep_fromHiggs_truth:
   fLepHiggsTruth.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(entry.lep_fromHiggs_truth.obj.Pt()) + '|' + str(entry.lep_fromHiggs_truth.obj.Eta()) + '|' + str(entry.lep_fromHiggs_truth.obj.Phi()) + '|' + str(entry.lep_fromHiggs_truth.pdgID) + '|' + str(entry.lep_fromHiggs_truth.dxy) + '|' + str(entry.lep_fromHiggs_truth.dz) + '|' + str(entry.lep_fromHiggs_truth.charge) + '|' + str(entry.lep_fromHiggs_truth.relIso) + '|' + str(entry.lep_fromHiggs_truth.miniIso) + '|' + str(entry.lep_fromHiggs_truth.genPdgID) + '|' + str(entry.lep_fromHiggs_truth.isPromptFinalState) + '|' + str(entry.lep_fromHiggs_truth.isDirectPromptTauDecayProductFinalState) + '|' + str(entry.lep_fromHiggs_truth.genMotherPdgID) + '|' + str(entry.lep_fromHiggs_truth.genGrandMotherPdgID) + '|' + str(entry.lep_fromHiggs_truth.lepMVA) + '|' + str(entry.lep_fromHiggs_truth.miniIsoCharged) + '|' + str(entry.lep_fromHiggs_truth.miniIsoNeutral) + '|' + str(entry.lep_fromHiggs_truth.jetPtRatio) + '|' + str(entry.lep_fromHiggs_truth.jetPtRel) + '|' + str(entry.lep_fromHiggs_truth.csv) + '|' + str(entry.lep_fromHiggs_truth.sip3D) + '|' + str(entry.lep_fromHiggs_truth.jet_nCharged_tracks) + '|' + str(entry.lep_fromHiggs_truth.miniAbsIsoCharged) + '|' + str(entry.lep_fromHiggs_truth.miniAbsIsoNeutral) + '|' + str(entry.lep_fromHiggs_truth.rho) + '|' + str(entry.lep_fromHiggs_truth.effArea) + '|' + str(entry.lep_fromHiggs_truth.miniIsoR) + '|' + str(entry.lep_fromHiggs_truth.miniAbsIsoNeutralcorr) + '\n' )

   #Leptons from Top BDT tlv
   #for tlv in entry.lep_fromTop_bdt_tlv:
   fLepTopBDT_tlv.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(entry.lep_fromTop_bdt_tlv.Pt()) + '|' + str(entry.lep_fromTop_bdt_tlv.Eta()) + '|' + str(entry.lep_fromTop_bdt_tlv.Phi()) + '|' + str(entry.lep_fromTop_bdt_tlv.M())+'\n')

   #Leptons from Higgs BDT tlv
   #for tlv in entry.lep_fromHiggs_bdt_tlv:
   fLepHiggsBDT_tlv.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(entry.lep_fromHiggs_bdt_tlv.Pt()) + '|' + str(entry.lep_fromHiggs_bdt_tlv.Eta()) + '|' + str(entry.lep_fromHiggs_bdt_tlv.Phi()) + '|' + str(entry.lep_fromHiggs_bdt_tlv.M())+'\n')

   #bJet from Had Top BDT tlv
   #for tlv in entry.bjet_fromHadTop_bdt_tlv:
   fBJetHadTopBDT_tlv.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(entry.bjet_fromHadTop_bdt_tlv.Pt()) + '|' + str(entry.bjet_fromHadTop_bdt_tlv.Eta()) + '|' + str(entry.bjet_fromHadTop_bdt_tlv.Phi()) + '|' + str(entry.bjet_fromHadTop_bdt_tlv.M())+'\n')

   #bJet from Lep Top BDT tlv
   #for tlv in entry.bjet_fromLepTop_bdt_tlv:
   fBJetLepTopBDT_tlv.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(entry.bjet_fromLepTop_bdt_tlv.Pt()) + '|' + str(entry.bjet_fromLepTop_bdt_tlv.Eta()) + '|' + str(entry.bjet_fromLepTop_bdt_tlv.Phi()) + '|' + str(entry.bjet_fromLepTop_bdt_tlv.M())+'\n')

   #wJet 1 from Had Top BDT tlv
   #for tlv in entry.wjet1_fromHadTop_bdt_tlv:
   fWJet1HadTopBDT_tlv.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(entry.wjet1_fromHadTop_bdt_tlv.Pt()) + '|' + str(entry.wjet1_fromHadTop_bdt_tlv.Eta()) + '|' + str(entry.wjet1_fromHadTop_bdt_tlv.Phi()) + '|' + str(entry.wjet1_fromHadTop_bdt_tlv.M())+'\n')

   #wJet 1 from Had Top BDT tlv
   #for tlv in entry.wjet2_fromHadTop_bdt_tlv:
   fWJet2HadTopBDT_tlv.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(entry.wjet2_fromHadTop_bdt_tlv.Pt()) + '|' + str(entry.wjet2_fromHadTop_bdt_tlv.Eta()) + '|' + str(entry.wjet2_fromHadTop_bdt_tlv.Phi()) + '|' + str(entry.wjet2_fromHadTop_bdt_tlv.M())+'\n')

   #wJet 1 from Higgs BDT tlv
   #for tlv in entry.wjet1_fromHiggs_bdt_tlv:
   fWJet1HiggsBDT_tlv.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(entry.wjet1_fromHiggs_bdt_tlv.Pt()) + '|' + str(entry.wjet1_fromHiggs_bdt_tlv.Eta()) + '|' + str(entry.wjet1_fromHiggs_bdt_tlv.Phi()) + '|' + str(entry.wjet1_fromHiggs_bdt_tlv.M())+'\n')

   #wJet 2 from Higgs BDT tlv
   #for tlv in entry.wjet2_fromHiggs_bdt_tlv:
   fWJet2HiggsBDT_tlv.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(entry.wjet2_fromHiggs_bdt_tlv.Pt()) + '|' + str(entry.wjet2_fromHiggs_bdt_tlv.Eta()) + '|' + str(entry.wjet2_fromHiggs_bdt_tlv.Phi()) + '|' + str(entry.wjet2_fromHiggs_bdt_tlv.M())+'\n')

   #w from Had Top BDT tlv
   #for tlv in entry.w_fromHadTop_bdt_tlv:
   fWHadTopBDT_tlv.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(entry.w_fromHadTop_bdt_tlv.Pt()) + '|' + str(entry.w_fromHadTop_bdt_tlv.Eta()) + '|' + str(entry.w_fromHadTop_bdt_tlv.Phi()) + '|' + str(entry.w_fromHadTop_bdt_tlv.M())+'\n')

   #w from Higgs BDT tlv
   #for tlv in entry.w_fromHiggs_bdt_tlv:
   fWHiggsBDT_tlv.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(entry.w_fromHiggs_bdt_tlv.Pt()) + '|' + str(entry.w_fromHiggs_bdt_tlv.Eta()) + '|' + str(entry.w_fromHiggs_bdt_tlv.Phi()) + '|' + str(entry.w_fromHiggs_bdt_tlv.M())+'\n')

   #Higgs BDT tlv
   #for tlv in entry.higgs_bdt_tlv:
   fHiggsBDT_tlv.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(entry.higgs_bdt_tlv.Pt()) + '|' + str(entry.higgs_bdt_tlv.Eta()) + '|' + str(entry.higgs_bdt_tlv.Phi()) + '|' + str(entry.higgs_bdt_tlv.M())+'\n')

   #Had top BDT tlv
   #for tlv in entry.hadTop_bdt_tlv:
   fHadTopBDT_tlv.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(entry.hadTop_bdt_tlv.Pt()) + '|' + str(entry.hadTop_bdt_tlv.Eta()) + '|' + str(entry.hadTop_bdt_tlv.Phi()) + '|' + str(entry.hadTop_bdt_tlv.M())+'\n')

   #Lep top BDT tlv
   #for tlv in entry.lepTop_bdt_tlv:
   fLepTopBDT_tlv.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(entry.lepTop_bdt_tlv.Pt()) + '|' + str(entry.lepTop_bdt_tlv.Eta()) + '|' + str(entry.lepTop_bdt_tlv.Phi()) + '|' + str(entry.lepTop_bdt_tlv.M())+'\n')

   #Lep top Higgs BDT tlv
   #for tlv in entry.lepTop_higgs_bdt_tlv:
   fLepTopHiggsBDT_tlv.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(entry.lepTop_higgs_bdt_tlv.Pt()) + '|' + str(entry.lepTop_higgs_bdt_tlv.Eta()) + '|' + str(entry.lepTop_higgs_bdt_tlv.Phi()) + '|' + str(entry.lepTop_higgs_bdt_tlv.M())+'\n')

   #Had top higgs BDT tlv
   #for tlv in entry.hadTop_higgs_bdt_tlv:
   fHadTopHiggsBDT_tlv.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(entry.hadTop_higgs_bdt_tlv.Pt()) + '|' + str(entry.hadTop_higgs_bdt_tlv.Eta()) + '|' + str(entry.hadTop_higgs_bdt_tlv.Phi()) + '|' + str(entry.hadTop_higgs_bdt_tlv.M())+'\n')

   #Lep top Had top BDT tlv
   #for tlv in entry.lepTop_hadTop_bdt_tlv:
   fLepTopHadTopBDT_tlv.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(entry.lepTop_hadTop_bdt_tlv.Pt()) + '|' + str(entry.lepTop_hadTop_bdt_tlv.Eta()) + '|' + str(entry.lepTop_hadTop_bdt_tlv.Phi()) + '|' + str(entry.lepTop_hadTop_bdt_tlv.M())+'\n')

   #tth BDT tlv
   #for tlv in entry.tth_bdt_tlv:
   ftthBDT_tlv.write( str(entry.runNumber) + '|' + str(entry.lumiBlock) + '|' + str(entry.eventnum) + '|' + SampleID + '|' + str(entry.tth_bdt_tlv.Pt()) + '|' + str(entry.tth_bdt_tlv.Eta()) + '|' + str(entry.tth_bdt_tlv.Phi()) + '|' + str(entry.tth_bdt_tlv.M())+'\n')

fPreLep.close()
fPreElec.close()
fPreMuon.close()
fPreTau.close()
fPreJet.close()
fPrunedGenPart.close()
fPackGenPart.close()
fMatchJet.close()
fMatchJetTruth.close()
fLepHiggsBDT.close()
fLepTopBDT.close()
fLepTopTruth.close()
fLepHiggsTruth.close()
fEvent.close()
#tlv files
fLepTopBDT_tlv.close()
fLepHiggsBDT_tlv.close()
fLepTopBDT_tlv.close()
fBJetHadTopBDT_tlv.close()
fBJetLepTopBDT_tlv.close()
fWJet1HadTopBDT_tlv.close()
fWJet2HadTopBDT_tlv.close()
fWJet1HiggsBDT_tlv.close()
fWJet2HiggsBDT_tlv.close()
fWHadTopBDT_tlv.close()
fWHiggsBDT_tlv.close()
fHiggsBDT_tlv.close()
fHadTopBDT_tlv.close()
fLepTopBDT_tlv.close()
fLepTopHiggsBDT_tlv.close()
fHadTopHiggsBDT_tlv.close()
fLepTopHadTopBDT_tlv.close()
ftthBDT_tlv.close()

endTime = time.time() - startTime

print('total time: {}'.format(endTime))

	

