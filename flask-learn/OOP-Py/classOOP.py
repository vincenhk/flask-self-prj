# v1 = 1.2
#
# print(type(v1))
#
# class Sample():
#     pass
#
# x = Sample()
#
# print(type(x))


# class Dog():
#     def __init__(self, breed):
#         self.breed = breed
#
# x = Dog('lab')
# print(x.breed)

class Animal():
    def __init__(self, fur):
        self.fur = fur
        print('Animal Created')

    def report(self):
        print('Animal')

    def eat(self):
        print('Eating')

class Dog(Animal):
    def __init__(self, fur):
        Animal.__init__(self, fur)
        print('Dog Created')

    def report(self):
        print('I am a dog')

x = Animal("Nama")
dog = Dog("Fuzzy")
print(x.fur)
print(dog.fur)