# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 09:06:37 2021

@author: crdub
"""

keepaid = ['region_name','dac_category','fiscal_year','amt']
trimmed = lic[keepaid]

grouped = trimmed.groupby(['agency','dac_category'])
summed = grouped['amt'].sum
grid = summed.unstack('agency')