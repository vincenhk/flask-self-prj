for i in range(0, 10):
    if i < 5:
        continue
    print(i)

print("New Part")
for i in range(0, 10):
    if i > 5:
        # continue
        break
    print(i)


namaList = ["vincen", "hendri", "kurni"]
for nama in namaList:
    print(nama)