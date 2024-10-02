# Function Tasks
#
#
# Let's see if you can solve these word problems by creating functions.
# The function "skeleton" has been set up for you to fill in below the problem
# description, as well as example outputs of what the function should return
# given certain inputs. Best of luck, some of these will be challenging!
#
# The tasks will start off easy and proceed to get harder and harder.

# ## Task 1
#
#  Create a function that takes in two integers and returns
## a Boolean True if their sum is 10, False if their sum is something else.

l1 = []


def check_ten(n1, n2):
    l1.append(n1)
    l1.append(n2)
    result = sum(l1)
    if result == 10:
        return True
    else :
        return False


print(f"Result Ten : {check_ten(1, 2)}")


# ## Task 2
#
# Create a function that takes in two integers and returns True if their
# sum is 10, otherwise, return the actual sum value.

def check_ten_sum(n1, n2):
    operate = n1 + n2
    if operate == 10:
        return True
    else :
        return operate

print(f"Result : {check_ten_sum(1, 2)}")


# ## Task 3
#
# Create a function that takes in a string and returns back the
# first character of that string in upper case.


def first_upper(mystring):
    print(mystring.capitalize())

first_upper("tow")
# Code Here


# ## Task 4
#
# Create a function that takes in a string and returns the last two characters.
# If there are less than two chracters, return the string:  "Error".
# Use this link if you need help/hint.
# (https://stackoverflow.com/questions/7983820/get-the-last-4-characters-of-a-string)


def last_two(mystring):
    com = len(mystring)
    if com < 2:
        print("Error")
    else :
        print(mystring[-2:])

last_two("vincen")

# ## Task 5
#
# Given a list of integers, return True if the sequence [1,2,3] is somewhere
# in the list. Hint: Use slicing and a for loop.


def seq_check(nums):
    # Step 1 : Have to split first the problem inside list there will be source data for seeking condition [1,2,3]
    # Step 2 : Looking the best way for solving problem, in this case using split array for looking the same condition [1,2,3]
    # Step 3 : Code of it spliting the parameters [1,2,3,4,5] and increase the first num using loop for read evry start queue
    # and make upper limit (3) in split the value of this part will looked equal with condition
    for num in range(0,len(nums)):
        if nums[num:num+3] == [1,2,3]:
            return True

    return False

lili = [1,2,3,4,5]
print(seq_check(lili))




# ## Task 6
#
# Given a 2 strings, create a function that returns the difference in length
# between them. This difference in length should always be a positive number
# (or just 0). Hint: Absolute Value.**

def compare_len(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    diff = abs(len1 - len2)
    if diff % 2 == 0 :
        print("Absolute Value")
    else :
        print("Relative Value")

compare_len("tow", "vin")



# ## Task 7
#
# Given a list of integers, if the length of the list is an even number,
# return the sum of the list. If the length of the list is odd, return the max
## value in that list.


def sum_or_max(mylist):
    if len(mylist) > 0:
        max(mylist)

