#!/usr/bin/env python

import os

f = open('filelist_C++.txt','w')

numFiles = 0

#tth files - write 1 for sampleID
for rootFile in os.listdir('/hadoop/store/user/lannon/bdtreco_v0/tth_nonbb/'):
   if rootFile != 'dummy.txt':
      #numFiles += 1
      f.write('/hadoop/store/user/lannon/bdtreco_v0/tth_nonbb/' + rootFile + ' ')
      numFiles += 1
      if numFiles % 4 == 0:
	f.write('\n')

for rootFile in os.listdir('/hadoop/store/user/lannon/bdtreco_v0/ttjets_semilep/'):
   if os.path.getsize('/hadoop/store/user/lannon/bdtreco_v0/ttjets_semilep/'+rootFile) > 1000000000:
      #numFiles += 1
      f.write('/hadoop/store/user/lannon/bdtreco_v0/ttjets_semilep/'+rootFile + ' ')
      numFiles += 1
      if numFiles % 4 == 0:
	f.write('\n')

f.close()
