import streamlit as st
import time

# ──────────── KONFIGURASI HALAMAN ───────────────────
st.set_page_config(page_title="Cinema XXI Booking System", page_icon="🎬", layout="centered")

st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #e50914;
        color: white;
    }
    .stTextInput>div>div>input {
        color: #f1f1f1;
    }
    .ticket-box {
        border: 2px dashed #f1c40f;
        padding: 20px;
        border-radius: 10px;
        background-color: #1c1c1c;
    }
    </style>
    """, unsafe_allow_html=True)

# ───────────────────── DATA PROGRAM ───────────────────
USERNAME_BENAR = "admin"
PASSWORD_BENAR = "123"
DAFTAR_FILM = {
    1: "Avengers: Endgame",
    2: "Interstellar",
    3: "Frozen II",
    4: "Spider-Man: No Way Home"
}

# ─── INISIALISASI SESSION STATE (STATE TRANSITION) ────
if 'state' not in st.session_state:
    st.session_state.state = "LOGIN"
if 'user_data' not in st.session_state:
    st.session_state.user_data = {}

# ─────────────── FUNGSI NAVIGASI ──────────────────────
def pindah_state(nama_state):
    st.session_state.state = nama_state
    st.rerun()

# ──────────────────────── STATE: LOGIN ───────────────────────────────────────── 
if st.session_state.state == "LOGIN":
    st.image("cinema.png", use_container_width=True)
    st.title("Login Bioskop Cinema XXI")
    
    with st.container():
        username = st.text_input("Username", placeholder="Masukkan username admin")
        password = st.text_input("Password", type="password", placeholder="Masukkan password")
        
        if st.button("Login"):
            if username == USERNAME_BENAR and password == PASSWORD_BENAR:
                st.success("Login Berhasil!")
                time.sleep(1)
                pindah_state("PEMESANAN")
            else:
                st.error("Username atau Password salah!")


# ──────────── STATE: PEMESANAN (Nama, Film, Tiket, Bayar) ───────────────────
elif st.session_state.state == "PEMESANAN":
    st.title("Form Pemesanan Tiket 🎬")
    
    with st.form("form_pesan"):
        nama = st.text_input("Nama Pemesan", placeholder="Contoh: Budi Santoso")
        
        col1, col2 = st.columns(2)
        with col1:
            film = st.selectbox("Pilih Film", options=list(DAFTAR_FILM.values()))
        with col2:
            # IMPLEMENTASI BVA (1-10)
            jumlah = st.number_input("Jumlah Tiket (1-10)", min_value=0, max_value=15, step=1, value=1)
            st.caption("BVA Test: Batas valid 1-10")

        metode = st.radio("Metode Pembayaran", ["Cash", "QRIS", "Debit"], horizontal=True)
        
        submit = st.form_submit_button("Proses Pemesanan")

        if submit:
            # Validasi State Transition & BVA
            if not nama.strip():
                st.warning("Nama tidak boleh kosong!")
            elif jumlah < 1 or jumlah > 10:
                st.error(f"Gagal! Jumlah tiket {jumlah} tidak valid. (BVA: Harus 1-10)")
            else:
                st.session_state.user_data = {
                    "nama": nama,
                    "film": film,
                    "jumlah": jumlah,
                    "metode": metode
                }
                with st.spinner('Memproses Struk...'):
                    time.sleep(2)
                pindah_state("STRUK")

    if st.button("⬅ Logout"):
        pindah_state("LOGIN")

# ──────────────────────── STATE: STRUK (HASIL AKHIR) ───────────────────────────────
elif st.session_state.state == "STRUK":
    st.balloons()
    st.title("Struk Pemesanan Anda 🍿")
    
    data = st.session_state.user_data
    
    st.markdown(f"""
    <div class="ticket-box">
        <h2 style='text-align: center; color: #f1c40f;'>CINEMA XXI TICKET</h2>
        <hr>
        <p><b>Nama Pemesan :</b> {data['nama']}</p>
        <p><b>Film Dipilih :</b> {data['film']}</p>
        <p><b>Jumlah Tiket :</b> {data['jumlah']} Tiket</p>
        <p><b>Metode Bayar :</b> {data['metode']}</p>
        <hr>
        <h3 style='text-align: center; color: #2ecc71;'>STATUS: PEMESANAN BERHASIL</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("Silakan tunjukkan struk ini ke petugas bioskop.")
    
    if st.button("Pesan Tiket Lagi"):
        pindah_state("PEMESANAN")