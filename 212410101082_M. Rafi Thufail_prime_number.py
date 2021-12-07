nama = 'M. Rafi Thufail'
nim = 212410101082
print('Nama : ' + (nama))
print('NIM  : ' + str(nim))

nomer = int(input('Masukkan angka dari 2 - 30 : '))

if nomer > 1 and nomer <= 30: 
    if (nomer == 2 or nomer == 3 or nomer == 5 or nomer == 7) or (nomer % 2 != 0 and nomer % 3 != 0 and nomer % 5 != 0 and nomer % 7 != 0):
        print('PRIME')
    else:
        print('NOT PRIME')
else:
    print('Masukkan angka saja kurang dari 30')