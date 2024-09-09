# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 20:14:25 2019

@author: aqngu
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#matplotlib inline

df = pd.read_csv("/Users/aqngu/Desktop/URS/Files_For_Sorting/hg002_svs_giab_illumina_filtered.txt",sep='\t'
                ,header=None)
# add a header
df.columns = ['chrom','start','end','svtype','svlen','illcalls','mendel','dad','mom','gt','illgt']
df.head()

dels = np.array(df.loc[df['svtype']=='DEL']['svlen']) * -1
ints = np.array(df.loc[df['svtype']=='INS']['svlen'])

dels = np.log10(dels)
ints = np.log10(ints)

plt.hist(dels,bins = 100)
plt.show()

plt.hist(ints,bins = 100)
plt.show()

def make_hist(arr):
    plt.hist(arr, bins=100)
    # labels for the axes
    plt.ylabel("Frequency")
    plt.xlabel("log10(SV length) [ bp ]")
    
    # make the limits consistent
    plt.xlim(1,5)
    plt.ylim(0,500)
    plt.show()
    
make_hist(dels)
make_hist(ints)

# you can also overlap the distributions on the same figure
# alpha will make the figure transparent
bins=100
plt.hist(dels,bins,alpha=0.5,label='DEL')
plt.hist(ints,bins,alpha=0.5,label='INS')

# show your labels
plt.legend()

plt.show()

# subplot: 1 figure but 2 plots
def make_hist(arr, ax,title, color):
    ax.hist(arr, 
            bins=100, 
            color=color,
            histtype='step',
            linewidth=2
           )
    
    
    # labels for the axes
    ax.set_ylabel("Frequency")
    ax.set_xlabel("log10(SV length) [ bp ]")
    
    # make the limits consistent
    ax.set_xlim(1,5)
    ax.set_ylim(0,500)
    
    # make the title
    ax.set_title(title,weight="bold",fontsize=12)

# sublpots(number of rows, number of columns, figsize = (width, height) )
fig, ax = plt.subplots(1,2,figsize=(8,4))

#DEL hist
make_hist(dels, ax[0], 'DEL', '#ff6666')
#INS 
make_hist(ints, ax[1], 'INS', 'blue')

fig.tight_layout()
# save figure: always save after tight_layout()
#fig.savefig("h002_filtered_sv_len.png")
#fig.savefig("h002_filtered_sv_len.svg", dpi= 500)
fig.show()

import seaborn as sns

df['svlen'] = abs(df['svlen'])
df['loglen'] = np.log10(df['svlen'])

sns.swarmplot(x='svtype',y='loglen',data=df)

