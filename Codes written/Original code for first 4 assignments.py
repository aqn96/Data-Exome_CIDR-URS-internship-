# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 10:39:11 2019

@author: aqngu
"""

import os

os.chdir(r'C:\Users\aqngu\Desktop\URS\Files_For_Sorting')

open('newfile','w').writelines([ line for line in open('hg002_svs_giab_illumina_calls_06_25_2019.txt') if 'FALSE' in line and "./." not in line and gt == ill_gt ])