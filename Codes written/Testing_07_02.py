# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 12:39:51 2019

@author: aqngu
"""
import os

os.chdir(r'C:\Users\aqngu\Desktop\URS\Files_For_Sorting')

my_r1_list = [] 

txt = open('my_output_Table.txt','r')
for line in txt:
    #print(line)
#line = txt.readlines()
#print(line)
    string = line.rstrip().split().pop()
       # pops off the last element in a list
    my_r1_list.append(string)

print(my_r1_list)