# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 10:53:31 2019

@author: aqngu
"""

import os
os.chdir(r'C:\Users\aqngu\Desktop\URS\Files_For_Sorting')

# open a file for output
outp = open("hg002_svs_giab_illumina_calls_06_25_2019_chr19_passed.txt",'w')
outf = open("hg002_svs_giab_illumina_calls_06_25_2019_chr19_failed.txt",'w')
outa = open("hg002_svs_giab_illumina_calls_06_25_2019_chr19.txt",'w')
outb = open("hg002_svs_giab_illumina_calls_06_25_2019_chr19_dad00_momnot.txt",'w')
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
        if chrom == "19" and svtp == "DEL":
            outa.write(line)
            if men_error == "FALSE" and ill_gt != "./." and hg_003 != "./." and hg_004 != "./." and gt == ill_gt:
                outp.write(line)#+"\n")
            else:
                outf.write(line)
                
        if chrom =="19" and svtp == "DEL" and men_error == "FALSE" and ill_gt != "./." and hg_003 != "./." and hg_004 != "./." and gt == ill_gt:
            if hg_003 == "0/0" and hg_004 != "0/0" :
                outb.write(line)
outa.close()
outp.close()
outb.close()
outf.close()