#!/opt/vertica/oss/python/bin/python

import hp_vertica_client
import os
import time


conn = hp_vertica_client.connect("")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS eventSelection_scale")

startTime = time.time()

cur.execute("CREATE TABLE eventSelection_scale AS SELECT t1.Run, t1.Lumi, t1.Event, t1.SampleID FROM passCommon_scale AS t1 JOIN pass2lss_scale AS t2 ON t1.Run = t2.Run AND t1.Lumi = t2.Lumi AND t1.Event = t2.Event AND t1.SampleID = t2.SampleID GROUP BY t1.Run, t1.Lumi, t1.Event, t1.SampleID") 

endTime = time.time() - startTime

cur.execute("SELECT COUNT(*) FROM eventSelection_scale")

numEvents = cur.fetchall()

print(numEvents)
print("time: {}".format(endTime))
 
