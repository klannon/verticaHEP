drop table if exists fakeDataFlex cascade;

create flex table fakeDataFlex();

--\set input_file '/home/newdbadmin/fakeDataTests/fakeData.txt';

copy fakeDataFlex from '/home/newdbadmin/fakeDataTests/fakeData.txt' parser fdelimitedparser(); -- :input_file;
-- DELIMITER '|';
--NULL ''
--record terminator E'\f';


