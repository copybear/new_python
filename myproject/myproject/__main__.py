#!/usr/bin/env python
from geminisample1 import suggest_urls_articles
from geminisample2 import get_url_list
from helloworld import dispWindow
from hellopsg import dispPsgWindow
from imgviewer import dispImgViewer
from keywordToAnswer import dispKAViewer
import const

const.GOOGLE_AI_API_KEY=os.getenv('GGAI_API_KEY')
const.GOOGLE_CL_API_KEY=os.getenv('GGCL_API_KEY')

def main():
    """
    # キーワードを取得
    keyword = input("探したいキーワードを入力してください: ")
    # ニュース記事を提案
    #geminisample1.suggest_news_articles(keyword)
    url_list = get_url_list(keyword)
    # 取得したURLについて生成AIに要約を依頼
    suggest_urls_articles(url_list)
    """
    dispKAViewer()

if __name__ == '__main__':
    main()
