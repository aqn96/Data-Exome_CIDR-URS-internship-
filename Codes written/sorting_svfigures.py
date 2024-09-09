# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 19:46:34 2019

@author: aqngu
"""

import os
os.chdir(r'C:\Users\aqngu\Desktop\URS\Files_For_Sorting')

# open a file for output
out = open("sv_figures_son11.txt",'w')

'''
# this opens the file
with open('hg002_svs_giab_illumina_calls_06_25_2019.txt','r') as x:
    # goes line-by-line
    for line in x:
        # remove the new-line character and split into a list
        row = line.rstrip().split('\t')

        chrom = row[0]
        pos = row[1]
        end = row[2]
        svtp = row[3]
        svlen = row[4]
        ill_calls = row[5]
        men_error = row[6]
        hg_003 = row[7]
        hg_004 = row[8]
        gt = row[9]
        ill_gt = row[10]
        
        if chrom != "X" and ill_gt != "./." and hg_003 != "./." and hg_004 != "./.":
            out.write(line)#+"\n")

out.close()

with open('sv_figures_nochromx_nounk.txt','r') as x:
    # goes line-by-line
    for line in x:
        # remove the new-line character and split into a list
        row = line.rstrip().split('\t')

        chrom = row[0]
        pos = row[1]
        end = row[2]
        svtp = row[3]
        svlen = row[4]
        ill_calls = row[5]
        men_error = row[6]
        hg_003 = row[7]
        hg_004 = row[8]
        gt = row[9]
        ill_gt = row[10]
        
        if gt == ill_gt:
            out.write(line)#+"\n")

out.close()

with open('sv_figures_nochromx_nounk.txt','r') as x:
    # goes line-by-line
    for line in x:
        # remove the new-line character and split into a list
        row = line.rstrip().split('\t')

        chrom = row[0]
        pos = row[1]
        end = row[2]
        svtp = row[3]
        svlen = row[4]
        ill_calls = row[5]
        men_error = row[6]
        hg_003 = row[7]
        hg_004 = row[8]
        gt = row[9]
        ill_gt = row[10]
        
        if gt != ill_gt:
            out.write(line)#+"\n")

out.close()

with open('sv_figures_nochromx_nounk.txt','r') as x:
    # goes line-by-line
    for line in x:
        # remove the new-line character and split into a list
        row = line.rstrip().split('\t')

        chrom = row[0]
        pos = row[1]
        end = row[2]
        svtp = row[3]
        svlen = row[4]
        ill_calls = row[5]
        men_error = row[6]
        hg_003 = row[7]
        hg_004 = row[8]
        gt = row[9]
        ill_gt = row[10]
        
        if men_error == "FALSE":
            out.write(line)#+"\n")

out.close()
'''
with open('sv_figures_nochromx_nounk.txt','r') as x:
    # goes line-by-line
    for line in x:
        # remove the new-line character and split into a list
        row = line.rstrip().split('\t')

        chrom = row[0]
        pos = row[1]
        end = row[2]
        svtp = row[3]
        svlen = row[4]
        ill_calls = row[5]
        men_error = row[6]
        hg_003 = row[7]
        hg_004 = row[8]
        gt = row[9]
        ill_gt = row[10]
        
        if gt == "1/1":
            out.write(line)#+"\n")

out.close()