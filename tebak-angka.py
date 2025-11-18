import random
import time

a = random.randint(1, 100)
b = int(input("Tebak angkanya (1-100): "))

while b != a: 
    if b > a:
        print("Angka kamu", b, "- terlalu besar!")
    elif b < a:
        print("Angka kamu", b, "- terlalu kecil!")
    
    time.sleep(1)
    b = int(input("Coba lagi: "))

print("Selamat! Angka yang benar adalah", a)
