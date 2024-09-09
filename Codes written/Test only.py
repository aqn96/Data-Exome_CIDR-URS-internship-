# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 07:49:39 2019

@author: aqngu
"""

import os
os.chdir(r'C:\Users\aqngu\Desktop\URS\Files_For_Sorting')

# open a file for output
out = open("my_output_test.txt",'w')


# this opens the file
with open('hg002_svs_giab_illumina_calls_06_25_2019.txt','r') as x:
    # goes line-by-line
    for line in x:
        # remove the new-line character and split into a list
        row = line.rstrip().split('\t')
        out.write(line)
out.close()