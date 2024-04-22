import requests
from urllib.parse import urlparse
import base64
from PIL import Image
from io import BytesIO

def is_valid_url(url):
    result = urlparse(url)
    # スキーマがhttpまたはhttpsであることも確認
    return all([result.scheme in ['http', 'https'], result.netloc])
    return False

def is_image_url(url):
    # URLが正当であることを確認
    if not is_valid_url(url):
        return False

    # Send a HTTP HEAD request
    try:
        response = requests.head(url)
    except Exception as e:
        return False
    # Check if "content-type" header exists and starts with "image"
    if "content-type" in response.headers and response.headers["content-type"].startswith("image"):
        return True
    else:
        return False

def anal_pict(message,chat_history,image_box):

    if len(chat_history) == 0:
         chat_llm.history=[] # チャットメモリも空に

    if is_image_url(message): #url  check
        # URLが正しい場合の処理
        url = message
        #image_box =message
    else:
        chat_history.append((message,"正しい画像URLではありません。"))
        return "", chat_history,""

    # gemini pro vision setting
    #model_image  = genai.GenerativeModel('gemini-pro-vision')
    try:
        response = requests.get(url)
    except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
        chat_history.append((message,"画像のダウンロードに失敗しました。URLが正しいか確認してください。"))
        return "",chat_history,""

    try:
        img = Image.open(BytesIO(response.content))
        image_box=img
    except Exception as e:
        chat_history.append((message,"画像読み込み時にエラーが出ました。正しい画像URLを確認してください。"))
        return "",chat_history,""


    prompt = "画像について、日本語で説明してください。"
    response = model_image.generate_content([prompt, img])

    content = "画像の説明:\n"+response.text

    chat_history.append((message, content))

    return "", chat_history,image_box
