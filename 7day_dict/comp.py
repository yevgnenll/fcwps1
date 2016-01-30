number = [number for number in range(0,101)]
# print(number)

min = [minx-1 for minx in range(0,101)]
# print(min)
#for앞의 변수가 = 앞의 변수로 들어간다

# print(type(number), type(min))

# a = list(range(0,10))
#
# a_list = [ref for ref in range(0,10) if ref % 2 == 0]
# print(a_list)
#
# rows = range(0,5)
# cols = range(0,10)
# #1, 3, 5, 7, 9
#
# ret = [(row, col) for row in rows if row % 2 == 0 for col in cols if col % 2 == 1]
# print(ret)

word = 'letters'
letters_count = {letter:word.count(letter) for letter in word}
#word라는 단어가 letter안에서 몇번이나 반복되는지 그 수를 리턴함
print(letters_count)
let_set = {letter : word.count(letter) for letter in set(word)}
# count로 찾는 범위는 word이지 set(word)가 아니다
print("origin", let_set)
let_set = {}
for letter in set(word):
    let_set[letter] = word.count(letter)
    # 찾는 범위는 word이지 set(word)가 아니다


let_co = {}
for let in word:
    let_co[let] = word.count(let)
    #전체단어.count(찾는단어)
    # print(let, word.count(let))

print(let_co)