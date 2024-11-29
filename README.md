#概要  
Filmarksの映画のトレンド情報をcsv形式で保存します。現在はタイトルと評価のみです。  
RequestsライブラリのGetメソッドでHTTPのGetリクエストを送信し、取得した情報をBeautifulSoupで分析しています。  

#このリポジトリについて  
scrape_filmarks.pyが処理の内容になっていて、movie.csvに情報が入ります。  
  
#使い方  
１．このリポジトリをクローンする
```bash
git clone https://github.com/cinamocha/scrape-movie-review.git
  
２．下記ライブラリのインストール  
pip install requests beautifulsoup4  
  
３．スクリプト実行  
python scrape_filmarks.py  
  
オプション
冒頭の
url = 'ここで'
URLの指定ができます。  

Python 3.13.0  
beautifulsoup4 4.12.3  
bs4 0.0.2  
requests 2.32.3  
