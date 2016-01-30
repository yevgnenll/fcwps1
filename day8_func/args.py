# 여기 선언하면 전역변수


def print_agrs(*args):
    if len(args) == 0:
        print(None)
    else:
        print(len(args),"args[0]:" ,args[0])
        print("test", args)

def print_kwargs(**args):
    print('keyword:', args)

print_agrs(1,2,3,4,6)
print_agrs()

print_kwargs(first="1",second="2",name="3")
print_kwargs(wine="merlot", entree="mutton")
e = 4
def answer():
    global e
    e = 5
    print(42, e)
print("**", e)

answer()
print("**", e)




def run_someting(abc):
    """
    함수 안에서 함수가 호출됨
    :param abc: 여기에 함수가 들어가야 한다
    :return: 없음
    """
    abc()
    print("--")

# run_someting(answer)