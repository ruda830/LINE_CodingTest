import pandas as pd
import numpy as np

df = pd.read_csv("taxi_record_2.csv")

dfn = pd.DataFrame(df.values, columns=['時間','走行距離'])
print(df.columns)
loads = dfn['走行距離'].sum()
print(loads)
"""
with open('taxi_record_2.csv') as f:
    lines = f.readlines()

    for line in lines:
        line = line.replace(' ', ',')
    print(lines)
"""