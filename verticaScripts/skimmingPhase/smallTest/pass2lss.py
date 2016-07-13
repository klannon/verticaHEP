#!/opt/vertica/oss/python/bin/python

import hp_vertica_client
import os
import time


conn = hp_vertica_client.connect("")
cur = conn.cursor()

cur.execute("DROP VIEW IF EXISTS psLepSize_2lss_small")
cur.execute("DROP VIEW IF EXISTS psLepSize2_2lss_small")

cur.execute("DROP VIEW IF EXISTS tightLepSize_2lss_small")
cur.execute("DROP VIEW IF EXISTS lepSize1_2lss_small ")
cur.execute("DROP VIEW IF EXISTS lepSize2_2lss_small ")
cur.execute("DROP VIEW IF EXISTS lepSize_2lss_small ")
cur.execute("DROP VIEW IF EXISTS lepCharge_2lss_small")
cur.execute("DROP VIEW IF EXISTS isGsfTrue_2lss_small")
cur.execute("DROP VIEW IF EXISTS muChargeFlip_2lss_small")
cur.execute("DROP VIEW IF EXISTS numPsJets_2lss_small")
cur.execute("DROP VIEW IF EXISTS tightLepPt_2lss_small")
cur.execute("DROP VIEW IF EXISTS isGsfTrue_2lss_small")
cur.execute("DROP VIEW IF EXISTS sumPt_2lss_small")
cur.execute("DROP TABLE IF EXISTS pass2lss_small")


startTime = time.time()


cur.execute("CREATE view psLepSize_2lss_small AS SELECT Run, Lumi, Event, SampleID FROM psLeps_small GROUP BY Run, Lumi, Event, SampleID having count(run) =2")

cur.execute("CREATE view tightLepSize_2lss_small AS SELECT Run, Lumi, Event, SampleID, MIN(Pt) AS minPt, MAX(Pt) AS maxPt FROM tightLeps_small GROUP BY Run, Lumi, Event, SampleID having count(run) =2")

cur.execute("CREATE VIEW lepSize1_2lss_small AS SELECT psLepSize_2lss_small.Run, psLepSize_2lss_small.Lumi, psLepSize_2lss_small.Event, psLepSize_2lss_small.SampleID  FROM psLepSize_2lss_small JOIN tightLepSize_2lss_small ON  psLepSize_2lss_small.Run = tightLepSize_2lss_small.Run AND psLepSize_2lss_small.Lumi = tightLepSize_2lss_small.Lumi AND  psLepSize_2lss_small.Event = tightLepSize_2lss_small.Event AND psLepSize_2lss_small.SampleID = tightLepSize_2lss_small.SampleID")

cur.execute("CREATE VIEW psLepSize2_2lss_small AS SELECT Run, Lumi, Event, SampleID, MIN(Pt) as minPt FROM psLeps_small GROUP BY Run, Lumi, Event, SampleID HAVING COUNT(Run) = 3")

cur.execute("CREATE VIEW lepSize2_2lss_small AS SELECT v1.Run, v1.Lumi, v1.Event, v1.SampleID FROM psLepSize2_2lss_small AS v1 JOIN tightLepSize_2lss_small AS v2 ON v1.Run = v2.Run AND v1.Lumi = v2.Lumi AND v1.Event = v2.Event AND v1.SampleID = v2.SampleID WHERE v1.minPt < v2.minPt")

cur.execute("CREATE VIEW lepSize_2lss_small AS SELECT * FROM lepSize1_2lss_small UNION ALL SELECT * FROM lepSize2_2lss_small")

#cur.execute("CREATE VIEW lepSize2_2lss as SELECT ps.Run, ps.Lumi, ps.Event, ps.SampleID  FROM (  SELECT Run, Lumi, Event, SampleID FROM psLeps_small GROUP BY Run, Lumi, Event, SampleID HAVING COUNT(Run) = 3 ) AS ps JOIN (SELECT * FROM tightLepSize_2lss_small) AS tight ON ps.Run = tight.Run AND ps.Lumi = tight.Lumi AND ps.Event = tight.Event AND ps.SampleID = tight.SampleID JOIN (SELECT ps2.Run, ps2.Lumi, ps2.Event, ps2.SampleID FROM (SELECT Run, Lumi, Event, SampleID, Pt FROM psLeps_small GROUP BY Run, Lumi, Event, SampleID ORDER BY Pt ASC LIMIT 1 OFFSET 2) ps2 JOIN (SELECT * FROM tightLeps_small GROUP BY tightLeps_small.Run, tightLeps_small.Lumi, tightLeps_small.Event, tightLeps_small.SampleID ORDER BY tightLeps_small.Pt ASC LIMIT 1 OFFSET 1) tight2 ON tight2.Run = ps2.Run AND tight2.Lumi = ps2.Lumi AND tight2.Event = ps2.Event AND tight2.SampleID = ps2.SampleID where ps2.Pt < tight2.Pt) AS sub3 ON ps.Run = sub3.run AND ps.Lumi = sub3.Lumi AND ps.Event = sub3.Event AND ps.SampleID = sub3.SampleID ")

