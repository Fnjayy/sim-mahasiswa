"""Laporan prioritas dan nilai barang inventaris."""

import math

INVENTARIS: list[dict[str, object]] = [
    {"nama": "Laptop", "stok": 14, "harga": 8_500_000},
    {"nama": "Mouse", "stok": 8, "harga": 125_000},
    {"nama": "Keyboard", "stok": 4, "harga": 275_000},
    {"nama": "Kertas A4", "stok": 0, "harga": 55_000},
    {"nama": "Tinta printer", "stok": 3, "harga": 185_000},
    {"nama": "Proyektor", "stok": 11, "harga": 4_200_000},
    {"nama": "Kabel HDMI", "stok": 6, "harga": 90_000},
    {"nama": "Flash drive", "stok": 18, "harga": 85_000},
    {"nama": "Spidol", "stok": 2, "harga": 15_000},
]

PRIORITAS = {"Habis": 1, "Rendah": 2, "Peringatan": 3, "Aman": 4}
NAMA_PRIORITAS = {1: "P1", 2: "P2", 3: "P3", 4: "P4"}


def status_stok(stok: int) -> str:
    if stok < 0:
        raise ValueError("Stok tidak boleh negatif.")
    if stok == 0:
        return "Habis"
    if stok <= 5:
        return "Rendah"
    if stok <= 10:
        return "Peringatan"
    return "Aman"


def ringkasan_inventaris(
    inventaris: list[dict[str, object]] | None = None,
) -> dict[str, object]:
    barang = INVENTARIS if inventaris is None else inventaris
    statistik = {nama: 0 for nama in PRIORITAS}
    total_nilai = 0
    for item in barang:
        stok = int(item["stok"])
        harga = float(item["harga"])
        if stok < 0 or not math.isfinite(harga) or harga < 0:
            raise ValueError("Stok dan harga barang tidak boleh negatif.")
        status = status_stok(stok)
        statistik[status] += 1
        total_nilai += stok * harga

    perlu_restock = statistik["Habis"] + statistik["Rendah"] + statistik["Peringatan"]
    return {
        "jumlah_item": len(barang),
        "statistik": statistik,
        "total_nilai": total_nilai,
        "perlu_restock": perlu_restock,
    }


def tampilkan_laporan(
    inventaris: list[dict[str, object]] | None = None,
) -> None:
    barang = INVENTARIS if inventaris is None else inventaris
    urut = sorted(
        barang,
        key=lambda item: (
            PRIORITAS[status_stok(int(item["stok"]))],
            str(item["nama"]).lower(),
        ),
    )
    print("\nLAPORAN PERINGATAN STOK")
    print(f"{'Prioritas':<10} {'Barang':<20} {'Stok':>6} {'Harga/unit':>16} {'Nilai':>16}")
    print("-" * 74)
    for item in urut:
        stok = int(item["stok"])
        harga = float(item["harga"])
        status = status_stok(stok)
        print(
            f"{NAMA_PRIORITAS[PRIORITAS[status]] + ' - ' + status:<10} "
            f"{str(item['nama']):<20} "
            f"{stok:>6} Rp{harga:>13,.0f} Rp{stok * harga:>13,.0f}  {status}"
        )

    ringkasan = ringkasan_inventaris(barang)
    statistik = ringkasan["statistik"]
    print("\nRingkasan:")
    print(f"Jumlah item: {ringkasan['jumlah_item']}")
    print(f"Total nilai inventaris: Rp{ringkasan['total_nilai']:,.0f}")
    print(f"Item perlu restock: {ringkasan['perlu_restock']}")
    for status in PRIORITAS:
        print(f"  {status}: {statistik[status]}")


def main() -> None:
    tampilkan_laporan()


if __name__ == "__main__":
    main()
