# PROGRAM RENTAL MOBIL

# Dict List Data Rental Mobil
dictMobil = {
    'CAR001': ['Toyota Avanza', 'Bensin', 'AT', 7, 5, 350000],
    'CAR002': ['Honda Brio', 'Bensin', 'MT', 5, 3, 275000],
    'CAR003': ['Hyundai Ioniq', 'Listrik', 'AT', 5, 2, 650000],
    'CAR004': ['Wuling Air Ev', 'Listrik', 'AT', 8, 4, 250000],
    'CAR005': ['Daihatsu Xenia', 'Bensin', 'MT', 7, 3, 325000]
}

# Def Function Program
def tampilData():
    if len(dictMobil) == 0:
        print("\nData tidak tersedia!")
        return
    print("\n" + "=" * 102)
    print(f"| {'Kode':<8} | {'Nama Mobil':<21} | {'Bahan Bakar':<12} | {'Transmisi':<11} | {'Kapasitas':<10} | {'Stok':<6} | {'Harga/Hari':<12} |")
    print("=" * 102)
    for kode in sorted(dictMobil):
        data = dictMobil[kode]
        harga = f"Rp{data[5]:,}"
        print(f"| {kode:<8} | {data[0]:<21} | {data[1]:<12} | {data[2]:<11} | {data[3]:<10} | {data[4]:<6} | {harga:<12} |")
    print("=" * 102)

def tampilHeader():
    print("=" * 102)
    print(f"| {'Kode':<8} | {'Nama Mobil':<21} | {'Bahan Bakar':<12} | {'Transmisi':<11} | {'Kapasitas':<10} | {'Stok':<6} | {'Harga/Hari':<12} |")
    print("=" * 102)

def generateKode():
    nomor = 1
    while True:
        if nomor < 10:
            kode = "CAR00" + str(nomor)
        elif nomor < 100:
            kode = "CAR0" + str(nomor)
        else:
            kode = "CAR" + str(nomor)
        if kode not in dictMobil:
            return kode
        nomor += 1

def validBahanBakar():
    while True:
        bahanBakar = input("Masukkan Bahan Bakar (Bensin/Listrik): ").title()
        if bahanBakar in ['Bensin', 'Listrik']:
            return bahanBakar
        print("Jenis bahan bakar tidak valid!")

def validTransmisi():
    while True:
        transmisi = input("Masukkan Transmisi (AT/MT): ").upper()
        if transmisi in ['AT', 'MT']:
            return transmisi
        print("Transmisi tidak valid!")

def inputAngka(pesan):
    while True:
        nilai = input(pesan)
        if nilai.isdigit():
            return int(nilai)
        else:
            print("Input tidak valid! Harus berupa angka tanpa koma atau tanpa titik!")

def menuRead():
    while True:
        pilih = input("""
------ TAMPILKAN DATA MOBIL ------
1. Tampilkan Seluruh Data Rental
2. Cari/Filter Data Rental
3. Kembali
----------------------------------
Pilih Angka: """)
        if pilih == '1':
            tampilData()
        elif pilih == '2':
            if len(dictMobil) == 0:
                print("Data tidak tersedia!")
                continue
            filterMenu = input("""
----- CARI/FILTER DATA -----
1. Bahan Bakar
2. Transmisi
3. Harga Maksimum
4. Kembali
------------------------------
Pilih Angka: """)
            ditemukan = False
            if filterMenu == '1':
                bahanBakar = input("Masukkan Jenis Bahan Bakar (Bensin/Listrik): ").title()
                tampilHeader()
                for kode, data in dictMobil.items():
                    if data[1] == bahanBakar:
                        harga = f"Rp{data[5]:,}"
                        print(f"| {kode:<8} | {data[0]:<21} | {data[1]:<12} | {data[2]:<11} | {data[3]:<10} | {data[4]:<6} | {harga:<12} |")
                        ditemukan = True
                if ditemukan:
                    print("=" * 102)

            elif filterMenu == '2':
                transmisi = input("Masukkan Transmisi (AT/MT): ").upper()
                tampilHeader()
                for kode, data in dictMobil.items():
                    if data[2] == transmisi:
                        harga = f"Rp{data[5]:,}"
                        print(f"| {kode:<8} | {data[0]:<21} | {data[1]:<12} | {data[2]:<11} | {data[3]:<10} | {data[4]:<6} | {harga:<12} |")
                        ditemukan = True
                if ditemukan:
                    print("=" * 102)

            elif filterMenu == '3':
                hargaMax = inputAngka("Masukkan Harga Maksimum (contoh: 250000): ")
                tampilHeader()
                for kode, data in dictMobil.items():
                    if data[5] <= hargaMax:
                        harga_tampil = f"Rp{data[5]:,}"
                        print(f"| {kode:<8} | {data[0]:<21} | {data[1]:<12} | {data[2]:<11} | {data[3]:<10} | {data[4]:<6} | {harga_tampil:<12} |")
                        ditemukan = True
                if ditemukan:
                    print("=" * 102)

            elif filterMenu == '4':
                continue

            else:
                print("Pilihan tidak ada pada menu!")
                continue

            if ditemukan == False:
                print("Data tidak tersedia!")

        elif pilih == '3':
            break
        else:
            print("Pilihan tidak ada pada menu!")

