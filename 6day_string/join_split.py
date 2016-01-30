# -*- encoding:utf-8 -*-
crypto_list = ['Yeti', 'Bigfoot', 'Loch Ness Monster']
crypto_string = ','.join(crypto_list)
print("result is: ", crypto_string)

print(type(crypto_string))

doc = "Returns an iterator of tuples, where the i-th tuple contains the i-th " \
      "element from each of the argument sequences or iterables. The iterator stops " \
      "when the shortest input iterable is exhausted. With a single iterable argument, " \
      "it returns an iterator of 1-tuples. With no arguments, it returns an empty iterator. Equivalent to:"


print(len(doc))
print(doc.startswith("Return"))
print(doc.endswith("to:"))
#첫 번째로 of로 시작하는 자리
print(doc.find("of"))
print(doc[20],doc[21])

print(doc.rfind("of"))
print(doc[250], doc[251])

print(doc.title())


"""
if type(crypto_string) == "<class 'str'>":
    print(type(crypto_string))
elif(type(crypto_string) == str):
    print("string---")
else:
    print("wrong")

test = 1234
if type(test) == int:
    print("integer")
"""