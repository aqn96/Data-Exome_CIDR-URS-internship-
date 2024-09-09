# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 02:36:52 2019

@author: aqngu
"""

import pandas as pd
import numpy as np
import math
import os
os.chdir(r'C:\Users\aqngu\Desktop\URS\Files_For_Sorting')
#matplotlib inline

my_dict = {}
mom00_dad01 = 0
mom00_dad11 = 0
mom00_dad00 = 0
mom01_dad00 = 0
mom01_dad01 = 0
mom11_dad11 = 0

sv_less50 = 0
sv_bet50_100 = 0
sv_bet100_250 = 0
sv_bet250_500 = 0
sv_bet500_1kb = 0
sv_bet1kb_5kb = 0
sv_bet5kb_10kb = 0
sv_bet10kb_100kb = 0
sv_more100kb = 0
total = 0

chrom1less500bp = 0
chrom1more500bp = 0
chrom2less500bp = 0
chrom2more500bp = 0
chrom3less500bp = 0
chrom3more500bp = 0
chrom4less500bp = 0
chrom4more500bp = 0
chrom5less500bp = 0
chrom5more500bp = 0
chrom6less500bp = 0
chrom6more500bp = 0
chrom7less500bp = 0
chrom7more500bp = 0
chrom8less500bp = 0
chrom8more500bp = 0
chrom9less500bp = 0
chrom9more500bp = 0
chrom10less500bp = 0
chrom10more500bp = 0
chrom11less500bp = 0
chrom11more500bp = 0
chrom12less500bp = 0
chrom12more500bp = 0
chrom13less500bp = 0
chrom13more500bp = 0
chrom14less500bp = 0
chrom14more500bp = 0
chrom15less500bp = 0
chrom15more500bp = 0
chrom16less500bp = 0
chrom16more500bp = 0
chrom17less500bp = 0
chrom17more500bp = 0
chrom18less500bp = 0
chrom18more500bp = 0
chrom19less500bp = 0
chrom19more500bp = 0
chrom20less500bp = 0
chrom20more500bp = 0
chrom21less500bp = 0
chrom21more500bp = 0
chrom22less500bp = 0
chrom22more500bp = 0
 
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
        
        if hg_003 == "0/1" and hg_004 == "0/0":
            mom00_dad01 += 1
        if hg_003 == "1/1" and hg_004 == "0/0":
            mom00_dad11 += 1
        if hg_003 == "0/0" and hg_004 == "0/0":
            mom00_dad00 += 1
        if hg_003 == "0/0" and hg_004 == "0/1":
            mom01_dad00 += 1   
        if hg_003 == "0/1" and hg_004 == "0/1":
            mom01_dad01 += 1
        if hg_003 == "1/1" and hg_004 == "1/1":
            mom11_dad11 += 1
        
        if abs(int(svlen)) <= 50:
            sv_less50 += 1
        elif 50 < abs(int(svlen)) <= 100:
            sv_bet50_100 += 1       
        elif 100 < abs(int(svlen)) <= 250:
            sv_bet100_250 += 1
        elif 250 < abs(int(svlen)) <= 500:
            sv_bet250_500 += 1
        elif 500 < abs(int(svlen)) <= 1000:
            sv_bet500_1kb += 1
        elif 1000 < abs(int(svlen)) <= 5000:
            sv_bet1kb_5kb += 1
        elif 5000 < abs(int(svlen)) <= 10000:
            sv_bet5kb_10kb += 1
        elif 10000 < abs(int(svlen)) <= 100000:
            sv_bet10kb_100kb += 1
        elif abs(int(svlen)) > 100000:
            sv_more100kb += 1
            
        if svtp == "DEL"  and (hg_004 == "0/1" or hg_004 == "1/1"):
            if chrom == "1" and hg_003 == "0/0" and abs(int(svlen)) <= 500:chrom1less500bp += 1
            elif chrom == "1" and hg_003 == "0/0" and abs(int(svlen)) > 500:chrom1more500bp += 1      
            elif chrom == "2" and hg_003 == "0/0" and abs(int(svlen)) <= 500:chrom2less500bp += 1
            elif chrom == "2" and hg_003 == "0/0" and abs(int(svlen)) > 500:chrom2more500bp += 1
            elif chrom == "3" and hg_003 == "0/0" and abs(int(svlen)) <= 500:chrom3less500bp += 1
            elif chrom == "3" and hg_003 == "0/0" and abs(int(svlen)) > 500:chrom3more500bp += 1
            elif chrom == "4" and hg_003 == "0/0" and abs(int(svlen)) <= 500:chrom4less500bp += 1
            elif chrom == "4" and hg_003 == "0/0" and abs(int(svlen)) > 500:chrom4more500bp += 1
            elif chrom == "5" and hg_003 == "0/0" and abs(int(svlen)) <= 500:chrom5less500bp += 1
            elif chrom == "5" and hg_003 == "0/0" and abs(int(svlen)) > 500:chrom5more500bp += 1
            elif chrom == "6" and hg_003 == "0/0" and abs(int(svlen)) <= 500:chrom6less500bp += 1
            elif chrom == "6" and hg_003 == "0/0" and abs(int(svlen)) > 500:chrom6more500bp += 1
            elif chrom == "7" and hg_003 == "0/0" and abs(int(svlen)) <= 500:chrom7less500bp += 1
            elif chrom == "7" and hg_003 == "0/0" and abs(int(svlen)) > 500:chrom7more500bp += 1
            elif chrom == "8" and hg_003 == "0/0" and abs(int(svlen)) <= 500:chrom8less500bp += 1
            elif chrom == "8" and hg_003 == "0/0" and abs(int(svlen)) > 500:chrom8more500bp += 1
            elif chrom == "9" and hg_003 == "0/0" and abs(int(svlen)) <= 500:chrom9less500bp += 1
            elif chrom == "9" and hg_003 == "0/0" and abs(int(svlen)) > 500:chrom9more500bp += 1
            elif chrom == "10" and hg_003 == "0/0" and abs(int(svlen)) <= 500:chrom10less500bp += 1
            elif chrom == "10" and hg_003 == "0/0" and abs(int(svlen)) > 500:chrom10more500bp += 1
            elif chrom == "11" and hg_003 == "0/0" and abs(int(svlen)) <= 500:chrom11less500bp += 1
            elif chrom == "11" and hg_003 == "0/0" and abs(int(svlen)) > 500:chrom11more500bp += 1
            elif chrom == "12" and hg_003 == "0/0" and abs(int(svlen)) <= 500:chrom12less500bp += 1
            elif chrom == "12" and hg_003 == "0/0" and abs(int(svlen)) > 500:chrom12more500bp += 1
            elif chrom == "13" and hg_003 == "0/0" and abs(int(svlen)) <= 500:chrom13less500bp += 1
            elif chrom == "13" and hg_003 == "0/0" and abs(int(svlen)) > 500:chrom13more500bp += 1
            elif chrom == "14" and hg_003 == "0/0" and abs(int(svlen)) <= 500:chrom14less500bp += 1
            elif chrom == "14" and hg_003 == "0/0" and abs(int(svlen)) > 500:chrom14more500bp += 1
            elif chrom == "15" and hg_003 == "0/0" and abs(int(svlen)) <= 500:chrom15less500bp += 1
            elif chrom == "15" and hg_003 == "0/0" and abs(int(svlen)) > 500:chrom15more500bp += 1
            elif chrom == "16" and hg_003 == "0/0" and abs(int(svlen)) <= 500:chrom16less500bp += 1
            elif chrom == "16" and hg_003 == "0/0" and abs(int(svlen)) > 500:chrom16more500bp += 1
            elif chrom == "17" and hg_003 == "0/0" and abs(int(svlen)) <= 500:chrom17less500bp += 1
            elif chrom == "17" and hg_003 == "0/0" and abs(int(svlen)) > 500:chrom17more500bp += 1
            elif chrom == "18" and hg_003 == "0/0" and abs(int(svlen)) <= 500:chrom18less500bp += 1
            elif chrom == "18" and hg_003 == "0/0" and abs(int(svlen)) > 500:chrom18more500bp += 1
            elif chrom == "19" and hg_003 == "0/0" and abs(int(svlen)) <= 500:chrom19less500bp += 1
            elif chrom == "19" and hg_003 == "0/0" and abs(int(svlen)) > 500:chrom19more500bp += 1
            elif chrom == "20" and hg_003 == "0/0" and abs(int(svlen)) <= 500:chrom20less500bp += 1
            elif chrom == "20" and hg_003 == "0/0" and abs(int(svlen)) > 500:chrom20more500bp += 1
            elif chrom == "21" and hg_003 == "0/0" and abs(int(svlen)) <= 500:chrom21less500bp += 1
            elif chrom == "21" and hg_003 == "0/0" and abs(int(svlen)) > 500:chrom21more500bp += 1
            elif chrom == "22" and hg_003 == "0/0" and abs(int(svlen)) <= 500:chrom22less500bp += 1
            elif chrom == "22" and hg_003 == "0/0" and abs(int(svlen)) > 500:chrom22more500bp += 1
            
        if svtp == "DEL"  and (hg_003 == "0/1" or hg_003 == "1/1"):
            if chrom == "1" and hg_004 == "0/0" and abs(int(svlen)) <= 500:chrom1less500bp += 1
            elif chrom == "1" and hg_004 == "0/0" and abs(int(svlen)) > 500:chrom1more500bp += 1      
            elif chrom == "2" and hg_004 == "0/0" and abs(int(svlen)) <= 500:chrom2less500bp += 1
            elif chrom == "2" and hg_004 == "0/0" and abs(int(svlen)) > 500:chrom2more500bp += 1
            elif chrom == "3" and hg_004 == "0/0" and abs(int(svlen)) <= 500:chrom3less500bp += 1
            elif chrom == "3" and hg_004 == "0/0" and abs(int(svlen)) > 500:chrom3more500bp += 1
            elif chrom == "4" and hg_004 == "0/0" and abs(int(svlen)) <= 500:chrom4less500bp += 1
            elif chrom == "4" and hg_004 == "0/0" and abs(int(svlen)) > 500:chrom4more500bp += 1
            elif chrom == "5" and hg_004 == "0/0" and abs(int(svlen)) <= 500:chrom5less500bp += 1
            elif chrom == "5" and hg_004 == "0/0" and abs(int(svlen)) > 500:chrom5more500bp += 1
            elif chrom == "6" and hg_004 == "0/0" and abs(int(svlen)) <= 500:chrom6less500bp += 1
            elif chrom == "6" and hg_004 == "0/0" and abs(int(svlen)) > 500:chrom6more500bp += 1
            elif chrom == "7" and hg_004 == "0/0" and abs(int(svlen)) <= 500:chrom7less500bp += 1
            elif chrom == "7" and hg_004 == "0/0" and abs(int(svlen)) > 500:chrom7more500bp += 1
            elif chrom == "8" and hg_004 == "0/0" and abs(int(svlen)) <= 500:chrom8less500bp += 1
            elif chrom == "8" and hg_004 == "0/0" and abs(int(svlen)) > 500:chrom8more500bp += 1
            elif chrom == "9" and hg_004 == "0/0" and abs(int(svlen)) <= 500:chrom9less500bp += 1
            elif chrom == "9" and hg_004 == "0/0" and abs(int(svlen)) > 500:chrom9more500bp += 1
            elif chrom == "10" and hg_004 == "0/0" and abs(int(svlen)) <= 500:chrom10less500bp += 1
            elif chrom == "10" and hg_004 == "0/0" and abs(int(svlen)) > 500:chrom10more500bp += 1
            elif chrom == "11" and hg_004 == "0/0" and abs(int(svlen)) <= 500:chrom11less500bp += 1
            elif chrom == "11" and hg_004 == "0/0" and abs(int(svlen)) > 500:chrom11more500bp += 1
            elif chrom == "12" and hg_004 == "0/0" and abs(int(svlen)) <= 500:chrom12less500bp += 1
            elif chrom == "12" and hg_004 == "0/0" and abs(int(svlen)) > 500:chrom12more500bp += 1
            elif chrom == "13" and hg_004 == "0/0" and abs(int(svlen)) <= 500:chrom13less500bp += 1
            elif chrom == "13" and hg_004 == "0/0" and abs(int(svlen)) > 500:chrom13more500bp += 1
            elif chrom == "14" and hg_004 == "0/0" and abs(int(svlen)) <= 500:chrom14less500bp += 1
            elif chrom == "14" and hg_004 == "0/0" and abs(int(svlen)) > 500:chrom14more500bp += 1
            elif chrom == "15" and hg_004 == "0/0" and abs(int(svlen)) <= 500:chrom15less500bp += 1
            elif chrom == "15" and hg_004 == "0/0" and abs(int(svlen)) > 500:chrom15more500bp += 1
            elif chrom == "16" and hg_004 == "0/0" and abs(int(svlen)) <= 500:chrom16less500bp += 1
            elif chrom == "16" and hg_004 == "0/0" and abs(int(svlen)) > 500:chrom16more500bp += 1
            elif chrom == "17" and hg_004 == "0/0" and abs(int(svlen)) <= 500:chrom17less500bp += 1
            elif chrom == "17" and hg_004 == "0/0" and abs(int(svlen)) > 500:chrom17more500bp += 1
            elif chrom == "18" and hg_004 == "0/0" and abs(int(svlen)) <= 500:chrom18less500bp += 1
            elif chrom == "18" and hg_004 == "0/0" and abs(int(svlen)) > 500:chrom18more500bp += 1
            elif chrom == "19" and hg_004 == "0/0" and abs(int(svlen)) <= 500:chrom19less500bp += 1
            elif chrom == "19" and hg_004 == "0/0" and abs(int(svlen)) > 500:chrom19more500bp += 1
            elif chrom == "20" and hg_004 == "0/0" and abs(int(svlen)) <= 500:chrom20less500bp += 1
            elif chrom == "20" and hg_004 == "0/0" and abs(int(svlen)) > 500:chrom20more500bp += 1
            elif chrom == "21" and hg_004 == "0/0" and abs(int(svlen)) <= 500:chrom21less500bp += 1
            elif chrom == "21" and hg_004 == "0/0" and abs(int(svlen)) > 500:chrom21more500bp += 1
            elif chrom == "22" and hg_004 == "0/0" and abs(int(svlen)) <= 500:chrom22less500bp += 1
            elif chrom == "22" and hg_004 == "0/0" and abs(int(svlen)) > 500:chrom22more500bp += 1
         
    
dad_gt = ["0/1","1/1","0/0","0/0","0/1","1/1"]
mom_gt = ["0/0","0/0","0/0","0/1","0/1","1/1"]
num_sv = map(str, [mom00_dad01,mom00_dad11,mom00_dad00,mom01_dad00,mom01_dad01,mom11_dad11])
my_num_sv = list(num_sv)
num_bin_size = ["<50","51-100","101-250","251-500","501-1kb","1kb-5kb","5kb-10kb","10kb-100kb",">100kb","Total"]
data_bin_size = map(str, [sv_less50,sv_bet50_100,sv_bet100_250,sv_bet250_500,sv_bet500_1kb,sv_bet1kb_5kb,sv_bet5kb_10kb,sv_bet10kb_100kb,sv_more100kb,total])
my_data_bin_size = list(data_bin_size)

chrom = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22']
del_less500bp = [chrom1less500bp,chrom2less500bp,chrom3less500bp,chrom4less500bp,chrom5less500bp,chrom6less500bp,chrom7less500bp,
                 chrom8less500bp,chrom9less500bp,chrom10less500bp,chrom11less500bp,chrom12less500bp,chrom13less500bp,chrom14less500bp,
                 chrom15less500bp,chrom16less500bp,chrom17less500bp,chrom18less500bp,chrom19less500bp,chrom20less500bp,chrom21less500bp,chrom22less500bp]

del_more500bp = [chrom1more500bp,chrom2more500bp,chrom3more500bp,chrom4more500bp,chrom5more500bp,chrom6more500bp,chrom7more500bp,
                 chrom8more500bp,chrom9more500bp,chrom10more500bp,chrom11more500bp,chrom12more500bp,chrom13more500bp,chrom14more500bp,
                 chrom15more500bp,chrom16more500bp,chrom17more500bp,chrom18more500bp,chrom19more500bp,chrom20more500bp,chrom21more500bp,chrom22more500bp]





table1 = { 'DAD GT': dad_gt, 'MOM GT': mom_gt, 'NUMBER of SVs': my_num_sv}
table2 = {'NUMBER of SV SIZE BIN': num_bin_size, '[DATA] NUMBER of SV SIZE BIN': my_data_bin_size}
table3 = { 'HG003 at gt 0/0 and HG004 at gt 0/1 or 1/1 [Chrom]': chrom, '# Dels less than 500bp': del_less500bp , '#Dels greater than 500bp': del_more500bp}

df1 = pd.DataFrame(data=table1)
df2 = pd.DataFrame(data=table2)
df3 = pd.concat([df1,df2], axis=1) 
df4 = pd.DataFrame(data=table3)

df3.to_csv('Filtered_SVs_table.csv', index = None)
df3.to_csv('Filtered_SVs_table.txt', index=None, sep='\t')
df4.to_csv('Chrom_lessthan_or_greaterthan_500bp.csv', index = None)
