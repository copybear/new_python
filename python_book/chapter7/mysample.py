import re

# 電話番号を抜き出す
phone_regex=re.compile(r"""(
    (0\d{0,3}|\(0\d{0,3}\))?
    (\s|-)?
    (\d{1,4})
    (\s|-)
    (\d{4})
)""",re.VERBOSE)
print('Phone:')
print(phone_regex.findall('電話番号は(078)200-4510です！FAX番号は078-200-4501です！'))

# 4文字の単語だけを抜き出す
test1_regex=re.compile(r"""(
    (^\w{4}\s|\s\w{4}\s|\w{4}\.?$)
)""",re.VERBOSE)
print('Test1:')
print(test1_regex.findall('Test String length Text move'))

# searchの動きがよくわからない
testTxt=r'Test String'
test2_regex=re.compile(r'(.){1,4}')
print('Test2:')
print(test2_regex.findall(testTxt))
test3_regex=re.compile(r'(.{1,4})')
print('Test3:')
print(test3_regex.findall(testTxt))
test4_regex=re.compile(r'((.){1,4})')
print('Test4:')
print(test4_regex.findall(testTxt))
test5_regex=re.compile(r'((.{1,4}))')
print('Test5:')
print(test5_regex.findall(testTxt))
test6_regex=re.compile(r'(.)(.)(.)(.)')
print('Test6:')
print(test6_regex.findall(testTxt))
test7_regex=re.compile(r'(.){4}')
print('Test7:')
print(test7_regex.findall(testTxt))
test8_regex=re.compile(r'((.)(.)(.)(.))')
print('Test8:')
print(test8_regex.findall(testTxt))

# +の判定がおかしい
test9_regex=re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.%+-]+\.[a-zA-Z]{2,4}')
print('Test9:')
print(test9_regex.findall('test_10@t_ratora.com'))
# A-zがタイプミスでこれが原因で問題が発生
test10_regex=re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-z0-9.%+-]+\.[a-zA-Z]{2,4}')
print('Test10:')
print(test10_regex.findall('test_10@t_ratora.com'))

test11_regex=re.compile(r"""(https?://[a-zA-Z0-9._%+-]+(\.[a-zA-Z]{2,4}))""")
print('Test11:')
print(test11_regex.findall('http://google.co.jp'))

test12_regex=re.compile(r"""
(https?://[a-zA-Z0-9._%+-]+(\.[a-zA-Z]{2,4}))""")
print('Test12:')
print(test12_regex.findall('https://google.co.jp'))

# tab文字判定
test13_regex=re.compile(r'\t\w+')
print('Test13:')
print(test13_regex.findall('test\tcom'))
