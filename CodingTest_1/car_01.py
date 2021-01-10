'''
01. ミッションの内容を理解しよう(自分なりに仕様を整理しよう)
所要時間：約1~4H
a,いくつかの走行距離において、それぞれ料金がいくらになるか計算してみよう。
b,低速走行時間が含まれていた場合、料金がどうなるか考えてみよう。
c,深夜料金になる22時をまたいだ場合、料金がどうなるか考えてみよう

'''

class Taxi:

    def __init__(self):
        self.hatu_money = 410
        self.kasan_money = 0
        self.action_num = 0

    def kasan(self, load):
        # 1052m超えてからの加算回数とその金額を計算
        nums = int((load - 1052) / 237)
        for num in range(nums):
            self.kasan_money += 80
        return self.kasan_money

    def unchin(self):
        # unchinの合計を出力
        # 本当は 関数内で unchin = self.hatu_money + self.kasan_money としたいのに出来ない…。
        return self.hatu_money + self.kasan_money

    def taxi_step(self):
        print("タクシー降車中")


if __name__ == '__main__':

    taxi = Taxi()
    while True:
        action = int(input("走った距離を教えてください："))
        #例)　3km　→　3000m (1052m+1948m)　→　410+640 = 1050円
        taxi.kasan(action)
        goukei = taxi.unchin()
        print("合計は"+str(goukei)+"円です。")
        taxi.taxi_step()
        break


#ここからメモ--------------------------------------------------
"""
お金と距離を分離して考えた方がいい。
"""
"""
#本当はgoukeiの変数を使いたい。
#hatu_money, kasan_money, teisoku引数にいる？←いらないっぽい
    def unchin(self, goukei):
        goukei = self.hatu_money + self.kasan_money + self.teisoku
        return goukei                        
"""
"""
kasanの計算コードが2パターンある。と思う。
１．メゾットkasanに条件分岐　　変数にnかけるか。
class taxi:
    def __init__(self):
        self.n = int((走行距離-1052)/237)
    def kasan(self):
        if n<0:
            pass
        else:
            self.kasan_money += 80 * n

２．__main__下に、条件分岐　　メゾットをn回呼び出すか。
n = int((走行距離-1052)/237)
if n<0:
    hatu()
    unchin()
else:
    kasan()がn回呼び出し
    unchin()
"""


