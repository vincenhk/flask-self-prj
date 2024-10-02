
print("==================TUPLE==================")
# tuple is immutable, meaning their element cant be modified
# but tuple can operate (+) with other tuple

t1 = (1,2,3)
t2 = [4,5,6]

print("tuple type",isinstance(t1, tuple))
t_bunch = t1
print(t_bunch)

print("==================SET================== ")

# SET TYPE SETS
x = set()
print(x)
x.add(1)
x.add(2)
x.add(3)
print(x)
x.remove(2)
x.add(2)
print(x)
print(isinstance(x, tuple))

# ANOTHER WAY TO MAKE SETS
mylist = [1,2,3,4,5,6,7,8,9]

sets = set(mylist)
print("Check data type",isinstance(sets, set))
print("Data design",sets)

print("==================BOOLEAN================== ")

a = True
b = False
# Special Keyword
c = None
print(1 < 2)
