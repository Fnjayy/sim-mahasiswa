"""Kalkulator diskon biaya kuliah."""

import math


def hitung_diskon(
    spp: float,
    anak_karyawan: bool,
    ipk: float,
    tepat_waktu: bool,
) -> tuple[list[tuple[str, float]], float, float, float]:
    """Return diskon terpakai, persen total, nominal potongan, dan biaya akhir."""
    if not math.isfinite(spp) or spp < 0:
        raise ValueError("Biaya SPP harus berupa angka valid dan tidak boleh negatif.")
    if not math.isfinite(ipk) or not 0 <= ipk <= 4:
        raise ValueError("IPK harus berada pada rentang 0 sampai 4.")

    diskon: list[tuple[str, float]] = []
    if anak_karyawan:
        diskon.append(("Anak karyawan", 25.0))

    if ipk >= 3.8:
        diskon.append(("IPK minimal 3.8", 20.0))
    elif ipk >= 3.5:
        diskon.append(("IPK minimal 3.5", 15.0))
    elif ipk >= 3.0:
        diskon.append(("IPK minimal 3.0", 10.0))

    if tepat_waktu:
        diskon.append(("Pembayaran tepat waktu", 5.0))

    persen_total = sum(persen for _, persen in diskon)
    potongan = round(spp * persen_total / 100, 2)
    biaya_akhir = round(spp - potongan, 2)
    return diskon, persen_total, potongan, biaya_akhir


def _input_ya_tidak(prompt: str) -> bool:
    while True:
        jawaban = input(prompt).strip().lower()
        if jawaban in ("y", "n"):
            return jawaban == "y"
        print("Masukkan y atau n.")


def input_data_diskon() -> tuple[float, bool, float, bool]:
    while True:
        try:
            spp = float(input("Biaya SPP (Rp): ").strip())
            if math.isfinite(spp) and spp >= 0:
                break
        except ValueError:
            pass
        print("Biaya SPP harus berupa angka dan tidak boleh negatif.")

    anak_karyawan = _input_ya_tidak("Anak karyawan? (y/n): ")
    while True:
        try:
            ipk = float(input("IPK (0.0-4.0): ").strip())
            if math.isfinite(ipk) and 0 <= ipk <= 4:
                break
        except ValueError:
            pass
        print("IPK harus berupa angka dari 0.0 sampai 4.0.")
    tepat_waktu = _input_ya_tidak("Pembayaran tepat waktu? (y/n): ")
    return spp, anak_karyawan, ipk, tepat_waktu


def tampilkan_hasil_diskon(
    spp: float,
    anak_karyawan: bool,
    ipk: float,
    tepat_waktu: bool,
) -> None:
    diskon, persen, potongan, akhir = hitung_diskon(
        spp, anak_karyawan, ipk, tepat_waktu
    )
    print("\nRINCIAN DISKON")
    if diskon:
        for nama, persentase in diskon:
            print(f"- {nama}: {persentase:.0f}%")
    else:
        print("- Tidak ada diskon.")
    print(f"Total diskon: {persen:.0f}%")
    print(f"Potongan biaya: Rp{potongan:,.2f}")
    print(f"Biaya final: Rp{akhir:,.2f}")


def main() -> None:
    tampilkan_hasil_diskon(*input_data_diskon())


if __name__ == "__main__":
    main()
