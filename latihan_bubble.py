#membuat garis
def garis():
    print("-------------------------------------")

#fungsi bubble sort ascending(dari kecil ke besar)
def sort_asc(array):
    n = len(array) # n itu jumlah list
    #perulangan pertama
    for i in range(n):
        #perulangan kedua
        for j in range (n-i-1):
            #bandingkan masing masing elemen ke kanan
            if array[j] > array [i]:
                #jika lebih besar tukar kekanan , swap
                array[j], array[j+1] = array[j+1], array[j]
    return array

#fungsi bubble sort descending (dari besar ke kecil)
def sort_dsc(array):
    n = len(array) # n itu jumlah list
    #perulangan pertama
    for i in range(n):
        #perulangan kedua
        for j in range (n-i-1):
            #bandingkan masing masing elemen ke kanan
            if array[j] < array [j+1]:
                #jika lebih kecil maka dia pindah , swap
                array[j], array[j+1] = array[j+1], array[j]
    return array

#fungsi rata-rata
def rata_rata(angka):
    return sum(angka) / len(angka)

#input masukan nilai
garis()
print("Masukkan nilai sebanyak yang kamu mau !")
print("contoh : 7 6 5 4 8 ")
angka = list(map(int, input("Masukkan Nilainya : ").split()))
garis()
print()

#input memilih pilihan asc dan dsc
garis()
print("Pilih Metodenya!")
print("Ascending = 1 | Descending = 2")
pilih = int(input("pilihan = "))

#menentukan nilai
if pilih == 1:
    print()
    print("HASIL AKHIR-------")
    print("Urutan angka Ascending ", (sort_asc(angka)))
else:
    print()
    print("HASIL AKHIR-------")
    print("Urutan angka Descending", (sort_dsc(angka)))

#cari angka terbesar
print("Angka Terbesar : ",max(angka))

#cari angka terkecil
print("Angka Terkecil : ",min(angka))

#jumlahkan angkanya
print("Jumlahnya : ",sum(angka))

#tampilkan rata rata
print("Rata - rata nya :",round(rata_rata(angka),2))
