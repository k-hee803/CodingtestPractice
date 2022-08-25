N = int(input())
words = []
for _ in range(N):
    words.append(input())

word = list(set(words))
word.sort()
word.sort(key=len)
for i in range(len(word)):
    print(word[i])