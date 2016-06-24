#!/usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np
# from bedb import add_IDs
import pyhdust.phc as phc


fname = '../srcs/vie16a.tex'
tex = phc.readtextable(fname)

for i in range(len(tex)):
    tex[i][0] = 'hd'+tex[i][0]

np.savetxt('../BeDB/vie16a.bdb', tex, delimiter=', ', fmt='%s')
