# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 19:03:48 2021

@author: crdub
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# open clean-aid from previous script 
aidhist = pd.read_csv('clean_aid.csv')

#select Foreign Aid from 1980 forward 
aidhist = aidhist[aidhist['fiscal_year'] != '1976tq']
aidhist['fiscal_year'] = aidhist['fiscal_year'].astype(int)
aidhist = aidhist[aidhist.fiscal_year>=1980]
aidhist = aidhist.set_index(['fiscal_year'])
aidhist = aidhist.sort_index()
aidhist.to_csv('aid1980.csv')

# select aid to Afghanistan only 
afg_aid = aidhist[aidhist['country']=='Afghanistan']
afg_aid = afg_aid.drop(columns=['region_name', 'income',])
afg_aid = afg_aid.rename(columns={'country':'Afghanistan'})

result = pd.concat ([aidhist, afg_aid], ignore_index=False)

# group Afghanistan by year 
afg_list = afg_aid.groupby(['fiscal_year'])
afg_total = afg_list['amt'].sum()
amil = afg_total.sum(level=['fiscal_year'])
amil = amil/1e9

# plot Afghanistan aid by year 
fig,ax1 = plt.subplots(dpi=300)
fig.suptitle("Foreign Aid to Afghanistan")
amil.plot(ax=ax1)
ax1.set_xlabel('Years')
ax1.set_ylabel('Million Dollars')
fig.tight_layout()
fig.savefig("afg_aid.png")

# create dataframe without Aghanistan aid 
afg_sin = aidhist[aidhist['country']!='Afghanistan']

# group by year 
afg_sin_list = afg_sin.groupby(['fiscal_year'])
afg_sin_total = afg_sin_list['amt'].sum()
sanmil = afg_sin_total.sum(level=['fiscal_year'])
sanmil = sanmil/1e9

# plot foreing aid without afhanistan 
fig,ax1 = plt.subplots(dpi=300)
fig.suptitle("Foreign Aid without Afghanistan")
sanmil.plot(ax=ax1)
ax1.set_xlabel('Years')
ax1.set_ylabel('Million Dollars')
fig.tight_layout()
fig.savefig("afg_sin_aid.png")

# group total aid by year 
res_list = result.groupby(['fiscal_year'])
res_total = res_list['amt'].sum()
rmil = res_total.sum(level=['fiscal_year'])
rmil = rmil/1e9

#%%
#plot both lines together 
fig,ax1 = plt.subplots(dpi=300)
sns.lineplot(data=rmil, label='Total Aid')
sns.lineplot(data=sanmil, label ='W/o Afghanistan')
fig.suptitle("Foreign Aid with/o Afghanistan")
ax1.set_xlabel("Year")
ax1.set_ylabel("Millions of Dollars")
plt.legend()
fig.savefig('AfghanAid.png')

