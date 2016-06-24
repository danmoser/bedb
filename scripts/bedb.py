#!/usr/bin/env python
# -*- coding:utf-8 -*-

# import numpy as np
import re


def add_IDs(ids):
    fids = open("../IDs.txt").read().lower().replace(' ', '')
    fids = re.split('\n|,', fids)
    f0 = open("../IDs.txt", 'a')
    for i in range(len(ids)):
        if ids[i].lower().replace(' ', '') not in fids:
            f0.writelines(ids[i].lower().replace(' ', '')+"\n")
    f0.close()
    return

if __name__ == '__main__':
    print('# BeDB: a lot of things need to be done!')
