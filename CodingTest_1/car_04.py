import pandas as pd
import datetime
import numpy as np
"""
df = pd.DataFrame({'a': range(1, 6),
                   'b': [x**2 for x in range(1, 6)],
                   'c': [x**3 for x in range(1, 6)]})

df['b_diff'] = df['b'].diff(-1)
print(df)
print(type(df))

#    a   b    c  b_diff
# 0  1   1    1    -3.0
# 1  2   4    8    -5.0
# 2  3   9   27    -7.0
# 3  4  16   64    -9.0
# 4  5  25  125     NaN
"""
#読み込み
df = pd.read_csv('taxi_record_4.csv', header=None)
dfn = pd.DataFrame(df.values, columns=['a', 'b'])

#日付カラムをdatetime型に変換
dfn['a'] = pd.to_datetime(dfn['a'])
#走行時間を逐一記録する
dfn['a_diff'] = dfn['a'].diff(1) #-> 0 days 00:00:02.878000
#走行時間を秒数に変換
dfn['a_diff'] = dfn['a_diff'] / np.timedelta64(1, 's')

#スピードを計算(m/s)
dfn['speed'] = dfn['b']/dfn['a_diff']

#低速運行の時に時間を記録する。2.78m/s以下。
low_Minutes = 0
print(dfn.index)
num = len(dfn.index)
print('このカラムの長さは：'+str(num))
for i in range(num):
    if dfn['speed'][i] >= 20.778:
        low_Minutes += dfn['a_diff'][i]

print('合計低速時間は：'+str(format(low_Minutes, '.3f')+'秒です。'))
print(dfn)

#print(24.170+3.735+0.286)
#DFN['a'] = pd.to_datetime['a']
#df.time = pd.to_datetime(DFN['a'], format='%H%M%S%f')

#DFN['a'] = datetime.datetime.strptime(DFN['a'])
#DFN['a_diff'] = DFN['a'].diff(-1)


