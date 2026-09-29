import pytest

from src.models import DaftarMahasiswa, Mahasiswa


class TestMahasiswa:
    def test_buat_mahasiswa_valid(self):
        mhs = Mahasiswa(
            "20241320042",
            "Muhammad Fajar",
            "Sistem Informasi",
            2024,
            3.50,
        )
        assert mhs.nim == "20241320042"
        assert mhs.ipk == 3.50

    def test_nim_tidak_valid(self):
        with pytest.raises(ValueError):
            Mahasiswa("abc", "Test", "SI", 2024, 3.0)

    def test_nim_kosong(self):
        with pytest.raises(ValueError):
            Mahasiswa("", "Test", "SI", 2024, 3.0)

    def test_nama_sangat_panjang(self):
        nama = "A" * 200

        mhs = Mahasiswa(
            "20241320043",
            nama,
            "Sistem Informasi",
            2024,
            3.0,
        )

        assert mhs.nama == nama

    def test_ipk_boundary_minimum(self):
        mhs = Mahasiswa(
            "20241320044",
            "Boundary Min",
            "SI",
            2024,
            0.0,
        )

        assert mhs.ipk == 0.0

    def test_ipk_boundary_maksimum(self):
        mhs = Mahasiswa(
            "20241320045",
            "Boundary Max",
            "SI",
            2024,
            4.0,
        )

        assert mhs.ipk == 4.0

    def test_ipk_diluar_range(self):
        with pytest.raises(ValueError):
            Mahasiswa("20241320042", "Test", "SI", 2024, 5.0)


class TestDaftarMahasiswa:
    def test_tambah_dan_cari(self):
        db = DaftarMahasiswa()
        mhs = Mahasiswa("20241320042", "Muhammad Fajar", "Sistem Informasi", 2024)
        db.tambah(mhs)
        assert db.cari("20241320042") == mhs
        assert db.jumlah == 1

    def test_nim_duplikat(self):
        db = DaftarMahasiswa()
        m1 = Mahasiswa("20241320042", "Muhammad Fajar", "Sistem Informasi", 2024)
        m2 = Mahasiswa("20241320042", "Fajar", "Sistem Informasi", 2024)
        db.tambah(m1)
        with pytest.raises(ValueError):
            db.tambah(m2)

    def test_cari_nim_tidak_ada(self):
        db = DaftarMahasiswa()

        assert db.cari("99999999999") is None

    def test_hapus_nim_tidak_ada(self):
        db = DaftarMahasiswa()

        assert db.hapus("99999999999") is False

    def test_edit_ipk_berhasil(self):
        db = DaftarMahasiswa()

        mhs = Mahasiswa(
            "20241320042",
            "Muhammad Fajar",
            "Sistem Informasi",
            2024,
            3.0,
        )

        db.tambah(mhs)

        assert db.edit_ipk("20241320042", 3.8) is True
        assert mhs.ipk == 3.8

    def test_edit_ipk_nim_tidak_ada(self):
        db = DaftarMahasiswa()

        assert db.edit_ipk("99999999999", 3.5) is False