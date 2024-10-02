#####################################
#### PART 6: EXERCISE REVIEW  #######
#####################################

# Time to review all the basic data types we learned! This should be a
# relatively straight-forward and quick assignment.

###############
## Problem 1 ##
###############

# Given the string:
s = 'flask'

# Use indexing to print out the following:
# 'f'
print("f :",s[0])
# 's'
print(f"s : {s[3]}")
# 'ask'
print(f"ask : {s[2:]}")
# 'las'
print("las : {}".format(s[1:4]))
# 'k'
print("k : {}".format(s[4::1]))

# Bonus: Use indexing to reverse the string
print("ls : {}".format(s[::-1]))


###############
## Problem 2 ##
###############

# Given this nested list:
mylist = [3,7,[1,4,'hello']]
# Reassign "hello" to be "goodbye"
mylist[2][2] = "goodbye"
print("my list : ",mylist)


###############
## Problem 3 ##
###############

# Using keys and indexing, grab the 'hello' from the following dictionaries:

d1 = {'simple_key':'hello'}
print("Get 1 :",d1.get('simple_key'))

d2 = {'k1':{'k2':'hello'}}
print("Get 2 :",d2['k1']["k2"])

d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print("Get 3 :", d3.get("k1")[0]["nest_key"][1][0])


###############
## Problem 4 ##
###############

# Use a set to find the unique values of the list below:
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
print("UNIQ VALUES :",set(mylist))


###############
## Problem 5 ##
###############

# You are given two variables:
age = 4
name = "Sammy"

# Use print formatting to print the following string:
"Hello my dog's name is Sammy and he is 4 years old"
print("Hello my dog's name is {} and he is {} years old".format(name, age))
