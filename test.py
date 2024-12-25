import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Halaman Navigasi
st.set_page_config(page_title="Website Streamlit", layout="wide")

# CSS untuk mempercantik sidebar
st.markdown(
    """
    <style>
    [data-testid="sidebar"] {
        background-color: #2f3640;
        padding: 20px;
        color: #f5f6fa;
        border-right: 2px solid #353b48;
    }
    [data-testid="sidebar"] h1 {
        color: #00a8ff;
        font-size: 22px;
        font-weight: bold;
        text-align: center;
    }
    [data-testid="sidebar"] .stRadio > label {
        display: block;
        font-size: 18px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    [data-testid="sidebar"] .stRadio > div {
        display: flex;
        flex-direction: column;
        gap: 15px;
        padding-left: 10px;
    }
    [data-testid="stSidebar"] .css-1y4p8pa {
        font-size: 16px;
        font-weight: bold;
    }
    [data-testid="stSidebar"] label {
        color: #f5f6fa;
        font-size: 16px;
    }
    .stRadio div div {
        align-items: flex-start;
    }
    </style>
    """,
    unsafe_allow_html=True
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
    "\U0001F50D Pilih Halaman:",  # Unicode fixed
    ["Home", "Data", "Visualisasi", "Tentang"],
    index=0
)

# Halaman Home
if menu == "Home":
    st.markdown(
        """
        <style>
        .header {
            font-size: 50px;
            font-weight: bold;
            background: -webkit-linear-gradient(45deg, #ff6b6b, #feca57);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown('<div class="header">Selamat Datang di Website Streamlit</div>',
                unsafe_allow_html=True)
    st.subheader("Website sederhana namun menarik menggunakan Streamlit")
    st.write("""
        **Fitur-fitur utama:**
        - Input data pengguna
        - Tabel data interaktif
        - Visualisasi grafik
        - Halaman informasi
    """)

    st.image(
        "https://images.unsplash.com/photo-1503676260728-1c00da094a0b",
        caption="Mahasiswa bekerja di depan laptop",
        use_container_width=True
    )

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
            # Tambahkan data baru ke Session State
            new_row = {"Nama": nama, "Usia": usia, "Pekerjaan": pekerjaan}
            st.session_state.data = pd.concat(
                [st.session_state.data, pd.DataFrame([new_row])], ignore_index=True
            )
            st.success("\u2705 Data berhasil disimpan!")

    # Tabel Data
    st.subheader("Tabel Data")
    st.table(st.session_state.data)

# Halaman Visualisasi
elif menu == "Visualisasi":
    st.title("Visualisasi Data")
    st.subheader("Tampilkan data dalam bentuk grafik")

    # Pilih jenis grafik
    graph_type = st.radio("Pilih jenis grafik:", ["Bar Chart", "Pie Chart"])

    if graph_type == "Bar Chart":
        st.subheader("Bar Chart Usia")
        fig, ax = plt.subplots()
        st.session_state.data["Usia"].value_counts().plot(
            kind="bar", ax=ax, color="#48dbfb", edgecolor="#1dd1a1")
        ax.set_title("Distribusi Usia", fontsize=16, color="#ff6b6b")
        ax.set_xlabel("Usia", fontsize=12)
        ax.set_ylabel("Jumlah", fontsize=12)
        st.pyplot(fig)

    elif graph_type == "Pie Chart":
        st.subheader("Pie Chart Pekerjaan")
        fig, ax = plt.subplots()
        st.session_state.data["Pekerjaan"].value_counts().plot(
            kind="pie", ax=ax, autopct='%1.1f%%',
            colors=["#ff6b6b", "#48dbfb", "#1dd1a1", "#feca57"],
            startangle=90, wedgeprops={"edgecolor": "black"}
        )
        ax.set_title("Distribusi Pekerjaan", fontsize=16, color="#ff6b6b")
        ax.set_ylabel("")
        st.pyplot(fig)

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
        <li>Visualisasi menggunakan Matplotlib</li>
        <li>Markdown dan gaya teks</li>
    </ul>
    """, unsafe_allow_html=True)
    st.info("Dibuat oleh **Rizqi Reza Danuarta**", icon="ℹ️")
