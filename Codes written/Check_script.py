# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 00:18:04 2019lq

@author: aqngu
"""

import os
output_dir = "/oasis/tscc/scratch/aqn018/aj_dad_lb/32"
cmd_file = input()
with open(cmd_file) as f:
   for line in f:
       cmd, ftp = line.rstrip().split(' ')
       # pops off the last element in a list
    
       file_name = ftp.split('/').pop()
    
       fq = output_dir + file_name
       
       if not os.path.isfile(fq): 
             print("WARNING: ",line)
            
#for fastq in jobs_file:
#    output = output_dir + job_file
#    if not os.path.isfile(output):
#           print("WOAH ", fastq)