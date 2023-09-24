basis = input('Masukan basis bilangan: ')
digit = input('Masukan panjang digit: ')
n = int(basis) # Konversi str ke int
d = int(digit)
a = [0 for i in range(d)] # Memasukan nilai default array
hasil = 0

for i in range(d):
  a[i] = input(f"Masukan nilai digit ke-{i+1}: ")
  a[i] = int(a[i]) # konversi nilai array str ke int

for i in range(d):
  hasil = a[i] + hasil * n # operasi konversi sistem bilangan

print(f"Hasil konversi ke bilangan desimal: {hasil}")