def menuCreate():
    while True:
        pilih = input("""
--- TAMBAH DATA RENTAL ---
1. Buat Data Baru
2. Kembali
--------------------------
Pilih Angka: """)
        if pilih == '1':
            print("\nKetersediaan Data Rental")
            tampilData()
            kode = generateKode()
            nama = input("Nama Mobil Baru: ").title()
            sudahAda = False
            for data in dictMobil.values():
                if data[0].lower() == nama.lower():
                    sudahAda = True
                    break
            if sudahAda:
                print("\n== !Data mobil sudah tersedia! ==")
                continue
            bahanBakar = validBahanBakar()
            transmisi = validTransmisi()
            kapasitas = inputAngka("Kapasitas Penumpang: ")
            stok = inputAngka("Jumlah Stok: ")
            harga = inputAngka("Harga per Hari (Contoh: 300000): ")
            print("\n=== PREVIEW DATA ===")
            print("Kode        :", kode)
            print("Nama        :", nama)
            print("Bahan Bakar :", bahanBakar)
            print("Transmisi   :", transmisi)
            print("Kapasitas   :", kapasitas)
            print("Stok        :", stok)
            print("Harga       :", harga)

            while True:
                konfirmasi = input("\nSimpan Data Baru? (Y/N): ").upper()
                if konfirmasi == 'Y':
                    dictMobil[kode] = [nama, bahanBakar, transmisi, kapasitas, stok, harga]
                    print("\nData baru berhasil ditambahkan!")
                    tampilData()
                    break
                elif konfirmasi == 'N':
                    print("\nData baru batal ditambahkan!")
                    break
                else:
                    print("Input tidak valid! Masukkan hanya Y atau N")
            if konfirmasi == 'N':
                continue

        elif pilih == '2':
            break

        else:
            print("Pilihan tidak ada pada menu!")

