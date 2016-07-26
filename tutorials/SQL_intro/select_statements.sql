DROP TABLE IF EXISTS KirkOrPicard;
DROP TABLE IF EXISTS BestCharacters;

CREATE TABLE KirkOrPicard (Institution varchar, Kirk int, Picard int);
CREATE TABLE BestCharacters (Institution varchar, Kirk int, Picard int, Spock int, Data int);

copy KirkOrPicard from stdin DELIMITER ',';
Calvin, 13, 1337
Notre Dame, 500, 1701
Hope, 1116, 42
\.

copy BestCharacters from stdin DELIMITER ',';
Calvin, 13, 1337, 100, 42
Notre Dame, 500, 1701, 96, 200
Hope, 1116, 42, 11, 13
\.

Select * from KirkOrPicard;

--sELeCt * FROm KirkORPICARD;

--Select * from KirkOrPicard where Institution = 'Notre Dame';

--Select Institution from KirkOrPicard where Picard > Kirk;

--Select Institution, Picard/(Picard+Kirk) as Proportion from KirkOrPicard where Picard > Kirk;  

--Select Institution from BestCharacters where Picard > Kirk and Data > Spock;

--Select Institution from (Select * from BestCharacters where Picard > Kirk) as Picard where Data > Spock;




