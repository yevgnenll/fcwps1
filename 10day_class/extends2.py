class person():
    def __init__(self, name):
        self.name = name

# 사람은 태어날때 이름을 가지고 태어나기 때문에 처음에 반드시 이름을 가지고 태어나야한다
class MDPerson(person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email

class JDPerson(person):
    def __init__(self, name):
        self.name = name + ", Esquire"


normal = person("yoon")
doctor = MDPerson(None, "test")

# normal과 doctor는 서로 다른 객체이다 어떻게도 영향을 줄 수 없다

print(doctor.email, doctor.name)