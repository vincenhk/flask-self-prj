my_list = [1, 2, 3, 4, 5]

result = sum(my_list)

print(result)  # Output: 15

l1 = []


def check_ten(n1, n2):
    l1.append(n1)
    l1.append(n2)
    result = sum(l1)
    return result


print(f"Result : {check_ten(1, 2)}")

def check_ten_sum(n1, n2):
    operate = n1 + n2
    if operate == 10:
        return True
    else :
        return operate

print(check_ten_sum(5,4))

