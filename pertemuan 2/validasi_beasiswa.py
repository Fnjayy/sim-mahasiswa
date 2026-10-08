"""Contoh validasi komposit untuk pengajuan beasiswa mahasiswa."""


def evaluasi_beasiswa(
    status_aktif: bool,
    ipk: float,
    semester: int,
    pendapatan_orang_tua: int,
    menerima_beasiswa_lain: bool,
) -> tuple[bool, str]:
    """Validasi input, lalu evaluasi kriteria kelayakan beasiswa."""
    if not isinstance(status_aktif, bool):
        raise ValueError("Status aktif harus bernilai True atau False.")
    if not isinstance(ipk, (int, float)) or isinstance(ipk, bool):
        raise ValueError("IPK harus berupa angka.")
    if not 0 <= ipk <= 4:
        raise ValueError("IPK harus berada pada rentang 0 sampai 4.")
    if not isinstance(semester, int) or isinstance(semester, bool):
        raise ValueError("Semester harus berupa bilangan bulat.")
    if semester < 1:
        raise ValueError("Semester minimal adalah 1.")
    if (
        not isinstance(pendapatan_orang_tua, int)
        or isinstance(pendapatan_orang_tua, bool)
    ):
        raise ValueError("Pendapatan orang tua harus berupa bilangan bulat.")
    if pendapatan_orang_tua < 0:
        raise ValueError("Pendapatan orang tua tidak boleh negatif.")
    if not isinstance(menerima_beasiswa_lain, bool):
        raise ValueError("Status beasiswa lain harus bernilai True atau False.")

    memenuhi_kriteria = (
        status_aktif
        and ipk >= 3.5
        and 2 <= semester <= 6
        and pendapatan_orang_tua <= 5_000_000
        and not menerima_beasiswa_lain
    )

    if memenuhi_kriteria:
        return True, "Pengajuan memenuhi kriteria beasiswa."
    return False, "Pengajuan belum memenuhi seluruh kriteria beasiswa."


if __name__ == "__main__":
    try:
        layak, pesan = evaluasi_beasiswa(
            status_aktif=True,
            ipk=3.7,
            semester=4,
            pendapatan_orang_tua=4_000_000,
            menerima_beasiswa_lain=False,
        )
    except ValueError as error:
        print(f"Input tidak valid: {error}")
    else:
        print(pesan)
