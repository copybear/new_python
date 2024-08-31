import pyinputplus as pyip

prompt = "パンの種類を選んでください。\n"
pan=''
pan = pyip.inputMenu(['小麦パン','白パン','サワー種'],prompt,numbered=True)
prompt = "タンパク質の種類を選んでください。\n"
tanpac=''
tanpac=pyip.inputMenu(['チキン','ターキー','ハム','豆腐'],prompt,numbered=True)
prompt = 'チーズはいかが？'
cheeze = pyip.inputYesNo(prompt)
if cheeze=='yes':
    prompt = 'チーズの種類を選んでください'
    cheeze=pyip.inputMenu(['チェダー','スイス','モツァレラ'],numbered=True)
prompt = 'マヨネーズはいかが？'
mayo = pyip.inputYesNo(prompt)
prompt = 'からしはいかが？'
kara = pyip.inputYesNo(prompt)
prompt = 'レタスはいかが？'
reta = pyip.inputYesNo(prompt)
prompt = 'トマトはいかが？'
toma = pyip.inputYesNo(prompt)
prompt = 'サンドイッチはいくつ必要ですか？'
cnt = pyip.inputInt(prompt,min=1,max=10)
print(f'あなたのオーダー：パン：{pan} タンパク質：{tanpac} チーズ：{cheeze} マヨネーズ：{mayo} からし：{kara} レタス：{reta} トマト：{toma} 注文数：{cnt}')
