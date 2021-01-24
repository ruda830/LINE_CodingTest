import pandas as pd
import numpy as np
import datetime


def load_calc(dfn):
    #df = pd.read_csv(file)
    #dfn = pd.DataFrame(df.values, columns=['時間', '走行距離'])
    #print(df.columns) ->Index(['13:50:08.245', '0.0'], dtype='object')
    loads = dfn['走行距離'].sum()

    return loads

"""
def teisoku_calc():
    # 読み込み
    df = pd.read_csv('taxi_record_1.csv', header=None)
    dfn = pd.DataFrame(df.values, columns=['a', 'b'])

    # 日付カラムをdatetime型に変換
    dfn['a'] = pd.to_datetime(dfn['a'])
    # 走行時間を逐一記録する
    dfn['a_diff'] = dfn['a'].diff(1)  # -> 0 days 00:00:02.878000
    # 走行時間を秒数に変換
    dfn['a_diff'] = dfn['a_diff'] / np.timedelta64(1, 's')

    # スピードを計算(m/s)
    dfn['speed'] = dfn['b'] / dfn['a_diff']

    # 低速運行の時に時間を記録する。2.78m/s以下。
    low_Minutes = 0
    print(dfn.index)
    num = len(dfn.index)
    print('このカラムの長さは：' + str(num))
    for i in range(num):
        if dfn['speed'][i] >= 20.778:
            low_Minutes += dfn['a_diff'][i]

    print('合計低速時間は：' + str(format(low_Minutes, '.3f') + '秒です。'))
    print(dfn)
"""