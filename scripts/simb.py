#!/usr/bin/env python
# -*- coding:utf-8 -*-

from astropy.io.votable import parse
import numpy as np
import pyhdust.phc as phc

simb = '../srcs/simb160623.xml.bz2'
votab = parse(simb)  # xml file
table = votab.get_first_table()
# table  # prints the table
data = table.array
# data[0] will NOT work! (It is a np structured array)
datacols = list(data.dtype.names)
dids = np.array(data['MAIN_ID']).astype(str)

ids = []
for i in dids:
    ids.append('_'.join(i.split()))

if False:
    import re 

    cats = ['hd_', 'hr_', 'HD_', 'HR_', 'CD-', 'CPD', 'BD-', 'BD+']
    IDs = phc.fileread('../IDs.txt').split('\n')[:-1]
    f0 = open('../newIDs.txt', 'w')
    for i in range(len(IDs)):
        ilist = re.split(', ', IDs[i])+[ ids[i] ]
        row = [j for j in ilist if (j[:3] not in cats)]
        f0.writelines(', '.join(row)+'\n')
    f0.close()
