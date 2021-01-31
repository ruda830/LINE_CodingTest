"""
タクシー代を求めるには、
下の../taxi_record/record_1.csvを適宜変更し、
CUIでmain.pyを実行してください。
$ python main.py

レコードデータに対応した運賃が返されます。
"""
import dfcalc  # データフレーム生成及び、速度と距離算出
import moneycalc  # 運賃計算
import sys

if __name__ == '__main__':
    try:
        # データ成形(used class Record)
        rd = dfcalc.Record()
        dfn_1 = rd.make_df('../taxi_record/record_7.csv')
        # 総走行距離、スピード算出
        all_load = rd.load_calc(dfn_1)
        every_speed = rd.speed_calc(dfn_1)
        all_low_Minutes = rd.lowspeed_time(dfn_1)
        all_midnight_loads = rd.midnight_load_bool(dfn_1)

        # 運賃計算(used class Taxi)
        taxi = moneycalc.Taxi()
        taxi.kasan_sinya(all_midnight_loads, all_load)
        taxi.teisoku(all_low_Minutes)
        goukei = taxi.unchin()
        print(goukei)  # 円
        sys.exit(0)

    except FileNotFoundError as e:
        print("ファイルがみつかりません", e)
        sys.exit(1)

"""
# デバック用
        print('総走行距離は：' + str(all_load) + 'mです。')
        print('低速時間は：' + str(all_low_Minutes) + '秒です。')
        all_midnight_loads_calc = all_midnight_loads * 1.25
        print('深夜時間帯走行距離は：' + str(all_midnight_loads) + 'mです。')
        print("総合計料金(初乗り＋加算＋低速＋深夜)は" + str(goukei) + "円です。")
"""
