import os
import gradio as gr
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

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE"
    }
]

model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)
chat_llm = model.start_chat(history=[])

with gr.Blocks() as win:
     # コンポーネント
    chatbot = gr.Chatbot()
    #pelsona = gr.Textbox(label="persona")
    pelsona = gr.Dropdown(['なんでも知ってる博士','大人になりたい小さな男の子','陰気なギャル','陽気なギャル','生意気な２０代の男性','皮肉が好きな紳士','とても厳しいおじいさん','嫌味なお金持ち','チャラ男','キース・ヘリング','ピカチュウ','世紀末覇者ラオウ'],label='pelsona')
    msg = gr.Textbox(label="message")
    with gr.Row():
        msg_button = gr.Button('Send Message')
        reset_button = gr.Button('Reset')

    # 関数
    def chat_ai(pelsona,message,chat_history):
        # 通常のチャット処理

        if len(chat_history) == 0:
            chat_llm.history=[] # 履歴が空なら、チャットメモリも空に

        prompt = '問い合わせ：' + message + '\n'
        prompt = prompt + 'ペルソナ：' + pelsona

        print(prompt)

        try:
            response = chat_llm.send_message(prompt)
            chat_history.append((message, response.text))
        except:
            chat_history.append((message, '会話の取得に失敗しました。'))

        return "", chat_history

    def reset_chat_history(chat_history):
        chat_history=[]
        chat_llm.history=[] # チャットメモリも空に

        return "",""

    # イベント
    msg_button.click(chat_ai,[pelsona,msg,chatbot],[msg,chatbot])
    reset_button.click(reset_chat_history,[chatbot],[msg,chatbot])

win.launch(share=True)
