# img_viewer.py

import PySimpleGUI as sg
import os.path
from geminisample1 import suggest_urls_articles
from geminisample2 import get_url_list
import json

# First the window layout in 2 columns

def dispKAViewer():
    keyword_list_column = [
        [
            sg.Text("KeyWord:"),
            sg.In(size=(25, 1), enable_events=True, key="-KEYWORD-"),
            sg.Button("Search",key="-QUERY-"),
        ],
    ]

    # For now will only show the name of the file that was chosen
    answer_list_column = [
        [sg.Text("Answer from generativeAI:")],
        [sg.Text(
            "", size=(100, 70), key="-ANSWER-"
        )],
    ]

    # ----- Full layout -----
    layout = [
        [
            sg.Column(keyword_list_column),
            sg.VSeperator(),
            sg.Column(answer_list_column),
        ]
    ]

    window = sg.Window("Keyword to Answer", layout)

    # Run the Event Loop
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        # Folder name was filled in, make a list of files in the folder
        if event == "-QUERY-":
            keyword = values["-KEYWORD-"]

            # ニュース記事を提案
            url_list = get_url_list(keyword)
            print(url_list)
            # 取得したURLについて生成AIに要約を依頼
            ansList=suggest_urls_articles(url_list)
            print(ansList)

            window["-ANSWER-"].update(json.dumps(ansList, ensure_ascii=False, indent=2))

    window.close()