def menuUpdate():
    while True:
        pilih = input("""
--- EDIT DATA RENTAL ---
1. Edit Data
2. Kembali
------------------------
Pilih Angka: """)
        if pilih == '1':
            tampilData()
            kode = input("Masukkan Kode Mobil: ").upper()
            if kode not in dictMobil:
                print("Data yang dicari tidak ada!")
                continue
            print("\nData ditemukan:")
            print("\n=== DATA YANG AKAN DIEDIT ===")
            print(f"Kode         : {kode}")
            print(f"Nama Mobil   : {dictMobil[kode][0]}")
            print(f"Bahan Bakar  : {dictMobil[kode][1]}")
            print(f"Transmisi    : {dictMobil[kode][2]}")
            print(f"Kapasitas    : {dictMobil[kode][3]}")
            print(f"Stok         : {dictMobil[kode][4]}")
            print(f"Harga/Hari   : {dictMobil[kode][5]}")

            while True:
                konfirmasi = input("\nApakah Data Ingin Diedit? (Y/N): ").upper()
                if konfirmasi == 'Y':
                    break
                elif konfirmasi == 'N':
                    print("Data batal diedit!")
                    break
                else:
                    print("Input tidak valid! Masukkan hanya Y atau N")
            if konfirmasi == 'N':
                continue

            pilihKolom = input("""
---------------------
1. Nama Mobil
2. Bahan Bakar
3. Transmisi
4. Kapasitas
5. Stok
6. Harga
7. Edit Seluruh Data
8. Kembali
---------------------
Pilih Angka: """)
            if pilihKolom == '1':
                dictMobil[kode][0] = input("Nama Baru: ").title()
            elif pilihKolom == '2':
                dictMobil[kode][1] = validBahanBakar()
            elif pilihKolom == '3':
                dictMobil[kode][2] = validTransmisi()
            elif pilihKolom == '4':
                dictMobil[kode][3] = inputAngka("Kapasitas Baru: ")
            elif pilihKolom == '5':
                dictMobil[kode][4] = inputAngka("Stok Baru: ")
            elif pilihKolom == '6':
                dictMobil[kode][5] = inputAngka("Harga Baru: ")
            elif pilihKolom == '7':
                namaBaru = input("Nama Mobil Baru: ").title()
                bahanBakarBaru = validBahanBakar()
                transmisiBaru = validTransmisi()
                kapasitasBaru = inputAngka("Kapasitas Baru: ")
                stokBaru = inputAngka("Stok Baru: ")
                hargaBaru = inputAngka("Harga Baru: ")
                dictMobil[kode] = [namaBaru, bahanBakarBaru, transmisiBaru, kapasitasBaru, stokBaru, hargaBaru]
            elif pilihKolom == '8':
                print("Kembali ke menu edit data...")
                continue
            else:
                print("Pilihan tidak ada pada menu!")
                continue

            print("\n===Data berhasil diedit!===")
            print(f"Kode         : {kode}")
            print(f"Nama Mobil   : {dictMobil[kode][0]}")
            print(f"Bahan Bakar  : {dictMobil[kode][1]}")
            print(f"Transmisi    : {dictMobil[kode][2]}")
            print(f"Kapasitas    : {dictMobil[kode][3]}")
            print(f"Stok         : {dictMobil[kode][4]}")
            print(f"Harga/Hari   : {dictMobil[kode][5]}")

        elif pilih == '2':
            break
        else:
            print("Pilihan tidak ada pada menu!")

def menuDelete():
    while True:
        pilih = input("""
--- HAPUS DATA MOBIL ---
1. Hapus Data
2. Kembali
------------------------
Pilih: """)
        if pilih == '1':
            tampilData()
            kode = input("Masukkan kode mobil yang ingin dihapus: ").upper()
            if kode not in dictMobil:
                print("Data yang kamu cari tidak ada!")
                continue
            print("\nData ditemukan:")
            print(f"Kode         : {kode}")
            print(f"Nama Mobil   : {dictMobil[kode][0]}")
            print(f"Bahan Bakar  : {dictMobil[kode][1]}")
            print(f"Transmisi    : {dictMobil[kode][2]}")
            print(f"Kapasitas    : {dictMobil[kode][3]}")
            print(f"Stok         : {dictMobil[kode][4]}")
            print(f"Harga/Hari   : {dictMobil[kode][5]}")

            while True:
                konfirmasi = input("Yakin ingin menghapus data? (Y/N): ").upper()
                if konfirmasi == 'Y':
                    del dictMobil[kode]
                    print("\nData berhasil dihapus!")
                    tampilData()
                    break
                elif konfirmasi == 'N':
                    print("\nData batal dihapus!")
                    tampilData()
                    break
                else:
                    print("Input tidak valid! Masukkan hanya Y atau N")

        elif pilih == '2':
            break
        else:
            print("Pilihan tidak ada pada menu!")

def menuBooking():
    while True:
        pilih = input("""
---- BOOKING MOBIL ----
1. Proses Booking Mobil
2. Kembali ke Menu Utama
-----------------------
Pilih: """)
        if pilih == '1':
            cart = prosesBooking()
            prosesPembayaran(cart)
        elif pilih == '2':
            break
        else:
            print("Pilihan tidak ada pada menu!")

