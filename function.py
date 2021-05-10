# -*- coding: utf-8 -*-
"""
Created on Sun May  9 22:19:29 2021

@author: crdub

"""
import pandas as pd
import matplotlib.pyplot as plt


def category(db):
    group_by_dac = db.groupby(["dac_category"])
    by_dac = group_by_dac['amt'].sum()
    mil = by_dac.sum(level=['dac_category'])
    mil = mil/1e6
    by_dac = mil.sum(level='dac_category')
    top_dac = by_dac.sort_values()
    top_dac = top_dac[-10:]
    print('\nTop Development Assistance Category:',top_dac)
    fig,(ax1) = plt.subplots(dpi=300)
    fig.suptitle("Top DA Categories, Millions of Dollars")
    top_dac.plot.barh(ax=ax1,fontsize=7)
    fig.tight_layout()
    fig.savefig('topDAC.png')
    return;
    
#%%

clean = pd.read_csv("clean_aid.csv")
dac_bolivia = clean.query('country =="Pakistan"')

category(dac_bolivia)
    