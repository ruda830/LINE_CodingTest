"""
タクシー代を求めるには、
下の../taxi_record/record_1.csvを適宜変更し、
CUIでmain.pyを実行してください。
$ python main.py

レコードデータに対応した運賃が返されます。
"""
import dfcalc  # データフレーム生成及び、速度と距離算出
import moneycalc  # 運賃計算

if __name__ == '__main__':
    try:
        # ≺データ成形編:used class Record≻-------------------

        # インスタンス生成
        record = dfcalc.Record()
        dfn_1 = record.make_df('../taxi_record/record_2.csv')
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
        taxi = moneycalc.Taxi()
        # kasanの計算
        taxi.kasan_sinya(all_midnight_loads, all_load)
        # teisokuの計算
        taxi.teisoku(all_low_Minutes)
        # sinyaの計算

        # 合計
        goukei = taxi.unchin()
        print("総合計料金(初乗り＋加算＋低速＋深夜)は" + str(goukei) + "円です。")



    except FileNotFoundError as e:
        print("ファイルが見つかりません", e)
    except Exception as e:
        print("ファイルの読み込みエラーです", e)
