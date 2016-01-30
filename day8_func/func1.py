def echo(name, age, job):
    if job == "developer":
        print("my friend!!!")
    return str("my name is "+ name+ " and "+ str(age)+ "years old my job is "+job)

res = echo("seungkwon", 27, "developer")
print(res)
print(type(res))

def sum1(a, b):
    return a+b

print(sum1(1,2))

#
# def is_none(thing):
