class car():
    def exclaim(self):
        print("I'm a Car!")

class sonata(car):

    self.__name
    def exclaim(self):
        super().exclaim()
        print("I'm a Sonata!")

    @property
    def name(self):
        return self.__name

    @name.setter
    def set_name(self, input_name):
        self.__name = input_name


test = sonata()
test.__name = "yevg"

test.set_name("yevgnenll")
print(test.__name)

