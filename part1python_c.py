# -*- coding: utf-8 -*-
"""part1Python-c.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eHyx0zFYy48CM2my4xFyIgiE-7LNlKyj
"""

print("Hello World!")

nama = "Joni"

print(10+20)
print(10-60)
print(120/60)
print(10*60)
print(5**2)
print(nama)

link = "course.com"
kelas = 5

print(link)
print(kelas)

nama = input("Tulis nama Anda : ")
print(nama)

usia = input("Tulis usia Anda : ")
print(usia)

salam = "Hallo World!!"
print(salam)

cek = isinstance(salam, str)
print(cek)

nama = "Vincentius Hendri Kurniawan"
usia = 25
print("Hallo, apa kabar",nama,"usia anda adalah", usia)

"String Interpolation"

nama = "Vincentius Hendri Kurniawan"
usia = 25
print(f'Hallo, apa kabar {nama} umur kamu sekarang {usia}')

test1 = "Hey"
test2 = "Yow"
kalimat = test1+test2

print(kalimat)

"Operatior"

test1 = "a" * 2

print(test1)

angka = 7
angka2 = 1.15

luas_lingkaran = angka * (angka2**2)

print(luas_lingkaran)
type(luas_lingkaran)

nilai = input("Masukkan nilai : ")
nilai = int(nilai)
hasil = nilai + 10
print(hasil)
type(hasil)

nilai = input("Masukkan nilai : ")
nilai = float(nilai)
hasil = nilai + 10
print(hasil)

type(hasil)

print("*" * 40)
print("Aplikasi Penghitung Luas Lingkaran")
print("*" * 40)

nama = input("Tulis Nama Anda: ")
jari = input("Masukkan jari-jari lingkaran: ")
luas = 3.14 * float(jari) * float(jari)

print("*" * 40)
print("Halo! Ini adalah luas lingkaranmu, ", nama)
print("Luas Lingkaran = ", luas)
print("*" * 40)

angka1 = 10
angka2 = 20

print(angka1 is not angka2)