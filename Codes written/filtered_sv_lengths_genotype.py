# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 13:46:01 2019

@author: aqngu
"""

import os
import math
os.chdir(r'C:\Users\aqngu\Desktop\URS\Files_For_Sorting')

# open a file for output
out = open("my_svlength.txt",'w')


# this opens the file
with open("my_output.txt",'r') as x:
    # goes line-by-line
    for line in x:
        # remove the new-line character and split into a list
        row = line.rstrip().split('\t')

        chrom = row[0]
        pos = row[1]
        end = row[2]
        svtp = row[3]
        svlen = math.log10(abs(int(row[4])))
        ill_calls = row[5]
        men_error = row[6]
        hg_003 = row[7]
        hg_004 = row[8]
        gt = row[9]
        ill_gt = row[10]
               
        out.write(str(svlen)+"\n")

out.close()