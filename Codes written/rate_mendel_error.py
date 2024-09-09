# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 05:19:56 2019

@author: aqngu
"""


import os
os.chdir(r'C:\Users\aqngu\Desktop\URS\Files_For_Sorting')

# open a file for output
out = open("Mendel_error_data.txt2",'w')
total = 0 
error = 0
error_ins = 0
error_del = 0
son01_men_err = 0
all01 = 0
son11_men_err = 0
all11 = 0
# this opens the file
with open('sv_figures_nochromx_nounk.txt','r') as x:
    # goes line-by-line
    for line in x:
        # remove the new-line character and split into a list
        row = line.rstrip().split('\t')
        total += 1

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
        
        if men_error == "TRUE":
            error += 1
        
        if men_error == "TRUE" and svtp == "INS":
            error_ins += 1
        
        if men_error == "TRUE" and svtp == "DEL":
            error_del += 1
        
        if men_error == "TRUE" and gt == "0/1":
            son01_men_err += 1
        
        if gt == "0/1":
            all01 += 1
        
        if men_error == "TRUE" and gt == "1/1":
            son11_men_err += 1
        
        if gt == "1/1":
            all11 += 1
        
rate_error = error/total
rate_ins_error = error_ins/total
rate_del_error = error_del/total
rate_son01_error = son01_men_err/all01
rate_son11_error = son11_men_err/all11 

out.write( "This is the total number of lines after filtering chrom X and unknowns " + str(total) + "\nThis is the total mendelian errors "
      + str(error) + "\nThe rate of error is " + str(rate_error) + 
      "\nThe rate of insertion errors is " + str(rate_ins_error) +
      "\nThe rate of deletion errors is " + str(rate_del_error) +
      "\nThe rate of errors when son is 0/1 over all 0/1 occurances is " + str(rate_son01_error) +
      "\nThe rate of error when son is 1/1 over all 1/1 occurances is " + str(rate_son11_error) )
out.close()