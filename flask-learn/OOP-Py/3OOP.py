# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f'{self.name} is {self.age} years'
#
#
# person1 = Person('John', 20)
# print(isinstance(person1, Person))


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

# Creating an instance of the Point class
point1 = Point(3, 5)

# Using the __repr__ method implicitly
print(repr(point1))