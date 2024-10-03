
class Perpustakaan : 
    def __init__(self):
        self.buku = []  
    
    def tambah_buku(self, judul, pengarang):
        buku_baru = {'judul': judul, 'pengarang': pengarang}
        self.buku.append(buku_baru)
        print(f"Buku '{judul}' oleh {pengarang} berhasil ditambahkan.")
    
    def tampilkan_buku(self):
        if not self.buku:
            print("Tidak ada buku di perpustakaan.")
        else:
            print("\nDaftar Buku di Perpustakaan:")
            for index, buku in enumerate(self.buku, start=1):
                print(f"{index}. {buku['judul']} oleh {buku['pengarang']}")
    
    def cari_buku(self, judul):
        for buku in self.buku:
            if buku['judul'].lower() == judul.lower():
                return buku
        return None

def tampilkan_menu():
    print("\n=== Menu Perpustakaan ===")
    print("1. Tambah Buku")
    print("2. Lihat Daftar Buku")
    print("3. Cari Buku")
    print("4. Keluar")

def ambil_input():
    pilihan = input("Pilih menu: ")
    return pilihan


def main():
    perpustakaan = Perpustakaan()  
    
    while True:
        tampilkan_menu()  
        pilihan = ambil_input()  
        
        if pilihan == "1": 
            judul = input("Masukkan judul buku: ")
            pengarang = input("Masukkan nama pengarang: ")
            perpustakaan.tambah_buku(judul, pengarang)
        
        elif pilihan == "2":  
            perpustakaan.tampilkan_buku()
        
        elif pilihan == "3":  
            judul_cari = input("Masukkan judul buku yang ingin dicari: ")
            hasil = perpustakaan.cari_buku(judul_cari)
            if hasil:
                print(f"Buku ditemukan: '{hasil['judul']}' oleh {hasil['pengarang']}")
            else:
                print(f"Buku dengan judul '{judul_cari}' tidak ditemukan.")
        
        elif pilihan == "4":  
            print("Terima kasih telah menggunakan sistem perpustakaan.")
            break
        
        else:
            print("Pilihan tidak valid, silakan coba lagi.")


main()

