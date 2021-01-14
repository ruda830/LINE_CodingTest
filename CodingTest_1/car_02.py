import pandas as pd
import numpy as np

def load_calc(file):
    df = pd.read_csv(file)
    dfn = pd.DataFrame(df.values, columns=['時間', '走行距離'])
    #print(df.columns) ->Index(['13:50:08.245', '0.0'], dtype='object')
    loads = dfn['走行距離'].sum()

    return loads


if __name__ == '__main__':
    df = pd.read_csv('taxi_record_2.csv')
    dfn = pd.DataFrame(df.values, columns=['時間', '走行距離'])
    # print(df.columns) ->Index(['13:50:08.245', '0.0'], dtype='object')
    loads = dfn['走行距離'].sum()




"""
with open('taxi_record_2.csv') as f:
    lines = f.readlines()

    for line in lines:
        line = line.replace(' ', ',')
    print(lines)
"""