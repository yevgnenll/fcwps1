word = input()
mid_count = len(word) // 2
isPalin = True
if len(word)%2 == 0:
    revers = word[mid_count:]
else :
    revers = word[mid_count+1:]
revers = revers[::-1]
for idx, w in enumerate(word[0:mid_count]):
    if w != revers[idx]:
        isPalin = False
print(int(isPalin))