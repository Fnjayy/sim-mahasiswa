"""Program latihan string, list, set, dictionary, dan file."""

import math
import re
from pathlib import Path


def analisis_kalimat(kalimat: str) -> tuple[int, int, str, str]:
    """Kembalikan jumlah kata/karakter, kata terpanjang, dan title case."""
    kata = kalimat.split()
    kata_terpanjang = max(kata, key=len, default="")
    return len(kata), len(kalimat), kata_terpanjang, kalimat.title()


def kategori_nilai(nilai: float) -> str:
    """Kelompokkan nilai 0-100: A >=80, B >=70, C >=60, D >=50, selainnya E."""
    if nilai >= 80:
        return "A"
    if nilai >= 70:
        return "B"
    if nilai >= 60:
        return "C"
    if nilai >= 50:
        return "D"
    return "E"


def analisis_nilai(
    daftar_nilai: list[float],
) -> tuple[float, float, float, dict[str, list[float]], dict[str, int]]:
    """Hitung ringkasan nilai, pengelompokan kategori, dan frekuensinya."""
    if not daftar_nilai:
        raise ValueError("Daftar nilai tidak boleh kosong.")
    if any(
        not math.isfinite(nilai) or nilai < 0 or nilai > 100
        for nilai in daftar_nilai
    ):
        raise ValueError("Setiap nilai harus berada pada rentang 0 sampai 100.")

    kelompok = {kategori: [] for kategori in "ABCDE"}
    for nilai in daftar_nilai:
        kelompok[kategori_nilai(nilai)].append(nilai)

    frekuensi = {kategori: len(nilai) for kategori, nilai in kelompok.items()}
    return (
        sum(daftar_nilai) / len(daftar_nilai),
        max(daftar_nilai),
        min(daftar_nilai),
        kelompok,
        frekuensi,
    )


def analisis_beasiswa(
    penerima_a: list[str], penerima_b: list[str]
) -> tuple[set[str], set[str], set[str], set[str]]:
    """Cari irisan, selisih, dan gabungan dua daftar penerima beasiswa."""
    beasiswa_a = set(penerima_a)
    beasiswa_b = set(penerima_b)
    return (
        beasiswa_a & beasiswa_b,
        beasiswa_a - beasiswa_b,
        beasiswa_b - beasiswa_a,
        beasiswa_a | beasiswa_b,
    )


def tambah_barang(
    inventaris: dict[str, tuple[float, int]],
    nama: str,
    harga: float,
    stok: int,
) -> None:
    """Tambahkan barang baru; harga harus nonnegatif dan stok bilangan bulat."""
    nama = nama.strip()
    if not nama:
        raise ValueError("Nama barang tidak boleh kosong.")
    if nama in inventaris:
        raise ValueError(f"Barang '{nama}' sudah ada di inventaris.")
    if not math.isfinite(harga) or harga < 0:
        raise ValueError("Harga harus berupa angka terbatas dan tidak negatif.")
    if stok < 0:
        raise ValueError("Stok tidak boleh negatif.")
    inventaris[nama] = (harga, stok)


def update_stok(
    inventaris: dict[str, tuple[float, int]], nama: str, stok_baru: int
) -> None:
    """Ganti jumlah stok barang yang sudah ada."""
    if nama not in inventaris:
        raise ValueError(f"Barang '{nama}' tidak ditemukan.")
    if stok_baru < 0:
        raise ValueError("Stok tidak boleh negatif.")
    harga, _ = inventaris[nama]
    inventaris[nama] = (harga, stok_baru)


def cari_barang(
    inventaris: dict[str, tuple[float, int]], harga_min: float, harga_max: float
) -> dict[str, tuple[float, int]]:
    """Cari barang dengan harga dalam rentang inklusif."""
    if (
        not math.isfinite(harga_min)
        or not math.isfinite(harga_max)
        or harga_min < 0
        or harga_max < harga_min
    ):
        raise ValueError("Rentang harga tidak valid.")
    return {
        nama: data
        for nama, data in inventaris.items()
        if harga_min <= data[0] <= harga_max
    }


def hitung_nilai_inventaris(inventaris: dict[str, tuple[float, int]]) -> float:
    """Hitung total nilai barang berdasarkan harga dikali stok."""
    return sum(harga * stok for harga, stok in inventaris.values())


def analisis_file(teks: str) -> tuple[dict[str, int], list[tuple[str, int]], list[str], float]:
    """Hitung frekuensi kata, top 10, hapax legomena, dan type-token ratio."""
    kata = re.findall(r"[^\W\d_]+", teks.casefold(), flags=re.UNICODE)
    frekuensi: dict[str, int] = {}
    for item in kata:
        frekuensi[item] = frekuensi.get(item, 0) + 1

    sepuluh_teratas = sorted(
        frekuensi.items(), key=lambda item: (-item[1], item[0])
    )[:10]
    hapax = sorted(item for item, jumlah in frekuensi.items() if jumlah == 1)
    rasio_ttr = len(set(kata)) / len(kata) if kata else 0.0
    return frekuensi, sepuluh_teratas, hapax, rasio_ttr


