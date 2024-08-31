import re

# 7-18 subは置き換え
num_regex=re.compile(r"\d+")
ret18=num_regex.sub('X', '12 drummers, 11 pipers, five rings, 3 hens')
print("7-18 answer:")
print(ret18)

# 7-20
regex_20=re.compile(r"(^\d{1,3}(,[0-9]{3})+)|\d{1,3}")

val="1,234,567"
ret20=regex_20.search(val)
print("7-20 answer:")
print(ret20.group(0))if ret20!=None and ret20.group(0)==val  else print("No Match")

# 7-21
regex_21=re.compile(r"[A-Z][a-z]*\sWatanabe")
val="Haruto watanabe"
ret21=regex_21.search(val)
print("7-21 answer:")
print(ret21.group(0))if ret21!=None and ret21.group(0)==val  else print("No Match")

# 7-22
regex_22=re.compile(r"(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs).",re.IGNORECASE)
val="Alice Eats Apples."
ret22=regex_22.search(val)
print("7-22 answer:")
print(ret22.group(0))if ret22!=None and ret22.group(0)==val  else print("No Match")
