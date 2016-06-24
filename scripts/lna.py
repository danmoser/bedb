#!/usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np
import csv


def start_IDs(lna):
    f0 = open('../IDs.txt', 'w')
    for row in lna:
        f0.writelines(', '.join([row[0], row[1], row[4]])+'\n')
    f0.close()
    return

lna = []
lines = csv.reader(open('../srcs/lna160623.csv'))
for row in lines:
    row[0] = row[0].replace(' ', '_')
    row[1] = 'hd'+row[1]
    lna.append(row)

if False:
    start_IDs(lna)
if False:
    f0 = open('../tmp.txt', 'w')
    for row in lna:
        f0.writelines(row[1]+'\n')
    f0.close()


bdb = []
for row in lna:
    if str(row[1]) != 'hd0':
        bdb.append([row[1], '1'])
    else:
        bdb.append([row[4], '1'])

np.savetxt('../BeDB/lna.bdb', bdb, fmt='%s', delimiter=', ')
