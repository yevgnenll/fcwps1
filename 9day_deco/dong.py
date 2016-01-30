#
# '''이번에는 세 인자를 취하는 run_someting_with_args() 함수를 호출해보자
# func : 실행할 함수
# arg1 : func함수의 첫번째 인자
# arg2 : func함수의 두번째 인자'''
#
def run_something_with_args(func,arg1,arg2):
    func(arg1,arg2)



def sum_args(*args):
    return sum(args)
       #sum(1,2,3,4)
def run_with_positional_args(func,*args):
    return func(*args)
       #sum_args(1,2,3,4)
print(run_with_positional_args(sum_args,1,2,3,4))