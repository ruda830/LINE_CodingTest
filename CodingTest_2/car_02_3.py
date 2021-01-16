import pandas as pd
import numpy as np
import datetime
import math


class Record:
    """
    #多分初期化しないと、いけない。
    def __init__(self,file):
        self.file = file
    """


    #データフレーム
    def make_df(self,file):
        df = pd.read_csv(file, header=None)
        dfn = pd.DataFrame(df.values, columns=['時間', '走行距離'])
        return dfn


    #総走行距離
    def load_calc(self, dfn):
        loads = dfn['走行距離'].sum()
        return loads

    #各スピード
    def speed_calc(self, dfn):
        # 読み込み
        #df = pd.read_csv('taxi_record_4.csv', header=None)
        #dfn = pd.DataFrame(df.values, columns=['a', 'b'])

        # 日付カラムをdatetime型に変換
        dfn['時間'] = pd.to_datetime(dfn['時間'])
        # 走行時間を逐一記録する
        dfn['時間_diff'] = dfn['時間'].diff(1)  # -> 0 days 00:00:02.878000
        # 走行時間を秒数に変換
        dfn['時間_diff'] = dfn['時間_diff'] / np.timedelta64(1, 's')

        # スピードを計算(m/s)
        dfn['speed'] = dfn['走行距離'] / dfn['時間_diff']

        return dfn['speed']

    # 低速スピードの収集
    def lowspeed_time(self, dfn):
        # 低速運行の時に時間を記録する。2.78m/s以下。
        low_Minutes = 0

        nums = len(dfn.index) # print('このカラムの長さは：' + str(num))
        for i in range(nums):
            if dfn['speed'][i] <= 2.778:
                low_Minutes += dfn['時間_diff'][i]
        #端数は切り捨て
        low_Minutes = math.ceil(low_Minutes)
        # low_Minutes = format(low_Minutes, '.3f')
        # print('これは関係ありません。合計低速時間は：' + str(format(low_Minutes, '.3f') + '秒です。'))
        return low_Minutes


    def midnight_load_bool(self,dfn):
        # 深夜時間帯を抽出
        from_midnight = datetime.datetime(1900, 0o1, 0o1, 22, 00, 00, 000)
        #to_midnight = datetime.datetime(1900, 0o1, 0o2, 0o5, 00, 00, 000)

        dfn.loc[from_midnight <= dfn['時間'], '朝夜'] = 'midnight'
        dfn.loc[from_midnight > dfn['時間'], '朝夜'] = 'sun'
        # dfn_midに記録
        dfn_mid = dfn.query("朝夜=='midnight'")
        # 深夜走行距離を算出
        midnight_loads = dfn_mid['走行距離'].sum()

        return midnight_loads

