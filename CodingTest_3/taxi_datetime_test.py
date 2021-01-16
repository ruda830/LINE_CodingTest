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

from_midnight = datetime.datetime(1900, 0o1, 0o1, 22, 00, 00, 000)
to_midnight = datetime.datetime(1900, 0o1, 0o2, 0o5, 00, 00, 000)
nums = len(dfn.index)
dfn.loc[from_midnight <= dfn['a'], 'c'] = 'midnight'
dfn.loc[from_midnight > dfn['a'], 'c'] = 'sun'
print(dfn)
"""
dfn['c']
for t in range(nums):
    if from_midnight <= dfn['a'][t] <= to_midnight:
        print('本データ夜')
        dfn['c'][t] = dfn.extend([2])
    else:
        print('本データ昼')
        dfn['c'][t] = dfn.extend([1])
"""
"""
if from_midnight <= dfn['a'][2] <= to_midnight:
    print('本データ夜')
else:
    print('本データ昼')
"""
#print(from_midnight)
#nums = len(dfn.index) # print('このカラムの長さは：' + str(num))
#for i in range(nums):
#    dfn['c']. = datetime.datetime.strptime(str(dfn['a'][i]), '%Y-%m-%d %H:%M:%S.%f').strftime('%H:%M:%S.%f')

"""
#===================================
DF = pd.read_csv('taxi_test.csv', header=None)
DFn = pd.DataFrame(DF.values, columns=['a', 'b'])

#df_xx['予'] = df_xx['予'].str.strip()

DFn['a'] = DFn['a'].str.strip()
print(DFn['a'])
DFn['c'] = datetime.datetime.strptime(str(DFn['a']), '%Y-%m-%d %H:%M:%S.%f')
print(DFn['c'])

date = '2017/10/19 10:54:29'
print(dfn['a'][2] > datetime.date.today())
"""
