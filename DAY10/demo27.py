class P:
   def display(self):
       print("display - product details")

class C(P):
   def display(self):
       print("display - Customer details")
       super().display() # invoke parent class display method

obj = C()
obj.display()