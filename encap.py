class Encapsulation:
    a = 10
    b = 20

    def __init__(self, c, d):
        self.c = c
        self.d = d

    def display(self):
        print(self.c, self.d)

    def ch_c(self, new):
        self.c = new

    @classmethod
    def disp(cls):
        print(cls.c, cls.d)

    @staticmethod
    def msg():
        print("public access specifiers")


user = Encapsulation(10, 20)
user.display()
user.ch_c(40)
user.display()

