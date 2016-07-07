#!/opt/vertica/oss/python/bin/python

import hp_vertica_client
import os
import time

def main():
   startTime = time.time()
   conn = hp_vertica_client.connect("")
   cur = conn.cursor()
   
   cur.execute("drop table if exists preselected_jets_small cascade")

   cur.execute("drop table if exists preselected_leptons_small  cascade")

   cur.execute("drop table if exists preselected_electrons_small cascade")

   cur.execute("drop table if exists event_info_small cascade")

   cur.execute("DROP TABLE IF EXISTS preselected_muons_small  CASCADE")

   cur.execute("DROP TABLE IF EXISTS preselected_taus_small  CASCADE")
   cur.execute("DROP TABLE IF EXISTS pruned_gen_particles_small CASCADE")
   cur.execute("DROP TABLE IF EXISTS packed_gen_particles_small CASCADE")
   cur.execute("DROP TABLE IF EXISTS matched_jets_small CASCADE")
   cur.execute("DROP TABLE IF EXISTS matched_jets_truth_small CASCADE")
   cur.execute("DROP TABLE IF EXISTS lep_fromHiggs_bdt_small CASCADE")
   cur.execute("DROP TABLE IF EXISTS lep_fromTop_bdt_small CASCADE")
   cur.execute("DROP TABLE IF EXISTS lep_fromTop_truth_small CASCADE")
   cur.execute("DROP TABLE IF EXISTS lep_fromHiggs_truth_small CASCADE")
   cur.execute("DROP TABLE IF EXISTS lep_fromTop_bdt_tlv_small CASCADE")
   cur.execute("DROP TABLE IF EXISTS lep_fromHiggs_bdt_tlv_small CASCADE")
   cur.execute("DROP TABLE IF EXISTS bjet_fromHadTop_bdt_tlv_small CASCADE")
   cur.execute("DROP TABLE IF EXISTS bjet_fromLepTop_bdt_tlv_small CASCADE")
   cur.execute("DROP TABLE IF EXISTS wjet1_fromHadTop_bdt_tlv_small CASCADE")
   cur.execute("DROP TABLE IF EXISTS wjet2_fromHadTop_bdt_tlv_small CASCADE")
   cur.execute("DROP TABLE IF EXISTS wjet1_fromHiggs_bdt_tlv_small CASCADE")
   cur.execute("DROP TABLE IF EXISTS wjet2_fromHiggs_bdt_tlv_small CASCADE")
   cur.execute("DROP TABLE IF EXISTS w_fromHadTop_bdt_tlv_small CASCADE")
   cur.execute("DROP TABLE IF EXISTS w_fromHiggs_bdt_tlv_small CASCADE")
   cur.execute("DROP TABLE IF EXISTS higgs_bdt_tlv_small CASCADE")
   cur.execute("DROP TABLE IF EXISTS hadTop_bdt_tlv_small CASCADE")
   cur.execute("DROP TABLE IF EXISTS lepTop_bdt_tlv_small CASCADE")
   cur.execute("DROP TABLE IF EXISTS lepTop_higgs_bdt_tlv_small CASCADE")
   cur.execute("DROP TABLE IF EXISTS hadTop_higgs_bdt_tlv_small CASCADE")
   cur.execute("DROP TABLE IF EXISTS lepTop_hadTop_bdt_tlv_small CASCADE")
   cur.execute("DROP TABLE IF EXISTS tth_bdt_tlv_small CASCADE")
   cur.execute("DROP TABLE IF EXISTS passTrigger_small")
   cur.execute("DROP TABLE IF EXISTS matching_results_small")

  
   #event table 
   cur.execute("create table event_info_small (Run int, Lumi int, Event int, SampleID int, mcwgt float, wgt float, higgs_decay float, reco_score float, norm_score_sum float, num_real_jets_bdt float, num_jet_matches_truth float, metPt float, metPhi float, PRIMARY KEY (Run, Lumi, Event, SampleID))")
   #copy event table
   cur.execute("COPY event_info_small FROM '/home/newdbadmin/skimmingPhase/smallInput/event.txt'")


   #passTrigger table
   cur.execute("create table passTrigger_small (Run int, Lumi int, Event int, SampleID int, passTrigger varchar, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info_small(Run, Lumi, Event, SampleID))" )
   #copy table - no passtrig file
   #cur.execute("COPY passTrigger_small FROM '/home/newdbadmin/skimmingPhase/smallInput/passTrigger.txt'")

   #matching Results table
   cur.execute("create table matching_results_small (Run int, Lumi int, Event int, SampleID int, passTrigger varchar, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info_small(Run, Lumi, Event, SampleID))" )
   #copy table - no match results file
   #cur.execute("COPY matching_results_small FROM '/home/newdbadmin/skimmingPhase/smallInput/matchingResults/*' GZIP")
   
   #preselected lepton table
   cur.execute("create table preselected_leptons_small (Run int, Lumi int, Event int, SampleID int, Pt float, Eta float, Phi float, pidgID float, dxy float, dz float, Charge float, relIso float, miniIso float, genPdgID float, isPromptFinalState float, isDirectPromptTauDecayProductFinalState float, genMotherPdgID float, genGrandMotherPdgID float, lepMVA float, miniIsoCharged float, miniIsoNeutral float, jetPtRatio float, jetPtRel float, csv float, sip3D float, jet_nCharged_tracks float, miniAbsIsoCharged float, miniAbsIsoNeutral float, rho float, effArea float, minIsoR float, miniAbsIsoNeutralcorr float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info_small(Run, Lumi, Event, SampleID))" )
   #copy preselected lepton table
   cur.execute("COPY preselected_leptons_small FROM '/home/newdbadmin/skimmingPhase/smallInput/preLep.txt'")

   #preselected electrons table
   cur.execute("create table preselected_electrons_small (Run int, Lumi int, Event int, SampleID int, Pt float, Eta float, Phi float, pdgID float, dxy float, dz float, charge float, relIso float, miniIso float, genPdgID float, isPromptFinalState float, isDirectPrompTauDecayProductFinalState float, genMotherPdgID float, genGrandMotherPdgID float, lepMVA float, miniIsoCharged float, miniIsoNeutral float, jetPtRatio float, jetPtRel float, csv float, sip3D float, jet_nCharged_tracks float, miniAbsIsoCharged float, minAbsIsoNeutral float, rho float, effArea float, miniIsoR float, miniAbsIsoNeutralcorr float, SCeta float, isGsfCtfScPixChargeConsistent float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info_small(Run, Lumi, Event, SampleID))")
   #copy preselected electrons table
   cur.execute("COPY preselected_electrons_small FROM '/home/newdbadmin/skimmingPhase/smallInput/preElec.txt' ") 

   #preselected muons table
   cur.execute("CREATE TABLE preselected_muons_small (Run int, Lumi int, Event int, SampleID int, Pt float, Eta float, Phi float, pdgID float, dxy float, dz float, charge float, relIso float, miniIso float, genPdgID float, isPromptFinalState float, isDirectPrompTauDecayProductFinalState float, genMotherPdgID float, genGrandMotherPdgID float, lepMVA float, miniIsoCharged float, miniIsoNeutral float, jetPtRatio float, jetPtRel float, csv float, sip3D float, jet_nCharged_tracks float, miniAbsIsoCharged float, minAbsIsoNeutral float, rho float, effArea float, miniIsoR float, miniAbsIsoNeutralcorr float, chargeFlip float, isPFMuon float, isTrackerMuon float, isGlobalMuon float, normalizedChi2 float, numberOfValidMuonHits float, numberOfMatchedStations float, numberOfValidPixelHits float, trackerLayersWithMeasurement float, localChi2 float, trKink float, validFrac float, segCompatibility float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info_small(Run, Lumi, Event, SampleID))")
   #copy preselected muons table
   cur.execute("COPY preselected_muons_small FROM '/home/newdbadmin/skimmingPhase/smallInput/preMuon.txt'")
   
   #preslected taus
   cur.execute("CREATE TABLE preselected_taus_small (Run int, Lumi int, Event int, SampleID int, Pt float, Eta float, Phi float, charge float, genPdgID float, genMotherPdgID float, genGrandMotherPdgID float, csv float, qgid float, pdgID float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info_small(Run, Lumi, Event, SampleID))") 
   #copy preselected taus table
   cur.execute("COPy preselected_taus FROM '/home/newdbadmin/skimmingPhase/smallInput/preTau.txt' ")

   #preselected jets
   cur.execute("create table preselected_jets_small (Run int, Lumi int, Event int, SampleID int, Pt float, Eta float, Phi float, Mass float, Charge float, genPdgID float, genMotherPdgID float, genGrandMotherPdgID float, csv float, qgid float, pdgID float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info_small(Run, Lumi, Event, SampleID))" )
   #copy preselected jes
   cur.execute("COPY preselected_jets_small FROM '/home/newdbadmin/skimmingPhase/smallInput/preJet.txt' ")

   #Pruned gen particles
   cur.execute("CREATE TABLE pruned_gen_Particles_small (Run int, Lumi int, Event int, SampleID int, Pt float, Eta float, Phi float, Mass float, pdgID float, status float, isPromptFinalState float, isPromptDecayed float, isDirectPromptTauDecayProductFinalState float, child0 float, child1 float, mother float, grandmother float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info_small(Run, Lumi, Event, SampleID))")
   cur.execute("COPY pruned_gen_Particles_small FROM '/home/newdbadmin/skimmingPhase/smallInput/prunedGenPart.txt' ")

   #packed gen particles
   cur.execute("CREATE TABLE packed_gen_Particles_small (Run int, Lumi int, Event int, SampleID int, Pt float, Eta float, Phi float, Mass float, pdgID float, status float, isPromptFinalState float, isPromptDecayed float, isDirectPromptTauDecayProductFinalState float, child0 float, child1 float, mother float, grandmother float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info_small(Run, Lumi, Event, SampleID))")
   #copy packed gen particles
   cur.execute("COPY packed_gen_Particles_small FROM '/home/newdbadmin/skimmingPhase/smallInput/prunedGenPart.txt' ")

   #Matched jets
   cur.execute("CREATE TABLE matched_jets_small (Run int, Lumi int, Event int, SampleID int, Pt float, Eta float, Phi float, Mass float, charge float, genPdgID float, genMotherPdgID float, genGrandMotherPdgID float, csv float, qgid float, pdgID float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info_small(Run, Lumi, Event, SampleID))")
   #copy matched jets
   cur.execute("COPY matched_jets_small FROM '/home/newdbadmin/skimmingPhase/smallInput/matchJet.txt' ")
  
   #Matched jets truth
   cur.execute("CREATE TABLE matched_jets_truth_small (Run int, Lumi int, Event int, SampleID int, Pt float, Eta float, Phi float, Mass float, charge float, genPdgID float, genMotherPdgID float, genGrandMotherPdgID float, csv float, qgid float, pdgID float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info_small(Run, Lumi, Event, SampleID))")
   #copy matched jets truth
   cur.execute("COPY matched_jets_truth_small FROM '/home/newdbadmin/skimmingPhase/smallInput/matchJetTruth.txt' ")

   #lep from Higgs BDT
   cur.execute("create table lep_fromHiggs_bdt_small (Run int, Lumi int, Event int, SampleID int, Pt float, Eta float, Phi float, pidgID float, dxy float, dz float, Charge float, relIso float, miniIso float, genPdgID float, isPromptFinalState float, isDirectPromptTauDecayProductFinalState float, genMotherPdgID float, genGrandMotherPdgID float, lepMVA float, miniIsoCharged float, miniIsoNeutral float, jetPtRatio float, jetPtRel float, csv float, sip3D float, jet_nCharged_tracks float, miniAbsIsoCharged float, miniAbsIsoNeutral float, rho float, effArea float, minIsoR float, miniAbsIsoNeutralcorr float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info_small(Run, Lumi, Event, SampleID))" )
   #copy lep from Higgs BDT table
   cur.execute("COPY lep_fromHiggs_bdt_small FROM '/home/newdbadmin/skimmingPhase/smallInput/lepHiggsBDT.txt' ")
   
   #lep from Top BDT
   cur.execute("create table lep_fromTop_bdt_small (Run int, Lumi int, Event int, SampleID int, Pt float, Eta float, Phi float, pidgID float, dxy float, dz float, Charge float, relIso float, miniIso float, genPdgID float, isPromptFinalState float, isDirectPromptTauDecayProductFinalState float, genMotherPdgID float, genGrandMotherPdgID float, lepMVA float, miniIsoCharged float, miniIsoNeutral float, jetPtRatio float, jetPtRel float, csv float, sip3D float, jet_nCharged_tracks float, miniAbsIsoCharged float, miniAbsIsoNeutral float, rho float, effArea float, minIsoR float, miniAbsIsoNeutralcorr float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info_small(Run, Lumi, Event, SampleID))" )
   #copy lep from Top BDT table
   cur.execute("COPY lep_fromTop_bdt_small FROM '/home/newdbadmin/skimmingPhase/smallInput/lepTopBDT.txt' ")
 
   #lep from Top Truth
   cur.execute("create table lep_fromTop_truth_small (Run int, Lumi int, Event int, SampleID int, Pt float, Eta float, Phi float, pidgID float, dxy float, dz float, Charge float, relIso float, miniIso float, genPdgID float, isPromptFinalState float, isDirectPromptTauDecayProductFinalState float, genMotherPdgID float, genGrandMotherPdgID float, lepMVA float, miniIsoCharged float, miniIsoNeutral float, jetPtRatio float, jetPtRel float, csv float, sip3D float, jet_nCharged_tracks float, miniAbsIsoCharged float, miniAbsIsoNeutral float, rho float, effArea float, minIsoR float, miniAbsIsoNeutralcorr float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info_small(Run, Lumi, Event, SampleID))" )
   #copy lep from Top truth table
   cur.execute("COPY lep_fromTop_truth_small FROM '/home/newdbadmin/skimmingPhase/smallInput/lepTopTruth.txt' ")

   #lep from Higgs Truth
   cur.execute("create table lep_fromHiggs_truth_small (Run int, Lumi int, Event int, SampleID int, Pt float, Eta float, Phi float, pidgID float, dxy float, dz float, Charge float, relIso float, miniIso float, genPdgID float, isPromptFinalState float, isDirectPromptTauDecayProductFinalState float, genMotherPdgID float, genGrandMotherPdgID float, lepMVA float, miniIsoCharged float, miniIsoNeutral float, jetPtRatio float, jetPtRel float, csv float, sip3D float, jet_nCharged_tracks float, miniAbsIsoCharged float, miniAbsIsoNeutral float, rho float, effArea float, minIsoR float, miniAbsIsoNeutralcorr float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info_small(Run, Lumi, Event, SampleID))" )
   #copy lep from Higgs truth table
   #cur.execute("COPY lep_fromHiggs_truth_small FROM '/home/newdbadmin/skimmingPhase/smallInput/lepHiggsTruth.txt' ")

   #lep from top BDT tlv_small
   cur.execute("create table lep_fromTop_bdt_tlv_small (Run int, Lumi int, Event int, SampleID int, Pt float, Eta float, Phi float, Mass float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info_small(Run, Lumi, Event, SampleID))")
   #copy lep from top bdt tlv_small
   #cur.execute("COPY lep_fromTop_bdt_tlv_small FROM '/home/newdbadmin/skimmingPhase/smallInput/lepFromTopBDT_tlv.txt' ")


   #lep from Higgs BDT tlv_small
   cur.execute("create table lep_fromHiggs_bdt_tlv_small (Run int, Lumi int, Event int, SampleID int, Pt float, Eta float, Phi float, Mass float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info_small(Run, Lumi, Event, SampleID))")
   #copy lep from Higgs bdt tlv_small
   cur.execute("COPY lep_fromHiggs_bdt_tlv_small FROM '/home/newdbadmin/skimmingPhase/smallInput/lepHiggsBDT_tlv.txt*' ")
  
   #bJet from Had Top BDT tlv_small
   cur.execute("create table bJet_fromHadTop_bdt_tlv_small (Run int, Lumi int, Event int, SampleID int, Pt float, Eta float, Phi float, Mass float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info_small(Run, Lumi, Event, SampleID))")
   #copy bJet from Had top bdt tlv_small
   cur.execute("COPY bJet_fromHadTop_bdt_tlv_small FROM '/home/newdbadmin/skimmingPhase/smallInput/bJetHadTopBDT_tlv.txt' ")

   #bJet from Lep Top BDT tlv_small
   cur.execute("create table bJet_fromLepTop_bdt_tlv_small (Run int, Lumi int, Event int, SampleID int, Pt float, Eta float, Phi float, Mass float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info_small(Run, Lumi, Event, SampleID))")
   #copy bJet from Lep top bdt tlv_small
   cur.execute("COPY bJet_fromLepTop_bdt_tlv_small FROM '/home/newdbadmin/skimmingPhase/smallInput/bJetLepTopBDT_tlv.txt' ")

   #wJet1 from Had Top BDT tlv_small
   cur.execute("create table wJet1_fromHadTop_bdt_tlv_small (Run int, Lumi int, Event int, SampleID int, Pt float, Eta float, Phi float, Mass float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info_small(Run, Lumi, Event, SampleID))")
   #copy wJet1 from Had top bdt tlv_small
   cur.execute("COPY wJet1_fromHadTop_bdt_tlv_small FROM '/home/newdbadmin/skimmingPhase/smallInput/wJet1HadTopBDT_tlv.txt' ")

   #wJet from Had Top BDT tlv_small
   cur.execute("create table wJet2_fromHadTop_bdt_tlv_small (Run int, Lumi int, Event int, SampleID int, Pt float, Eta float, Phi float, Mass float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info_small(Run, Lumi, Event, SampleID))")
   #copy wJet2 from Had top bdt tlv_small
   cur.execute("COPY wJet2_fromHadTop_bdt_tlv_small FROM '/home/newdbadmin/skimmingPhase/smallInput/wJet2HadTopBDT_tlv.txt' ")

   #wJet1 from Higgs BDT tlv_small
   cur.execute("create table wJet1_fromHiggs_bdt_tlv_small (Run int, Lumi int, Event int, SampleID int, Pt float, Eta float, Phi float, Mass float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info_small(Run, Lumi, Event, SampleID))")
   #copy wJet1 from Higgs bdt tlv_small
   cur.execute("COPY wJet1_fromHiggs_bdt_tlv_small FROM '/home/newdbadmin/skimmingPhase/smallInput/wJet1HiggsBDT_tlv.txt' ")

   #wJet2 from Higgs BDT tlv_small
   cur.execute("create table wJet2_fromHiggs_bdt_tlv_small (Run int, Lumi int, Event int, SampleID int, Pt float, Eta float, Phi float, Mass float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info_small(Run, Lumi, Event, SampleID))")
   #copy wJet2 from Higgs bdt tlv_small
   cur.execute("COPY wJet2_fromHiggs_bdt_tlv_small FROM '/home/newdbadmin/skimmingPhase/smallInput/wJet2HiggsBDT_tlv.txt' ")

   #w from Had Top BDT tlv_small
   cur.execute("create table w_fromHadTop_bdt_tlv_small (Run int, Lumi int, Event int, SampleID int, Pt float, Eta float, Phi float, Mass float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info_small(Run, Lumi, Event, SampleID))")
   #copy w from Had top bdt tlv_small
   cur.execute("COPY w_fromHadTop_bdt_tlv_small FROM '/home/newdbadmin/skimmingPhase/smallInput/wHadTopBDT_tlv.txt' ")

   #w from Higgs BDT tlv_small
   cur.execute("create table w_fromHiggs_bdt_tlv_small (Run int, Lumi int, Event int, SampleID int, Pt float, Eta float, Phi float, Mass float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info_small(Run, Lumi, Event, SampleID))")
   #copy w from Higgs bdt tlv_small
   cur.execute("COPY w_fromHiggs_bdt_tlv_small FROM '/home/newdbadmin/skimmingPhase/smallInput/wHiggsBDT_tlv.txt' ")

   #Higgs BDT tlv_small
   cur.execute("create table Higgs_bdt_tlv_small (Run int, Lumi int, Event int, SampleID int, Pt float, Eta float, Phi float, Mass float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info_small(Run, Lumi, Event, SampleID))")
   #copy Higgs bdt tlv_small
   cur.execute("COPY Higgs_bdt_tlv_small FROM '/home/newdbadmin/skimmingPhase/smallInput/higgsBDT_tlv.txt' ")

   #Had top BDT tlv_small
   cur.execute("create table HadTop_bdt_tlv_small (Run int, Lumi int, Event int, SampleID int, Pt float, Eta float, Phi float, Mass float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info_small(Run, Lumi, Event, SampleID))")
   #copy Had bdt tlv_small
   cur.execute("COPY HadTop_bdt_tlv_small FROM '/home/newdbadmin/skimmingPhase/smallInput/hadTopBDT_tlv.txt'")

   #Lep top BDT tlv_small
   cur.execute("create table LepTop_bdt_tlv_small (Run int, Lumi int, Event int, SampleID int, Pt float, Eta float, Phi float, Mass float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info_small(Run, Lumi, Event, SampleID))")
   #copy Lep top bdt tlv_small
   cur.execute("COPY LepTop_bdt_tlv_small FROM '/home/newdbadmin/skimmingPhase/smallInput/lepTopBDT_tlv.txt' ")

   #Lep top Higgs BDT tlv_small
   cur.execute("create table LepTop_Higgs_bdt_tlv_small (Run int, Lumi int, Event int, SampleID int, Pt float, Eta float, Phi float, Mass float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info_small(Run, Lumi, Event, SampleID))")
   #copy Lep top Higgs bdt tlv_small
   cur.execute("COPY LepTop_Higgs_bdt_tlv_small FROM '/home/newdbadmin/skimmingPhase/smallInput/lepTopHiggsBDT_tlv.txt'")

   #Had top Higgs BDT tlv_small
   cur.execute("create table HadTop_Higgs_bdt_tlv_small (Run int, Lumi int, Event int, SampleID int, Pt float, Eta float, Phi float, Mass float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info_small(Run, Lumi, Event, SampleID))")
   #copy Had top Higgs bdt tlv_small
   cur.execute("COPY HadTop_Higgs_bdt_tlv_small FROM '/home/newdbadmin/skimmingPhase/smallInput/hadTopHiggsBDT_tlv.txt' ")

   #Lep top Had top BDT tlv_small
   cur.execute("create table LepTopHadTop_bdt_tlv_small (Run int, Lumi int, Event int, SampleID int, Pt float, Eta float, Phi float, Mass float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info_small(Run, Lumi, Event, SampleID))")
   #copy Lep top Had top bdt tlv_small
   cur.execute("COPY LepTopHadTop_Higgs_bdt_tlv_small FROM '/home/newdbadmin/skimmingPhase/smallInput/lepTopHadTopBDT_tlv.txt'")

   #tth BDT tlv_small
   cur.execute("create table tth_bdt_tlv_small (Run int, Lumi int, Event int, SampleID int, Pt float, Eta float, Phi float, Mass float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info_small(Run, Lumi, Event, SampleID))")
   #copy tth bdt tlv_small
   cur.execute("COPY tth_bdt_tlv_small FROM '/home/newdbadmin/skimmingPhase/smallInput/tthBDT_tlv.txt'")


   cur.execute("commit")
      
   tableTime = time.time() - startTime
   queryStart = time.time()
   #query = " select Pt from jets;"

   #cur.execute(query)

   queryTime = time.time() - queryStart
   totalTime = time.time() - startTime

   print('Fill table: {}\nQuery time: {}\nTotal: {}'.format(tableTime, queryTime, totalTime) )

if __name__== "__main__":
   main()
