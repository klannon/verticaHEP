drop table if exists fakeData cascade;

create table fakeData (col1 integer, col2 float );

--\set input_file '/home/newdbadmin/fakeDataTests/fakeData.txt';

copy fakeData from '/home/newdbadmin/fakeDataTests/fakeData.txt'; -- :input_file;
-- DELIMITER '|';
--NULL ''
--record terminator E'\f';


