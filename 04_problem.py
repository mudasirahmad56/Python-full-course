class calculator:

    def __init__(self,n):
        self.n = n
    def square(self):
        print(f"the square is {self.n*self.n}")
    def cube(self):
        print(f"the cube is {self.n*self.n*self.n}")
    
    def square_root(self):
        print(f"the square root is {self.n**1/2}")
    @staticmethod
    def print_message():
        print("hello world")

a = calculator(4)
a.print_message()
a.square()
a.cube()
a.square_root()