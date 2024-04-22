 #gradio
import gradio as gr
import requests
from urllib.parse import urlparse
import base64
from PIL import Image
from io import BytesIO

import os
import datetime
import google.generativeai as genai

GGAI_API_KEY = os.getenv('GGAI_API_KEY')
genai.configure(api_key=GGAI_API_KEY)

# chat model
# initial setting
# モデルの設定
generation_config = {
  "temperature": 0.9,  # 生成するテキストのランダム性を制御
  "top_p": 1,          # 生成に使用するトークンの累積確率を制御
  "top_k": 1,          # 生成に使用するトップkトークンを制御
  "max_output_tokens": 2048,  # 最大出力トークン数を指定
}
model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config)

chat_llm = model.start_chat(history=[])
#model_image = genai.GenerativeModel('gemini-pro-vision')
model_image = genai.GenerativeModel('gemini-1.5-pro-latest')

with gr.Blocks() as demo:
     # コンポーネント
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    with gr.Row():
        reset_w_save = gr.Button("Save&reset history")
        reset_wo_save = gr.Button("reset history")
    with gr.Row():
        analyze_picture = gr.Textbox(label="画像の説明　URLを貼り付けてください。")
        with gr.Row():
            image_box = gr.Image()
            image_button =gr.Button('Send Image')

    def save_chat_history(message,chat_history):
        filename = "chatlog"+datetime.datetime.now().strftime("%Y%m%d-%H%M%S")+".txt"
        with open(filename, 'w',encoding='utf-8') as f:
            for chat in chat_history:
                f.write(f"User: {chat[0]}\nAI: {chat[1]}\n")
        chat_history=[]
        chat_llm.history=[] #チャットメモリも空に
        return "",""

    def reset_chat_history(message,chat_history):
        chat_history=[]
        chat_llm.history=[] # チャットメモリも空に

        return "",""


    def chat_ai(message,chat_history):
        # 通常のチャット処理

        if len(chat_history) == 0:
            chat_llm.history=[] # 履歴が空なら、チャットメモリも空に

        prompt=message
        response = chat_llm.send_message(prompt)
        chat_history.append((message, response.text))

        return "", chat_history
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

    def anal_imagebox(chat_history,image_box):
        if len(chat_history) == 0:
             chat_llm.history=[] # チャットメモリも空に

        img=Image.fromarray(image_box.astype("uint8"), "RGB")

        print(img)

        prompt = "画像について、日本語で説明してください。"
        response = model_image.generate_content([prompt, img])

        content = "画像の説明:\n"+response.text

        chat_history.append(('',content))

        return chat_history


    msg.submit(chat_ai, [msg, chatbot], [msg, chatbot])
    reset_wo_save.click(reset_chat_history, [msg, chatbot], [msg, chatbot])
    reset_w_save.click(save_chat_history, [msg, chatbot], [msg, chatbot])
    analyze_picture.submit(anal_pict,[analyze_picture,chatbot,image_box],[analyze_picture,chatbot,image_box])
    image_button.click(anal_imagebox, [chatbot,image_box],chatbot)

demo.launch(share=True)