def prosesBooking():
    if len(dictMobil) == 0:
        print("Data tidak tersedia!")
        return []
    
    cart = []

    while True:
        tampilData()
        kode = input("Masukkan Kode Mobil: ").upper()
        if kode not in dictMobil:
            print("Kode mobil tidak ditemukan!")
            continue

        jumlah = inputAngka("Jumlah Mobil: ")

        sudahDipesan = 0

        for item in cart:
            if item[0] == kode:
                sudahDipesan += item[2]

        stokTersedia = dictMobil[kode][4] - sudahDipesan

        if jumlah > stokTersedia:
            print("\nStok Melebihi Batas!")
            print(f"Mobil ini sudah ada {sudahDipesan} unit di cart.")
            print(f"Sisa stok yang dapat dipesan hanya {stokTersedia} unit.")
            continue
    
        hari = inputAngka("Lama Sewa (Hari): ")

        subtotal = dictMobil[kode][5] * jumlah * hari

        cart.append([kode,
                     dictMobil[kode][0],
                     jumlah,
                     hari,
                     subtotal])
        
        tampilCart(cart)

        while True:
            lagi = input("Tambah booking mobil lagi? (Y/N): ").upper()
            if lagi == 'Y':
                break
            elif lagi == 'N':
                print("\nLanjut ke pembayaran...")
                return cart
            else:
                print("Input tidak valid! Masukkan Y atau N")

def prosesPembayaran(cart):
    if len(cart) == 0:
        print("Belum ada mobil yang dibooking!")
        return

    total = 0

    print("\n" + "=" * 45)
    print("STRUK BOOKING")
    print("=" * 45)

    for item in cart:
        print(f"\n{item[1]}")
        print(f"Kode Mobil    : {item[0]}")
        print(f"Nama Mobil    : {item[1]}")
        print(f"Jumlah Mobil  : {item[2]}")
        print(f"Lama Sewa     : {item[3]} Hari")
        print(f"Subtotal      : Rp{item[4]:,}")
        total += item[4]

    print("-" * 45)
    print(f"TOTAL BAYAR : Rp{total:,}")
    print("=" * 45)

    while True:
        bayar = inputAngka("\nMasukkan Uang Pembayaran contoh(100000): ")

        if bayar < total:
            kurang = total - bayar
            print(f"Uang kurang Rp{kurang:,}")
            print("Silahkan masukkan uang kembali!")
        else:
            kembalian = bayar - total
            print(f"Kembalian : Rp{kembalian:,}")
            for item in cart:
                kode = item[0]
                jumlah = item[2]
                dictMobil[kode][4] -= jumlah
            print("\nTerima kasih telah booking mobil di City Auto Rent!!!")
            break
        
    while True:
        pilih = input("""
1. Kembali ke Menu Booking
2. Exit
Pilih: """)
        if pilih == '1':
            return
        elif pilih == '2':
            print("Anda telah keluar... Terima kasih!")
            exit()
        else:
            print("Pilihan tidak ada pada menu!")

def tampilCart(cart):
    if len(cart) == 0:
        print("Keranjang masih kosong!")
        return
    print("\n" + "=" * 76)
    print(f"| {'Kode':<8} | {'Nama Mobil':<21} | {'Jumlah':<10} | {'Hari':<6} | {'Subtotal':<15} |")
    print("=" * 76)

    total = 0

    for item in cart:
        print(f"| {item[0]:<8} | {item[1]:<21} | {item[2]:<10} | {item[3]:<6} | Rp{item[4]:<13,} |")
        total += item[4]

    print("=" * 76)
    print(f"Total Sementara : Rp{total:,}")

# MENU UTAMA
while True:
    menu = input("""
======== CITY AUTO RENT ========
---------- Menu Utama ----------
1. Tampilkan Data Mobil Rental
2. Tambahkan Data Rental
3. Edit Data Rental
4. Hapus Data Mobil
5. Booking Mobil
6. Exit
--------------------------------
Pilih Angka Menu: """)
    if menu == '1':
        menuRead()
    elif menu == '2':
        menuCreate()
    elif menu == '3':
        menuUpdate()
    elif menu == '4':
        menuDelete()
    elif menu == '5':
        menuBooking()
    elif menu == '6':
        print("Anda telah keluar... Terima kasih!")
        break
    else:
        print("Pilihan tidak ada pada menu utama!")