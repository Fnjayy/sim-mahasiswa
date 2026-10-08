"""Validasi NIM, IPK, SKS, dan semester mahasiswa."""

import math


def _bilangan_bulat(nilai: object) -> int | None:
    if isinstance(nilai, bool):
        return None
    try:
        teks = str(nilai).strip()
        if not teks or any(karakter not in "0123456789+-" for karakter in teks):
            return None
        hasil = int(teks)
    except (TypeError, ValueError):
        return None
    return hasil


def validasi_data(nim: str, ipk: object, sks: object, semester: object) -> list[str]:
    """Kembalikan seluruh pesan error untuk satu rekaman mahasiswa."""
    errors: list[str] = []
    nim = str(nim).strip()
    if len(nim) != 10 or not nim.isdigit():
        errors.append("NIM harus terdiri dari tepat 10 digit angka.")
    elif not 2000 <= int(nim[:4]) <= 2037:
        errors.append("Empat digit awal NIM harus menunjukkan tahun 2000-2037.")

    try:
        nilai_ipk = float(str(ipk).strip())
        if not math.isfinite(nilai_ipk) or not 0.0 <= nilai_ipk <= 4.0:
            errors.append("IPK harus berada pada rentang 0.0 sampai 4.0.")
    except (TypeError, ValueError):
        errors.append("IPK harus berupa angka.")

    nilai_sks = _bilangan_bulat(sks)
    if nilai_sks is None or not 0 <= nilai_sks <= 24:
        errors.append("SKS harus berupa bilangan bulat dari 0 sampai 24.")

    nilai_semester = _bilangan_bulat(semester)
    if nilai_semester is None or not 1 <= nilai_semester <= 14:
        errors.append("Semester harus berupa bilangan bulat dari 1 sampai 14.")

    return errors


def main() -> None:
    print("Masukkan data mahasiswa untuk divalidasi.")
    nim = input("NIM (10 digit): ").strip()
    ipk = input("IPK: ").strip()
    sks = input("SKS: ").strip()
    semester = input("Semester: ").strip()

    errors = validasi_data(nim, ipk, sks, semester)
    if errors:
        print("\nData tidak valid:")
        for error in errors:
            print(f"- {error}")
    else:
        print("\nData mahasiswa valid.")


if __name__ == "__main__":
    main()
