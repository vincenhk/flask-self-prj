print("==============LIST==============")

list = [1,2,3,4,5,6,7,8,9,10]

print(f"Len : {len(list)}")
print(f"List : {list}")
print("List : {}".format(list[0:3]))

list.append("z") # 1 Parameter unselecting index alwys add in last queue
print(f"list.append : {list}")

list.insert(4, 'T') # add list with choose index and object there can be
print(f"list.insert(index, object) : {list}")

pop_list = list.pop() # delete last index
print(f"after pop : {list}")
print(pop_list)

my_list = [1,2,3]
my_list2 = [4,5,6]
my_list3 = [7,8,9]

mega_list = [my_list, my_list2, my_list3]
print("Mega List LEN : {}".format(len(mega_list)))
print("Mega List : {}".format(mega_list[2][1]))
