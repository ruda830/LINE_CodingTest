import pandas as pd
import numpy as np
import datetime
import car_02_3

#データフレームを読み込むところを一括でまとめたい。


if __name__ == '__main__':
    #インスタンス生成
    record = car_02_3.Record()
    #データフレーム作製
    dfn_1 = record.make_df('taxi_record_4.csv')
    #総走行距離を算出
    all_load = record.load_calc(dfn_1)
    print('総走行距離は：'+str(all_load))
    #各スピードを計算
    every_speed = record.speed_calc(dfn_1)
    #print('各スピードは：'+str(every_speed))


    print(dfn_1)


"""
def teisoku_calc():
    # 読み込み
    df = pd.read_csv('taxi_record_4.csv', header=None)
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