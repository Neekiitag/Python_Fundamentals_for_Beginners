class Father():
    def gardening(self):
        print("I enjoy gardening")


class Mother():
    def cooking(self):
        print("I enjoy cooking")

class Child(Father, Mother):                                        # child is a derived class from the base classes - mother & father
    def sports(self):
        print("i love sports")

c = Child()
c.sports()
c.gardening()
c.cooking()

