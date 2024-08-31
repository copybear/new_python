import pyinputplus as pyip

while True:
    prompt="バカを何時間も忙しくさせる方法を知りたいですか？\n"
    response=pyip.inputYesNo(prompt)
    if response == "no":
        print("ありがとうごきげんよう！")
        break
    
