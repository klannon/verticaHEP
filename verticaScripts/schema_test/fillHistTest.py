#!/opt/vertica/oss/python/bin/python

import hp_vertica_client
import os
import time
import ROOT
import sys

def main():
   
   startTime = time.time()
   conn = hp_vertica_client.connect("")
   cur = conn.cursor()
   
   cur.execute("drop table if exists tempTable")
   cur.execute("drop table if exists tempTable2")
   cur.execute("DROP TABLE IF EXISTS tempTable3")

   cur.execute("DROP TABLE IF EXISTS jetCosPhi")
   my_file = ROOT.TFile("test_1.root", "RECREATE")

   histJetPt = ROOT.TH1F("jetpt", "Pt", 100,0,200)
   lepPtHistSig = ROOT.TH1F("lepPt","Lepton Pt",100,0,200)
   lepEtaHistSig = ROOT.TH1F("lepEta","Lepton #eta",100,-2,2)
   lepPhiHistSig = ROOT.TH1F("lepPhiHistSig","Lepton #phi",100,-4,4)
   jetPt_2lep = ROOT.TH1F("jetPt_2lep","Jet Pt",100,0,200)  
   jetPt_2lep2 = ROOT.TH1F("jetPt_2lep2","Jet Pt",100,0,200)   
   jetPt_2lepCharge = ROOT.TH1F("jetPt_2lepCharge","Jet Pt",100,0,200) 
   jetPt_2lepChargeJet = ROOT.TH1F("jetPt_2lepChargeJet","Jet Pt",100,0,200)
   jet2Pt40 = ROOT.TH1F("jet2Pt40","nJets >= 2 Pt>40",100,0,200)
   jetCosPhi = ROOT.TH1F("jetCosPhi","Cos(phi)",100,-2,2)

   fill_hist_from_query(histJetPt,"select Pt from jets",cur)
   fill_hist_from_query(lepPtHistSig,"select Pt from leptons",cur)
   fill_hist_from_query(lepEtaHistSig, "select Eta from leptons where Pt >35",cur)
   
   cur.execute("CREATE TEMPORARY TABLE tempTable(Event, sumCharge) ON COMMIT PRESERVE ROWS AS select event_info.Event, SUM(leptons.Charge) from event_info left outer join leptons on event_info.Event = leptons.Event group by event_info.Event having count(leptons.Event) = 2" )  

   fill_hist_from_query(jetPt_2lep, "select Pt from jets where Event in (select event_info.Event from event_info left outer join leptons on event_info.Event = leptons.Event group by event_info.Event having count(leptons.Event) = 2)",cur)


   fill_hist_from_query(jetPt_2lep2, "select Pt from jets where Event IN (SELECT Event FROM tempTable)",cur)

   
   #cur.execute("CREATE TEMPORARY TABLE tempTable2(Event) ON COMMIT PRESERVE ROWS AS select Event from leptons where Event in (SELECT * FROM tempTable) AND SUM(Charge) != 0 GROUP BY Event ")
   fill_hist_from_query(jetPt_2lepCharge, "select Pt from jets where Event in (select event_info.Event from event_info left outer join leptons on event_info.Event = leptons.Event group by event_info.Event having count(leptons.Event) = 2) AND Event in (Select Event from tempTable where sumCharge != 0) ",cur)
   #fill_hist_from_query(lepPhiHistSig,"select leptons.Phi from leptons",cur)

   fill_hist_from_query(jetPt_2lepChargeJet, "select Pt from jets where Event in (select Event from tempTable)  AND Event in (Select Event from tempTable where sumCharge != 0) AND Event in (SELECT event_info.Event from event_info left outer join jets on event_info.Event = jets.Event GROUP BY event_info.Event HAVING COUNT(jets.Event) > 2) ",cur) 
  
   cur.execute("CREATE TEMPORARY TABLE tempTable3(Event) ON COMMIT PRESERVE ROWS AS SELECT Event FROM jets where Pt >40 GROUP BY Event HAVING COUNT(Event) >= 2")

   fill_hist_from_query(jet2Pt40, "SELECT Pt from jets WHERE Event in (SELECT Event FROM tempTable3)",cur)
  
   cur.execute("CREATE TABLE jetCosPhi(Event, CosPhi) AS SELECT Event, CASE WHEN min = 0 THEN 0 WHEN neg%2 =1 THEN -1*EXP(prod)  ELSE EXP(prod) END FROM ( SELECT Event, SUM(LN(ABS(COS(Phi)))) AS prod, SUM(CASE WHEN COS(Phi)  < 0 THEN 1 ELSE 0 END) AS neg,  MIN(ABS(COS(Phi))) as min FROM jets GROUP BY Event)subQ ")  
 
   fill_hist_from_query(jetCosPhi, "SELECT CosPhi FROM jetCosPhi", cur)
   my_file.Write()
   my_file.Close()

   cur.execute("DROP TABLE tempTable")
   #cur.execute("DROP TABLE tempTable2")
   cur.execute("DROP TABLE tempTable3")

def fill_hist_from_query(target_hist, query, cursor):
   cursor.execute(query)

   for x in cursor.fetchall():
      if len(x) < 1:
	raise ValueError("could not parse output {0}".format(x))
      target_hist.Fill(x[0])      

if __name__== "__main__":
   main()
