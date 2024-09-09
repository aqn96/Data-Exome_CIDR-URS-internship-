# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 05:42:29 2019

@author: aqngu
"""
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 13:20:14 2019

@author: aqngu
"""

import pandas as pd
from pandas import ExcelWriter
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline


txt1 = '4dbsm_genomecov_out-1.txt'
txt2 = '4dbsm_genomecov_out-2.txt'
txt3 = '4dbsm_genomecov_out-3.txt'
txt4 = '4dbsm_genomecov_out-4.txt'
txt5 = '4dbsm_genomecov_out-5.txt'
txt6 = '4dbsm_genomecov_out-6.txt'
txt7 = '4dbsm_genomecov_out-7.txt'
txt8 = '4dbsm_genomecov_out-8.txt'
txt9 = '4dbsm_genomecov_out-9.txt'
txt10 = '4dbsm_genomecov_out-10.txt'
txt11 = '4dbsm_genomecov_out-11.txt'
txt12 = '4dbsm_genomecov_out-12.txt'

#lstxt1 = [txt1,txt2,txt3]
#lstxt2 = [txt4,txt5,txt6]

chrom = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','X','Y','genome']

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


table1 = {'Chrom': chrom, 'Depth': depth1}    
table2 = {'Chrom': chrom, 'Depth': depth2}
table3 = {'Chrom': chrom, 'Depth': depth3}    
table4 = {'Chrom': chrom, 'Depth': depth4}
table5 = {'Chrom': chrom, 'Depth': depth5}    
table6 = {'Chrom': chrom, 'Depth': depth6}
table7 = {'Chrom': chrom, 'Depth': depth7}    
table8 = {'Chrom': chrom, 'Depth': depth8}
table9 = {'Chrom': chrom, 'Depth': depth9}    
table10 = {'Chrom': chrom, 'Depth': depth10}
table11 = {'Chrom': chrom, 'Depth': depth11}    
table12 = {'Chrom': chrom, 'Depth': depth12}


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


df7.insert(0, "Sample Name", "4dbsm_genomecov_out_1_genomecov")
df8.insert(0, "Sample Name", "4dbsm_genomecov_out_2_genomecov")
df9.insert(0, "Sample Name", "4dbsm_genomecov_out_3_genomecov")
df10.insert(0, "Sample Name", "4dbsm_genomecov_out_4_genomecov")
df11.insert(0, "Sample Name", "4dbsm_genomecov_out_5_genomecov")
df12.insert(0, "Sample Name", "4dbsm_genomecov_out_6_genomecov")
df13.insert(0, "Sample Name", "4dbsm_genomecov_out_7_genomecov")
df14.insert(0, "Sample Name", "4dbsm_genomecov_out_8_genomecov")
df15.insert(0, "Sample Name", "4dbsm_genomecov_out_9_genomecov")
df16.insert(0, "Sample Name", "4dbsm_genomecov_out_10_genomecov")
df17.insert(0, "Sample Name", "4dbsm_genomecov_out_11_genomecov")
df18.insert(0, "Sample Name", "4dbsm_genomecov_out_12_genomecov")

dflist4dbsm = [df7,df9,df11,df13,df15,df17,df8,df10,df12,df14,df16,df18]


writer = ExcelWriter('../aqngu/Desktop/URS/Results/4dbsm_genomecov.xlsx')
for n, df in enumerate(dflist4dbsm):
    df.to_excel(writer, 'sheet%s' % str(n + 1))
writer.save()
