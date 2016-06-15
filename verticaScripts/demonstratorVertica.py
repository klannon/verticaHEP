#!/opt/vertica/oss/python/bin/python

import hp_vertica_client
import os
import time

def main():
   startTime = time.time()
   conn = hp_vertica_client.connect("")
   cur = conn.cursor()
   
   cur.execute("drop table if exists demonstrator cascade")

   makeTable = "create table demonstrator (row int, instance int, preselect float)"

   cur.execute(makeTable)
   cur.execute("copy demonstrator from '/home/newdbadmin/demonstrator/verticaInput4.txt' parser fdelimitedparser()")
   cur.execute("commit")
      
   tableTime = time.time() - startTime
   queryStart = time.time()
   query = " select preselect from demonstrator;"

   cur.execute(query)

   queryTime = time.time() - queryStart
   totalTime = time.time() - startTime

   print('Fill table: {}\nQuery time: {}\nTotal: {}'.format(tableTime, queryTime, totalTime) )

if __name__== "__main__":
   main()
