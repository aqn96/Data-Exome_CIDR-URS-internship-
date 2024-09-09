# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 13:20:14 2019

@author: aqngu
"""

import pandas as pd
from pandas import ExcelWriter
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline


txt1 = 'HG003.100subs.chr19.txt'
txt2 = 'HG004.100subs.chr19.txt'
txt3 = 'HG003.150subs.chr19.txt'
txt4 = 'HG004.50subs.chr19.txt'
txt5 = 'HG003.175subs.chr19.txt'
txt6 = 'HG004.25subs.chr19.txt'
txt7 = 'HG003.187.5subs.chr19.txt'
txt8 = 'HG004.12.5subs.chr19.txt'
txt9 = 'HG003.193.75subs.chr19.txt'
txt10 = 'HG004.6.25subs.chr19.txt'
txt11 = 'HG003.196.875subs.chr19.txt'
txt12 = 'HG004.3.125subs.chr19.txt'

lstxt1 = [txt1,txt2,txt3]
lstxt2 = [txt4,txt5,txt6]

chrom = ['19']

depth1 = []
depth2 = []
depth3 = []
depth4 = []
depth5 = []
depth6 = []
depth7 = []
depth8 = []
depth9 = []
depth10 =[]
depth11 = []
depth12 = []


#lsdepth1 = [depth1,depth2,depth3]
#lsdepth2 = [depth4,depth5,depth6]

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
    a = doc(df.loc[df['chrom']== x])
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

df7 = pd.read_csv('../aqngu/Desktop/URS/Results/'+txt7, sep="\t", header = None)
header = ['chrom','depth','count','length','prop']
df7.columns = header
df7.head()

df7['chrom'] = df7['chrom'].astype(str)

for x in chrom:
    a = doc(df7.loc[df7['chrom']== x])
    depth7.append(a)
    
df8 = pd.read_csv('../aqngu/Desktop/URS/Results/'+txt8, sep="\t", header = None)
header = ['chrom','depth','count','length','prop']
df8.columns = header
df8.head()

df8['chrom'] = df8['chrom'].astype(str)

for x in chrom:
    a = doc(df8.loc[df8['chrom']== x])
    depth8.append(a)
    
df9 = pd.read_csv('../aqngu/Desktop/URS/Results/'+txt9, sep="\t", header = None)
header = ['chrom','depth','count','length','prop']
df9.columns = header
df9.head()

df9['chrom'] = df9['chrom'].astype(str)

for x in chrom:
    a = doc(df9.loc[df9['chrom']== x])
    depth9.append(a)
    
df10 = pd.read_csv('../aqngu/Desktop/URS/Results/'+txt10, sep="\t", header = None)
header = ['chrom','depth','count','length','prop']
df10.columns = header
df10.head()

df10['chrom'] = df10['chrom'].astype(str)

for x in chrom:
    a = doc(df10.loc[df10['chrom']== x])
    depth10.append(a)
    
df11 = pd.read_csv('../aqngu/Desktop/URS/Results/'+txt11, sep="\t", header = None)
header = ['chrom','depth','count','length','prop']
df11.columns = header
df11.head()

df11['chrom'] = df11['chrom'].astype(str)

for x in chrom:
    a = doc(df11.loc[df11['chrom']== x])
    depth11.append(a)
    
df12 = pd.read_csv('../aqngu/Desktop/URS/Results/'+txt12, sep="\t", header = None)
header = ['chrom','depth','count','length','prop']
df12.columns = header
df12.head()

df12['chrom'] = df12['chrom'].astype(str)

for x in chrom:
    a = doc(df12.loc[df12['chrom']== x])
    depth12.append(a)


table1 = {'Chrom': '19', 'Depth': depth1}    
table2 = {'Chrom': '19', 'Depth': depth2}
table3 = {'Chrom': '19', 'Depth': depth3}    
table4 = {'Chrom': '19', 'Depth': depth4}
table5 = {'Chrom': '19', 'Depth': depth5}    
table6 = {'Chrom': '19', 'Depth': depth6}
table7 = {'Chrom': '19', 'Depth': depth7}    
table8 = {'Chrom': '19', 'Depth': depth8}
table9 = {'Chrom': '19', 'Depth': depth9}    
table10 = {'Chrom': '19', 'Depth': depth10}
table11 = {'Chrom': '19', 'Depth': depth11}    
table12 = {'Chrom': '19', 'Depth': depth12}


df7 = pd.DataFrame(data=table1)
df8 = pd.DataFrame(data=table2)
df9 = pd.DataFrame(data=table3)
df10 = pd.DataFrame(data=table4)
df11 = pd.DataFrame(data=table5)
df12 = pd.DataFrame(data=table6)
df13 = pd.DataFrame(data=table7)
df14 = pd.DataFrame(data=table8)
df15 = pd.DataFrame(data=table9)
df16 = pd.DataFrame(data=table10)
df17 = pd.DataFrame(data=table11)
df18 = pd.DataFrame(data=table12)


df7.insert(0, "Sample Name", "HG003.100subs.chr19.genomecov")
df8.insert(0, "Sample Name", "HG004.100subs.chr19.genomecov")
df9.insert(0, "Sample Name", "HG003.150subs.chr19.genomecov")
df10.insert(0, "Sample Name", "HG004.50subs.chr19.genomecov")
df11.insert(0, "Sample Name", "HG003.175subs.chr19.genomecov")
df12.insert(0, "Sample Name", "HG004.25subs.chr19.genomecov")
df13.insert(0, "Sample Name", "HG003.187.5subs.chr19.genomecov")
df14.insert(0, "Sample Name", "HG004.12.5subs.chr19.genomecov")
df15.insert(0, "Sample Name", "HG003.193.75subs.chr19.genomecov")
df16.insert(0, "Sample Name", "HG004.6.25subs.chr19.genomecov")
df17.insert(0, "Sample Name", "HG003.196.875subs.chr19.genomecov")
df18.insert(0, "Sample Name", "HG004.3.125subs.chr19.genomecov")

dflistHG003 = [df7,df9,df11,df13,df15,df17]
dflistHG004 = [df8,df10,df12,df14,df16,df18]

writer = ExcelWriter('../aqngu/Desktop/URS/Results/HG003_subschr19_genomecov.xlsx')
for n, df in enumerate(dflistHG003):
    df.to_excel(writer, 'sheet%s' % str(n + 1))
writer.save() 

writer = ExcelWriter('../aqngu/Desktop/URS/Results/HG004_subschr19_genomecov.xlsx')
for n, df in enumerate(dflistHG004):
    df.to_excel(writer, 'sheet%s' % str(n + 1))
writer.save()
