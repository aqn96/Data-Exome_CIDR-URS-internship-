# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 05:12:17 2019

@author: aqngu
"""

import os
os.chdir(r'C:\Users\aqngu\Desktop\URS\Files_For_Sorting')

unfiltered = 'hg002_svs_giab_illumina_calls_06_25_2019.txt'
filtered = 'hg002_svs_giab_illumina_filtered.txt'

out = open("svlength_data.txt",'w')

count_un_sv = 0
count_fil_sv = 0

count_un_son01 = 0
count_un_son11 = 0
count_fil_son01 = 0
count_fil_son11 = 0

with open(unfiltered,'r') as x:
        for line in x:
                row = line.rstrip().split('\t')
                
                svlen = row[4]
                son_gt = row[9]
                
                if str(abs(int(svlen))).isdigit():
                    count_un_sv += 1
                else:
                    print("error something wrong with unfiltered")
                    
                if son_gt == "0/1":
                    count_un_son01 += 1
                
                if son_gt == "1/1":
                    count_un_son11 += 1

with open(filtered,'r') as x:
        for line in x:
                row = line.rstrip().split('\t')
                
                svlen = row[4]
                son_gt = row[9]
                
                if str(abs(int(svlen))).isdigit():
                    count_fil_sv += 1
                else:
                    print("error something wrong with filtered")
                
                if son_gt == "0/1":
                    count_fil_son01 += 1
                
                if son_gt == "1/1":
                    count_fil_son11 += 1

print(str(count_un_sv) + " " + str(count_fil_sv) + " " + str(count_un_son01) +
      " " + str(count_un_son11) + " " + str(count_fil_son01) + " " + str(count_fil_son11))

diff = count_un_sv - count_fil_sv

out.write("The total number of unfiltered sv length is " + str(count_un_sv) +
          " and the total number of filtered sv length is " + str(count_fil_sv) +   
       "\nThe difference between total unfiltered and filtered is " + str(diff) 
      + "\n" + "The number of unfiltered sv lengths with gtype son of 0/1 is " +
      str(count_un_son01) + " and gtype of 1/1 is " + str(count_un_son11) + "\n"
      "The number of filtered sv lengths with gtype son of 0/1 is " + str(count_fil_son01)
      + " and gtype of 1/1 is " + str(count_fil_son11) )


           

