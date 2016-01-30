# while True:
#     stuff = input("String to capitailze [type q to quit]:")
#     if stuff == "q":
#         break
#     print(stuff.capitalize())

#continue
numbers = [1,2,5]
position = 0
while position < len(numbers):
    print("position:",position)
    number = numbers[position]
    print("number:",number)
    if number % 2 ==0:
        print("found even number", number)
        break
    position += 1
else:
    print("no even number found")
