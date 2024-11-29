import requests
from bs4 import BeautifulSoup
import csv

#取得したいwebページのURLの指定
url = 'https://filmarks.com/list/trend'
#リクエストに含める追加の情報、User‐Agentは自分がどんなブラウザを使っているかの指定、人間ですよアピール
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}
#RequestsライブラリのGetメソッド、HTTPのGetリクエストを送信する
response = requests.get(url, headers=headers)     #ここで取得した情報はresponseに格納される
soup = BeautifulSoup(response.text, 'html.parser')      #Webスクレイピング用のライブラリ、HTMLを解析しやすくする
#response.textはWebページの中身そのまま、html.parserはBeautifulSoupに解析方法の指定

#取得した情報の中のほしいところをとりあえず変数に格納
title_class = 'p-content-cassette__title'
rating_class = 'c-rating__score'

movies = soup.find_all('h3', class_=title_class)  #h3タグの中でtitle_classと一致するものを探す
#class_はPythonのclassと区別するため

#csvファイルを開いて書き込む作業
with open('movies.csv', mode='w', newline='', encoding='utf-8') as file:      #open()が開く関数、mode='w'は書き込みモード、newlineは改行
    writer = csv.writer(file)
    writer.writerow(['タイトル', '評価'])  
#withを使うと自動で閉じてくれる

    for movie in movies:
        # タイトル取得
        title = movie.text.strip()

        # 評価取得
        parent = movie.find_parent()  # タイトルの親要素を探す
        rating = (
            parent.find('div', class_=rating_class).text.strip()
            if parent and parent.find('div', class_=rating_class)
            else '評価なし'
        )

        #csvに書き込み
        writer.writerow([title, rating])

print('映画情報をCSVファイルに保存しました！')