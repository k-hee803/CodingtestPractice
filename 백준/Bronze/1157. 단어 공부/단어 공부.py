word = input().upper()

alp = ''.join(dict.fromkeys(word))

cnt = []
for i in alp:
    cnt.append(word.count(i))

c = max(cnt)

if cnt.count(c) >=2 :
    print("?")
else :
    print(alp[cnt.index(c)])