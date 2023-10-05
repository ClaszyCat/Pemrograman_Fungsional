book_data = {}
peminjaman = {}


def add_buku():
    judul = input("Title: ")
    penulis = input("Author: ")
    bidang = input("Genre: ")

    book_id = len(book_data) + 1

    book_data[book_id] = {"Title": judul, "Author": penulis, "Genre": bidang }
    print(f"Buku dengan ID {book_id} Berhasil ditambahkan.")


def pinjam_buku():
    tampilkan_daftar_buku()
    id_buku = int(input("Masukkan ID buku yang ingin dipinjam: "))
    nama_peminjam = input("Masukkan nama Anda: ")      

    if id_buku in book_data:
        title = book_data[id_buku]["Title"]
        if id_buku in peminjaman: 
            print(f"Buku dengan ID {id_buku} Telah dipinjam oleh {peminjaman[id_buku]['Peminjam']}.")
        else:
            peminjaman[id_buku] = {"Judul": title, "Peminjam": nama_peminjam}
            print(f"{title} telah dipinjam oleh {nama_peminjam}.")
    else:
        print("Buku dengan ID tersebut tidak ada.")

     

def pengembalian():
    nama_peminjam = input("Masukkan nama Anda: ")

#show the list books that someones borrow
    borrowed_books = [] 
    for id_buku, data in peminjaman.items():
        if data["Peminjam"] == nama_peminjam:
            borrowed_books.append({"ID Buku": id_buku, "Judul": data["Title"]})

    if len(borrowed_books) == 0:
        print("Tidak ada buku yang dipinjam oleh nama tersebut.")
    else:
        print(f"Buku telah dipinjam oleh {nama_peminjam}:")
        for buku in borrowed_books:
            print(f"ID: {buku['ID Buku']}, Judul: {buku['Title']}")

        id_buku_kembali = int(input("Inputkan ID Buku yang ingin dikembalikan :"))
        for buku in borrowed_books:
            if buku["ID Buku"] == id_buku_kembali:
                buku_ditemukan = True
                del peminjaman[id_buku_kembali]
                print(f"Buku dengan ID {id_buku_kembali} sudah dikembalikan.")
                break

        if not buku_ditemukan:
            print("Buku dengan ID tersebut tidak tersedia.")


def tampilkan_daftar_buku():
    print("\nDaftar Buku:")
    if not book_data:
        print("Tidak ada buku disini!")
        
    else :
        for id_buku, buku_info in book_data.items():
            print(f"ID: {id_buku}, Judul: {buku_info['Title']}, Penulis: {buku_info['Author']}, Genre: {buku_info['Genre']}")
while True:
    print("\n1. Login sebagai admin")
    print("2. Login sebagai user")
    print("3. Keluar")

    choose_login = input("Pilihan Anda: ")

    if choose_login == "1":
        print("\nHai Admin!")
        print("1. Tambah buku")
        print("2. List buku yang tersedia")

        admin_choose = input("Pilihan Anda: ")
        if admin_choose == "1":
            add_buku()
        elif admin_choose == "2":
            tampilkan_daftar_buku()

    elif choose_login == "2":
        print("\nSelamat datang di Perpustakaan UMM!")
        print("Apa yang ingin Anda lakukan?")
        print("1. Melihat daftar buku yang tersedia")
        print("2. Mengembalikan Buku")
        print("3. Pinjam Buku")
        choose = input("Saya ingin: ")

        if choose == "1":
            tampilkan_daftar_buku()
        elif choose == "2":
            pengembalian()
        elif choose == "3":
            pinjam_buku()

    elif choose_login == "3":
            break
        
