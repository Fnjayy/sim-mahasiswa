import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from models import DaftarMahasiswa, Mahasiswa


def test_mahasiswa_validasi_ipk():
    with pytest.raises(ValueError, match="IPK harus 0.0-4.0"):
        Mahasiswa("202310001", "Andi", "TI", 2023, 4.5)


def test_tambah_mahasiswa_baru():
    db = DaftarMahasiswa()
    mhs = Mahasiswa("202310001", "Andi", "TI", 2023, 3.75)

    db.tambah(mhs)

    assert db.jumlah == 1
    assert db.cari("202310001") == mhs


def test_tambah_nim_duplikat_raises():
    db = DaftarMahasiswa()
    db.tambah(Mahasiswa("202310001", "Andi", "TI", 2023, 3.75))

    with pytest.raises(ValueError, match="sudah terdaftar"):
        db.tambah(Mahasiswa("202310001", "Budi", "SI", 2024, 3.8))


def test_hapus_mahasiswa():
    db = DaftarMahasiswa()
    db.tambah(Mahasiswa("202310001", "Andi", "TI", 2023, 3.75))

    assert db.hapus("202310001") is True
    assert db.jumlah == 0
    assert db.cari("202310001") is None
