DROP TABLE IF EXISTS BestCharacters;
DROP TABLE IF EXISTS StarWars_StarTrek;

CREATE TABLE BestCharacters (Institution varchar, Department varchar, Kirk int, Picard int, Spock int, Data int); 

CREATE TABLE StarWars_StarTrek (Institution varchar, Department varchar, StarWars int, StarTrek int);

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

copy StarWars_StarTrek from stdin;
 Calvin      | Physics    | 6        | 3         
 Calvin      | Math       | 8        | 10        
 Notre Dame  | Physics    | 15       | 17        
 Notre Dame  | Math       | 30       | 11       
 Notre Dame  | CS         | 33       | 28        
\.

Select * from BestCharacters inner join StarWars_StarTrek on BestCharacters.Institution = StarWars_StarTrek.Institution and BestCharacters.Department = StarWars_StarTrek.Department;

Select * from BestCharacters left outer join StarWars_StarTrek on BestCharacters.Institution = StarWars_StarTrek.Institution and BestCharacters.Department = StarWars_StarTrek.Department;
