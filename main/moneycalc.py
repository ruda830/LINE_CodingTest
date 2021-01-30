class Taxi:

    def __init__(self):
        self.hatu_money = 410
        self.kasan_sinya_money = 0
        self.teisoku_money = 0
        self.midnight_load = 0
        self.low_Minutes = 0

    def kasan_sinya(self, midnight_load, load):
        # 深夜帯運行時の総走行距離補正
        self.midnight_load = midnight_load
        addload = self.midnight_load * 0.25
        load += addload

        # 1052m超えてからの加算回数と加算金額計算
        nums = int((load - 1052) / 237)
        self.kasan_sinya_money += 80 * nums

        return self.kasan_sinya_money

    def teisoku(self, low_Minutes):
        self.low_Minutes = low_Minutes
        teisoku_nums = int(low_Minutes/90)
        self.teisoku_money += 80 * teisoku_nums
        return self.teisoku_money

    def unchin(self):
        print("デバック初乗り_money:" + str(self.hatu_money))
        print("デバック加算_深夜_money:" + str(self.kasan_sinya_money))
        print("デバック低速_money:" + str(self.teisoku_money))
        print("デバック深夜時間帯")
        return self.hatu_money + self.kasan_sinya_money + self.teisoku_money

"""
    # 1052m超えてからの加算回数と加算金額計算
    def kasan(self, load):
        nums = int((load - 1052) / 237)
        self.kasan_money += 80 * nums
        print("デバック初乗り_money:" + str(self.hatu_money))
        print("デバック加算_money:" + str(self.kasan_money))
        return self.kasan_money

    # 22時超えてからの走行距離をもとに、金額補正
    def kasan_sinya(self, midnight_load, load):
        # 補正後の総走行距離
        self.midnight_load = midnight_load
        addload = self.midnight_load * 0.25
        load_re = load + addload

        # 金額計算
        nums_re = int((load_re - 1052) / 237)
        for num_re in range(nums_re):
            self.kasan_sinya_money += 80
        print("デバック深夜_money:" + str(self.kasan_sinya_money - self.kasan_money))
        return self.kasan_sinya_money
"""




