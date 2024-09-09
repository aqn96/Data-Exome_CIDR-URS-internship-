# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 10:44:06 2019

@author: aqngu
"""
my_r1_list = [] 
cmd_file = input()
open(cmd_file) as f:
   for line in f:
       string = line.split(' ').pop()
       # pops off the last element in a list
    
       file_name = my_r1_list.append(string)
    
       fq = output_dir + file_name



#list comprehension 
my_r2_list = [  x.replace('_R1_','_R2_')  for x in my_r1_list ] 

my_r1_cmd = 'zcat {}'.format(' '.join(my_r1_list) )
my_r2_cmd = 'zcat {}'.format(' '.join(my_r2_list) )

###################
my_r2_list=[]
for x in my_r1_list:
  my_r2_list.appned(x.replace(..... ) 