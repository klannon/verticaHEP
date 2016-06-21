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

   my_file = ROOT.TFile("test_2.root", "RECREATE")

   histJetPt = ROOT.TH1F("jetpt", "Pt", 100,0,200)
   lepPtHistSig = ROOT.TH1F("lepPt","Lepton Pt",100,0,200)
   lepEtaHistSig = ROOT.TH1F("lepEta","Lepton #eta",100,-2,2)
   lepPhiHistSig = ROOT.TH1F("lepPhiHistSig","Lepton #phi",100,-4,4)

   jetPt_bucket = ROOT.TH1F("jetPt_bucket","jet Pt",100,0,200)

   fill_hist_from_query(histJetPt,"select Pt from jets",cur)
   fill_hist_from_query(lepPtHistSig,"select Pt from leptons",cur)
   fill_hist_from_query(lepEtaHistSig, "select Eta from leptons where Pt >35",cur)
   
   fill_hist_from_widthBucket(jetPt_bucket,100, "SELECT WIDTH_BUCKET(Pt,0,200,100), COUNT(WIDTH_BUCKET(PT,0,200,100)) FROM jets GROUP BY WIDTH_BUCKET(PT,0,200,100)", cur)

   my_file.Write()
   my_file.Close()

   cur.execute("DROP TABLE IF EXISTS tempTable")
   #cur.execute("DROP TABLE tempTable2")
   cur.execute("DROP TABLE IF EXISTS tempTable3")

def fill_hist_from_widthBucket(target_hist, maxbin, query, cursor):
   cursor.execute(query)

   for x in cursor.fetchall():
      if len(x) <1:
	raise ValueError("could not parse output {0}.".format(x) )
      if x[0] <= maxbin:
	target_hist.SetBinContent(x[0],x[1])

def fill_hist_from_query(target_hist, query, cursor):
   cursor.execute(query)

   for x in cursor.fetchall():
      if len(x) < 1:
	raise ValueError("could not parse output {0}".format(x))
      target_hist.Fill(x[0])      

if __name__== "__main__":
   main()
