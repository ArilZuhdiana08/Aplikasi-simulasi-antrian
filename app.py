import streamlit as st
import matplotlib.pyplot as plt
import base64

# Fungsi untuk menambahkan background gambar lokal
def add_bg_from_local(image_file):
    with open(image_file, "rb") as file:
        encoded = base64.b64encode(file.read()).decode()
    page_bg = f"""
    <style>
    body {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-attachment: fixed;
        background-repeat: no-repeat;
    }}
    .block-container {{
        background-color: rgba(0, 0, 0, 0.6);
        padding: 2rem;
        border-radius: 1rem;
    }}
    h1, h2, h3, h4, h5, h6, p, label, .stNumberInput label {{
        color: white !important;
    }}
    .stNumberInput input {{
        background-color: #eef2f7;
        color: #000000;
        font-weight: 500;
    }}
    </style>
    """
    st.markdown(page_bg, unsafe_allow_html=True)

# Tambahkan background papan tulis
add_bg_from_local("image/papan.jpg")

# Konfigurasi halaman
st.set_page_config(page_title="Simulasi Antrian M/M/1", page_icon="📊", layout="centered")

# Judul utama
st.markdown("<h1 style='text-align: center;'>📊 Aplikasi Simulasi Antrian M/M/1</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>🔁 Hitung performa sistem antrian dengan visualisasi interaktif</p>", unsafe_allow_html=True)

# Deskripsi
st.markdown("### 📘 Deskripsi")
st.info("Aplikasi ini digunakan untuk menghitung rata-rata waktu tunggu, jumlah pelanggan dalam sistem, dan tingkat utilisasi layanan berdasarkan model antrian **M/M/1**.")

# Input user
st.markdown("### 🧮 Masukkan Parameter")
col1, col2 = st.columns(2)
with col1:
    λ = st.number_input("Rata-rata kedatangan (λ)", min_value=0.0, value=5.0, step=0.1, format="%.2f")
with col2:
    μ = st.number_input("Rata-rata layanan (μ)", min_value=0.0, value=8.0, step=0.1, format="%.2f")

# Proses perhitungan
if λ > 0 and μ > 0 and λ < μ:
    ρ = λ / μ
    L = λ / (μ - λ)
    Lq = λ**2 / (μ * (μ - λ))
    W = 1 / (μ - λ)
    Wq = λ / (μ * (μ - λ))

    # Tampilkan hasil
    st.markdown("### ✅ Hasil Perhitungan")
    st.success(f"**Utilisasi (ρ):** {ρ:.2f}")
    st.success(f"**Jumlah rata-rata pelanggan (L):** {L:.2f}")
    st.success(f"**Jumlah rata-rata dalam antrian (Lq):** {Lq:.2f}")
    st.success(f"**Waktu rata-rata dalam sistem (W):** {W:.2f} satuan waktu")
    st.success(f"**Waktu rata-rata dalam antrian (Wq):** {Wq:.2f} satuan waktu")

    # Visualisasi
    st.markdown("### 📈 Visualisasi Komponen Antrian")
    fig, ax = plt.subplots(figsize=(6, 4))
    names = ['L', 'Lq', 'W', 'Wq']
    values = [L, Lq, W, Wq]
    bar = ax.bar(names, values, color=['#0072f5', '#00c49a', '#f08080', '#f4d35e'])
    ax.set_ylabel("Nilai")
    ax.set_title("Diagram Komponen Antrian")
    st.pyplot(fig)

elif λ >= μ and λ > 0 and μ > 0:
    st.error("⚠️ λ harus lebih kecil dari μ agar sistem antrian stabil.")