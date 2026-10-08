"""Ringkasan statistik dari contoh kasus mahasiswa, diskon, dan inventaris."""

from diskon_biaya import hitung_diskon
from peringatan_stok import INVENTARIS, ringkasan_inventaris
from status_mahasiswa import hitung_status

DATA_MAHASISWA = [
    {"nim": "2024000001", "ipk": 3.2, "sks": 20},
    {"nim": "2024000002", "ipk": 1.8, "sks": 18},
    {"nim": "2024000003", "ipk": 1.2, "sks": 22},
    {"nim": "2024000004", "ipk": 3.8, "sks": 18},
    {"nim": "2024000005", "ipk": 2.5, "sks": 12},
]

DATA_DISKON = [
    (5_000_000, True, 3.9, True),
    (5_000_000, False, 3.6, True),
    (5_000_000, False, 3.2, False),
    (5_000_000, True, 2.8, False),
]


def main() -> None:
    statuses = [
        hitung_status(float(item["ipk"]), int(item["sks"]))
        for item in DATA_MAHASISWA
    ]
    jumlah_mahasiswa = len(statuses)
    jumlah_aktif = statuses.count("Aktif")
    jumlah_peringatan = statuses.count("Peringatan")
    jumlah_tidak_aktif = statuses.count("Tidak Aktif")
    jumlah_nonaktif = jumlah_mahasiswa - jumlah_aktif

    persen_aktif = 100 * jumlah_aktif / jumlah_mahasiswa if jumlah_mahasiswa else 0
    persen_nonaktif = (
        100 * jumlah_nonaktif / jumlah_mahasiswa if jumlah_mahasiswa else 0
    )
    persen_tidak_aktif = (
        100 * jumlah_tidak_aktif / jumlah_mahasiswa if jumlah_mahasiswa else 0
    )
    persen_peringatan = (
        100 * jumlah_peringatan / jumlah_mahasiswa if jumlah_mahasiswa else 0
    )

    diskon_persen = [
        hitung_diskon(*data)[1]
        for data in DATA_DISKON
    ]
    rata_rata_diskon = (
        sum(diskon_persen) / len(diskon_persen) if diskon_persen else 0
    )

    ringkasan_stok = ringkasan_inventaris(INVENTARIS)
    jumlah_item = int(ringkasan_stok["jumlah_item"])
    jumlah_restock = int(ringkasan_stok["perlu_restock"])
    persen_restock = 100 * jumlah_restock / jumlah_item if jumlah_item else 0

    print("RINGKASAN ALGORITMA")
    print("-" * 72)
    print(f"{'Metrik':<42} {'Hasil':>25}")
    print("-" * 72)
    print(f"{'Mahasiswa aktif':<42} {persen_aktif:>23.2f}%")
    print(f"{'Mahasiswa nonaktif (peringatan + tidak aktif)':<42} {persen_nonaktif:>23.2f}%")
    print(f"{'  Rincian status peringatan':<42} {persen_peringatan:>23.2f}%")
    print(f"{'  Rincian status tidak aktif':<42} {persen_tidak_aktif:>23.2f}%")
    print(f"{'Rata-rata diskon biaya kuliah':<42} {rata_rata_diskon:>23.2f}%")
    print(f"{'Item inventaris perlu restock':<42} {persen_restock:>23.2f}%")
    print("-" * 72)
    print(
        f"Data contoh: {jumlah_mahasiswa} mahasiswa, {len(diskon_persen)} "
        f"kalkulasi diskon, dan {jumlah_item} item inventaris."
    )


if __name__ == "__main__":
    main()