def jalankan_soal_1() -> None:
    kalimat = input("Masukkan sebuah kalimat: ")
    jumlah_kata, jumlah_karakter, terpanjang, title_case = analisis_kalimat(kalimat)
    print(f"Jumlah kata      : {jumlah_kata}")
    print(f"Jumlah karakter  : {jumlah_karakter}")
    print(f"Kata terpanjang  : {terpanjang or '-'}")
    print(f"Title case       : {title_case}")


def jalankan_soal_2() -> None:
    try:
        teks_nilai = input("Masukkan nilai (pisahkan dengan koma): ")
        nilai = [float(item.strip()) for item in teks_nilai.split(",") if item.strip()]
        rata_rata, tertinggi, terendah, kelompok, frekuensi = analisis_nilai(nilai)
    except ValueError as error:
        print(f"Input tidak valid: {error}")
        return

    print(f"Rata-rata       : {rata_rata:.2f}")
    print(f"Nilai tertinggi : {tertinggi:g}")
    print(f"Nilai terendah  : {terendah:g}")
    print("Pengelompokan nilai:")
    for kategori, daftar in kelompok.items():
        print(f"  {kategori}: {daftar or '-'}")
    print(f"Frekuensi kategori: {frekuensi}")


def baca_daftar_id(prompt: str) -> list[str]:
    return [item.strip() for item in input(prompt).split(",") if item.strip()]


def jalankan_soal_3() -> None:
    penerima_a = baca_daftar_id("ID penerima beasiswa A (pisahkan dengan koma): ")
    penerima_b = baca_daftar_id("ID penerima beasiswa B (pisahkan dengan koma): ")
    bersama, hanya_a, hanya_b, semua = analisis_beasiswa(penerima_a, penerima_b)
    print(f"Menerima kedua beasiswa : {sorted(bersama)}")
    print(f"Hanya beasiswa A        : {sorted(hanya_a)}")
    print(f"Beasiswa B, bukan A     : {sorted(hanya_b)}")
    print(f"Semua penerima unik     : {sorted(semua)}")


def jalankan_soal_4() -> None:
    inventaris: dict[str, tuple[float, int]] = {}
    while True:
        print("\n--- Inventaris Toko ---")
        print("1. Tambah barang")
        print("2. Update stok")
        print("3. Cari barang berdasarkan rentang harga")
        print("4. Lihat total nilai inventaris")
        print("5. Tampilkan inventaris")
        print("0. Kembali ke menu utama")
        pilihan = input("Pilih menu: ").strip()

        try:
            if pilihan == "1":
                nama = input("Nama barang: ")
                harga = float(input("Harga: "))
                stok = int(input("Stok: "))
                tambah_barang(inventaris, nama, harga, stok)
                print(f"Barang '{nama.strip()}' berhasil ditambahkan.")
            elif pilihan == "2":
                nama = input("Nama barang: ").strip()
                stok = int(input("Stok baru: "))
                update_stok(inventaris, nama, stok)
                print("Stok berhasil diperbarui.")
            elif pilihan == "3":
                harga_min = float(input("Harga minimum: "))
                harga_max = float(input("Harga maksimum: "))
                hasil = cari_barang(inventaris, harga_min, harga_max)
                print(f"Barang dalam rentang harga: {hasil or '-'}")
            elif pilihan == "4":
                print(f"Total nilai inventaris: Rp{hitung_nilai_inventaris(inventaris):,.2f}")
            elif pilihan == "5":
                print(f"Inventaris (nama: (harga, stok)): {inventaris or '-'}")
            elif pilihan == "0":
                break
            else:
                print("Pilihan tidak valid.")
        except ValueError as error:
            print(f"Input tidak valid: {error}")


def jalankan_soal_5() -> None:
    lokasi = input("Masukkan path file teks: ").strip()
    try:
        teks = Path(lokasi).read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        print(f"Gagal membaca file '{lokasi}': {error}")
        return

    frekuensi, teratas, hapax, rasio_ttr = analisis_file(teks)
    jumlah_kata = sum(frekuensi.values())
    print(f"Jumlah kata       : {jumlah_kata}")
    print(f"Frekuensi kata    : {frekuensi}")
    print("10 kata paling sering muncul:")
    if teratas:
        for kata, jumlah in teratas:
            print(f"  {kata}: {jumlah}")
    else:
        print("  Tidak ada kata dalam file.")
    print(f"Hapax legomena    : {hapax}")
    print(f"Type-token ratio  : {rasio_ttr:.4f}")


def main() -> None:
    menu = {
        "1": ("Analisis kalimat", jalankan_soal_1),
        "2": ("Analisis nilai mahasiswa", jalankan_soal_2),
        "3": ("Analisis penerima beasiswa", jalankan_soal_3),
        "4": ("Manajemen inventaris toko", jalankan_soal_4),
        "5": ("Analisis teks dari file", jalankan_soal_5),
    }

    while True:
        print("\n=== LATIHAN PERTEMUAN 5 ===")
        for nomor, (judul, _) in menu.items():
            print(f"{nomor}. {judul}")
        print("0. Keluar")
        pilihan = input("Pilih soal: ").strip()
        if pilihan == "0":
            print("Program selesai.")
            break
        if pilihan in menu:
            menu[pilihan][1]()
        else:
            print("Pilihan tidak valid. Masukkan angka 0 sampai 5.")


if __name__ == "__main__":
    main()
