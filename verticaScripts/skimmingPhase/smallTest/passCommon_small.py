#!/opt/vertica/oss/python/bin/python

import hp_vertica_client
import os
import time


conn = hp_vertica_client.connect("")
cur = conn.cursor()

cur.execute("DROP VIEW IF EXISTS comSize_small1")

cur.execute("DROP VIEW IF EXISTS comSize_small2")

cur.execute("DROP VIEW IF EXISTS comSize_small")
cur.execute("DROP VIEW IF EXISTS comPt_small")
cur.execute("DROP VIEW IF EXISTS comPreJetSize_small")
cur.execute("DROP VIEW IF EXISTS tagJetsLoose_small")
cur.execute("DROP VIEW IF EXISTS tagJetsTight_small")
cur.execute("DROP VIEW IF EXISTS tagJets_small")
cur.execute("DROP VIEW IF EXISTS passComView_small")
cur.execute("DROP VIEW IF EXISTS passCommon_small")
cur.execute("DROP TABLE IF EXISTS passCommon_small")
startTime = time.time()


cur.execute("CREATE view comSize_small1 AS SELECT Run, Lumi, Event, SampleID FROM psLeps_small GROUP BY Run, Lumi, Event, SampleID having count(Lumi) >3")


cur.execute("CREATE view comSize_small2 AS SELECT Run, Lumi, Event, SampleID FROM tightLeps_small GROUP BY Run, Lumi, Event, SampleID having count(Lumi) >1")
#cur.execute("CREATE TABLE tightMVABased_Electrons AS SELECT * FROM preselected_electrons WHERE lepMVA > 0.75 ")

cur.execute("CREATE VIEW comSize_small AS ((SELECT * FROM comSize_small1) UNION ALL (SELECT * FROM comSize_small2))")

#cur.execute("CREATE VIEW comPt_small AS Select Run, Lumi, Event, SampleID from psLeps_small group by Run, Lumi, Event, SampleID having max(Pt) > 20 and count( Pt >10 ) >=2 ")
cur.execute("CREATE VIEW comPt_small AS Select Run, Lumi, Event, SampleID from psLeps_small where Pt > 10 group by Run, Lumi, Event, SampleID having max(Pt) > 20 and count(run)>=2 ")
#cur.execute("CREATE VIEW comPt_small2 AS Select Run, Lumi, Event, SampleID from psLeps_small group by Run, Lumi, Event, SampleID, Pt having count(Pt > 10)>=2  ")
#cur.execute("create view comPt_small as select * from psLeps_small") #delete this

cur.execute("CREATE VIEW comPreJetSize_small AS SELECT Run, Lumi, Event, SampleID FROM  preselected_jets_small GROUP BY Run, Lumi, Event, SampleID HAVING COUNT(run) > 1")

cur.execute("CREATE VIEW tagJetsLoose_small AS SELECT Run, Lumi, Event, SampleID from preselected_jets_small where csv > 0.423 GROUP BY Run, Lumi, Event, SampleID HAVING COUNT(Run) > 1")

cur.execute("CREATE VIEW tagJetsTight_small AS SELECT Run, Lumi, Event, SampleID from preselected_jets_small where csv > 0.814 GROUP BY Run, Lumi, Event, SampleID HAVING COUNT(Run) > 0")

cur.execute("CREATE VIEW tagJets_small AS ((SELECT * FROM tagJetsLoose_small) UNION ALL (SELECT * FROM tagJetsTight_small))")

cur.execute("CREATE VIEW passComView_small AS SELECT comSize_small.Run, comSize_small.Lumi, comSize_small.Event, comSize_small.SampleID FROM comSize_small JOIN comPt_small ON (comSize_small.Run = comPt_small.Run AND comSize_small.Lumi = comPt_small.Lumi AND comSize_small.Event = comPt_small.Event AND comSize_small.SampleID = comPt_small.SampleID) JOIN comPreJetSize_small ON (comSize_small.Run = comPreJetSize_small.Run AND comSize_small.Lumi = comPreJetSize_small.Lumi AND comSize_small.Event = comPreJetSize_small.Event AND comSize_small.SampleID = comPreJetSize_small.SampleID) JOIN tagJets_small ON (comSize_small.Run = tagJets_small.Run AND comSize_small.Lumi = tagJets_small.Lumi AND comSize_small.Event = tagJets_small.Event AND comSize_small.SampleID = tagJets_small.SampleID)")

cur.execute("CREATE TABLE passCommon_small as SELECT * FROM passComView_small GROUP BY Run, Lumi, Event, SampleID")

cur.execute("commit")

cur.execute("Select count(*) from passCommon_small")
print(cur.fetchall())

endTime = time.time() - startTime

print("total time: {}".format(endTime))



