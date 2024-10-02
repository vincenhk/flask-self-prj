print("==================FUNCTION==================")


def report_person(name="BLACK"):
    print("Hello " + name + "!")


report_person()

print("==================JOIN==================")
mylist = ["a", "b", "c", "d"]

print('ad'.join(mylist))

print("==================FUNCTION CUSTOM==================")


def code_maker(mystring):
    output = list
    print(output)
    for index, letter in enumerate(mystring):
        for vowel in 'aeiou':
            if letter == vowel:
                output[index] = 'x'
    output = ''.join(output)
    return output


print(code_maker("vincen"))

print("==================FUNCTION GENAP/GANJIL==================")


def numberOrdinaryChecker(number):
    if (number % 2 != 0):
        return "Bilangan Ganjil"
    else:
        return "Bilangan Genap"


msg = numberOrdinaryChecker(4)
print(msg)

print("==================FUNCTION SUM==================")
list = ([1, 2, 3, 4, 5, 6, 7, 8, 9])
sum = 0
print(isinstance(sum, int))

def sumFunction(listNumber):
    print(listNumber[0])
    sum = sum(listNumber[0])


print(f"The sum is {sum}")

l1 = []
def check_ten(n1,n2):
    l1.append(int(n1))
    l1.append(int(n2))
    print(l1)
    # result = sum(l1)
    # return result

check_ten(1,2)
