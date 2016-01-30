def print_args(a, b, *args):
    print("fitst", a)
    print("second", b)
    print("the others", args)

def random_game(thisFunc, a, b, *args):
    thisFunc(a,b,*args)
    return "success"

def outer(first,second,third, fourth):
    def hap(a, b):
        return int(a +b)
    def gop(c, d):
        return int(c * d)
    return hap(first, second) + gop(third, fourth)

# print_args(1,2,("2323","rser",True))
# random_game(print_args,1,2,("2323","rser",True))
print(outer(2,3,0,4))


print(bin(ord('a')))
"""
def upper_new(text):
    if type(text) != type("str"):
        return "문자열로 입력해주세요~"
    else:
        for txt in text:
"""
