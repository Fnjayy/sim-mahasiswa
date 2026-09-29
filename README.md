# Sistem Informasi Mahasiswa (SIM)

Modul Praktikum Pemrograman Python

Aplikasi console-based untuk mengelola data mahasiswa pada Program Studi Sistem Informasi.

## Identitas

- Nama: Muhammad Fajar
- NIM: [20241320042]
- Kelas: [A1]

## Fitur

- Tambah data mahasiswa (NIM, nama, prodi, angkatan, IPK)
- Tampilkan seluruh data dalam tabel
- Cari mahasiswa berdasarkan NIM
- Hapus data mahasiswa
- Validasi data input

## Prasyarat

- Python 3.10+
- pip

## Instalasi

```bash
git clone https://github.com/Fnjayy/sim-mahasiswa.git
cd sim-mahasiswa
python -m venv venv

# Windows
venv\Scripts\activate

pip install -r requirements.txt
```

## Penggunaan

```bash
python src/main.py
```

## Pengujian

```bash
pytest tests/ -v
```

## Struktur Proyek

- src/models.py — Model data Mahasiswa
- src/main.py — Program utama & menu
- tests/ — Unit test

## Setup Checklist

- [x] Python terinstal (versi: 3.10.6)
- [x] Virtual environment dibuat & diaktivasi
- [x] Paket terinstal via requirements.txt
- [x] Program berjalan tanpa error
- [x] Unit test lulus
- [x] Repositori Git diinisiasi
- [x] Push ke GitHub berhasil
- [x] README.md lengkap
## Screenshot

### Menu Utama

![Menu Utama](docsmenu-utama.png)

### Daftar Mahasiswa

![Daftar Mahasiswa](docsdaftar-mahasiswa.png)