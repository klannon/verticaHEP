#!/opt/vertica/oss/python/bin/python

import hp_vertica_client
import os
import time


conn = hp_vertica_client.connect("")
cur = conn.cursor()

cur.execute("DROP VIEW IF EXISTS comSize_scale1")

cur.execute("DROP VIEW IF EXISTS comSize_scale2")

cur.execute("DROP VIEW IF EXISTS comSize_scale")
cur.execute("DROP VIEW IF EXISTS comPt_scale")
cur.execute("DROP VIEW IF EXISTS comPreJetSize_scale")
cur.execute("DROP VIEW IF EXISTS tagJetsLoose_scale")
cur.execute("DROP VIEW IF EXISTS tagJetsTight_scale")
cur.execute("DROP VIEW IF EXISTS tagJets_scale")
cur.execute("DROP VIEW IF EXISTS passComView_scale")
cur.execute("DROP VIEW IF EXISTS passCommon_scale")
cur.execute("DROP TABLE IF EXISTS passCommon_scale")
startTime = time.time()


cur.execute("CREATE view comSize_scale1 AS SELECT Run, Lumi, Event, SampleID FROM psLeps_scale GROUP BY Run, Lumi, Event, SampleID having count(Lumi) >3")


cur.execute("CREATE view comSize_scale2 AS SELECT Run, Lumi, Event, SampleID FROM tightLeps_scale GROUP BY Run, Lumi, Event, SampleID having count(Lumi) >1")
#cur.execute("CREATE TABLE tightMVABased_Electrons AS SELECT * FROM preselected_electrons WHERE lepMVA > 0.75 ")

cur.execute("CREATE VIEW comSize_scale AS ((SELECT * FROM comSize_scale1) UNION ALL (SELECT * FROM comSize_scale2))")

#cur.execute("CREATE VIEW comPt_scale AS Select Run, Lumi, Event, SampleID from psLeps_scale group by Run, Lumi, Event, SampleID having max(Pt) > 20 and count( Pt >10 ) >=2 ")
cur.execute("CREATE VIEW comPt_scale AS Select Run, Lumi, Event, SampleID from psLeps_scale where Pt > 10 group by Run, Lumi, Event, SampleID having max(Pt) > 20 and count(run)>=2 ")
#cur.execute("CREATE VIEW comPt_scale2 AS Select Run, Lumi, Event, SampleID from psLeps_scale group by Run, Lumi, Event, SampleID, Pt having count(Pt > 10)>=2  ")
#cur.execute("create view comPt_scale as select * from psLeps_scale") #delete this

cur.execute("CREATE VIEW comPreJetSize_scale AS SELECT Run, Lumi, Event, SampleID FROM  preselected_jets_scale GROUP BY Run, Lumi, Event, SampleID HAVING COUNT(run) > 1")

cur.execute("CREATE VIEW tagJetsLoose_scale AS SELECT Run, Lumi, Event, SampleID from preselected_jets_scale where csv > 0.423 GROUP BY Run, Lumi, Event, SampleID HAVING COUNT(Run) > 1")

cur.execute("CREATE VIEW tagJetsTight_scale AS SELECT Run, Lumi, Event, SampleID from preselected_jets_scale where csv > 0.814 GROUP BY Run, Lumi, Event, SampleID HAVING COUNT(Run) > 0")

cur.execute("CREATE VIEW tagJets_scale AS ((SELECT * FROM tagJetsLoose_scale) UNION ALL (SELECT * FROM tagJetsTight_scale))")

cur.execute("CREATE VIEW passComView_scale AS SELECT comSize_scale.Run, comSize_scale.Lumi, comSize_scale.Event, comSize_scale.SampleID FROM comSize_scale JOIN comPt_scale ON (comSize_scale.Run = comPt_scale.Run AND comSize_scale.Lumi = comPt_scale.Lumi AND comSize_scale.Event = comPt_scale.Event AND comSize_scale.SampleID = comPt_scale.SampleID) JOIN comPreJetSize_scale ON (comSize_scale.Run = comPreJetSize_scale.Run AND comSize_scale.Lumi = comPreJetSize_scale.Lumi AND comSize_scale.Event = comPreJetSize_scale.Event AND comSize_scale.SampleID = comPreJetSize_scale.SampleID) JOIN tagJets_scale ON (comSize_scale.Run = tagJets_scale.Run AND comSize_scale.Lumi = tagJets_scale.Lumi AND comSize_scale.Event = tagJets_scale.Event AND comSize_scale.SampleID = tagJets_scale.SampleID)")

cur.execute("CREATE TABLE passCommon_scale as SELECT * FROM passComView_scale GROUP BY Run, Lumi, Event, SampleID")

cur.execute("commit")

endTime = time.time() - startTime

cur.execute("Select count(*) from passCommon_scale")
print(cur.fetchall())
print("total time: {}".format(endTime))



