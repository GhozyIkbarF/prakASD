##a = ([5,3,2], [1,6,2], [3,9,6])
##b = ([23,2,5], [6,2,4], [3,8,4])
##c = ([2,3,1], [1,9,"5"])
##
#### NOMER 1a
##print('no 1a memastikan isi dan ukuran matrixnya konsisten')
##def cekMatrix(x):
##    baris = len(x)
##    kolom = len(x[0])
##    if kolom == baris:
##        print("ukuran kolom sama dengan ukuran baris")
##    else:
##        print("ukuran kolom tidak sama dengan ukuran baris")
##    for i in x:
##        for j in i:
##            if type(j) != int:
##                return False
##    return True
##print(cekMatrix(b))
##print(cekMatrix(c))
##
#### NOMER 1b
##print('')
##print('no 1b mengambil ukuran matrixnya')
##def ukuran(x):
##    kolom = len(x[0])
##    baris = len(x)
##    return "ordo "+str(kolom)+"x"+str(baris)
##print(ukuran(a))
##
#### NOMER 1c
##print('')
##print('no 1c menjumlahkan 2 matrix')
##def jumlah(m1, m2):
##    kolom = len(m1[0])
##    baris = len(m1)
##    Z = [[0 for x in range(kolom)] for y in range(baris)]
##    for i in range(baris):
##        for j in range(kolom):
##            Z[i][j] = m1[i][j] + m2[i][j]
##    return Z
##print(jumlah(a,b))#penjumlahan matrix
##
#### NOMER 1d
##print('')
##print('no 1d mengalikan 2 matrix')
##def kali(m1, m2):
##    kolom = len(m1[0])
##    baris = len(m1)
##    m3 = []
##    Z = [[0 for x in range(kolom)] for y in range(baris)]
##    for x in range(len(m1)):
##        row = []
##        for y in range(len(m1[0])):
##            total = 0
##            for z in range(len(m1)):
##                total = total + (m1[x][z]*m2[z][y])
##            row.append(total)
##        m3.append(row)
##    for x in range(len(m3)):
##        for y in range(len(m3[0])):
##            Z[x][y] = m3[x][y]
##    return Z
##print(kali(a,b))#perkalian matrix
##
#### NOMER 1e
##print('')
##print('no 1e menghitung determinan sebuah matrix bujursangkar')
##def determinan(x):
##    kolom = len(x[0])
##    baris = len(x)
##    for i in range(2):
##        if i == 0:
##            ad = x[i][i]*x[i+1][i+1]
##        elif i == 1:
##            bc = x[i-1][i]*x[i][i-1]
##    return ad-bc
##print(determinan(b))#menghitung determinan sebuah matrix bujursangkar
##
#### NOMER 2a
##print('')
##print('no 2a' )
##def buatNol(m):
##    'Masukkan ukuran'
##    matriks = [[0 for j in range(m)] for i in range(m)]
##    for baris in matriks:
##        print (baris)
##    print ("Matriks nol ber-ordo",m,'x',m)
##print(buatNol(3))
##def BuatNol(m, n):
##    'm nilai kolom dan n nilai baris'
##    matriks = [[0 for j in range(m)] for i in range(n)]
##    for baris in matriks:
##        print (baris)
##    print ("Matriks nol ber-ordo",m,'x',n)
##print(BuatNol(1,2))
##
#### NOMER 2b
##print('')
##print('no 2b')
##def buatIdentitas(m):
##    'Masukkan Ukuran'
##    matrix = [[1 if j == i else 0 for j in range(m)] for i in range(m)]
##    for baris in matrix:
##        print (baris)
##    print ("Matriks identitas ber ordo",m,'x',m)
##print(buatIdentitas(3))

