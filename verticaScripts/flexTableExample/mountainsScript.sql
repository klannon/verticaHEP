create flex table mountains();

copy mountains from '/home/newdbadmin/flexTableExample/mountains.json' parser fjsonparser();

select name, type, height from mountains;


