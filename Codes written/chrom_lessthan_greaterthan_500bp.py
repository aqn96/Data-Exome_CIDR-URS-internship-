# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 10:45:54 2019

@author: aqngu
"""
import pandas as pd
import numpy as np
import math
import csv
import os
os.chdir(r'C:\Users\aqngu\Desktop\URS\Files_For_Sorting')

my_dict1 = {}
my_dict2= {}

hg_003less = 0
hg_003more = 0
hg_004less = 0
hg_004more = 0
 
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
        
        
        if svtp == "DEL" and abs(int(svlen)) <= 500:
            if  ( ( '1' not in hg_003 and '1' in hg_004) or ('1' not in hg_004 and '1' in hg_003)) :
                hg_003less = hg_003
                hg_004less = hg_004
                key = ( chrom, hg_003less, hg_004less) 
                if my_dict1.get(key) == None: my_dict1[key]=1
                else: my_dict1[key]+=1
                
        if svtp == "DEL" and abs(int(svlen)) > 500:
            if  ( ( '1' not in hg_003 and '1' in hg_004) or ('1' not in hg_004 and '1' in hg_003)) :
                hg_003more = hg_003
                hg_004more = hg_004
                key = ( chrom, hg_003more, hg_004more) 
                if my_dict2.get(key) == None: my_dict2[key]=1
                else: my_dict2[key]+=1

for key in my_dict:       
    print(key, my_dict[key])
        
with open('Chrom_lessthan_or_greaterthan_500bp2.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in my_dict1.items():
        writer.writerow([key, value])    
    for key, value in my_dict2.items():
        writer.writerow([key, value])
    
        
        
        
        
        
        
        
        
        
        
        
        