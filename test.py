import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

# Halaman Navigasi
st.set_page_config(page_title="Website Streamlit", layout="wide")

# CSS
st.markdown(
    """
    <style>
    [data-testid="sidebar"] {
        background-color: #2f3640;
        padding: 20px;
        color: #f5f6fa;
        border-right: 2px solid #353b48;
        width: 250px;
    }
    [data-testid="mainmenu"] {
        display: none;
    }
    [data-testid="sidebar"] h1 {
        color: #00a8ff;
        font-size: 22px;
        font-weight: bold;
        text-align: center;
    }
    [data-testid="sidebar"] .stRadio > div {
        display: flex;
        flex-direction: column;
        gap: 15px;
        padding-left: 10px;
    }
    .header {
        font-size: 50px;
        font-weight: bold;
        background: -webkit-linear-gradient(45deg, #ff6b6b, #feca57);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .centered {
        display: flex;
        justify-content: center;
        align-items: center;
        text-align: center;
    }
    .btn-primary {
        background-color: #00a8ff;
        color: white;
        padding: 10px 20px;
        border-radius: 5px;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Inisialisasi Session State untuk data
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame({
        "Nama": ["Ali", "Budi", "Citra"],
        "Usia": [25, 30, 22],
        "Pekerjaan": ["Mahasiswa", "Pekerja", "Wiraswasta"]
    })

# Sidebar Navigasi
st.sidebar.title("\u2728 Navigasi \u2728")
menu = st.sidebar.radio(
    "\U0001F50D Pilih Halaman:",
    ["Home", "Data", "Visualisasi", "Tentang"],
    index=0
)

# Halaman Home
if menu == "Home":
    st.markdown(
        """
        <style>
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .animated-header {
            animation: fadeIn 1s ease-in-out;
            font-size: 50px;
            font-weight: bold;
            background: linear-gradient(45deg, #ff6b6b, #48dbfb);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
        }
        .subheading {
            font-size: 24px;
            font-weight: 500;
            text-align: center;
            color: #57606f;
        }
        .features {
            display: flex;
            justify-content: space-around;
            margin: 20px 0;
        }
        .feature {
            text-align: center;
            padding: 10px;
            flex: 1;
        }
        .feature-icon {
            font-size: 40px;
            color: #1dd1a1;
        }
        .feature-title {
            font-size: 18px;
            font-weight: bold;
            color: #2f3640;
            margin-top: 10px;
        }
        .image-container {
            display: flex;
            justify-content: center;
            margin-top: 20px;
        }
        .image-container img {
            border: 5px solid #feca57;
            border-radius: 15px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="animated-header">Selamat Datang di Website Streamlit</div>',
                unsafe_allow_html=True)
    st.markdown('<div class="subheading">Website sederhana namun menarik menggunakan Streamlit</div>',
                unsafe_allow_html=True)

    st.markdown(
        """
        <div class="features">
            <div class="feature">
                <div class="feature-icon">📝</div>
                <div class="feature-title">Input Data</div>
            </div>
            <div class="feature">
                <div class="feature-icon">📊</div>
                <div class="feature-title">Tabel Interaktif</div>
            </div>
            <div class="feature">
                <div class="feature-icon">📈</div>
                <div class="feature-title">Visualisasi Grafik</div>
            </div>
            <div class="feature">
                <div class="feature-icon">ℹ️</div>
                <div class="feature-title">Halaman Informasi</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="image-container"><img src="https://images.unsplash.com/photo-1503676260728-1c00da094a0b" alt="Mahasiswa bekerja di depan laptop" style="width: 70%;"></div>', unsafe_allow_html=True)


# Halaman Data
elif menu == "Data":
    st.title("Input dan Tabel Data")
    st.subheader("Tambahkan data Anda di sini")

    # Input data pengguna
    with st.form("data_form"):
        nama = st.text_input("Nama:")
        usia = st.number_input("Usia:", min_value=1, max_value=120, step=1)
        pekerjaan = st.selectbox(
            "Pekerjaan:", ["Mahasiswa", "Pekerja", "Wiraswasta", "Lainnya"])
        submitted = st.form_submit_button("Submit")

        if submitted:
            new_row = {"Nama": nama, "Usia": usia, "Pekerjaan": pekerjaan}
            st.session_state.data = pd.concat(
                [st.session_state.data, pd.DataFrame([new_row])], ignore_index=True
            )
            st.success("\u2705 Data berhasil disimpan!")

    # Tabel Data
    st.subheader("Tabel Data")
    st.dataframe(st.session_state.data, use_container_width=True)

# Halaman Visualisasi
elif menu == "Visualisasi":
    st.title("Visualisasi Data")
    st.subheader("Tampilkan data dalam bentuk grafik")

    tab1, tab2 = st.tabs(["Bar Chart", "Pie Chart"])

    with tab1:
        st.subheader("Bar Chart Usia")
        usia_counts = st.session_state.data["Usia"].value_counts(
        ).reset_index()
        # Ganti nama kolom untuk kejelasan
        usia_counts.columns = ["Usia", "count"]
        fig = px.bar(
            usia_counts,
            x="Usia", y="count",
            labels={"Usia": "Usia", "count": "Jumlah"},
            color_discrete_sequence=["#48dbfb"]
        )
        st.plotly_chart(fig, use_container_width=True)

    with tab2:
        st.subheader("Pie Chart Pekerjaan")
        fig = px.pie(
            st.session_state.data, names="Pekerjaan",
            color_discrete_sequence=["#ff6b6b",
                                     "#48dbfb", "#1dd1a1", "#feca57"]
        )
        st.plotly_chart(fig, use_container_width=True)

# Halaman Tentang
elif menu == "Tentang":
    st.title("Tentang Website")
    st.markdown("""Website ini dibuat menggunakan **Streamlit**, 
        sebuah framework Python untuk membuat aplikasi web interaktif dengan mudah.""")
    st.markdown("""
    **Fitur yang digunakan:**
    <ul>
        <li>Sidebar navigasi</li>
        <li>Input dan Tabel Data</li>
        <li>Visualisasi menggunakan Plotly</li>
        <li>Markdown dan gaya teks</li>
    </ul>
    """, unsafe_allow_html=True)
    st.info("Dibuat oleh **Rizqi Reza Danuarta**", icon="ℹ️")
