class Taxi:

    def __init__(self):
        self.hatu_money = 410
        self.kasan_money = 0
        self.teisoku_money = 0
        self.kasan_sinya_money = 0

    # 1052m超えてからの加算回数と加算金額計算
    def kasan(self, load):
        nums = int((load - 1052) / 237)
        self.kasan_money += 80 * nums
        print("デバック初乗り_money:" + str(self.hatu_money))
        print("デバック加算_money:" + str(self.kasan_money))
        return self.kasan_money

    # 低速運行の合計時間から、低速運賃の金額を算出
    def teisoku(self, low_Minutes):
        teisoku_nums = int(low_Minutes/90)
        self.teisoku_money += 80 * teisoku_nums
        print("デバック低速_money:" + str(self.teisoku_money))
        return self.teisoku_money

    # 22時超えてからの走行距離をもとに、金額補正
    def kasan_sinya(self, midnight_load, load):

        # 補正後の総走行距離
        addload = midnight_load * 0.25
        load_re = load + addload

        # 金額再計算
        nums_re = int((load_re - 1052) / 237)
        for num_re in range(nums_re):
            self.kasan_sinya_money += 80
        print("デバック深夜_money:" + str(self.kasan_sinya_money - self.kasan_money))
        return self.kasan_sinya_money

    # 運賃の合計を出力
    def unchin(self):
        # kasan_moneyとkasan_sinya_moneyはどちらかがTrueのスイッチング関係
        if self.kasan_sinya_money == 0:
            return self.hatu_money + self.kasan_money + self.teisoku_money
        else:
            return self.hatu_money + self.kasan_sinya_money + self.teisoku_money







