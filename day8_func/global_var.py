animal = "first"

def change_global():

    animal = "eeeee"
    #함수내부에서 선언하면 그냥 global과 이름만 같을뿐이지
    #실제로는 다른 변수이다
    #global이라 선언해야 전역 변수를 가져온다
    print(animal)
    return animal

print(animal)
change_global()
print(animal)