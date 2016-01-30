"""
days = ['Monday', 'Tuesday','Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']

for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day,": drink", drink, "- eat", fruit, "- enjoy", dessert)
"""
a = 1
list_a = []
while a <= 100:
    list_a.append(a)
    a += 1

print(list_a)


list_b = []
b = 1
while True:
    list_b.append(b)
    b += 1
    if b == 101:
        break

print(list_b)


print("---", chr(65))

number = [number for number in range(1,101)]
print(number)

rows = range(1,4)
cols = range(1,3)
cells =[(row, col) for row in rows for col in cols]

for cell in cells:
    print(cell)
    print(type(cell))

word = 'letters'
letter_counts = {letter:word.count(letter) for letter in word}
print(letter_counts)

print(set(word))


