print("====================VARIABLE====================")
v1 = 2
print(isinstance(v1, int))
v2 = "Fajar"
# for a in v2 :
#     print(a)
print(f'Hasil : {v2[2]}')
print(f'Len v2 : {len(v2)}')
print("====================SLAICING====================")

# SLAICING
v3 = "abcdefghijklmnop"
print(v3[::-1])

print("====================MODIFY====================")
v4 = "Hellow World"
v5 = "20, 20, 30"
print(f'upper : {v4.upper()}')
print(f'capitalize : {v4.capitalize()}')
print(f'lower : {v4.lower()}')
print(f'split : {v4.split()}')
print(f'split : {v5.split(", ")}')

username = "Addyani"
color = "blue"
print("The {} favorite color is {}".format(username, color))

# PYTHON 3.6 AND ABOVE
print(f"The {username} color is {color}")