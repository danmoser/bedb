#!/usr/bin/env python
# -*- coding:utf-8 -*-

""" Be stars paramaters database! 

:co-author: Rodrigo G. Vieira
:license: GNU GPL v3.0
"""

# import numpy as np
# import re as _re
from glob import glob as _glob
import numpy as _np

__version__ = '0.1.1'
__release__ = 'beta'
__author__ = "Daniel Moser"
__email__ = "dmfaes@gmail.com"


def search_IDlist(idname):
    idname = idname.lower().replace(' ', '')
    fids = open("IDs.txt").read().lower().replace(' ', '').split('\n')
    for i in fids:
        if idname in i:
            return i
    print('# Warning! {0} not in `IDs.txt` file'.format(idname))
    return []


def show_id_results(idname):
    idlist = search_IDlist(idname)
    if len(idlist) == 0:
        return
    bdb = _glob('BeDB/*.bdb')
    for db in bdb:
        idb = _np.loadtxt(db, dtype=str, delimiter=', ')
        for i in range(len(idb)):
            if idb[i, 0] in idlist:
                print('{0}:\n{1}\n'.format(db, idb[i]))
    return

if __name__ == '__main__':
    print('# This is a module. Import `bedb` at this folder!')
