class Taxi:

    def __init__(self):
        self.hatu_money = 410
        self.kasan_sinya_money = 0
        self.teisoku_money = 0
        self.load = 0
        self.midnight_load = 0
        self.low_Minutes = 0

    def kasan_sinya(self, midnight_load, load):
        # 先に、深夜帯運行時の走行距離補正
        self.load = load
        self.midnight_load = midnight_load
        addload = self.midnight_load * 0.25
        self.load += addload

        # 1052m超えてからの加算回数と加算金額計算
        if load < 1052:
            nums = 0
        else:
            nums = int((load - 1052) / 237)
        self.kasan_sinya_money += 80 * nums
        return self.kasan_sinya_money

    def teisoku(self, low_Minutes):
        self.low_Minutes = low_Minutes
        teisoku_nums = int(low_Minutes/90)
        self.teisoku_money += 80 * teisoku_nums
        return self.teisoku_money

    def unchin(self):
        return self.hatu_money + self.kasan_sinya_money + self.teisoku_money

"""
# デバック用
        print("デバック初乗り_money:" + str(self.hatu_money))
        print("デバック加算_深夜_money:" + str(self.kasan_sinya_money))
        print("デバック低速_money:" + str(self.teisoku_money))
        print("デバック深夜時間帯")
"""




