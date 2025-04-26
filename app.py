import streamlit as st

# Judul Aplikasi
st.title("🍎 Aplikasi Asupan Gizi & Nutrisi Sehat")

st.markdown("""
Aplikasi ini menghitung kebutuhan kalori harian, makronutrisi (protein, lemak, karbohidrat), memberikan informasi makanan sehat vs tidak sehat, dan tips pencegahan kurang gizi.
""")

# Input Data Pengguna
st.header("🔍 Masukkan Data Pribadimu")
nama = st.text_input("Nama")
usia = st.number_input("Usia (tahun)", min_value=1, max_value=100)
berat = st.number_input("Berat Badan (kg)", min_value=1.0)
tinggi = st.number_input("Tinggi Badan (cm)", min_value=30.0)
jenis_kelamin = st.selectbox("Jenis Kelamin", ["Laki-laki", "Perempuan"])
aktivitas = st.selectbox("Tingkat Aktivitas Fisik", ["Rendah", "Sedang", "Tinggi"])

# Fungsi menghitung BMR dan kebutuhan kalori
def hitung_kalori(berat, tinggi, usia, jenis_kelamin, aktivitas):
    if jenis_kelamin == "Laki-laki":
        bmr = 66 + (13.7 * berat) + (5 * tinggi) - (6.8 * usia)
    else:
        bmr = 655 + (9.6 * berat) + (1.8 * tinggi) - (4.7 * usia)

    if aktivitas == "Rendah":
        kalori = bmr * 1.2
    elif aktivitas == "Sedang":
        kalori = bmr * 1.55
    else:
        kalori = bmr * 1.9

    return round(kalori)

# Fungsi membagi makronutrien dari total kalori
def hitung_makronutrien(kalori):
    protein_kal = kalori * 0.15  # 15% protein
    lemak_kal = kalori * 0.25    # 25% lemak
    karbo_kal = kalori * 0.60    # 60% karbohidrat

    protein_gram = round(protein_kal / 4)  # 1 gram protein = 4 kkal
    lemak_gram = round(lemak_kal / 9)      # 1 gram lemak = 9 kkal
    karbo_gram = round(karbo_kal / 4)      # 1 gram karbohidrat = 4 kkal

    return protein_gram, lemak_gram, karbo_gram

# Tombol Proses
if st.button("Hitung Asupan Gizi"):
    kebutuhan_kalori = hitung_kalori(berat, tinggi, usia, jenis_kelamin, aktivitas)
    protein, lemak, karbo = hitung_makronutrien(kebutuhan_kalori)

    st.success(f"Halo {nama}, berikut kebutuhan harianmu:")
    st.write(f"🔥 Kalori: **{kebutuhan_kalori} kkal**")
    st.write(f"🥩 Protein: **{protein} gram**")
    st.write(f"🥑 Lemak: **{lemak} gram**")
    st.write(f"🍚 Karbohidrat: **{karbo} gram**")

    # Tampilkan tips pencegahan
    st.subheader("🛡️ Tips Pencegahan Kekurangan Nutrisi:")
    st.markdown("""
    - Konsumsi makanan beragam (nasi, sayur, buah, lauk-pauk).
    - Perbanyak protein dari telur, ikan, daging, tahu, tempe.
    - Makan buah dan sayuran segar setiap hari.
    - Minum cukup air putih.
    - Hindari diet ekstrem tanpa pengawasan ahli.
    - Lakukan pemeriksaan rutin berat badan dan status gizi.
    """)

# Informasi Makanan Sehat vs Tidak Sehat
st.header("🥗 Makanan Sehat vs 🍔 Makanan Tidak Sehat")

col1, col2 = st.columns(2)

with col1:
    st.subheader("✅ Makanan Sehat")
    st.markdown("""
    - Sayuran segar (bayam, brokoli, wortel)
    - Buah segar (apel, pisang, pepaya)
    - Ikan laut (salmon, sarden)
    - Telur, ayam tanpa kulit
    - Kacang-kacangan (kacang almond, kacang tanah)
    - Karbohidrat kompleks (beras merah, oats)
    - Air putih minimal 8 gelas sehari
    """)

with col2:
    st.subheader("🚫 Makanan Tidak Sehat")
    st.markdown("""
    - Gorengan berlebihan
    - Minuman bersoda & beralkohol
    - Makanan cepat saji (burger, pizza, fried chicken)
    - Snack kemasan tinggi gula dan MSG
    - Mie instan tanpa tambahan sayur dan protein
    """)

# Rekomendasi Kalori dan Makronutrisi berdasarkan Usia
st.header("📊 Rekomendasi Umum Kalori & Makronutrien Berdasarkan Usia")

st.markdown("""
# Update Tabel Rekomendasi Kalori dan Makronutrien Berdasarkan Usia
st.header("📊 Rekomendasi Kebutuhan Gizi Berdasarkan Usia (PMK No. 28 Tahun 2019)")
| Kelompok Umur | Energi (kkal) | Protein (g) | Lemak (g) | Karbohidrat (g) |
|:--------------|:-------------:|:-----------:|:---------:|:---------------:|
| 1–3 tahun     | 1350          | 20          | 45        | 215             |
| 4–6 tahun     | 1400          | 25          | 50        | 220             |
| 7–9 tahun     | 1650          | 40          | 55        | 250             |
| **Laki-laki** |||||
| 10–12 tahun   | 2000          | 50          | 65        | 300             |
| 13–15 tahun   | 2400          | 70          | 80        | 350             |
| 16–18 tahun   | 2650          | 75          | 85        | 400             |
| 19–29 tahun   | 2650          | 65          | 75        | 430             |
| 30–49 tahun   | 2550          | 65          | 70        | 415             |
| 50–64 tahun   | 2150          | 60          | 60        | 340             |
| 65–80 tahun   | 1800          | 60          | 50        | 275             |
| >80 tahun     | 1600          | 64          | 45        | 250             |
| **Perempuan** |||||
| 10–12 tahun   | 1900          | 55          | 60        | 280             |
| 13–15 tahun   | 2050          | 65          | 70        | 300             |
| 16–18 tahun   | 2100          | 65          | 70        | 300             |
| 19–29 tahun   | 2250          | 60          | 65        | 360             |
| 30–49 tahun   | 2150          | 60          | 60        | 340             |
| 50–64 tahun   | 1800          | 50          | 50        | 280             |
| 65–80 tahun   | 1550          | 58          | 45        | 230             |
| >80 tahun     | 1400          | 58          | 40        | 200             |


""")


# Footer
st.caption("http://hukor.kemkes.go.id/uploads/produk_hukum/PMK_No__28_Th_2019_ttg_Angka_Kecukupan_Gizi_Yang_Dianjurkan_Untuk_Masyarakat_Indonesia.pdf")

