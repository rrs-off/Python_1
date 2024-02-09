class Shape:
    def __init__(self,length):
        self.length=length
    def area(self):
        print(self.length*self.length)
l=int(input())
p1=Shape(l)
p1.area()