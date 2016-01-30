class duck():

    #def __init__(self,input_name):
    #    self._name = input_name

    # def __init__(self, input_name):
    #     self.__name = input_name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,input_name):
        self.__name = input_name


m = re.search(r"(\w+[\w\.]*)@(\w+[\w\.]*)\.([A-Za-z]+)",
              "My email address is SooKkaRak@gmail.com")

test = duck()
test.name = "sfsdfd"
print(test.name)
print(test.name)
# test.__name = 2
#test.set_name("yevgnen")
#print(test.name)
#print(test.name)
#print(test._name)