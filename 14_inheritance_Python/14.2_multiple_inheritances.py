class Father():
    def skills(self):
        print("Trading, gardening")


class Mother():
    def skills(self):
        print("cooking, Dancing")

class Child(Father, Mother):                                        # child is a derived class from the base classes - mother & father
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("sports")

c = Child()
c.skills()

