#!/opt/vertica/oss/python/bin/python

import hp_vertica_client
import os
import time

def main():
   startTime = time.time()
   conn = hp_vertica_client.connect("")
   cur = conn.cursor()
   
   cur.execute("drop table if exists preselected_jets cascade")

   cur.execute("drop table if exists preselected_leptons  cascade")

   cur.execute("drop table if exists preselected_electrons cascade")

   cur.execute("drop table if exists event_info cascade")

   cur.execute("DROP TABLE IF EXISTS preselected_muons  CASCADE")

   cur.execute("DROP TABLE IF EXISTS preselected_taus  CASCADE")
   cur.execute("DROP TABLE IF EXISTS pruned_gen_particles CASCADE")
   cur.execute("DROP TABLE IF EXISTS packed_gen_particles CASCADE")
   cur.execute("DROP TABLE IF EXISTS matched_jets CASCADE")
   cur.execute("DROP TABLE IF EXISTS matched_jets_truth CASCADE")
   cur.execute("DROP TABLE IF EXISTS lep_fromHiggs_bdt CASCADE")
   cur.execute("DROP TABLE IF EXISTS lep_fromTop_bdt CASCADE")
   cur.execute("DROP TABLE IF EXISTS lep_fromTop_truth CASCADE")
   cur.execute("DROP TABLE IF EXISTS lep_fromHiggs_truth CASCADE")
   cur.execute("DROP TABLE IF EXISTS lep_fromTop_bdt_tlv CASCADE")
   cur.execute("DROP TABLE IF EXISTS lep_fromHiggs_bdt_tlv CASCADE")
   cur.execute("DROP TABLE IF EXISTS bjet_fromHadTop_tlv CASCADE")
   cur.execute("DROP TABLE IF EXISTS bjet_fromLepTop_bdt_tlv CASCADE")
   cur.execute("DROP TABLE IF EXISTS wjet1_fromHadTop_bdt_tlv CASCADE")
   cur.execute("DROP TABLE IF EXISTS wjet2_fromHadTop_bdt_tlv CASCADE")
   cur.execute("DROP TABLE IF EXISTS wjet1_fromHiggs_bdt_tlv CASCADE")
   cur.execute("DROP TABLE IF EXISTS wjet2_fromHiggs_bdt_tlv CASCADE")
   cur.execute("DROP TABLE IF EXISTS w_fromHadTop_bdt_tlv CASCADE")
   cur.execute("DROP TABLE IF EXISTS w_fromHiggs_bdt_tlv CASCADE")
   cur.execute("DROP TABLE IF EXISTS higgs_bdt_tlv CASCADE")
   cur.execute("DROP TABLE IF EXISTS hadTop_bdt_tlv CASCADE")
   cur.execute("DROP TABLE IF EXISTS lepTop_bdt_tlv CASCADE")
   cur.execute("DROP TABLE IF EXISTS lepTop_higgs_bdt_tlv CASCADE")
   cur.execute("DROP TABLE IF EXISTS hadTop_higgs_bdt_tlv CASCADE")
   cur.execute("DROP TABLE IF EXISTS lepTop_hadTop_bdt_tlv CASCADE")
   cur.execute("DROP TABLE IF EXISTS tth_bdt_tlv CASCADE")
   cur.execute("DROP TABLE IF EXISTS passTrigger")
   cur.execute("DROP TABLE IF EXISTS matching_results")

  
   #event table 
   cur.execute("create table event_info (Run int, Lumi int, Event int, SampleID int, mcwgt float, wgt float, higgs_decay float, reco_score float, norm_score_sum float, num_real_jets_bdt float, num_jet_matches_truth float, metPt float, metPhi float, PRIMARY KEY (Run, Lumi, Event, SampleID))")
   #copy event table
   cur.execute("COPY event_info FROM '/home/newdbadmin/skimmingPhase/input/output/event/*' GZIP")


   #passTrigger table
   cur.execute("create table passTrigger (Run int, Lumi int, Event int, SampleID int, passTrigger varchar, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info(Run, Lumi, Event, SampleID))" )
   #copy table
   cur.execute("COPY passTrigger FROM '/home/newdbadmin/skimmingPhase/input/output/passTrigger/*' GZIP")

   #matching Results table
   cur.execute("create table matching_results (Run int, Lumi int, Event int, SampleID int, passTrigger varchar, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info(Run, Lumi, Event, SampleID))" )
   #copy table
   cur.execute("COPY matching_results FROM '/home/newdbadmin/skimmingPhase/input/output/matchingResults/*' GZIP")
   
   #preselected lepton table
   cur.execute("create table preselected_leptons (Run int, Lumi int, Event int, SampleID int, Pt float, Eta float, Phi float, pidgID float, dxy float, dz float, Charge float, relIso float, miniIso float, genPdgID float, isPromptFinalState float, isDirectPromptTauDecayProductFinalState float, genMotherPdgID float, genGrandMotherPdgID float, lepMVA float, miniIsoCharged float, miniIsoNeutral float, jetPtRatio float, jetPtRel float, csv float, sip3D float, jet_nCharged_tracks float, miniAbsIsoCharged float, miniAbsIsoNeutral float, rho float, effArea float, minIsoR float, miniAbsIsoNeutralcorr float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info(Run, Lumi, Event, SampleID))" )
   #copy preselected lepton table
   cur.execute("COPY preselected_leptons FROM '/home/newdbadmin/skimmingPhase/input/output/preLep/*' GZIP")

   #preselected electrons table
   cur.execute("create table preselected_electrons (Run int, Lumi int, Event int, SampleID int, Pt float, Eta float, Phi float, pdgID float, dxy float, dz float, charge float, relIso float, miniIso float, genPdgID float, isPromptFinalState float, isDirectPrompTauDecayProductFinalState float, genMotherPdgID float, genGrandMotherPdgID float, lepMVA float, miniIsoCharged float, miniIsoNeutral float, jetPtRatio float, jetPtRel float, csv float, sip3D float, jet_nCharged_tracks float, miniAbsIsoCharged float, minAbsIsoNeutral float, rho float, effArea float, miniIsoR float, miniAbsIsoNeutralcorr float, SCeta float, isGsfCtfScPixChargeConsistent float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info(Run, Lumi, Event, SampleID))")
   #copy preselected electrons table
   cur.execute("COPY preselected_electrons FROM '/home/newdbadmin/skimmingPhase/input/output/preElec/*' GZIP ") 

   #preselected muons table
   cur.execute("CREATE TABLE preselected_muons (Run int, Lumi int, Event int, SampleID int, Pt float, Eta float, Phi float, pdgID float, dxy float, dz float, charge float, relIso float, miniIso float, genPdgID float, isPromptFinalState float, isDirectPrompTauDecayProductFinalState float, genMotherPdgID float, genGrandMotherPdgID float, lepMVA float, miniIsoCharged float, miniIsoNeutral float, jetPtRatio float, jetPtRel float, csv float, sip3D float, jet_nCharged_tracks float, miniAbsIsoCharged float, minAbsIsoNeutral float, rho float, effArea float, miniIsoR float, miniAbsIsoNeutralcorr float, chargeFlip float, isPFMuon float, isTrackerMuon float, isGlobalMuon float, normalizedChi2 float, numberOfValidMuonHits float, numberOfMatchedStations float, numberOfValidPixelHits float, trackerLayersWithMeasurement float, localChi2 float, trKink float, validFrac float, segCompatibility float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info(Run, Lumi, Event, SampleID))")
   #copy preselected muons table
   cur.execute("COPY preselected_muons FROM '/home/newdbadmin/skimmingPhase/input/output/preMuon/*' GZIP")
   
   #preslected taus
   cur.execute("CREATE TABLE preselected_taus (Run int, Lumi int, Event int, SampleID int, Pt float, Eta float, Phi float, charge float, genPdgID float, genMotherPdgID float, genGrandMotherPdgID float, csv float, qgid float, pdgID float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info(Run, Lumi, Event, SampleID))") 
   #copy preselected taus table
   cur.execute("COPy preselected_taus FROM '/home/newdbadmin/skimmingPhase/input/output/preTau/*' GZIP")

   #preselected jets
   cur.execute("create table preselected_jets (Run int, Lumi int, Event int, SampleID int, Pt float, Eta float, Phi float, Mass float, Charge float, genPdgID float, genMotherPdgID float, genGrandMotherPdgID float, csv float, qgid float, pdgID float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info(Run, Lumi, Event, SampleID))" )
   #copy preselected jes
   cur.execute("COPY preselected_jets FROM '/home/newdbadmin/skimmingPhase/input/output/preJet/*' GZIP")

   #Pruned gen particles
   cur.execute("CREATE TABLE pruned_genParticles (Run int, Lumi int, Event int, SampleID int, Pt float, Eta float, Phi float, Mass float, pdgID float, status float, isPromptFinalState float, isPromptDecayed float, isDirectPromptTauDecayProductFinalState float, child0 float, child1 float, mother float, grandmother float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info(Run, Lumi, Event, SampleID))")
   cur.execute("COPY pruned_genParticles FROM '/home/newdbadmin/skimmingPhase/input/output/prunedGenPart/*' GZIP")

   #packed gen particles
   cur.execute("CREATE TABLE packed_genParticles (Run int, Lumi int, Event int, SampleID int, Pt float, Eta float, Phi float, Mass float, pdgID float, status float, isPromptFinalState float, isPromptDecayed float, isDirectPromptTauDecayProductFinalState float, child0 float, child1 float, mother float, grandmother float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info(Run, Lumi, Event, SampleID))")
   #copy packed gen particles
   cur.execute("COPY packed_genParticles FROM /home/newdbadmin/skimmingPhase/input/output/prunedGenPart/*' GZIP")

   #Matched jets
   cur.execute("CREATE TABLE matched_jets (Run int, Lumi int, Event int, SampleID int, Pt float, Eta float, Phi float, Mass float, charge float, genPdgID float, genMotherPdgID float, genGrandMotherPdgID float, csv float, qgid float, pdgID float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info(Run, Lumi, Event, SampleID))")
   #copy matched jets
   cur.execute("COPY matched_jets FROM /home/newdbadmin/skimmingPhase/input/output/matchJet/*' GZIP")
  
   #Matched jets truth
   cur.execute("CREATE TABLE matched_jets_truth (Run int, Lumi int, Event int, SampleID int, Pt float, Eta float, Phi float, Mass float, charge float, genPdgID float, genMotherPdgID float, genGrandMotherPdgID float, csv float, qgid float, pdgID float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info(Run, Lumi, Event, SampleID))")
   #copy matched jets truth
   cur.execute("COPY matched_jets_truth FROM /home/newdbadmin/skimmingPhase/input/output/matchJetTruth/*' GZIP")

   #lep from Higgs BDT
   cur.execute("create table lep_fromHiggs_bdt (Run int, Lumi int, Event int, SampleID int, Pt float, Eta float, Phi float, pidgID float, dxy float, dz float, Charge float, relIso float, miniIso float, genPdgID float, isPromptFinalState float, isDirectPromptTauDecayProductFinalState float, genMotherPdgID float, genGrandMotherPdgID float, lepMVA float, miniIsoCharged float, miniIsoNeutral float, jetPtRatio float, jetPtRel float, csv float, sip3D float, jet_nCharged_tracks float, miniAbsIsoCharged float, miniAbsIsoNeutral float, rho float, effArea float, minIsoR float, miniAbsIsoNeutralcorr float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info(Run, Lumi, Event, SampleID))" )
   #copy lep from Higgs BDT table
   cur.execute("COPY lep_fromHiggs_bdt FROM '/home/newdbadmin/skimmingPhase/input/output/lepHiggsBDT/*' GZIP")
   
   #lep from Top BDT
   cur.execute("create table lep_fromTop_bdt (Run int, Lumi int, Event int, SampleID int, Pt float, Eta float, Phi float, pidgID float, dxy float, dz float, Charge float, relIso float, miniIso float, genPdgID float, isPromptFinalState float, isDirectPromptTauDecayProductFinalState float, genMotherPdgID float, genGrandMotherPdgID float, lepMVA float, miniIsoCharged float, miniIsoNeutral float, jetPtRatio float, jetPtRel float, csv float, sip3D float, jet_nCharged_tracks float, miniAbsIsoCharged float, miniAbsIsoNeutral float, rho float, effArea float, minIsoR float, miniAbsIsoNeutralcorr float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info(Run, Lumi, Event, SampleID))" )
   #copy lep from Top BDT table
   cur.execute("COPY lep_fromTop_bdt FROM '/home/newdbadmin/skimmingPhase/input/output/lepTopBDT/*' GZIP")
 
   #lep from Top Truth
   cur.execute("create table lep_fromTop_truth (Run int, Lumi int, Event int, SampleID int, Pt float, Eta float, Phi float, pidgID float, dxy float, dz float, Charge float, relIso float, miniIso float, genPdgID float, isPromptFinalState float, isDirectPromptTauDecayProductFinalState float, genMotherPdgID float, genGrandMotherPdgID float, lepMVA float, miniIsoCharged float, miniIsoNeutral float, jetPtRatio float, jetPtRel float, csv float, sip3D float, jet_nCharged_tracks float, miniAbsIsoCharged float, miniAbsIsoNeutral float, rho float, effArea float, minIsoR float, miniAbsIsoNeutralcorr float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info(Run, Lumi, Event, SampleID))" )
   #copy lep from Top truth table
   cur.execute("COPY lep_fromTop_truth FROM '/home/newdbadmin/skimmingPhase/input/output/lepTopTruth/*' GZIP")

   #lep from Higgs Truth
   cur.execute("create table lep_fromHiggs_truth (Run int, Lumi int, Event int, SampleID int, Pt float, Eta float, Phi float, pidgID float, dxy float, dz float, Charge float, relIso float, miniIso float, genPdgID float, isPromptFinalState float, isDirectPromptTauDecayProductFinalState float, genMotherPdgID float, genGrandMotherPdgID float, lepMVA float, miniIsoCharged float, miniIsoNeutral float, jetPtRatio float, jetPtRel float, csv float, sip3D float, jet_nCharged_tracks float, miniAbsIsoCharged float, miniAbsIsoNeutral float, rho float, effArea float, minIsoR float, miniAbsIsoNeutralcorr float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info(Run, Lumi, Event, SampleID))" )
   #copy lep from Higgs truth table
   cur.execute("COPY lep_fromHiggs_truth FROM '/home/newdbadmin/skimmingPhase/input/output/lepHiggsTruth/*' GZIP")

   #lep from top BDT tlv
   cur.execute("create table lep_fromTop_bdt_tlv (Run int, Lumi int, Event int, SampleID int, Pt float, Eta float, Phi float, Mass float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info(Run, Lumi, Event, SampleID))")
   #copy lep from top bdt tlv
   cur.execute("COPY lep_fromTop_bdt_tlv FROM '/home/newdbadmin/skimmingPhase/input/output/lepFromTopBDT_tlv/*' GZIP")


   #lep from Higgs BDT tlv
   cur.execute("create table lep_fromHiggs_bdt_tlv (Run int, Lumi int, Event int, SampleuD int, Pt float, Eta float, Phi float, Mass float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info(Run, Lumi, Event, SampleID))")
   #copy lep from Higgs bdt tlv
   cur.execute("COPY lep_fromHiggs_bdt_tlv FROM '/home/newdbadmin/skimmingPhase/input/output/lepHiggsBDT_tlv/*' GZIP")
  
   #bJet from Had Top BDT tlv
   cur.execute("create table bJet_fromHadTop_bdt_tlv (Run int, Lumi int, Event int, SampleuD int, Pt float, Eta float, Phi float, Mass float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info(Run, Lumi, Event, SampleID))")
   #copy bJet from Had top bdt tlv
   cur.execute("COPY bJet_fromHadTop_bdt_tlv FROM '/home/newdbadmin/skimmingPhase/input/output/bJetHadTopBDT_tlv/*' GZIP")

   #bJet from Lep Top BDT tlv
   cur.execute("create table bJet_fromLepTop_bdt_tlv (Run int, Lumi int, Event int, SampleuD int, Pt float, Eta float, Phi float, Mass float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info(Run, Lumi, Event, SampleID))")
   #copy bJet from Lep top bdt tlv
   cur.execute("COPY bJet_fromLepTop_bdt_tlv FROM '/home/newdbadmin/skimmingPhase/input/output/bJetLepTopBDT_tlv/*' GZIP")

   #wJet1 from Had Top BDT tlv
   cur.execute("create table wJet1_fromHadTop_bdt_tlv (Run int, Lumi int, Event int, SampleuD int, Pt float, Eta float, Phi float, Mass float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info(Run, Lumi, Event, SampleID))")
   #copy wJet1 from Had top bdt tlv
   cur.execute("COPY wJet1_fromHadTop_bdt_tlv FROM '/home/newdbadmin/skimmingPhase/input/output/wJet1HadTopBDT_tlv/*' GZIP")

   #wJet from Had Top BDT tlv
   cur.execute("create table wJet2_fromHadTop_bdt_tlv (Run int, Lumi int, Event int, SampleuD int, Pt float, Eta float, Phi float, Mass float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info(Run, Lumi, Event, SampleID))")
   #copy wJet2 from Had top bdt tlv
   cur.execute("COPY wJet2_fromHadTop_bdt_tlv FROM '/home/newdbadmin/skimmingPhase/input/output/wJet2HadTopBDT_tlv/*' GZIP")

   #wJet1 from Higgs BDT tlv
   cur.execute("create table wJet1_fromHiggs_bdt_tlv (Run int, Lumi int, Event int, SampleuD int, Pt float, Eta float, Phi float, Mass float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info(Run, Lumi, Event, SampleID))")
   #copy wJet1 from Higgs bdt tlv
   cur.execute("COPY wJet1_fromHiggs_bdt_tlv FROM '/home/newdbadmin/skimmingPhase/input/output/wJet1HiggsBDT_tlv/*' GZIP")

   #wJet2 from Higgs BDT tlv
   cur.execute("create table wJet2_fromHiggs_bdt_tlv (Run int, Lumi int, Event int, SampleuD int, Pt float, Eta float, Phi float, Mass float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info(Run, Lumi, Event, SampleID))")
   #copy wJet2 from Higgs bdt tlv
   cur.execute("COPY wJet2_fromHiggs_bdt_tlv FROM '/home/newdbadmin/skimmingPhase/input/output/wJet2HiggsBDT_tlv/*' GZIP")

   #w from Had Top BDT tlv
   cur.execute("create table w_fromHadTop_bdt_tlv (Run int, Lumi int, Event int, SampleuD int, Pt float, Eta float, Phi float, Mass float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info(Run, Lumi, Event, SampleID))")
   #copy w from Had top bdt tlv
   cur.execute("COPY w_fromHadTop_bdt_tlv FROM '/home/newdbadmin/skimmingPhase/input/output/wHadTopBDT_tlv/*' GZIP")

   #w from Higgs BDT tlv
   cur.execute("create table w_fromHiggs_bdt_tlv (Run int, Lumi int, Event int, SampleuD int, Pt float, Eta float, Phi float, Mass float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info(Run, Lumi, Event, SampleID))")
   #copy w from Higgs bdt tlv
   cur.execute("COPY w_fromHiggs_bdt_tlv FROM '/home/newdbadmin/skimmingPhase/input/output/wHiggsBDT_tlv/*' GZIP")

   #Higgs BDT tlv
   cur.execute("create table Higgs_bdt_tlv (Run int, Lumi int, Event int, SampleuD int, Pt float, Eta float, Phi float, Mass float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info(Run, Lumi, Event, SampleID))")
   #copy Higgs bdt tlv
   cur.execute("COPY Higgs_bdt_tlv FROM '/home/newdbadmin/skimmingPhase/input/output/higgsBDT_tlv/*' GZIP")

   #Had top BDT tlv
   cur.execute("create table HadTop_bdt_tlv (Run int, Lumi int, Event int, SampleuD int, Pt float, Eta float, Phi float, Mass float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info(Run, Lumi, Event, SampleID))")
   #copy Had bdt tlv
   cur.execute("COPY HadTop_bdt_tlv FROM '/home/newdbadmin/skimmingPhase/input/output/hadTopBDT_tlv/*' GZIP")

   #Lep top BDT tlv
   cur.execute("create table LepTop_bdt_tlv (Run int, Lumi int, Event int, SampleuD int, Pt float, Eta float, Phi float, Mass float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info(Run, Lumi, Event, SampleID))")
   #copy Lep top bdt tlv
   cur.execute("COPY LepTop_bdt_tlv FROM '/home/newdbadmin/skimmingPhase/input/output/lepTopBDT_tlv/*' GZIP")

   #Lep top Higgs BDT tlv
   cur.execute("create table LepTop_Higgs_bdt_tlv (Run int, Lumi int, Event int, SampleuD int, Pt float, Eta float, Phi float, Mass float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info(Run, Lumi, Event, SampleID))")
   #copy Lep top Higgs bdt tlv
   cur.execute("COPY LepTop_Higgs_bdt_tlv FROM '/home/newdbadmin/skimmingPhase/input/output/lepTopHiggsBDT_tlv/*' GZIP")

   #Had top Higgs BDT tlv
   cur.execute("create table HadTop_Higgs_bdt_tlv (Run int, Lumi int, Event int, SampleuD int, Pt float, Eta float, Phi float, Mass float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info(Run, Lumi, Event, SampleID))")
   #copy Had top Higgs bdt tlv
   cur.execute("COPY HadTop_Higgs_bdt_tlv FROM '/home/newdbadmin/skimmingPhase/input/output/hadTopHiggsBDT_tlv/*' GZIP")

   #Lep top Had top BDT tlv
   cur.execute("create table LepTopHadTop_Higgs_bdt_tlv (Run int, Lumi int, Event int, SampleuD int, Pt float, Eta float, Phi float, Mass float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info(Run, Lumi, Event, SampleID))")
   #copy Lep top Had top bdt tlv
   cur.execute("COPY LepTopHadTop_Higgs_bdt_tlv FROM '/home/newdbadmin/skimmingPhase/input/output/lepTopHadTopBDT_tlv/*' GZIP")

   #tth BDT tlv
   cur.execute("create table tth_bdt_tlv (Run int, Lumi int, Event int, SampleuD int, Pt float, Eta float, Phi float, Mass float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info(Run, Lumi, Event, SampleID))")
   #copy tth bdt tlv
   cur.execute("COPY tth_bdt_tlv FROM '/home/newdbadmin/skimmingPhase/input/output/tthBDT_tlv/*' GZIP")


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
