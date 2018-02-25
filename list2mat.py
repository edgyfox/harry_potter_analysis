#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 15:38:40 2018

@author: arghanandan
"""

import pandas as pd

df=pd.read_csv("chars.csv",header=None)

for i in range(len(df.index)):
    df[df.iloc[i,0]]=0*len(df.index)

df.to_csv("char.csv")
