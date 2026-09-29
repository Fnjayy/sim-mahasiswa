from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from models import DaftarMahasiswa, Mahasiswa

console = Console()
db = DaftarMahasiswa()


def tampilkan_menu():
    """Tampilkan menu utama."""
    menu_text = (
        "[bold cyan]Sistem Informasi Mahasiswa[/]\n\n"
        "1. Tambah Mahasiswa\n"
        "2. Tampilkan Semua Mahasiswa\n"
        "3. Cari Mahasiswa (NIM)\n"
        "4. Hapus Mahasiswa\n"
        "5. Edit IPK Mahasiswa\n"
        "0. Keluar"
    )
    console.print(Panel(menu_text, title="Menu", border_style="cyan"))


def tambah_mahasiswa():
    """Form tambah mahasiswa baru."""
    console.print("\n[bold]Tambah Mahasiswa Baru[/]")
    nim = console.input(" NIM: ").strip()
    nama = console.input(" Nama: ").strip()
    prodi = console.input(" Program Studi: ").strip()

    try:
        angkatan = int(console.input(" Angkatan: ").strip())
        ipk = float(console.input(" IPK: ").strip())
        mhs = Mahasiswa(nim, nama, prodi, angkatan, ipk)
        db.tambah(mhs)
        console.print(f" [green]Berhasil: {nama} ditambahkan[/]")
    except ValueError as e:
        console.print(f" [red]Gagal: {e}[/]")
    except Exception:
        console.print(" [red]Data yang dimasukkan tidak valid.[/]")


def tampilkan_semua():
    """Tampilkan seluruh data dalam tabel."""
    if not db.data:
        console.print("[yellow]Belum ada data mahasiswa.[/]")
        return

    table = Table(title="Daftar Mahasiswa")
    table.add_column("NIM", style="cyan")
    table.add_column("Nama")
    table.add_column("Program Studi")
    table.add_column("Angkatan", justify="right")
    table.add_column("IPK", justify="right")

    for m in db.data:
        table.add_row(m.nim, m.nama, m.program_studi, str(m.angkatan), f"{m.ipk:.2f}")

    console.print(table)


def cari_mahasiswa():
    """Cari mahasiswa berdasarkan NIM."""
    console.print("\n[bold]Cari Mahasiswa[/]")
    nim = console.input(" NIM: ").strip()
    mhs = db.cari(nim)

    if not mhs:
        console.print("[yellow]Mahasiswa tidak ditemukan.[/]")
        return

    console.print(
        Panel(
            f"NIM: {mhs.nim}\n"
            f"Nama: {mhs.nama}\n"
            f"Program Studi: {mhs.program_studi}\n"
            f"Angkatan: {mhs.angkatan}\n"
            f"IPK: {mhs.ipk:.2f}",
            title="Detail Mahasiswa",
            border_style="green",
        )
    )


def hapus_mahasiswa():
    """Hapus mahasiswa berdasarkan NIM."""
    console.print("\n[bold]Hapus Mahasiswa[/]")
    nim = console.input(" NIM: ").strip()

    if db.hapus(nim):
        console.print(f" [green]Berhasil: mahasiswa dengan NIM {nim} dihapus.[/]")
    else:
        console.print(f" [red]Gagal: NIM {nim} tidak ditemukan.[/]")


def edit_ipk_mahasiswa():
    """Edit IPK mahasiswa berdasarkan NIM."""
    console.print("\n[bold]Edit IPK Mahasiswa[/]")
    nim = console.input(" NIM: ").strip()

    try:
        ipk_baru = float(console.input(" IPK Baru: ").strip())

        if db.edit_ipk(nim, ipk_baru):
            console.print(
                f"[green]Berhasil: IPK mahasiswa {nim} diperbarui menjadi {ipk_baru:.2f}[/]"
            )
        else:
            console.print(f"[red]Gagal: Mahasiswa dengan NIM {nim} tidak ditemukan.[/]")
    except ValueError as e:
        console.print(f"[red]{e}[/]")


def main():
    """Loop utama aplikasi."""
    while True:
        tampilkan_menu()
        pilihan = console.input("\nPilih [0-5]: ").strip()

        if pilihan == "1":
            tambah_mahasiswa()
        elif pilihan == "2":
            tampilkan_semua()
        elif pilihan == "3":
            cari_mahasiswa()
        elif pilihan == "4":
            hapus_mahasiswa()
        elif pilihan == "5":
            edit_ipk_mahasiswa()
        elif pilihan == "0":
            console.print("[bold]Sampai jumpa![/]")
            break
        else:
            console.print("[red]Pilihan tidak valid[/]")


if __name__ == "__main__":
    main()