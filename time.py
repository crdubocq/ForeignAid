# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 19:03:48 2021

@author: crdub
"""

import pandas as pd
import matplotlib.pyplot as plt


aidhist = pd.read_csv('clean_aid.csv')

aidhist = aidhist[aidhist['fiscal_year'] != '1976tq']
aidhist['fiscal_year'] = aidhist['fiscal_year'].astype(int)
aidhist = aidhist[aidhist.fiscal_year>=1980]
aidhist = aidhist.set_index(['fiscal_year'])
aidhist = aidhist.sort_index()

histlist = aidhist.groupby(['fiscal_year'])
by_year = histlist['amt'].sum()
mil = by_year.sum(level=['fiscal_year'])
mil = mil/1e9

fig,ax1 = plt.subplots(dpi=300)
fig.suptitle("Foreign Aid since 1980s")
mil.plot(ax=ax1)
ax1.set_xlabel('Years')
ax1.set_ylabel('Million Dollars')
fig.tight_layout()
fig.savefig("by_year.png")

afg_aid = aidhist[aidhist['country']=='Afghanistan']

afg_list = afg_aid.groupby(['fiscal_year'])
afg_total = afg_list['amt'].sum()
amil = afg_total.sum(level=['fiscal_year'])
amil = amil/1e9

fig,ax1 = plt.subplots(dpi=300)
fig.suptitle("Foreign Aid to Afghanistan")
amil.plot(ax=ax1)
ax1.set_xlabel('Years')
ax1.set_ylabel('Million Dollars')
fig.tight_layout()
fig.savefig("afg_aid.png")

afg_sin = aidhist[aidhist['country']!='Afghanistan']

afg_sin_list = afg_sin.groupby(['fiscal_year'])
afg_sin_total = afg_sin_list['amt'].sum()
sanmil = afg_sin_total.sum(level=['fiscal_year'])
sanmil = sanmil/1e9

fig,ax1 = plt.subplots(dpi=300)
fig.suptitle("Foreign Aid without Afghanistan")
sanmil.plot(ax=ax1)
ax1.set_xlabel('Years')
ax1.set_ylabel('Million Dollars')
fig.tight_layout()
fig.savefig("afg_sin_aid.png")

##sns.set_theme(style="darkgrid")
##fmri = sns.load_dataset('fmri')
##sns.lineplot(x="timepoint", y="signal",
##             hue="region", style="event",
##             data=fmri)