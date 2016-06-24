#!/usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np
import pyhdust.phc as phc
# from glob import glob
from bedb import add_IDs


f1n = '../srcs/cha01a/table6.dat'
fwth = [1, 7, 11, 14, 15, 18, 24, 29, 33, 36, 40, 44]
cha01a = phc.readfixwd(f1n, fwth)

cha01a = cha01a.astype((str, cha01a.dtype.itemsize+2))
for i in range(len(cha01a)):
    cha01a[i][0] = 'hd'+cha01a[i][0]

add_IDs(cha01a[:, 0])

np.savetxt('../BeDB/cha01a.bdb', cha01a, delimiter=', ', fmt='%s')
