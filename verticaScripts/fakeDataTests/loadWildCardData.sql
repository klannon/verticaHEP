drop table if exists Endor cascade;

create table Endor (rebels integer, empire float );

--\set input_file '/home/newdbadmin/fakeDataTests/fakeData.txt';

copy Endor from '/home/newdbadmin/fakeDataTests/wildCardData/*'; -- :input_file;
-- DELIMITER '|';
--NULL ''
--record terminator E'\f';