#### NOMER 3a
##print('')
##print('no 3a')
##class tugasLink(object):
##    def __init__(self, nama, next = None):
##        self.data = nama
##        self.next = next
##def cari(x, y):
##    if y == 1:
##        print (x.data)
##    elif y == 2:
##        print (x.next.data)
##    elif y == 3:
##        print (x.next.next.data)
##    elif y == 4:
##        print (x.next.next.next.data)
##    else:
##        print ("data tidak tersedia")
##a = tugasLink(11)
##b = tugasLink(21)
##c = tugasLink(31)
##d = tugasLink(41)
##a.next = b
##b.next = c
##c.next = d
##print ("Headnya a")
##print("(a, (urutan data yg dicari))")
##print(cari(a,3))
##
####NOMER 3b
##print('')
##print('no 3b')
##class tgsLink2(object):
##    def __init__(self, nama, next = None):
##        self.data = nama
##        self.next = next
##def tambahDepan():
##    print ("Simpul Awal")
##    print (a.data)
##    print (a.next.data)
##    print (a.next.next.data)
##    print (a.next.next.next.data)
##    l = input("Masukkan nilai tambahan untuk simpul depan :")
##    L = tgsLink2(l)
##    L.next = a
##    w = a
##    print (L.data)
##    print (L.next.data)
##    print (L.next.next.data)
##    print (L.next.next.next.data)
##    print (L.next.next.next.next.data)
##a = tgsLink2(4)
##b = tgsLink2(5)
##c = tgsLink2(6)
##d = tgsLink2(7)
##a.next = b
##b.next = c
##c.next = d
##print(tambahDepan())
##
####NOMER 3c
##print('')
##print('no  3c')
##class tgsLink3(object):
##    def __init__(self, nama, next = None):
##        self.data = nama
##        self.next = next
##def tambahAkhir():
##    a = tgsLink3(12)
##    b = tgsLink3(13)
##    c = tgsLink3(14)
##    d = tgsLink3(15)
##    a.next = b
##    b.next = c
##    c.next = d
##    print ("Simpul Awal")
##    print (a.data)
##    print (a.next.data)
##    print (a.next.next.data)
##    print (a.next.next.next.data)
##    l = input("Masukkan nilai tambahan untuk simpul diakhir :")
##    a = tgsLink3(11)
##    b = tgsLink3(12)
##    c = tgsLink3(13)
##    d = tgsLink3(14)
##    L = tgsLink3(l)
##    a.next = b
##    b.next = c
##    c.next = d
##    d.next = L
##    print (a.data)
##    print (a.next.data)
##    print (a.next.next.data)
##    print (a.next.next.next.data)
##    print (a.next.next.next.next.data)
##print(tambahAkhir())
##
#### NOMER 3d
##print('')
##print('no 3d')
##class tgsLink4(object):
##    def __init__(self, nama, next = None):
##        self.data = nama
##        self.next = next
##a = tgsLink4(5)
##b = tgsLink4(6)
##c = tgsLink4(7)
##d = tgsLink4(8)
##a.next = b
##b.next = c
##c.next = d
##print ("Simpul Awal")
##print (a.data)
##print (a.next.data)
##print (a.next.next.data)
##print (a.next.next.next.data)
##def tambah(posisi):
##    l = input("Masukkan nilai tambahan untuk simpul awal:")
##    a = tgsLink4(5)
##    b = tgsLink4(6)
##    c = tgsLink4(7)
##    d = tgsLink4(8)
##    L = tgsLink4(l)
##    if posisi == "awal":
##        L.next = a
##        a.next = b
##        b.next = c
##        c.next = d
##        print (L.data)
##        print (L.next.data)
##        print (L.next.next.data)
##        print (L.next.next.next.data)
##        print (L.next.next.next.next.data)
##print(tambah("awal"))
##
#### NOMER 3e
##print('')
##print('no 3e')
##print ("Simpul Awal")
##print (a.data)
##print (a.next.data)
##print (a.next.next.data)
##print (a.next.next.next.data)
##def hapus():
##    q = str(input('pilih bagian yang ingin di hapus:'))
##    a = tgsLink4(5)
##    b = tgsLink4(6)
##    c = tgsLink4(7)
##    d = tgsLink4(8)
##    if q == "awal":
##        b.next = c
##        c.next = d
##        print (b.data)
##        print (b.next.data)
##        print (b.next.next.data)
##    elif q == "tengah":
##        a.next = c
##        c.next = d
##        print (a.data)
##        print (a.next.data)
##        print (a.next.next.data)
##    elif q == "akhir":
##        a.next = b
##        b.next = c
##        print (a.data)
##        print (a.next.data)
##        print (a.next.next.data)
##print(hapus())#menghapus nilai 

## NOMER 4a
print('')
print('no 4a')
class Linked(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
a = Linked(15)
b = Linked(16)
c = Linked(17)
d = Linked(18)
print ("Simpul Awal")
print (a.data)
print (b.data)
print (c.data)
print (d.data)
print('')
print('mencetak dari depan')
def cetak_depan():
    a.next = b
    b.next = c
    c.next = d
    print (a.data)
    print (a.next.data)
    print (a.next.next.data)
    print (a.next.next.next.data)
print(cetak_depan())
print('')
print('mencetak dari belakang')
def cetak_belakang():
    d.prev = c
    c.prev = b
    b.prev = a
    print (d.data)
    print (d.prev.data)
    print (d.prev.prev.data)
    print (d.prev.prev.prev.data)
print(cetak_belakang())

##NOMER 4b
print('')
print('no 4b')
def tambahAwal():
    a.next = b
    b.next = c
    c.next = d
    l = input("Masukkan tambahan di awal:")
    L = Linked(l)
    L.next = a
    print (L.data)
    print (L.next.data)
    print (L.next.next.data)
    print (L.next.next.next.data)
    print (L.next.next.next.next.data)
print(tambahAwal())

##NOMER 4c
print('')
print('no 4c')
def tambahAkhir():
    k = input("Masukkan tambahan di akhir:")
    a = Linked(15)
    b = Linked(16)
    c = Linked(17)
    d = Linked(18)
    K = Linked(k)
    d.prev = c
    c.prev = b
    b.prev = a
    K.prev = d
    print (K.prev.prev.prev.prev.data)
    print (K.prev.prev.prev.data)
    print (K.prev.prev.data)
    print (K.prev.data)
    print (K.data)
print(tambahAkhir())
