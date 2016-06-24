#!/usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np
import pyhdust.phc as phc
# from glob import glob
from bedb import add_IDs


f1n = '../srcs/yud01a/appen1.dat.gz'
fwth = [12, 17, 23, 38, 39, 44, 50, 55, 59, 65]
yud01_1 = phc.readfixwd(f1n, fwth)

f2n = '../srcs/yud01a/appen2.dat.gz'
fwth = [12, 21, 22, 26, 31, 37, 42, 47, 48, 52, 53]
yud01_2 = phc.readfixwd(f2n, fwth)

for i in range(len(yud01_1)):
    yud01_1[i, 0] = yud01_1[i, 0].lower().replace(' ', '')

for i in range(len(yud01_2)):
    yud01_2[i, 0] = yud01_2[i, 0].lower().replace(' ', '')

add_IDs(yud01_1[:, 0])
add_IDs(yud01_2[:, 0])

np.savetxt('../BeDB/yud01a_1.bdb', yud01_1, delimiter=', ', fmt='%s')
np.savetxt('../BeDB/yud01a_2.bdb', yud01_2, delimiter=', ', fmt='%s')
