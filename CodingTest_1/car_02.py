import pandas as pd
import numpy as np

df = pd.read_csv("taxi_record_2.csv")

dfn = pd.DataFrame(df.values, columns=['カラム名1','カラム名2'])
print(df.columns)
print(dfn['カラム名2'])

"""
with open('taxi_record_2.csv') as f:
    lines = f.readlines()

    for line in lines:
        line = line.replace(' ', ',')
    print(lines)
"""