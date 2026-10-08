"""Input dan laporan status untuk lima mahasiswa."""


def hitung_status(ipk: float, sks: int) -> str:
    """Tentukan status berdasarkan IPK dan SKS yang sudah divalidasi."""
    if not 0 <= ipk <= 4:
        raise ValueError("IPK harus berada pada rentang 0 sampai 4.")
    if not 0 <= sks <= 24:
        raise ValueError("SKS harus berada pada rentang 0 sampai 24.")
    if ipk < 1.5:
        return "Tidak Aktif"
    if ipk < 2.0:
        return "Peringatan"
    if sks < 18:
        return "Peringatan"
    return "Aktif"


def _input_teks(prompt: str) -> str:
    while True:
        nilai = input(prompt).strip()
        if nilai:
            return nilai
        print("Input tidak boleh kosong.")


def _input_ipk() -> float:
    while True:
        try:
            ipk = float(input("IPK (0.0-4.0): ").strip())
            if 0 <= ipk <= 4:
                return ipk
        except ValueError:
            pass
        print("IPK harus berupa angka dari 0.0 sampai 4.0.")


def _input_sks() -> int:
    while True:
        try:
            teks = input("SKS (0-24): ").strip()
            sks = int(teks)
            if 0 <= sks <= 24:
                return sks
        except ValueError:
            pass
        print("SKS harus berupa bilangan bulat dari 0 sampai 24.")


def input_data_mahasiswa(jumlah: int = 5) -> list[dict[str, object]]:
    """Minta data mahasiswa sebanyak jumlah yang ditentukan."""
    data: list[dict[str, object]] = []
    for nomor in range(1, jumlah + 1):
        print(f"\nData mahasiswa ke-{nomor}")
        nim = _input_teks("NIM: ")
        nama = _input_teks("Nama: ")
        ipk = _input_ipk()
        sks = _input_sks()
        data.append({"nim": nim, "nama": nama, "ipk": ipk, "sks": sks})
    return data


def tampilkan_laporan(data: list[dict[str, object]]) -> None:
    print("\nLAPORAN STATUS MAHASISWA")
    print(f"{'NIM':<16} {'Nama':<24} {'IPK':>5} {'SKS':>5}  Status")
    print("-" * 68)
    for mahasiswa in data:
        ipk = float(mahasiswa["ipk"])
        sks = int(mahasiswa["sks"])
        print(
            f"{str(mahasiswa['nim']):<16} "
            f"{str(mahasiswa['nama']):<24} "
            f"{ipk:>5.2f} {sks:>5}  {hitung_status(ipk, sks)}"
        )


def main() -> None:
    tampilkan_laporan(input_data_mahasiswa(5))


if __name__ == "__main__":
    main()
