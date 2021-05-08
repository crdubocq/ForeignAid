# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 16:15:46 2021

@author: crdub
"""

import pandas as pd 

# make  a smaller sample size out of the dataset

aid_info = pd.read_csv('us_foreign_aid_complete.csv')
sample = aid_info.sample(frac=0.05)
sample.to_csv('fa_sample.csv')