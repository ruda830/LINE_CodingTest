import datetime as datetime
import pandas as pd
import numpy as np
import datetime

df = pd.read_csv('taxi_test.csv', header=None)
dfn = pd.DataFrame(df.values, columns=['a', 'b'])
# 日付カラムをdatetime型に変換
dfn['a'] = pd.to_datetime(dfn['a'], format='%H:%M:%S.%f')
print(type(dfn['a']))
print((dfn['a'][2]))

#深夜時間帯を抽出
from_midnight = datetime.datetime(1900, 0o1, 0o1, 22, 00, 00, 000)
to_midnight = datetime.datetime(1900, 0o1, 0o2, 0o5, 00, 00, 000)

dfn.loc[from_midnight <= dfn['a'], 'c'] = 'midnight'
dfn.loc[from_midnight > dfn['a'], 'c'] = 'sun'
#dfn_midに記録
dfn_mid = dfn.query("c=='midnight'")
#深夜走行距離を算出
midnight_loads = dfn_mid['b'].sum()
print(dfn_mid)
print(midnight_loads)

print(dfn)