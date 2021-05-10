# -*- coding: utf-8 -*-
"""
Created on Fri May  7 12:41:03 2021

@author: crdub
"""
import pandas as pd 
import matplotlib.pyplot as plt


# read database 
aiddist = pd.read_csv('clean_aid.csv')

# clean
aiddist = aiddist.drop(columns=['agency', 'channel','dac_category'])

#claculate percentage 
aiddist['percentage'] = (aiddist['amt']/aiddist['amt'].sum())*100

print (aiddist.describe())
print (aiddist.values)
print (aiddist.index)

afg = aiddist.query('country =="Afghanistan"')
afgsum = afg['amt'].sum()
afgper = afg['percentage'].sum()
print("\nSum of Afghanistan Aid:", afgsum)
print("\nPercentage of Afghanistan aid:", afgper)

whole = aiddist.query('country !="Afghanistan"')
wholesum = whole['amt'].sum()
wholeper = whole['percentage'].sum()
print("\nSum of Aid w/o AFG:", wholesum)
print("\nPercentage of Aid w/o AFG:", wholeper)

#%%

lic = aiddist.query('income =="LIC"')
licsum = lic['amt'].sum()
licper = lic['percentage'].sum()

lmic = aiddist.query('income =="LMIC"')
lmicsum = lmic['amt'].sum()
lmicper = lmic['percentage'].sum()

umic = aiddist.query('income =="UMIC"')
umicsum = umic['amt'].sum()
umicper = umic['percentage'].sum()

hic = aiddist.query('income =="HIC"')
hicsum = hic['amt'].sum()
hicper = hic['percentage'].sum()

print("\nPercentage of LIC:",licper)
print("\nPercentage of LMIC:",lmicper)
print("\nPercentage of UMIC:",umicper)
print("\nPercentage of HIC:",hicper)
#%%
#Percentage by Region 

by_region =aiddist.groupby(['region_name'])
regionper =by_region['percentage'].sum()
print(regionper)
#%%

income = aiddist[['fiscal_year','income','amt']].copy()
income['amt'] = income['amt'].astype(float)

group_by_income = income.groupby(["fiscal_year","income"])
by_income = group_by_income['amt'].sum()
unstacked = by_income.unstack()
#[1981, 1981, 1989, 1993, 1997, 2001, 2005, 2009, 2013, 2017, 2021]

fig, ax1 = plt.subplots(dpi=300)
fig.suptitle("Income Group Distribution")
unstacked.plot.area(ax=ax1, stacked=True)
ax1.set_xlabel('Years')
ax1.set_ylabel('Million of Dollars')
fig.tight_layout()
plt.legend(frameon=False)
fig.savefig('IncomeDistribution.png')

#%%

region = aiddist[['fiscal_year', 'region_name', 'amt']].copy()

group_by_region = region.groupby(["fiscal_year", "region_name"])
by_region =group_by_region['amt'].sum()
runstacked = by_region.unstack()

fig, ax1 = plt.subplots(dpi=300)
fig.suptitle("Regional Distribution")
runstacked.plot.area(ax=ax1, stacked=True)
ax1.set_xlabel('Years')
ax1.set_ylabel('Million of Dollars')
fig.tight_layout()
plt.legend(frameon=False)
fig.savefig("RegionDistribution.png")



