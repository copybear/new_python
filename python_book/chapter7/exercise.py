import re

# 日付の検出：閏年とか４月が３０日までとかは考えなくて良い:yyyy/mm/ddを検出
# 年は1000-2999まで
regex_cal=re.compile(r"[1-2][0-9]{3}/((1[0-2])|(0[1-9]))/(([3][0-1])|([1-2][0-9])|(0[1-9]))")
# 日付チェック
print("⭐️calender check:")
vals="2024/08/18,2024/08/32,2024/8/3,3024/08/03,2024/01/00,2024/02/31".split(",")
for val in vals:
    ans=regex_cal.search(val)
    print("input:"+val)
    print("output:"+ans.group(0)) if ans!=None else print("No match")

# 強いパスワードの検出
print("⭐️passwordcheck")
# 8文字以上、大文字小文字を含む、１つ以上の数値を含む
regex_pass1=re.compile(r"[a-z]+")
regex_pass2=re.compile(r"[A-Z]+")
regex_pass3=re.compile(r"[0-9]+")
vals=["abcds","Abc123defg","1234567890abc","aA12345","aA123456"]

for val in vals:
    print("input:"+val)
    chk1=regex_pass1.search(val)
    chk2=regex_pass2.search(val)
    chk3=regex_pass3.search(val)
    if chk1!=None and chk2!=None and chk3!=None and len(val)>=8:
        print("output:OK!")
    else:
        print("output:NG")



def cust_split(spchr,val):
    ret=[]
#    compstr="(("+spchr+r"\w+)|(^\w+))"
    compstr=r"((\t\w+)|(^\w+))"
    print(compstr)
    matches=re.compile(compstr).findall(val)
    for gr in matches:
        val=gr[0].strip()
        val=val.strip(spchr)
        if val!="" :
            ret.append(gr[0])
    return ret

# split関数と同様の関数を正規表現で実装
print("⭐️split function")
vals=["test,koko,gogo","ok",r" test\tgogo\tsplit, ok,go"]
for val in vals:
    retval=cust_split(",",val)
    print("input:"+val+" spritchar:"+",")
    print("output:")
    print(retval)

for val in vals:
    retval=cust_split("\t",val)
    print("input:"+val+" spritchar:"+"\t")
    print("output:")
    print(retval)
