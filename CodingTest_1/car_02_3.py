import pandas as pd
import numpy as np
import datetime


class Record:
    """
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
