#!/opt/vertica/oss/python/bin/python

import hp_vertica_client
import os
import time

def main():
   startTime = time.time()
   conn = hp_vertica_client.connect("")
   cur = conn.cursor()
   
   cur.execute("drop table if exists psLeps_small  cascade")

   cur.execute("drop table if exists tightLeps_small cascade")

   cur.execute("create table psLeps_small as ( (select Run, Lumi, Event, SampleID, Pt, Eta, Phi, charge from preselected_muons_small) UNION ALL (select Run, Lumi, Event, SampleID, Pt, Eta, Phi, charge from preselected_electrons_small))")


   cur.execute("create table tightLeps_small as ( (select Run, Lumi, Event, SampleID, Pt, Eta, Phi, charge from tightMVABased_muons_small) UNION ALL (select Run, Lumi, Event, SampleID, Pt, Eta, Phi, charge from tightMVABased_electrons_small))")
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
