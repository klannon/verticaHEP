

SELECT Run, Lumi, Event, Pt, DENSE_RANK() OVER (PARTITION BY Run,Lumi,Event ORDER BY Pt desc) rank
FROM tightLeps_small
ORDER BY Run, Lumi, Event;
