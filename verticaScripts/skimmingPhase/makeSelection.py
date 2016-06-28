#!/opt/vertica/oss/python/bin/python

import hp_vertica_client
import os
import time


conn = hp_vertica_client.connect("")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS tightMVABased_Muons")
cur.execute("DROP TABLE IF EXISTS tightMVABased_Electrons")

startTime = time.time()

#cur.execute("CREATE TABLE tightMVABased_Muons AS SELECT *, CASE WHEN (validFrac >= 0.8 and lepMVA > 0.75 and segCompatibility > CASE WHEN isGlobalMuon and normalizedChiSq < 3 and localChiSq < 12 and trKink < 20 THEN 0.303 ELSE 0.451 END) THEN 1 ELSE 0 END FROM preselected_muons")

#cur.execute("CREATE TABLE tightMVABased_Electrons AS SELECT *, CASE WHEN (lepMVA > 0.75 and numMissingInnerHits == 0) THEN 1 ELSE 0 END FROM preselected_electrons

cur.execute("CREATE TABLE tightMVABased_Muons AS SELECT * FROM preselected_muons WHERE validFrac >= 0.8 and lepMVA > 0.75 and segCompatibility > CASE WHEN isGlobalMuon and normalizedChiSq < 3 and localChiSq < 12 and trKink < 20 THEN 0.303 ELSE 0.451 END")

cur.execute("CREATE TABLE tightMVABased_Electrons AS SELECT * FROM preselected_electrons WHERE lepMVA > 0.75 and numMissingInnerHits == 0")

cur.execute("commit")

endTime = time.time() - startTime

print("total time: {}".format(endTime))



