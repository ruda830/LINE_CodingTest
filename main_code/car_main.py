#データフレームの成形モジュール
import car_dfcalc
#運賃の計算のモジュール
import car_moneycalc


if __name__ == '__main__':

    try:
        # ≺データ成形編:used class Record≻-------------------

        # インスタンス生成
        record = car_dfcalc.Record()
        dfn_1 = record.make_df('taxi_record_1.csv')
        # 総走行距離を算出
        all_load = record.load_calc(dfn_1)
        print('総走行距離は：' + str(all_load) + 'mです。')
        # 各スピードを計算、記録
        every_speed = record.speed_calc(dfn_1)

        # 低速スピードの時間を収集、記録
        all_low_Minutes = record.lowspeed_time(dfn_1)
        print('低速時間は：' + str(all_low_Minutes) + '秒です。')

        # 深夜時間帯走行距離の収集、算出
        all_midnight_loads = record.midnight_load_bool(dfn_1)
        all_midnight_loads_calc = all_midnight_loads * 1.25
        print('深夜時間帯走行距離は：' + str(all_midnight_loads) + 'mです。')
        # print(dfn_1)

        # ≺運賃計算編:used class Taxi≻-------------------

        # インスタンス生成
        taxi = car_moneycalc.Taxi()
        # kasanの計算
        taxi.kasan(all_load)
        # teisokuの計算
        taxi.teisoku(all_low_Minutes)
        # sinyaの計算
        taxi.kasan_sinya(all_midnight_loads, all_load)
        # 合計
        goukei = taxi.unchin()
        print("総合計料金(初乗り＋加算＋低速＋深夜)は" + str(goukei) + "円です。")

        # 終了の合図
        taxi.taxi_stop()

    except FileNotFoundError as e:
        print("ファイルが見つかりません", e)
    except Exception as e:
        print("ファイルの読み込みエラーです", e)




    """
    #内訳 改修中
    print("内訳は以下のようです。「料金(考慮した条件)は：～」として表示します。")
    print("料金(低速×、深夜×) は：" + str(taxi.kasan(all_load)) + "円です。")
    print("追加料金は(低速〇、深夜×)：" + str(taxi.teisoku(all_low_Minutes)) + "円です。")
    print("taxi.kasan_sinya:" + str(taxi.kasan_sinya(all_midnight_loads, all_load)))
    print("taxi.kasan):"+str(taxi.kasan(all_load)))
    print("追加料金は(低速×、深夜〇)：" + str(taxi.kasan_sinya(all_midnight_loads, all_load) - taxi.kasan(all_load))+ "円です。")
    """







"""
#以下、モジュール化する前の直コード。何かあった時用。
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