cur.execute("CREATE VIEW lepCharge_2lss_small AS SELECT Run, Lumi, Event, SampleID, SUM(Charge) FROM tightLeps_small GROUP BY Run, Lumi, Event, SampleID HAVING SUM(Charge) != 0")

#cur.execute("CREATE VIEW isGSfTrue_2lss_small AS SELECT t1.Run, t1.Lumi, t1.Event, t1.SampleID from event_info_small AS t1 LEFT OUTER JOIN tightMVABased_Electrons_small AS elec ON t1.Run = elec.Run AND t1.Lumi = elec.Lumi AND t1.Event = elec.Event AND t1.SampleID = elec.SampleID  GROUP BY t1.Run, t1.Lumi, t1.Event, t1.SampleID HAVING SUM(elec.isGsfCtfScPixChargeConsistent) = COUNT(elec.Run) ") 
cur.execute("CREATE VIEW isGSfTrue_2lss_small AS SELECT t1.Run, t1.Lumi, t1.Event, t1.SampleID, Sum(elec.isGsfCtfScPixChargeConsistent) from event_info_small AS t1 LEFT OUTER JOIN tightMVABased_Electrons_small AS elec ON t1.Run = elec.Run AND t1.Lumi = elec.Lumi AND t1.Event = elec.Event AND t1.SampleID = elec.SampleID  GROUP BY t1.Run, t1.Lumi, t1.Event, t1.SampleID HAVING SUM(elec.isGsfCtfScPixChargeConsistent) = COUNT(elec.Run) or COUNT(elec.Run) = 0 ") 

cur.execute("CREATE VIEW muChargeFlip_2lss_small AS SELECT t1.Run, t1.Lumi, t1.Event, t1.SampleID /*, MAX(mu.chargeFlip)*/ FROM event_info_small AS t1  LEFT OUTER JOIN  tightMVABased_Muons_small AS mu ON t1.Run = mu.Run AND t1.Lumi = mu.Lumi AND t1.Event = mu.Event AND t1.SampleID = mu.SampleID GROUP BY t1.Run, t1.Lumi, t1.Event, t1.SampleID  HAVING MAX(mu.chargeFlip) < 0.2 or COUNT(mu.Run) = 0 ")

cur.execute("CREATE VIEW numPsJets_2lss_small AS SELECT Run, Lumi, Event, SampleID FROM preselected_jets_small GROUP BY Run, Lumi, Event, SampleID HAVING COUNT(Run) > 3")

cur.execute("CREATE VIEW tightLepPt_2lss_small AS SELECT Run, Lumi, Event, SampleID FROM tightLeps_small WHERE Pt > 10 GROUP BY Run, Lumi, Event, SampleID HAVING COUNT(Run) >= 2 AND MAX(Pt) > 20")

cur.execute("CREATE VIEW sumPt_2lss_small AS SELECT v1.Run, v1.Lumi, v1.Event, v1.SampleID FROM tightLepSize_2lss_small AS v1 JOIN event_info_small AS v2 ON v1.Run = v2.Run AND v1.Lumi = v2.Lumi AND v1.Event = v2.Event AND v1.SampleID = v2.SampleID WHERE( v1.minPt + v1.maxPt + v2.metPt ) > 100")

cur.execute("CREATE TABLE pass2lss_small AS SELECT v1.Run, v1.Lumi, v1.Event, v1.SampleID FROM lepSize_2lss_small AS v1  JOIN lepCharge_2lss_small  AS v2 ON v1.Run = v2.Run AND v1.Lumi = v2.Lumi AND v1.Event = v2.Event AND v1.SampleID = v2.SampleID    JOIN isGSfTrue_2lss_small AS v3 ON v1.Run =v3.Run AND v1.Lumi = v3.Lumi AND v1.Event = v3.Event AND v1.SampleID = v3.SampleID    JOIN muChargeFlip_2lss_small AS v4 ON v1.Run = v4.Run AND v1.Lumi = v4.Lumi AND v1.Event = v4.Event AND v1.SampleID = v4.SampleID    JOIN numPsJets_2lss_small AS v5 ON v1.Run = v5.Run AND v1.Lumi = v5.Lumi AND v1.Event = v5.Event AND v1.SampleID = v5.SampleID    JOIN tightLepPt_2lss_small AS v6 ON v1.Run = v6.Run AND v1.Lumi = v6.Lumi AND v1.Event = v6.Event AND v1.SampleID = v6.SampleID   JOIN sumPt_2lss_small AS v7 ON v1.Run = v7.Run AND v1.Lumi = v7.Lumi AND v1.Event = v7.Event AND v1.SampleID = v7.SampleID    GROUP BY v1.Run, v1.Lumi, v1.Event, v1.SampleID")

cur.execute("commit")

cur.execute("Select count(*) from pass2lss_small")
print(cur.fetchall())

endTime = time.time() - startTime

print("total time: {}".format(endTime))



