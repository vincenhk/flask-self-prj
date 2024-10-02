x = "outside" # GLOBAL LEVEL x Variable

def report():
    # global x
    x = "inside"
    return x

print(report())
print(x)