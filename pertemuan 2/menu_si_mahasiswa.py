"""Menu interaktif untuk tiga studi kasus Sistem Informasi Mahasiswa."""

from diskon_biaya import input_data_diskon, tampilkan_hasil_diskon
from peringatan_stok import tampilkan_laporan as tampilkan_laporan_stok
from status_mahasiswa import input_data_mahasiswa, tampilkan_laporan


def main() -> None:
    while True:
        print("\n=== MENU SISTEM INFORMASI MAHASISWA ===")
        print("1. Cek Status Mahasiswa")
        print("2. Hitung Diskon Biaya")
        print("3. Cek Peringatan Stok")
        print("0. Keluar")
        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            data = input_data_mahasiswa(5)
            tampilkan_laporan(data)
        elif pilihan == "2":
            tampilkan_hasil_diskon(*input_data_diskon())
        elif pilihan == "3":
            tampilkan_laporan_stok()
        elif pilihan == "0":
            print("Terima kasih. Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Masukkan 0, 1, 2, atau 3.")


if __name__ == "__main__":
    main()
