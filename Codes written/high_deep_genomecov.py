# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 13:49:02 2019

@author: aqngu
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline


txt1 = 'HG002_High_genomecov.txt'
txt2 = 'HG003_High_genomecov.txt'
txt3 = 'HG004_High_genomecov.txt'
txt4 = 'HG002_Deep_genomecov.txt'
txt5 = 'HG003_Deep_genomecov.txt'
txt6 = 'HG004_Deep_genomecov.txt'
lstxt1 = [txt1,txt2,txt3]
lstxt2 = [txt4,txt5,txt6]

chrom = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','X','Y','genome']

depth1 = []
depth2 = []
depth3 = []
depth4 = []
depth5 = []
depth6 = []
lsdepth1 = [depth1,depth2,depth3]
lsdepth2 = [depth4,depth5,depth6]

def doc(df):
    
    num = sum(df['depth']*df['count'])
    dem = sum(df['count'])
    return num/dem
   
df = pd.read_csv('../aqngu/Desktop/URS/Results/'+txt1, sep="\t", header = None)
header = ['chrom','depth','count','length','prop']
df.columns = header
df.head()

df['chrom'] = df['chrom'].astype(str)

for x in chrom:
    a = doc(df.loc[df['chrom'] == x])
    depth1.append(a)
        
#print(depth1)


df2 = pd.read_csv('../aqngu/Desktop/URS/Results/'+txt2, sep="\t", header = None)
header = ['chrom','depth','count','length','prop']
df2.columns = header
df2.head()

df2['chrom'] = df2['chrom'].astype(str)

for x in chrom:
    a = doc(df2.loc[df2['chrom'] == x])
    depth2.append(a)

#print(depth2)

df3 = pd.read_csv('../aqngu/Desktop/URS/Results/'+txt3, sep="\t", header = None)
header = ['chrom','depth','count','length','prop']
df3.columns = header
df3.head()

df3['chrom'] = df3['chrom'].astype(str)

for x in chrom:
    a = doc(df3.loc[df3['chrom']== x])
    depth3.append(a)
        
#print(depth3)

df4 = pd.read_csv('../aqngu/Desktop/URS/Results/'+txt4, sep="\t", header = None)
header = ['chrom','depth','count','length','prop']
df4.columns = header
df4.head()

df4['chrom'] = df4['chrom'].astype(str)

for x in chrom:
    a = doc(df4.loc[df4['chrom']== x])
    depth4.append(str(a))
        
#print(depth4)


df5 = pd.read_csv('../aqngu/Desktop/URS/Results/'+txt5, sep="\t", header = None)
header = ['chrom','depth','count','length','prop']
df5.columns = header
df5.head()

df5['chrom'] = df5['chrom'].astype(str)

for x in chrom:
    a = doc(df5.loc[df5['chrom'] == x])
    depth5.append(a)

#print(depth5)

df6 = pd.read_csv('../aqngu/Desktop/URS/Results/'+txt6, sep="\t", header = None)
header = ['chrom','depth','count','length','prop']
df6.columns = header
df6.head()

df6['chrom'] = df6['chrom'].astype(str)

for x in chrom:
    a = doc(df6.loc[df6['chrom']== x])
    depth6.append(a)
        
#print(depth6)


table1 = {'Chrom': chrom, 'Depth': depth1}    
table2 = {'Chrom': chrom, 'Depth': depth2}
table3 = {'Chrom': chrom, 'Depth': depth3}    
table4 = {'Chrom': chrom, 'Depth': depth4}
table5 = {'Chrom': chrom, 'Depth': depth5}    
table6 = {'Chrom': chrom, 'Depth': depth6}

df7 = pd.DataFrame(data=table1)
df8 = pd.DataFrame(data=table2)
df9 = pd.DataFrame(data=table3)
df10 = pd.DataFrame(data=table4)
df11 = pd.DataFrame(data=table5)
df12 = pd.DataFrame(data=table6)
df7.insert(0, "Sample Name", "HG002_High_genomecov")
df8.insert(0, "Sample Name", "HG002_High_genomecov")
df9.insert(0, "Sample Name", "HG004_High_genomecov")
df10.insert(0, "Sample Name", "HG002_Deep_genomecov")
df11.insert(0, "Sample Name", "HG003_Deep_genomecov")
df12.insert(0, "Sample Name", "HG004_Deep_genomecov")

df13 = pd.concat([df7,df8,df9], axis=1)
df14 = pd.concat([df10,df11,df12], axis=1) 
                 
df13.to_csv('/Users/aqngu/Desktop/URS/Results/High_genomecov.csv2', index = None)
df14.to_csv('/Users/aqngu/Desktop/URS/Results/Deep_genomecov.csv2', index = None)