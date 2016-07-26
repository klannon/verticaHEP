DROP TABLE IF EXISTS BestCharacters;

CREATE TABLE BestCharacters (Institution varchar, Department varchar, Kirk int, Picard int, Spock int, Data int); 

copy BestCharacters from stdin;
 Calvin      | Physics    | 1    | 500    | 42    | 3    |
 Calvin      | Math       | 2    | 800    | 50    | 2    |
 Calvin      | CS         | 10   | 37     | 8     | 37   |
 Notre Dame  | Physics    | 200  | 500    | 30    | 15   |
 Notre Dame  | Math       | 250  | 500    | 60    | 15   |
 Notre Dame  | CS         | 50   | 701    | 6     | 170  |
 Hope        | Physics    | 600  | 42     | 0     | 2    |
 Hope        | Math       | 300  | 0      | 8     | 5    |
 Hope        | CS         | 216  | 0      | 3     | 6    |
\.

Select Institution, SUM(Kirk) as Kirk, SUM(Picard) as Picard, SUM(Spock) as Spock, SUM(Data) as Data from BestCharacters group by Institution;

Select Department, SUM(Kirk) as Kirk, SUM(Picard) as Picard, SUM(Spock) as Spock, SUM(Data) as Data from BestCharacters group by Department;

Select Institution from BestCharacters group by Institution having SUM(Picard) > SUM(Kirk);





