#!/opt/vertica/oss/python/bin/python

import hp_vertica_client
import os
import time

def main():
   startTime = time.time()
   conn = hp_vertica_client.connect("")
   cur = conn.cursor()
   
   cur.execute("drop table if exists jets cascade")

   cur.execute("drop table if exists leptons  cascade")

   cur.execute("drop table if exists event_info cascade")

   cur.execute("create table event_info (Run int, Lumi int, Event int, PRIMARY KEY (Run, Lumi, Event))")
   cur.execute("create table jets (Run int, Lumi int, Event int, Pt float, Eta float, Phi float, Charge float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event) REFERENCES event_info(Run, Lumi, Event))" )

   cur.execute("create table leptons (Run int, Lumi int, Event int, Pt float, Eta float, Phi float, Charge float, CONSTRAINT fk_event FOREIGN KEY (Run, Lumi, Event) REFERENCES event_info(Run, Lumi, Event))" )
   
   cur.execute("copy event_info from '/home/newdbadmin/schema_test/event.txt' parser fdelimitedparser()")

   cur.execute("copy leptons  from '/home/newdbadmin/schema_test/lep.txt' parser fdelimitedparser()")

   cur.execute("copy jets from '/home/newdbadmin/schema_test/jet.txt' parser fdelimitedparser()")
   cur.execute("commit")
      
   tableTime = time.time() - startTime
   queryStart = time.time()
   query = " select Pt from jets;"

   cur.execute(query)

   queryTime = time.time() - queryStart
   totalTime = time.time() - startTime

   print('Fill table: {}\nQuery time: {}\nTotal: {}'.format(tableTime, queryTime, totalTime) )

if __name__== "__main__":
   main()
