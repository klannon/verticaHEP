drop table if exists ttH_flatten cascade;

create flex table ttH_flatten();

copy ttH_flatten from '/home/newdbadmin/flexTableExample/ttH_flattenData.txt' parser fdelimitedparser();

select compute_flextable_keys('ttH_flatten');

select build_flextable_view('ttH_flatten');


