#! python3
# phoneAndEmail.py クリップボードから電話番号とEMailを検索する
# もとのものにURLも検索結果に加えるように追加
# なのでphoneAndEmailAndUrl.property.propertyのほうが正しいが長いのでそのまま

import pyperclip,re

phone_regex=re.compile(r"""(
    (0\d{0,3}|\(0\d{0,3}\))
    (\s|-)?
    (\d{1,4})
    (\s|-)
    (\d{4})
    (\s*(ext|x|ext.)\s*(\d{2,5}))?   # 内線番号
)""",re.VERBOSE)

email_regex=re.compile(r"""(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.%+-]+
    (\.[a-zA-Z]{2,4})
)""",re.VERBOSE)

url_regex=re.compile(r"""(
    https?://
    [a-zA-Z0-9.%+-]+
    (\.[a-zA-Z]{2,4})
)""",re.VERBOSE)

text=str(pyperclip.paste())
matches=[]
for groups in phone_regex.findall(text):  # ❷
    print(groups)
    phone_num = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phone_num += ' x' + groups[8]
    if (phone_num in matches) == False:
        matches.append(phone_num)
for groups in email_regex.findall(text):  # ❸
    if (groups[0] in matches) == False:
        matches.append(groups[0])
for groups in url_regex.findall(text):  # ❸
    if (groups[0] in matches) == False:
        matches.append(groups[0])

# 検索結果をクリップボードに貼り付ける。
if len(matches) > 0:
    s = '\n'.join(matches)
    pyperclip.copy(s)
    print('クリップボードにコピーしました:')
    print(s)
else:
    print('電話番号やメールアドレスは見つかりませんでした。')
