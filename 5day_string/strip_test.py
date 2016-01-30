# -*- coding: utf-8 -*-
setup = "aaaaa duck goes into a bar..."

a = setup.strip(".")
print(a +": ... 없앰")
b = setup.strip("a")
print(b + ": a를 없앰")
c = b.strip("a")
print(c + ": a 한번더없앴는데 뒤에 a는 사라지지않음")

