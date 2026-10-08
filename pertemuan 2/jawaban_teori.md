# A. Soal Teori

## 1. Aturan bisnis dan logika teknis

**Aturan bisnis (business rules)** adalah ketentuan yang berasal dari kebijakan atau proses organisasi. Aturan ini menjelaskan apa yang boleh, wajib, atau memenuhi syarat dalam kegiatan akademik. Aturan dapat berubah ketika kebijakan kampus berubah.

**Logika teknis (technical logic)** adalah cara program menerapkan aturan atau mengelola data dan proses komputasi. Logika ini berhubungan dengan implementasi perangkat lunak, bukan kebijakan akademiknya.

Contoh pada Sistem Informasi Mahasiswa:

- Aturan bisnis:
  1. Mahasiswa dapat mengisi KRS jika sudah melakukan registrasi semester.
  2. Mahasiswa dinyatakan lulus mata kuliah jika nilai akhirnya minimal 60.
- Logika teknis:
  1. Mengubah data formulir menjadi objek mahasiswa sebelum menyimpannya ke basis data.
  2. Mengurutkan daftar mahasiswa berdasarkan NIM menggunakan fungsi pengurutan.

## 2. Mengapa NIM sebaiknya bertipe string?

NIM adalah **pengenal**, bukan bilangan untuk operasi aritmetika. Tipe `str` mempertahankan format NIM, termasuk angka nol di depan dan karakter nonangka jika suatu kampus menggunakannya. Misalnya, NIM `"0012345"` tetap memiliki tujuh karakter.

Jika NIM disimpan sebagai `int`, angka nol di depan akan hilang (`0012345` menjadi `12345`), dan NIM yang mengandung huruf atau tanda pemisah tidak dapat direpresentasikan. Konversi ke angka juga berisiko menyebabkan perbandingan atau pengurutan dilakukan secara numerik, padahal yang diperlukan adalah perbandingan identitas atau format. Karena itu, NIM sebaiknya disimpan dan diproses sebagai string.

## 3. Operator `and` dan `or`

- `and` bernilai benar hanya jika **semua** kondisi yang digabungkan bernilai benar. Contoh aturan: mahasiswa boleh mengajukan KRS jika statusnya aktif **dan** sudah membayar biaya registrasi.
- `or` bernilai benar jika **setidaknya satu** kondisi bernilai benar. Contoh aturan: mahasiswa mendapat pembebasan biaya jika memiliki beasiswa penuh **atau** termasuk penerima bantuan khusus.

Gunakan tanda kurung bila gabungan `and` dan `or` dapat menimbulkan ambiguitas, agar pengelompokan aturan terlihat jelas.

## 4. Urutan kondisi `if-elif-else`

Python memeriksa kondisi dari atas ke bawah dan menjalankan blok pertama yang kondisinya benar. Karena itu, kondisi yang lebih spesifik perlu diperiksa sebelum kondisi yang lebih umum.

Contoh: jika `if nilai >= 60` diletakkan sebelum `elif nilai >= 85`, nilai 90 sudah memenuhi kondisi pertama. Cabang nilai tinggi tidak pernah dijalankan. Susunan yang tepat adalah menguji `nilai >= 85` lebih dahulu, lalu `nilai >= 60`, kemudian kondisi lainnya.

## 5. Kapan menggunakan `for` dan `while`?

- Gunakan `for` saat jumlah pengulangan atau kumpulan yang diproses sudah diketahui/tersedia. Contoh bisnis: memeriksa status registrasi setiap mahasiswa dalam daftar calon peserta KRS.
- Gunakan `while` saat pengulangan bergantung pada kondisi yang belum diketahui kapan berakhir. Contoh bisnis: meminta pengguna memasukkan PIN sampai PIN benar atau batas percobaan tercapai.

Pastikan kondisi `while` dapat berubah sehingga loop dapat berhenti, dan gunakan batas percobaan atau mekanisme penghentian yang sesuai.

## 6. Klausa `else` pada loop dan pada `if`

Pada `for` atau `while`, blok `else` dijalankan ketika loop selesai secara normal, yaitu tidak dihentikan oleh `break`. Contoh: memeriksa seluruh daftar mahasiswa; jika tidak ditemukan mahasiswa yang dicari, blok `else` dapat menampilkan pesan “tidak ditemukan”. Jika pencarian menghentikan loop dengan `break`, blok `else` tidak dijalankan.

Pada `if-else`, blok `else` adalah cabang alternatif yang dijalankan ketika kondisi `if` bernilai salah. Jadi, `else` pada `if` bergantung pada hasil kondisi, sedangkan `else` pada loop bergantung pada apakah loop selesai normal atau dihentikan oleh `break`.

## 7. Mengapa validasi input harus mendahului evaluasi aturan bisnis?

Validasi memastikan data memiliki format, tipe, dan rentang yang dapat diproses sebelum aturan bisnis menggunakannya. Contohnya, IPK harus berupa angka dalam rentang 0,00–4,00; jika tidak, perbandingan terhadap ambang IPK dapat menghasilkan kesalahan atau keputusan kelayakan yang tidak bermakna.

Tanpa validasi, sistem berisiko mengalami error saat dijalankan, menerima data tidak masuk akal, memberi keputusan yang salah, atau menyimpan data yang merusak laporan dan proses berikutnya. Validasi input tidak menggantikan aturan bisnis: setelah data dinyatakan valid, barulah kelayakan menurut kebijakan bisnis dievaluasi.

## 8. Validasi komposit dan contoh pengajuan beasiswa

**Validasi komposit** menggabungkan beberapa pemeriksaan untuk memutuskan apakah suatu pengajuan memenuhi seluruh kriteria. Contoh di bawah menggunakan kebijakan ilustratif: mahasiswa harus berstatus aktif, IPK minimal 3,50, berada di semester 2–6, pendapatan orang tua maksimal Rp5.000.000 per bulan, dan tidak sedang menerima beasiswa lain.

Pemeriksaan format dan rentang dilakukan lebih dahulu. Setelah input valid, aturan kelayakan digabungkan dengan `and`, sehingga semua kriteria harus terpenuhi. Ambang berikut hanya contoh dan harus disesuaikan dengan kebijakan kampus yang berlaku. Implementasi yang dapat dijalankan tersedia di [`validasi_beasiswa.py`](./validasi_beasiswa.py).
