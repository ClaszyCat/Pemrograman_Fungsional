# Sistem Penilaian Akhir Mahasiswa

# Fungsi menghitung nilai akhir
def hitung_nilai_akhir(uts, uas):
    return (uts + uas) / 2

# Fungis menghitung nilai akhir semua mahasiswa


def hitung_semua_nilai_akhir(data_mahasiswa):
    data_nilai_akhir = {}
    for nama, nilai in data_mahasiswa.items():
        nilai_akhir = hitung_nilai_akhir(nilai['uts'], nilai['uas'])
        data_nilai_akhir[nama] = nilai_akhir
    return data_nilai_akhir


def tampilkan_nilai_akhir(data_nilai_akhir):
    print("Hasil Nilai Akhir Mahasiswa")
    for nama, nilai_akhir in data_nilai_akhir.items():
        print("Nama:{}\tNilai Akhir:{:.2f}".format(nama, nilai_akhir))


def main():
    data_mahasiswa = {
        'Yovi': {'uts': 90, 'uas': 80},
        'Iqbal': {'uts': 85, 'uas': 100},
        'Rizky': {'uts': 75, 'uas': 90},
        'Rafli': {'uts': 95,  'uas': 70},
    }

    data_nilai_akhir = hitung_semua_nilai_akhir(data_mahasiswa)

    tampilkan_nilai_akhir(data_nilai_akhir)


if __name__ == "__main__":
    main()
