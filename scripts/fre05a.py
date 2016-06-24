#!/usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np
import pyhdust.phc as phc
from glob import glob
from bedb import add_IDs


def put_file_order(fname):
    arr = []
    aux = []
    n = 1
    f0 = open(fname).read().split('\n')
    i = 0
    while i < len(f0):
        if0 = f0[i].split()
        if len(if0) != n:
            if n != 1:
                flaux = phc.flatten(aux)
                for j in range(n):
                    arr.extend(flaux[j::n])
            n = len(if0)
            aux = []
        if len(if0) == 1:
            arr.extend(if0)
        else:
            aux.append(if0)
        i += 1
    return arr

files = glob('../srcs/fre05a_*.txt')
files.sort()
ncols = 17

if 'fre05a' in locals():
    del(fre05a)

for f in files:
    arr = put_file_order(f)
    arr = np.array(arr).reshape((-1, len(arr)/ncols)).T
    if 'fre05a' not in locals():
        fre05a = arr[:]
    else:
        fre05a = np.vstack((fre05a, arr))

fre05a = fre05a.astype((str, fre05a.dtype.itemsize+2))
for i in range(len(fre05a)):
    fre05a[i, 0] = 'hd'+fre05a[i, 0]

add_IDs(fre05a[:, 0])

Vrot = fre05a[:, 8].astype(float)/np.sin(fre05a[:, 10].astype(float)*np.pi/180)
Vrot = np.where(Vrot > fre05a[:, 9].astype(float), 
        fre05a[:, 9].astype(float), Vrot)
VVcrit = Vrot/fre05a[:, 9].astype(float)

# M, Rp::
# Vc = np.sqrt(G*M/(1.5*Rp)); logg = np.log(G*M/Rp**2)
# Rp = Vc**2*1.5/np.exp(logg)  # convert units

np.savetxt('../BeDB/fre05a.bdb', fre05a, delimiter=', ', fmt='%s')
