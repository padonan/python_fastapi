class Calc:
    def __init__(self, n1, n2):
        self.n1 = n1 
        self.n2 = n2
        return print(self.n1, self.n2)

    def __call__(self, n1, n2):
        self.n1 = n1 
        self.n2 = n2
        return print(self.n1 + self.n2)

s = Calc(1,2)

s(7,8)