# ==================================================
# PROGRAM PEMESANAN TIKET BIOSKOP
# Boundary Value Analysis & State Transition Testing
# ==================================================

# ──────────── DATA LOGIN ────────────────────
USERNAME_BENAR = "admin"
PASSWORD_BENAR = "123"


# ──────────── DAFTAR FILM ───────────────────
daftar_film = {
    1: "Avengers: Endgame",
    2: "Interstellar",
    3: "Frozen II",
    4: "Spider-Man: No Way Home"
}

# ──────────── LOGIN SYSTEM ──────────────────
print("======================================")
print("      LOGIN BIOSKOP CINEMA XXI       ")
print("======================================")

while True:
    username = input("Username : ")
    password = input("Password : ")

    if username == USERNAME_BENAR and password == PASSWORD_BENAR:
        print("\n[LOGIN BERHASIL]\n")
        break
    else:
        print("\n[ERROR] Username atau Password salah!")
        print("Silakan coba lagi.\n")


# ──────────── INPUT NAMA ─────────────────────
while True:
    nama = input("Masukkan Nama Pemesan : ")

    if nama.strip() != "":
        break
    else:
        print("[ERROR] Nama tidak boleh kosong!\n")


# ──────────── TAMPILKAN FILM ──────────────────
print("\n======================================")
print("           DAFTAR FILM                ")
print("======================================")

for kode, film in daftar_film.items():
    print(f"{kode}. {film}")


# ──────────── PILIH FILM ─────────────────────
while True:
    try:
        pilih_film = int(input("\nPilih Film (1-4) : "))

        if pilih_film in daftar_film:
            film_dipilih = daftar_film[pilih_film]
            break
        else:
            print("[ERROR] Pilihan film tidak tersedia!")

    except ValueError:
        print("[ERROR] Input harus berupa angka!")


# ─────── INPUT JUMLAH TIKET (BVA: 1-10 tiket) ────────────
while True:
    try:
        jumlah_tiket = int(input("Jumlah Tiket (1-10) : "))

        if 1 <= jumlah_tiket <= 10:
            break
        else:
            print("[ERROR] Jumlah tiket harus antara 1 - 10!")

    except ValueError:
        print("[ERROR] Input tiket harus berupa angka!")


# ─────────── PILIH METODE PEMBAYARAN ──────────
print("\n======================================")
print("         METODE PEMBAYARAN            ")
print("======================================")
print("1. Cash")
print("2. QRIS")
print("3. Debit")

while True:
    metode = input("Pilih metode pembayaran (1-3) : ")

    if metode == "1":
        metode_bayar = "Cash"
        break

    elif metode == "2":
        metode_bayar = "QRIS"
        break

    elif metode == "3":
        metode_bayar = "Debit"
        break

    else:
        print("[ERROR] Pilihan pembayaran tidak valid!")


# ──────────── CETAK STRUK ─────────────────────
print("\nMemproses pemesanan...\n")

print("======================================")
print("         STRUK PEMESANAN              ")
print("======================================")
print(f"Nama Pemesan     : {nama}")
print(f"Film Dipilih     : {film_dipilih}")
print(f"Jumlah Tiket     : {jumlah_tiket}")
print(f"Metode Bayar     : {metode_bayar}")
print("--------------------------------------")
print("STATUS            : PEMESANAN BERHASIL")
print("======================================")

print("\nTerima kasih telah memesan tiket 🎬")