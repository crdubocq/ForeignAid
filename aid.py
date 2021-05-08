# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 14:05:51 2021

@author: crdub
"""

import pandas as pd 
import matplotlib.pyplot as plt


# Open sample size of the dataset
aid_info = pd.read_csv('us_foreign_aid_complete.csv')
aid_info = aid_info.set_index(['region_name'])
aid_info = aid_info.sort_index()

# 'clean' dataset from unwanted material and rename columns for easier use
clean = aid_info[['country_name','income_group_acronym','implementing_agency_acronym','channel_category_name','dac_category_name','fiscal_year', 'constant_amount']]
clean = clean.drop('World')
clean = clean.rename(columns={'country_name':'country','income_group_acronym':'income','implementing_agency_acronym':'agency','channel_category_name':'channel','dac_category_name':'dac_category','constant_amount':'amount'})
clean = clean.dropna()
clean['amt'] = clean['amount'].astype(float)
clean = clean.drop('amount', axis='columns')
clean.to_csv('clean_aid.csv')

# group by Agency 
group_by_agency = clean.groupby(['agency','dac_category','country'])
by_agency_country = group_by_agency['amt'].sum()
mil = by_agency_country.sum(level=['agency','dac_category','country'])
mil = mil/1e6

# print top ten 'countries', 'agency','dac_category'
by_country = mil.sum(level='country')
top_country = by_country.sort_values()
top_country = top_country[-10:]
print('Top Recipient Countries:',top_country)

by_agency = mil.sum(level='agency')
top_agency = by_agency.sort_values()
top_agency = top_agency[-10:]
print('\nTop US Agencies:',top_agency)

by_dac = mil.sum(level='dac_category')
top_dac = by_dac.sort_values()
top_dac = top_dac[-10:]
print('\nTop Development Assistance Category:',top_dac)


# plot figures 
fig,(ax1,ax2) = plt.subplots(1,2,dpi=300)
fig.suptitle("Top Countries and Agencies, Millions of Dollars")
top_country.plot.barh(ax=ax1,fontsize=7)
ax1.set_ylabel=("Countries")
top_agency.plot.bar(ax=ax2, fontsize = 7)
ax2.set_xlabel("Agencies")
fig.tight_layout()
fig.savefig('top10.png')
fig,(ax3)=plt.subplots(1,dpi=300)
top_dac.plot.barh(ax=ax3, fontsize = 7)
ax3.set_xlabel('DAC Category')
fig.tight_layout()
fig.savefig('dac.png')






