# sytax eror dimana penulisan dari kode program tersebut kurang tepat
# contoh print(1+(1+2) SyntaxError: '(' was never closed

# exception itu dimana kode program suda benar tapi tidak sesuai dengan yang telah di tetapkan pada IDE
# contoh print(10/0) Division by Zero

# RAISE EXCEPTION
usia = 20
if usia < 17:
    raise Exception
print("Usia anda cukup, Silahkan Masuk")

# ASSERTION
usia = 20
assert (usia>17), f'usia anda tidak boleh lebih kecil dari 17 tahun, usia anda {usia}'
print("Usia anda cukup, Silahkan Masuk")

# Try Catch Py
# except digunakan untuk menangkap error
# else : digunakan untuk melakukan task setelah kode block try berjalan dan tidak tejadi except
# finally dilakukan terjadi keduanya antara except dan berhasil

angka = 0
huruf = "a"
try:
    print(huruf/angka)
except ZeroDivisionError:
    print('Angka tidak bisa dibagi 0')
except TypeError :
    print('Angka tidak dilakukan operasi dengan Huruf')
finally:
    print("Complate")

