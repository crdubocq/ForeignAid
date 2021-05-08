# -*- coding: utf-8 -*-
"""
Created on Sat May  8 13:12:06 2021

@author: crdub
"""

import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt


# read database 
aiddist = pd.read_csv('clean_aid.csv')


# grouby and csv 
group_by_region_cat = aiddist.groupby(['region_name','dac_category'])
by_region_cat = group_by_region_cat['amt'].sum()
by_region_cat.to_csv('by_region_cat.csv')

mil = by_region_cat.sum(level=['region_name','dac_category'])
mil=mil/1e6
by_dac = mil.sum(level='dac_category')
top_dac = by_dac.sort_values()
top_dac = top_dac[-10:]
print('\nTop Development Assistance Category:',top_dac)

by_reg = mil.sum(level='region_name')
top_reg = by_reg.sort_values()
top_reg = top_reg[-10:]
print('\nTop Regions:',top_reg)

reset = mil.reset_index()
keep_dac = reset['dac_category'].isin(top_dac.index)
keep_reg = reset['region_name'].isin(top_reg.index)
keep = keep_dac & keep_reg

sub= reset[keep]
grouped =sub.groupby(['region_name','dac_category'])
summed = grouped['amt'].sum()
grid = summed.unstack('region_name')

#plot heatmap 
fig, ax1 = plt.subplots(dpi=300, figsize=(8,8))
fig.suptitle("Contributions in Millions")
sns.heatmap(grid, annot=True, fmt=".0f", ax=ax1)
ax1.set_xlabel("Regions")
ax1.set_ylabel("DAC")
fig.tight_layout()
fig.savefig('heatmap.png')

#%%
group_by_country_cat = aiddist.groupby(['country','dac_category'])
by_country_cat = group_by_country_cat['amt'].sum()
by_country_cat.to_csv('by_country_cat.csv')

cmil = by_country_cat.sum(level=['country','dac_category'])
cmil=cmil/1e6

by_country = cmil.sum(level='country')
top_country = by_country.sort_values()
top_country = top_country[-10:]
print('Top Recipient Countries:',top_country)

reset = cmil.reset_index()
keep_dac = reset['dac_category'].isin(top_dac.index)
keep_coun = reset['country'].isin(top_country.index)
keep = keep_dac & keep_coun

sub= reset[keep]
grouped =sub.groupby(['country','dac_category'])
summed = grouped['amt'].sum()
grid = summed.unstack('country')

#plot heatmap
fig, ax1 = plt.subplots(dpi=300, figsize=(8,8))
fig.suptitle("Contributions in Millions")
sns.heatmap(grid, annot=True, fmt=".0f", ax=ax1)
ax1.set_xlabel("Countries")
ax1.set_ylabel("DAC")
fig.tight_layout()
fig.savefig('heatmap_countries.png')

