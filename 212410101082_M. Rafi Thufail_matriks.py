matrik_a = [
    [1, 3],
    [7, 9],
    [2, 3]
]
matriks_b = [
    [1, 2],
    [4, 5],
    [3, 2]
]

matriks_kali = []
#baris
for a in range(len(matrik_a)):
    baris_matriks = []
    #kolom
    for b in range(len(matriks_b[0])):
        jawab = 0
        for c in range(len(matrik_a[a])):
            jawab += matrik_a[a][c] * matriks_b[c][b]
        baris_matriks.append(jawab)
    matriks_kali.append(baris_matriks)

print('Hasil perkalian matrik 3 x 2:')
for baris_matriks in matriks_kali :
    print(baris_matriks)