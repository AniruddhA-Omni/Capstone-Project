import os
import time

import numpy as np
import pandas as pd

import audb
import audiofile
import opensmile

smile1 = opensmile.Smile(
    feature_set=opensmile.FeatureSet.eGeMAPSv02,
    feature_level=opensmile.FeatureLevel.Functionals,
)

smile2 = opensmile.Smile(
    feature_set=opensmile.FeatureSet.GeMAPSv01b,
    feature_level=opensmile.FeatureLevel.Functionals
)

d1 = pd.read_csv('data_info.csv')
k = d1['Filename'].tolist()


df = smile1.process_files(k[:20])
print(df)