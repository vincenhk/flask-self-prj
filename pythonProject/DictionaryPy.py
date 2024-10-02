telepon = {'Joni' :'081322703852', 'Vincen':'081323869823', 'Lily' : '071238127391'}

nama : str = input("Masukkan Nama : ")
if nama in telepon:
    print("Nomor HP", nama, "yang anda cari",telepon[nama])
else :
    print("Nomor HP yang ada cari tidak ada")
    for nama in telepon:
        print(nama, telepon[nama])
