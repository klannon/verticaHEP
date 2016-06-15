drop table if exists fakeFlex cascade;

create flex table fakeFlex();

copy fakeFlex from '/home/newdbadmin/flexTableExample/fakeData.txt' parser fdelimitedparser();




