import pandas as pd
import numpy as np
import datetime
"""
def load_calc(file):
    df = pd.read_csv(file)
    dfn = pd.DataFrame(df.values, columns=['時間', '走行距離'])
    #print(df.columns) ->Index(['13:50:08.245', '0.0'], dtype='object')
    loads = dfn['走行距離'].sum()

    return loads
"""

if __name__ == '__main__':
    #本番時には消す↓
    df = pd.read_csv('taxi_record_2.csv')
    dfn = pd.DataFrame(df.values, columns=['時間', '走行距離'])



    print(pd.to_datetime(dfn['時間']))
    dfn['時間'] = pd.to_datetime(dfn['時間'])
    df['b_diff'] = df['時間'].diff(-1)
    print(dfn)


    #dfn['jp'] = dfn['時間'][1].second
    #print(dfn['時間'][1].second - dfn['時間'][0].second) #13:50:11.123

"""
    dfn['差分'] = 0
    for m in dfn['走行距離']:
        dfn['差分'].loc[m +1 ] = 10
    print(dfn)
    #dfn['差分'].append




    #dfn['差分'] = []
    #dfn['差分'].append = dfn['時間'][1] - dfn['時間'][0]
    #for m in dfn:
    #    dfn['差分'].append = dfn['時間'][m + 1] - dfn['時間'][m]

    #print(dfn['時間'][i+1]-dfn['時間'][i] for i in range(len(dfn['時間'])-1))
    #dfn['差分'] = (df.dtime[i+1] - df.dtime[i] for i in pd.to_datetime(dfn['時間']))
    #dfn['差分'] = pd.to_datetime(dfn['時間'])/np.timedelta64(1, 's')
    #for
"""


    #print(type(dfn['時間'][0]))
    #str_time = str(dfn['時間'])

    #文字列型から日付型に変える。
    #before = '2017-05-23 12:47:23'　　　->'%Y-%m-%d %H:%M:%S'
    #after = datetime.datetime.strptime(dfn['時間'], '%H:%M:%S:%f')

    #print(type(before))
    #print(type(after))



"""
with open('taxi_record_2.csv') as f:
    lines = f.readlines()

    for line in lines:
        line = line.replace(' ', ',')
    print(lines)
"""