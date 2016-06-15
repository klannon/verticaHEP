drop table if exists ttHTable;

create  table ttHTable(nRow integer, Ht float, nJets integer, jet0pt float, jet0eta float, jet0phi float, jet1pt float, jet1eta float, jet1phi float, jet2pt float, jet2eta float, jet2phi float, jet3pt float, jet3eta float, jet3phi float, jet4pt float, jet4eta float, jet4phi float, nLep integer, lep0pt float, lep0eta float, lep0phi float, lep1pt float, lep1eta float, lep1phi float, lep2pt float, lep2eta float, lep2phi float, lep3pt float, lep3eta float, lep3phi float, lep4pt float, lep4eta float, lep4phi float);

copy ttHTable from '/home/newdbadmin/fakeDataTests/ttH_flattenData.txt' parser fdelimitedparser();
