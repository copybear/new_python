import google.generativeai as genai
import const
import json

def suggest_news_articles(keyword):

    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-pro')

    option='*なお、回答はJSON形式でお願いします。Format{"answer":["answer1","answer2",...]}'

    response = model.generate_content(keyword+option)
    print(response.text)

def suggest_urls_articles(urls):
    # APIキーを設定
    GOOGLE_API_KEY = os.getenv('GGAI_API_KEY')
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    items=[]
    for url in urls:
        #msg='次のURLの内容の要約を100文字いないでお願いします。URL:'
        msg='次のURLの内容に英語で詩的なタイトルをつけてください。URL:'
        msg=msg+url
        response = model.generate_content(msg)
        item = {"url":url,"article":response.text}
        items.append(item)
    return items
