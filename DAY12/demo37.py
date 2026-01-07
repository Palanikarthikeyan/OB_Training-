class Product:
    def __init__(self,pcost):
        self.__pcost = pcost
    @property
    def getter_method(self):
        print('Getter block is invoked')
        return self.__pcost
    @getter_method.setter
    def getter_method(self,pcost):
        print('Setter block is invoked')
        self.__pcost = pcost
        return self.__pcost
'''
obj1 = Product(1000)
print(obj1.getter_method())
obj2 = Product(2000)
print(obj2.getter_method())
'''
obj1 = Product(1000)
print(obj1.getter_method)
obj1.getter_method = 2000  # calling setter block
print(obj1.getter_method)
obj1.getter_method = 3000 # calling setter block
print(obj1.getter_method)
