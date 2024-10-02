print("===================FOR===================")

list = [1, 2, 3]

for i in list:
    print(i)

print("===================FOR DICTIONARY===================")
dic = [('a', 1), ('b', 2), ('c', 2)]

# print(isinstance( dic[0], tuple))
# TUPLE UNPACKING
for (item1, item2) in dic:
    print("dalam kepala {} {}".format(item1, item2))

print("===================WHILE===================")

i = 1
while i < 5 :
    print(f"is Currently {i}")
    i += 1

print("===================RANGE===================")
for x in range(0, 5):
    print(f"{x} is")

print("===================LOOKING FOR===================")
print("s" in "asodasodoqwmlfkqmlfsdpfsdsdokps")