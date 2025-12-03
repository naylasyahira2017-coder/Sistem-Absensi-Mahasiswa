nama_toko = "TOKO MAKMUR JAYA"
print(f"===== SISTEM PENDATAAN {nama_toko} =====")

barang_list = [
    {"nama": "Mie Instan", "harga": 3000, "stok": 20},
    {"nama": "Gula", "harga": 12000, "stok": 10},
    {"nama": "Beras", "harga": 50000, "stok": 5},
    {"nama": "Teh Celup", "harga": 7000, "stok": 15},
]

def tampilkan_barang():
    print(f"\n===== DATA BARANG {nama_toko} =====")
    print("| KODE |    NAMA BARANG    |  HARGA  | STOK |")
    print("---------------------------------------------")
    for i, b in enumerate(barang_list, start=1):
        print(f"| {i:<4}| {b['nama']:<17}| Rp.{b['harga']:<6}| {b['stok']:<4}|")
    print("---------------------------------------------\n")

def tambah_barang():
    print("\n=== TAMBAH BARANG ===")
    nama = input("Nama barang : ").strip()
    harga = int(input("Harga      : "))
    stok = int(input("Stok        : "))
    barang_list.append({"nama": nama, "harga": harga, "stok": stok})
    print("Barang berhasil ditambahkan!\n")

def edit_barang():
    tampilkan_barang()
    kode = int(input("Masukkan kode barang yang ingin diedit: ")) - 1
    if 0 <= kode < len(barang_list):
        print("Kosongkan jika tidak ingin mengubah.")
        nama = input("Nama baru : ")
        harga = input("Harga baru: ")
        stok = input("Stok baru : ")
        if nama != "": barang_list[kode]["nama"] = nama
        if harga != "": barang_list[kode]["harga"] = int(harga)
        if stok != "": barang_list[kode]["stok"] = int(stok)
        print("Data barang berhasil diubah!\n")
    else:
        print("Kode tidak valid!\n")

def hapus_barang():
    tampilkan_barang()
    kode = int(input("Masukkan kode barang yang ingin dihapus: ")) - 1
    if 0 <= kode < len(barang_list):
        barang_list.pop(kode)
        print("Barang berhasil dihapus!\n")
    else:
        print("Kode tidak valid!\n")

def cari_barang():
    keyword = input("Masukkan kata kunci nama barang: ").lower()
    print("\n=== HASIL PENCARIAN ===")
    found = False
    for b in barang_list:
        if keyword in b["nama"].lower():
            print(f"- {b['nama']} | Harga: Rp.{b['harga']} | Stok: {b['stok']}")
            found = True
    if not found:
        print("Barang tidak ditemukan.\n")

while True:
    print(f"===== MENU {nama_toko} =====")
    print("1. Tampilkan Barang")
    print("2. Tambah Barang")
    print("3. Edit Barang")
    print("4. Hapus Barang")
    print("5. Cari Barang")
    print("6. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1": tampilkan_barang()
    elif pilihan == "2": tambah_barang()
    elif pilihan == "3": edit_barang()
    elif pilihan == "4": hapus_barang()
    elif pilihan == "5": cari_barang()
    elif pilihan == "6":
        print("Terima kasih telah menggunakan program!")
        break
    else:
        print("Pilihan tidak valid!\n")


