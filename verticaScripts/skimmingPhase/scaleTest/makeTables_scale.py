#!/opt/vertica/oss/python/bin/python

import hp_vertica_client
import os
import time

def main():
   startTime = time.time()
   conn = hp_vertica_client.connect("")
   cur = conn.cursor()
   
   cur.execute("drop table if exists preselected_electrons_scale cascade")

   cur.execute("drop table if exists event_info_scale cascade")

   cur.execute("DROP TABLE IF EXISTS preselected_muons_scale  CASCADE")

   cur.execute("drop table if exists preselected_jets_scale cascade")

  
   #event table 
   cur.execute("create table event_info_scale (Run int, Lumi int, Event int, SampleID int, mcwgt float, wgt float, higgs_decay float, reco_score float, norm_score_sum float, num_real_jets_bdt float, num_jet_matches_truth float, metPt float, metPhi float, PRIMARY KEY (Run, Lumi, Event, SampleID))")
   #copy event table
   cur.execute("COPY event_info_scale FROM '/home/newdbadmin/skimmingPhase/scaleInput/event/*' GZIP")


   #preselected electrons table
   cur.execute("create table preselected_electrons_scale (Run int, Lumi int, Event int, SampleID int, Pt float, Eta float, Phi float, Px float, Py float, Pz float, En float,  Mass float, pdgID float, dxy float, dz float, charge float, relIso float, miniIso float, genPdgID float, isPromptFinalState float, isDirectPrompTauDecayProductFinalState float, genMotherPdgID float, genGrandMotherPdgID float, lepMVA float, miniIsoCharged float, miniIsoNeutral float, jetPtRatio float, jetPtRel float, csv float, sip3D float, jet_nCharged_tracks float, miniAbsIsoCharged float, minAbsIsoNeutral float, rho float, effArea float, miniIsoR float, miniAbsIsoNeutralcorr float, SCeta float, isGsfCtfScPixChargeConsistent float, numMissingInnerHits float, passConversioVeto float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info(Run, Lumi, Event, SampleID))")
   #copy preselected electrons table
   cur.execute("COPY preselected_electrons_scale FROM '/home/newdbadmin/skimmingPhase/scaleInput/preElec/*' GZIP ") 

   #preselected muons table
   cur.execute("CREATE TABLE preselected_muons_scale (Run int, Lumi int, Event int, SampleID int, Pt float, Eta float, Phi float, Px float, Py float, Pz float, En float,  Mass float, pdgID float, dxy float, dz float, charge float, relIso float, miniIso float, genPdgID float, isPromptFinalState float, isDirectPrompTauDecayProductFinalState float, genMotherPdgID float, genGrandMotherPdgID float, lepMVA float, miniIsoCharged float, miniIsoNeutral float, jetPtRatio float, jetPtRel float, csv float, sip3D float, jet_nCharged_tracks float, miniAbsIsoCharged float, minAbsIsoNeutral float, rho float, effArea float, miniIsoR float, miniAbsIsoNeutralcorr float, chargeFlip float, isPFMuon float, isTrackerMuon float, isGlobalMuon float, normalizedChi2 float, numberOfValidMuonHits float, numberOfMatchedStations float, numberOfValidPixelHits float, trackerLayersWithMeasurement float, localChi2 float, trKink float, validFrac float, segCompatibility float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info(Run, Lumi, Event, SampleID))")
   #copy preselected muons table
   cur.execute("COPY preselected_muons_scale FROM '/home/newdbadmin/skimmingPhase/scaleInput/preMuon/*' GZIP")
   
   #preselected jets
   cur.execute("create table preselected_jets_scale (Run int, Lumi int, Event int, SampleID int, Pt float, Eta float, Phi float,  Px float, Py float, Pz float, En float, Mass float, Charge float, genPdgID float, genMotherPdgID float, genGrandMotherPdgID float, csv float, qgid float, pdgID float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event, SampleID) REFERENCES event_info_scale(Run, Lumi, Event, SampleID))" )
   #copy preselected jes
   cur.execute("COPY preselected_jets_scale FROM '/home/newdbadmin/skimmingPhase/scaleInput/preJet/*' GZIP ")

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
