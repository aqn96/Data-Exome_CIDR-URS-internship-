# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 20:20:36 2019

@author: aqngu
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#matplotlib inline

df = pd.read_csv("/Users/aqngu/Desktop/URS/Files_For_Sorting/sv_figures_mendelistrue.txt",sep='\t'
                ,header=None)
# add a header
df.columns = ['chrom','start','end','svtype','svlen','illcalls','mendel','dad','mom','gt','illgt']
df.head()

dels = np.array(df.loc[df['svtype']=='DEL']['svlen']) * -1
ints = np.array(df.loc[df['svtype']=='INS']['svlen'])

dels = np.log10(dels)
ints = np.log10(ints)

#del_figure = plt.hist(dels,bins = 100)
#lt.savefig("/Users/aqngu/Desktop/URS/Files_For_Sorting/sv_del_nochromx_nounk.png")
#int_figure = plt.hist(ints,bins = 100)
#plt.savefig("/Users/aqngu/Desktop/URS/Files_For_Sorting/sv_int_nochromx_nounk.png")
#plt.savefig("/Users/aqngu/Desktop/URS/Files_For_Sorting/sv_figure_nochromx_nounk.png")
'''
def make_hist(arr):
    plt.hist(arr, bins=100)
    # labels for the axes
    plt.ylabel("Frequency")
    plt.xlabel("log10(SV length) [ bp ]")
    
    # make the limits consistent
    plt.xlim(1,5)
    plt.ylim(0,500)
    plt.savefig("/Users/aqngu/Desktop/URS/Files_For_Sorting/sv_int_nochromx_nounk.png")
'''
bins=100
plt.hist(dels,bins,alpha=0.8,label='DEL')
plt.hist(ints,bins,alpha=0.5,label='INS')

# show your labels
plt.legend()
plt.title("Ints/Dels with Mendelian Error" )
plt.ylabel("Frequency")
plt.xlabel("log10(SV length) [ bp ]")
#plt.savefig("/Users/aqngu/Desktop/URS/Files_For_Sorting/sv_figures_nochromx_nounk.png")
#plt.savefig("/Users/aqngu/Desktop/URS/Files_For_Sorting/sv_figure_gtisillgt.png")
plt.savefig("/Users/aqngu/Desktop/URS/Files_For_Sorting/sv_figures_mendelistrue.png")

