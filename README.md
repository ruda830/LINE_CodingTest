##ファイル構成
* Requirement_definition_document.md : 要件定義書
* main : 実行時のメインファイル。
* taxi_record : タクシーレコードデータ。



#### mainの中身
  ```plain
  main.py       実行ファイル
  dfcalc.py     csvをデータフレームへ加工するモジュール
  moneycalc.py  運賃を算出するモジュール
  ```

#### taxi_recordの中身
  ```plain
  csv           条件
  ーーーーーーーーーーーーーーーーーーーーーーーーー
  record_1.csv  初乗り＋加算＋低速＋深夜
  record_2.csv  初乗り＋加算＋低速
  record_3.csv  初乗り＋加算              *急発進、急停車する
  record_2.csv  初乗り＋加算＋深夜         *深夜から乗り始めた
  ```

この問題はTechbowl様の提供するMISSIONです。
