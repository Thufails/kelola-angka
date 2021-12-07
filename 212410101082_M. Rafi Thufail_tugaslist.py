print('================================================================================================================')
negara = ['indonesia','denmark','amerika','chili','ekuador','hungaria','jepang','bangladesh','filipina','ghana']
print(negara)
print('================================================================================================================')

print('A. Tambahkan Negara' )
print('B. Hapus Negara')
choice = input('pilihlah A atau B : ')
print('\n')

if choice.lower != 'a' or choice.lower != 'b':
    print('Pilih sesuai ketentuan')
elif choice.lower() == 'a':
    print('Anda Memilih Menambahkan Negara')
    tambah = input('Tuliskan Negara yang ingin ditambahkan : ')
    print(tambah, 'Berhasil ditambahkan')
    negara.append(tambah)
    print('sehingga menjadi', negara)
    print('\n')
    for a in range(len(negara)):
        for b in range(len(negara)):
            if a >= b:
                continue
            if negara[a] > negara[b]:
                c = negara[a]
                negara[a] = negara [b]
                negara[b] = c
    print('Urutan Negara berdasarkan abjadnya')
    print(negara)
    print('\n')
    for a in range(0, len(negara)):
        for b in range(a+1, len(negara)):
            if len(negara[a]) > len(negara[b]):
                c = negara[a]
                negara[a] = negara [b]
                negara[b] = c
    print('Urutan Negara berdasarkan panjang string')
    print(negara)

elif choice.lower() == 'b':
    print('Anda Memilih Menghapus Negara')
    hapus = input('Tuliskan Negara yang ingin anda hapus dari list : ')
    if hapus in negara:
       print(hapus, 'Berhasil dihapus')
       negara.remove(hapus)
       print('sehingga menjadi', negara)
       print('\n')
       for a in range(len(negara)):
            for b in range(len(negara)):
                if a >= b:
                    continue
                if negara[a] > negara[b]:
                    c = negara[a]
                    negara[a] = negara [b]
                    negara[b] = c
    print('Urutan Negara berdasarkan abjadnya')
    print(negara)
    print('\n')
    for a in range(0, len(negara)):
        for b in range(a+1, len(negara)):
            if len(negara[a]) > len(negara[b]):
                c = negara[a]
                negara[a] = negara [b]
                negara[b] = c
    print('Urutan Negara berdasarkan panjang string')
    print(negara)
    