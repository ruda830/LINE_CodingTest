# タクシーの走行レコードから運賃を求める
<img src="https://4.bp.blogspot.com/-78LRlanhYIs/VqI8UldL9RI/AAAAAAAA3QM/dzJ2ogGy_84/s800/car_taxi2.png" width=50%>

#### レコードデータ(csv)を読み取り、要件定義書に書かれた方法で運賃を算出します。
#### レコードデータディレクトリにはいくつかのテストケースがおいてあります。


## 実行環境 (win, Python 3.7.2)
* DateTime	4.3
* numpy	1.19.5
* pandas	1.2.0


## 構成
* Requirement_definition_document.md : 要件定義書。
* main : 実行時のメインディレクトリ。
* taxi_record : タクシーレコードデータのディレクトリ。

### main
  ```plain
  main.py       実行ファイル
  dfcalc.py     csvをデータフレームへ加工するモジュール
  moneycalc.py  運賃を算出するモジュール
  ```

### taxi_record
  ```plain
  csv           条件
  ーーーーーーーーーーーーーーーーーーーーーーーーー
  record_1.csv  初乗り＋加算＋低速＋深夜       *基本形
  record_2.csv  初乗り＋加算＋低速             *基本形
  record_3.csv  初乗り＋加算        　         *急発進、急停車する
  record_4.csv  初乗り＋加算＋深夜             *深夜から乗り始めた
  record_5.csv  初乗り＋加算＋深夜(早朝ver.)   *早朝から乗り始めた
  record_6.csv  初乗り                       *乗ったけど直ぐに降りた
  ```
