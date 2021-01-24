class Taxi:

    def __init__(self):
        self.hatu_money = 410
        self.kasan_money = 0
        self.teisoku_money = 0


    def kasan(self, load):
        # 1052m超えてからの加算回数とその金額を計算
        nums = int((load - 1052) / 237)
        for num in range(nums):
            self.kasan_money += 80
        return self.kasan_money

    def teisoku(self, low_Minutes):
        # 低速運行の合計時間から、低速運賃の金額を算出
        teisoku_nums = int(low_Minutes/90)
        for teisoku_num in range(teisoku_nums):
            self.teisoku_money += 80
        return self.teisoku_money

    """
    def sinya(self, midnight_load):
        # 22時超えてからの走行距離をもとに、×1.25の金額補正を行う
        midnight_loads_calc = midnight_load * 1.25


        return self.shinya_money
    """

    def unchin(self):
        # 運賃の合計を出力
        # 本当は 関数内で unchin = self.hatu_money + self.kasan_money としたいのに出来ない…。
        return self.hatu_money + self.kasan_money + self.teisoku_money

    def taxi_stop(self):
        # 終了ログ"0"を表示
        print("0")


if __name__ == '__main__':
    # 例)　3km　→　3000m (1052m+1948m)　→　410+640 = 1050円
    taxi = Taxi()


    while True: #?
        #loadsの入力
        action = car_02.load_calc('taxi_record_2.csv')
        #kasanの計算
        taxi.kasan(action)
        #teisokuの計算
        taxi.teisoku(3003.191)

        #合計
        goukei = taxi.unchin()
        print("合計は"+str(goukei)+"円です。")

        #終了の合図
        taxi.taxi_step()
        break









