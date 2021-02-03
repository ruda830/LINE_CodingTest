import pandas as pd
import numpy as np
import datetime
import math


class Record:

    # pandasでのDF加工に、時間と走行距離カラムを作製
    def make_df(self, file):
        df = pd.read_csv(file, header=None)
        dfn = pd.DataFrame(df.values, columns=['時間', '走行距離'])
        dfn['時間'] = pd.to_datetime(dfn['時間'], format='%H:%M:%S.%f')
        return dfn

    def load_calc(self, dfn):
        loads = dfn['走行距離'].sum()
        return loads

    # 低速運転チェックのため、speedカラムを設置
    def speed_calc(self, dfn):
        dfn['時間'] = pd.to_datetime(dfn['時間'])
        dfn['時間_diff'] = dfn['時間'].diff(1)  # -> 0 days 00:00:02.878000
        dfn['時間_diff'] = dfn['時間_diff'] / np.timedelta64(1, 's')
        dfn['speed'] = dfn['走行距離'] / dfn['時間_diff']
        return dfn['speed']

    # 低速運賃の計算用に、低速運行時の総時間を記録　(10km/h = 2.778m/s以下)
    def lowspeed_time(self, dfn):
        low_Minutes = 0
        nums = len(dfn.index)
        for i in range(nums):
            if dfn['speed'][i] <= 2.778:
                low_Minutes += dfn['時間_diff'][i]
        low_Minutes = math.ceil(low_Minutes)
        return low_Minutes

    # 深夜帯運賃の計算用に、深夜時間帯の総距離を記録
    def midnight_load_bool(self, dfn):
        from_midnight = datetime.datetime(1900, 0o1, 0o1, 22, 00, 00, 000)
        to_midnight = datetime.datetime(1900, 0o1, 0o1, 0o5, 00, 00, 000)

        # 朝夜カラムにmidnightまたはdaytimeの判定を記録
        dfn.loc[(from_midnight <= dfn['時間']) | (to_midnight >= dfn['時間']), '朝夜'] = 'midnight'
        dfn.loc[(from_midnight > dfn['時間']) | (to_midnight >= dfn['時間']), '朝夜'] = 'daytime'
        dfn_mid = dfn.query("朝夜=='midnight'")
        midnight_loads = dfn_mid['走行距離'].sum()
        return midnight_loads