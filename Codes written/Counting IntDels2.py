# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 13:27:43 2019

@author: aqngu
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 11:14:03 2019

@author: aqngu
"""

import os
os.chdir(r'C:\Users\aqngu\Desktop\URS\Files_For_Sorting')
unfiltered = 'hg002_svs_giab_illumina_calls_06_25_2019.txt'
filtered = 'hg002_svs_giab_illumina_filtered.txt'
# open a file for output
out = open("my_output_count_filtered.txt",'w')
file = open(filtered,'r')
count_ins = 0
count_inshg300 = 0
count_inshg301 = 0
count_inshg311 = 0
count_inshg400 = 0
count_inshg401 = 0
count_inshg411 = 0
count_insgt00 = 0
count_insgt01 = 0
count_insgt11 = 0
count_dels = 0
count_delshg300 = 0
count_delshg301 = 0
count_delshg311 = 0
count_delshg400 = 0
count_delshg401 = 0
count_delshg411 = 0
count_delsgt00 = 0
count_delsgt01 = 0 
count_delsgt11 = 0

for line in file:
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
    
    if svtp == "INS":
        count_ins += 1
    if svtp == "DEL":
        count_dels += 1
        
    if hg_003 == "0/0" and svtp == "INS":
        count_inshg300 += 1
    if hg_003 == "0/1" and svtp == "INS":
        count_inshg301 += 1
    if hg_003 == "1/1" and svtp == "INS":
        count_inshg311 += 1
        
    if hg_003 == "0/0" and svtp == "DEL":
        count_delshg300 += 1
    if hg_003 == "0/1" and svtp == "DEL":
        count_delshg301 += 1
    if hg_003 == "1/1" and svtp == "DEL":
        count_delshg311 += 1
        
    
    if hg_004 == "0/0" and svtp == "INS":
        count_inshg400 += 1
    if hg_004 == "0/1" and svtp == "INS":
        count_inshg401 += 1
    if hg_004 == "1/1" and svtp == "INS":
        count_inshg411 += 1
        
    if hg_004 == "0/0" and svtp == "DEL":
        count_delshg400 += 1
    if hg_004 == "0/1" and svtp == "DEL":
        count_delshg401 += 1
    if hg_004 == "1/1" and svtp == "DEL":
        count_delshg411 += 1
    
    
    if gt == "0/0" and svtp == "INS":
        count_insgt00 += 1
    if gt == "0/1" and svtp == "INS":
        count_insgt01 += 1
    if gt == "1/1" and svtp == "INS":
        count_insgt11 += 1
        
    if gt == "0/0" and svtp == "DEL":
        count_delsgt00 += 1
    if gt == "0/1" and svtp == "DEL":
        count_delsgt01 += 1
    if gt == "1/1" and svtp == "DEL":
        count_delsgt11 += 1
    
    
   
out.write("Insertions"+'\n'+str(count_inshg300)+'\n'+str(count_inshg301)+'\n'+str(count_inshg311)+'\n'+str(count_inshg400)
+'\n'+str(count_inshg401)+'\n'+str(count_inshg411)+'\n'+str(count_insgt00)+'\n'+str(count_insgt01)
+'\n'+str(count_insgt11)+'\n'+str(count_ins)+'\n'+"Deletions"+'\n'+str(count_delshg300)+'\n'+str(count_delshg301)+'\n'+str(count_delshg311)
+'\n'+str(count_delshg400)+'\n'+str(count_delshg401)+'\n'+str(count_delshg411)+'\n'+str(count_delsgt00)+'\n'+str(count_delsgt01)
+'\n'+str(count_delsgt11)+'\n'+str(count_dels)) 
            
out.close()
        