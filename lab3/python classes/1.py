class MyClass:
    def getString(self):
        self.my_string = input()
    def printString(self):
        print(self.my_string.upper())
obj=MyClass()
obj.getString()
obj.printString()

