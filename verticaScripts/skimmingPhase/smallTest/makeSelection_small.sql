
DROP TABLE IF EXISTS tightMVABased_Muons_small;
DROP TABLE IF EXISTS tightMVABased_Electrons_small;

PROFILE SELECT * FROM preselected_muons_small WHERE validFrac >= 0.8 and lepMVA > 0.75 and segCompatibility > CASE WHEN isGlobalMuon = 1 and normalizedChi2 < 3 and localChi2 < 12 and trKink < 20 THEN 0.303 ELSE 0.451 END ;

PROFILE SELECT * FROM preselected_electrons_small WHERE lepMVA > 0.75;



CREATE TABLE tightMVABased_Muons_small AS SELECT * FROM preselected_muons_small WHERE validFrac >= 0.8 and lepMVA > 0.75 and segCompatibility > CASE WHEN isGlobalMuon = 1 and normalizedChi2 < 3 and localChi2 < 12 and trKink < 20 THEN 0.303 ELSE 0.451 END ;

CREATE TABLE tightMVABased_Electrons_small AS SELECT * FROM preselected_electrons_small WHERE lepMVA > 0.75;

SELECT COUNT(*) FROM tightMVABased_Electrons_small;

SELECT COUNT(*) FROM tightMVABased_Muons_small;

