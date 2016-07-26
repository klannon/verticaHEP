#!/opt/vertica/oss/python/bin/python

import hp_vertica_client
import os
import time

def main():
   startTime = time.time()
   conn = hp_vertica_client.connect("")
   cur = conn.cursor()
   
   cur.execute("drop table if exists psLeps_scale  cascade")

   cur.execute("drop table if exists tightLeps_scale cascade")

   cur.execute("create table psLeps_scale as ( (select Run, Lumi, Event, SampleID, Pt, Eta, Phi, Px, Py, Pz, En, Mass, charge from preselected_muons_scale) UNION ALL (select Run, Lumi, Event, SampleID, Pt, Eta, Phi, Px, Py, Pz, En, Mass, charge from preselected_electrons_scale))")


   cur.execute("create table tightLeps_scale as ( (select Run, Lumi, Event, SampleID, Pt, Eta, Phi, Px, Py, Pz, En, Mass, charge from tightMVABased_muons_scale) UNION ALL (select Run, Lumi, Event, SampleID, Pt, Eta, Phi, Px, Py, Pz, En, Mass, charge from tightMVABased_electrons_scale))")
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
