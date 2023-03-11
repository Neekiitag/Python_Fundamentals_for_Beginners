class Human:                                                               # defining a class
    def __init__(self, n, o):                                              # defining the properties of a class - human
        self.name = n
        self.occupation = o

    def do_work(self):                                                   # defining first method of class - human
        if self.occupation == "Tennis Player" :
            print(self.name, "plays tennis")
        elif self.occupation == "Actor":
            print(self.name, "shoots for a film")

    def speaks(self):                                                    # defining second method of class - human
        print(self.name, "says how are you?")

tom = Human("tom cruise", "Actor")
tom.do_work()
tom.speaks()

saina = Human("Saina Nehwal", "Tennis Player")
saina.do_work()
saina.speaks()


