import streamlit as st
import pandas as pd

# Load dataset
df = pd.read_csv("allShades.csv")

# Bersihkan data
df = df.drop_duplicates()

# Kalau Skin_Tone belum ada, buat dari kolom 'name'
if "Skin_Tone" not in df.columns or df["Skin_Tone"].isnull().all():
    def categorize_tone(text):
        text = str(text).lower()
        if "light" in text or "ivory" in text or "fair" in text or "porcelain" in text:
            return "Light"
        elif "medium" in text or "beige" in text or "tan" in text:
            return "Medium"
        elif "deep" in text or "dark" in text or "warm" in text:
            return "Dark"
        else:
            return "Other"
    df["Skin_Tone"] = df["name"].apply(categorize_tone)

# ================= Streamlit UI =================
st.title("💄 Foundation Shade Recommendation")

# Input user
skin_tone = st.selectbox("Pilih Skin Tone:", df["Skin_Tone"].unique())
brand_pref = st.selectbox("Pilih Brand:", df["brand"].unique())

# Filter rekomendasi
recommendations = df[(df["Skin_Tone"] == skin_tone) & (df["brand"] == brand_pref)]

# Tampilkan hasil
st.subheader("Rekomendasi Produk:")
st.write(recommendations[["product", "name", "description"]].head(10))

# Tambahkan gambar kalau ada kolom imgSrc
st.subheader("Preview Gambar Shade:")
for idx, row in recommendations.head(5).iterrows():
    st.image(row["imgSrc"], caption=row["name"])
