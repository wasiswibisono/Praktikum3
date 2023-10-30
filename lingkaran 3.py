import math

# Masukan jari-jari lingkaran 
r = float(input("masukan jari-jari lingkaran: "))

# Hitung luas lingkaran
luas = math.pi * r**2

# Hitung keliling lingkaran
keliling = math.pi * r

# Tampilkan hasil
print(f"luas lingkaran: {luas:2f}")
print(f"Keliling lingkaran: {keliling:.2f}")