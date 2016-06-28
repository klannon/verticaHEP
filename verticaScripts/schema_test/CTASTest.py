#!/opt/vertica/oss/python/bin/python

import hp_vertica_client
import os
import time

def main():
   startTime = time.time()
   conn = hp_vertica_client.connect("")
   cur = conn.cursor()

   cur.execute("DROP TABLE IF EXISTS jets_v2")
   cur.execute("DROP TABLE IF EXISTS sum_jet_vars")
   cur.execute("DROP TABLE IF EXISTS sum_lep_vars")
   cur.execute("DROP TABLE IF EXISTS jets_v3")
   cur.execute("DROP TABLE IF EXISTS jets_v4")

   cur.execute("CREATE TABLE jets_v2 AS SELECT Run, Lumi, Event, Pt, Eta, Phi, Pt*Pt as Ptsq FROM jets")   

   cur.execute("ALTER TABLE jets DROP Ptsq")   

   cur.execute("ALTER TABLE jets ADD COLUMN PtSq float DEFAULT Pt*Pt")

   cur.execute("CREATE TABLE sum_jet_vars AS SELECT Run, Lumi, Event, SUM(Pt) as sum_pt, SUM(Pt*Pt) AS sum_pt_sq FROM jets GROUP BY Run, Lumi, Event")

   cur.execute("CREATE TABLE sum_lep_vars AS SELECT leptons.Run AS Run, leptons.Lumi AS Lumi, leptons.Event AS Event, SUM(Leptons.Pt) as sum_pt, SUM(jets.Pt + leptons.Pt) AS sum_jet_lep_pt FROM jets, leptons WHERE jets.Run = leptons.Run AND jets.Lumi = leptons.Lumi AND jets.Event = leptons.Event GROUP BY leptons.Run, leptons.Lumi, leptons.Event") 

   cur.execute("CREATE TABLE jets_v3 AS SELECT *,Pt*Pt*Pt as Pt3 FROM jets")

   cur.execute("CREATE TABLE jets_v4 AS SELECT *, CASE WHEN Pt > 30 THEN 1 ELSE 0 END AS check FROM jets")

   cur.execute("commit")
      



if __name__== "__main__":
   main()
