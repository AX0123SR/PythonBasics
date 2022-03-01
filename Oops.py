class Calculator:
     n = 100    #class variables

     def __init__(self,a, b):   #Constructor is automatically called when an object is created.
         self.fn = a         # fn,sn are instance variables
         self.sn = b
         print("I am automatically called when an object is created.")

     def greet(self):
         print("Hello Ayush")

     def add(self):
         return self.fn + self.sn


obj = Calculator(2, 3)
obj.greet()
print(obj.add())

