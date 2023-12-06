import streamlit as st

def load_view():
    # Menampilkan gambar dari file lokal
    with st.container():
        col1, col5 = st.columns([3,2])
        # col1.subheader("Hai, Selamat Datang di :wave:")
        col1.markdown("<h3 style='color: #034832;'>Hai, Selamat Datang di</h3>", unsafe_allow_html=True)
        col1.markdown("<span style='color: #034832; margin-top: -30px; font-weight: 1000; font-size: 90px; '>SANS APK</span>", unsafe_allow_html=True)
        col1.write(
            "Merupakan aplikasi Sentimen Analisis TikTok menggunakan Model LSTM berdasarkan review di Playstore. Dengan aplikasi ini pengguna dapat mengecek apakah sebuah review memiliki sentimen positif, netral, mmaupun negatif. Aplikasi ini juga dapat melihat informasi sentimen analisis dari aplikasi TikTok serta aplikasi lainnya di Playtore. Aplikasi ini merupakan hasil dari Capstone Project Kelompok 4 Atlas dari kegiatan Studi Independen Bersertifikat MSIB Kampus Merdeka di Orbit Future Academy Batch 5"
        )
        col1.write("[Learn More >](https://github.com/muh-ilhamkurniawan/Sans-Streamlit)")
        
        # Path ke file gambar lokal
        local_image_path = "logo.png"

        # Menampilkan gambar dari file lokal
        col5.image(local_image_path, width=200, output_format='auto', use_column_width=True)

