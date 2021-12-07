nama = 'M. Rafi Thufail'
nim = 212410101082
print('Nama : ' + (nama))
print('NIM  : ' + str(nim))

nilai = float(input('Masukkan angka : '))

hasil = None 
if nilai <= 100 and nilai > 80:
    hasil = 'A'
elif nilai <= 80 and nilai >= 76:
    hasil = 'AB'
elif nilai <= 75 and nilai >= 71:
    hasil = 'B'
elif nilai <= 70 and nilai >= 66:
    hasil = 'BC'
elif nilai <=65 and nilai >= 56:
    hasil = 'C'
elif nilai <=55 and nilai >= 51:
    hasil = 'CD'
elif nilai <=50 and nilai > 45:
    hasil = 'D'
elif nilai <=45 and nilai >= 41:
    hasil = 'ED'
elif nilai <=40 and nilai >= 0:
    hasil = 'E'
else:
    print('Masukkan angka dibawah 100 saja!!!')
 
print('Nilai {} =  {}'.format(nilai, hasil))

