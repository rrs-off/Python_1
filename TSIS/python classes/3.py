class Rectangle:
    def area(self):
        self.length=int(input())
        self.width=int(input())
        print("area =", self.length*self.width)
a=Rectangle()
a.area()