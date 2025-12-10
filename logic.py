from database import data

keranjang = []

def daftar():
    print("\n===== DAFTAR BARANG =====")
    print("Kode   Nama                 Harga     Stok")
    print("============================================")
    for kode, item in data.items():
        print(f"{kode:<6} {item['nama']:<20} {item['harga']:<8} {item['stok']}")
    print("============================================")

def tambah(kode, qty):
    kode = kode.upper()
    if kode not in data:
        print("Kode Tidak ditemukan !!")
        return False
    
    if data[kode]["stok"] < qty:
        print("Stok tidak cukup")
        return False
    
    keranjang.append({
        "kode": kode,
        "nama":data[kode]["nama"],
        "harga":data[kode]["harga"],
        "qty": qty
    })
    return True

def cek():
    if not keranjang:
        print("Keranjang masih kosong !!")
        return
    print("\n===== ISI KERANJANG =====")
    for i, item in enumerate(keranjang, start=1):
        sub = item["harga"] * item["qty"]
        print(f"{i}. {item["nama"]} x {item["qty"]} = {sub}")
    print()
    
def checkout():
    if not keranjang:
        print("Keranjang masih kosong !!")
        return
    
    print("\n===== STRUK BELANJA =====")
    total = 0
    
    for item in keranjang:
        kode = item["kode"]
        qty = item["qty"]
        
        data[kode]['stok'] -= qty
        
        sub = item["harga"] * qty
        total += sub
        
        print(f"{item['nama']} X {qty} = {sub}")
    print("========================================")
    print(f"TOTAL BAYAR        =        {total:<15}")
    print("========================================\n")
    
    keranjang.clear()

def stok():
    print("================= DAFTAR STOK BARANG =================")
    for kode, barang in data.items():
        print(f"Kode   : {kode}")
        print(f"Nama   : {barang['nama']}")
        print(f"Stok   : {barang['stok']}")
        print(f"Harga  : {barang['harga']}")
        print("-------------------------------------------------------")

    
while True:
    print("===== CASSAVA STORE =====")
    print("1. TAMBAH BARANG")
    print("2. CEK KERANJANG")
    print("3. CHECKOUT")
    print("4. CEK KETERSEDIAAN")
    print("5. KELUAR")
    
    pilihan = input("Masukan perintah : ")
    
    if pilihan == "1":
        daftar()
        kode = input("Masukan kode barang : ").strip().upper()
        qty = int(input("Masukan jumlah barang : "))
        tambah(kode, qty)
    
    elif pilihan == "2":
        cek()
    elif pilihan == "3":
        checkout()
    elif pilihan == "4":
        stok()
    elif pilihan == "5":
        print("Terima kasih !!")
        break
    else:
        print("Plilihan tidak valid")
        
    input("\nENTER untuk kembali ke menu ....")