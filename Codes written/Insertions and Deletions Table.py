# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 13:15:42 2019

@author: aqngu
"""

import os
os.chdir(r'C:\Users\aqngu\Desktop\URS\Files_For_Sorting')

# open a file for output
#out = open("my_output_Table.txt",'w')
#List = open("my_output_count.txt").read().splitlines()

#with open("my_output_Table.txt", 'w') as f:
#    for item in List:
#       f.write("%s \t" % item)
            
#out.close()


out = open("my_output_Table.txt",'w')
#List = open("my_output_count.txt").read().splitlines()
List = open("my_output_count.txt").read().splitlines()
y = ["\t","0/0","0/1","1/1","0/0","0/1","1/1","0/0","0/1","1/1"]
z = ["Table","Dad","\tMom","\tChild","\tTotal"]
print(List)

c = List[0:11]
d = List[11:22]
string = '\t\t'.join(z)+'\n'+'\t'.join(y)+'\n'+'\t'.join(c)+'\n'+'\t'.join(d)
out.write(string)
           
out.close()
