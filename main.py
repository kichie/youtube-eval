#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests 
import collections

from scraping import Youtube

 
#感情分析したいテキスト
text = """
外国人のファンです。このチャンネルはとてもプロフェッショナルな感じですね。まだまだですが最近勉強になりました。ありがとうございます。
音量バランス、、、
普段どこからbgm拾ってきていますか？OPのbgmが大好きで、自分の動画でも使いたいのですが教えていただけないでしょうか？
とても参考になります
これからも更新楽しみにしています😊
めちゃくちゃ勉強になりました！ありがとうございます！
スローにすると画質が悪くなるんですよね🤔
初心者です！わかりやすい！ファイルのゴミがたまるので、そうすればいいんだって気が付きました！ありがとうございました！
Sam kolder参考にしたりする？
パソコンの中整理すんの苦手。
動画編集に興味がありこれからやってみようと思いますが、パソコンはWindows Mac どちらがいいですか？初心者でも分かりやすい動画などオススメがあれば教えてください！これから徐々に勉強していきたいです！
カラーLUTをShareしていただけませんか？
とても分かりやすい動画で本当に参考になります。動画編集初心者ですが色々挑戦していこうと思います。
質問です。編集モードをARRIcinemaにするといいんですか？そもそも、編集モードを変えると画質とか変わるんですか？教えてください。
カメラワーク教えてほしいです！
カチカチしてるだけでどうやって動画を引き出して来たかとかも全くわからないし初心者向けとは思えない
めっちゃ参考になりました☺️これからも楽しみにしてます🍎🍎🍎映像編集初めてどのくらいですか？趣味でやりだしてから、と、仕事としてやりだしてからを教えてただけると嬉しいです！
最近動画始めたものです！映画っぽい画質にしたいんですが、そちらの動画出して欲しいです！あとは、透けるように動画と動画のところが滑らかに変わるやり方も知りたいです
はじめまして！いつも動画見て勉強させてもらってます！
説明がしづらいんですが、カットチェンジの時にブン！ってなる感じのスライドしながら（回りながら?）のやり方を教えていただきたいです。よろしくお願いします。
"""

    
#442 206 https://www.youtube.com/watch?v=71eE1Se43DQ
#youtube_page = Youtube('71eE1Se43DQ',50)
#2万 561 https://www.youtube.com/watch?v=31b2vy0Azaw
#youtube_page = Youtube('31b2vy0Azaw',50)
#1558 984 https://www.youtube.com/watch?v=UXl2LBo3_Zs
#youtube_page = Youtube('UXl2LBo3_Zs',50)
#4316 5747 https://www.youtube.com/watch?v=caMTVgInf4s&list=PLYMkLgJPxM5p69XAPM0KG8n1_p6y4uUtF
#youtube_page = Youtube('caMTVgInf4s',50)
#113 21 https://www.youtube.com/watch?v=YSefF0u1Vb0
youtube_page = Youtube('YSefF0u1Vb0', 50)
text = youtube_page.get_youbou()
#print(youtube_page.comments[25])
print(youtube_page.get_youbou())
