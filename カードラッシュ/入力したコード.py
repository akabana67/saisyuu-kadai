PS C:\Users\zakky> python
Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import pandas as pd
>>> 
>>> df_list = pd.read_html("response.html")
>>> df = df_list[0]
>>> print(df.head())
                                  カード名/商品名        買取価格
0  ポケモンカードゲーム 20周年記念 ロケット団スペシャルケース(未開封BOX)  ¥1,100,000
1                       マリオピカチュウ(スペシャルBOX)  ¥1,100,000
2              レックウザポンチョを着たピカチュウ(スペシャルBOX)    ¥950,000
3          メガリザードンXのポンチョを着たピカチュウ(スペシャルBOX)    ¥850,000
4         コイキングごっこ＆ギャラドスごっこピカチュウ(スペシャルBOX)    ¥800,000
>>> import pandas as pd
>>> 
>>> # HTMLファイルから読み込み
>>> df_list = pd.read_html("response.html")
>>> df = df_list[0]
>>> 
>>> # 条件：'カード名/商品名' に「未開封BOX」または「スペシャルBOX」を含む行だけ抽出
>>> filtered_df = df[df["カード名/商品名"].str.contains("未開封BOX|スペシャルBOX", na=False)]
>>> 
>>> # 結果をCSVとして保存
>>> filtered_df.to_csv("box_only.csv", index=False, encoding="utf-8-sig")
>>> 
>>> # 確認表示（任意）
>>> print(filtered_df)
                                    カード名/商品名        買取価格
0    ポケモンカードゲーム 20周年記念 ロケット団スペシャルケース(未開封BOX)  ¥1,100,000
1                         マリオピカチュウ(スペシャルBOX)  ¥1,100,000
2                レックウザポンチョを着たピカチュウ(スペシャルBOX)    ¥950,000
3            メガリザードンXのポンチョを着たピカチュウ(スペシャルBOX)    ¥850,000
4           コイキングごっこ＆ギャラドスごっこピカチュウ(スペシャルBOX)    ¥800,000
..                                       ...         ...
416       バトルマスターデッキ 『テラスタル リザードンex』(未開封BOX)      ¥1,200
417      スターターデッキ＆ビルドセット『古代のコライドンex』(未開封BOX)      ¥1,000
418      スターターデッキ＆ビルドセット『未来のミライドンex』(未開封BOX)      ¥1,000
419            スペシャルジャンボカードセット オーガポン(未開封BOX)      ¥1,000
424             バトルマスターデッキ 『パオジアンex』(未開封BOX)        ¥700

[180 rows x 2 columns]
>>> import pandas as pd
>>> 
>>> # HTMLファイルから読み込み
>>> df_list = pd.read_html("response.html")
>>> df = df_list[0]
>>> 
>>> # 「未開封パック」を含む行だけ抽出
>>> # 「未開封パック」を含む行だけ抽出
>>> pack_df = df[df["カード名/商品名"].str.contains("未開封パック", na=False)]
>>> 
>>> 
>>> # CSVとして保存
>>> pack_df.to_csv("sealed_packs_only.csv", index=False, encoding="utf-8-sig")
>>> 
>>> # 確認表示
>>> print(pack_df)
>>> print(pack_df)
                              カード名/商品名      買取価格
16                      ギフトパック(未開封パック)  ¥350,000
30            クイックスターター ギフトパック(未開封パック)  ¥200,000
35                ロケット団 ギフトパック(未開封パック)  ¥170,000
40                第1弾 スターターパック(未開封パック)  ¥160,000
41                   劇場限定VSパック(未開封パック)  ¥150,000
..                                 ...       ...
427    対戦スターターパック ブーバーンVSエレキブル(未開封パック)      ¥500
428    対戦スターターパック ヒードランVSレジギガス(未開封パック)      ¥500
429    対戦スターターパック ギラティナVSディアルガ(未開封パック)      ¥500
430  対戦スターターパックSP ゴウカザルVSエルレイド(未開封パック)      ¥500
431  構築スタンダードデッキ アルセウスLV.X 草&炎(未開封パック)      ¥500

[228 rows x 2 columns]