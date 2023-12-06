# about.py
import streamlit as st
import cv2

def load_view():    
    st.markdown("<h1 style='text-align: center; margin-bottom: 30px; color: #034832;'>Meet Our Team</h1>", unsafe_allow_html=True)

    imgfajar = cv2.imread('fajar.jpg')
    imgfathur = cv2.imread('fathur.jpg')
    imgilham = cv2.imread('ilham.jpg')
    imghafiz = cv2.imread('hafiz.jpg')
    imgtata = cv2.imread('tata.jpg')

    col1, col2, col3, col4, col5 = st.columns([1,1,1,1,1])

    # Fungsi untuk merubah gambar menjadi bulat
    def make_round(image):
        img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        img_round = cv2.circle(img_rgb, (img_rgb.shape[1]//2, img_rgb.shape[0]//2), min(img_rgb.shape)//2, (0, 0, 0), -1)
        
        return img_round    
        

    col1.image(make_round(imghafiz), use_column_width=True,)
    col1.markdown("<h4 style='text-align: center;'>Achmad Hafizh Choirul</h4>", unsafe_allow_html=True)

    col2.image(make_round(imgtata), use_column_width=True)
    col2.markdown("<h4 style='text-align: center;'>Oktavia Fauzaturroisiyah</h4>", unsafe_allow_html=True)

    col3.image(make_round(imgilham), use_column_width=True)
    col3.markdown("<h4 style='text-align: center;'>Muhammad Ilham Kurniawan</h4>", unsafe_allow_html=True)

    col4.image(make_round(imgfajar), use_column_width=True)
    col4.markdown("<h4 style='text-align: center;'>Mohamad Fajar</h4>", unsafe_allow_html=True)
    col5.image(make_round(imgfathur), use_column_width=True)

    col5.markdown("<h4 style='text-align: center;'>Fathur Rahmansyah Maulana Muhammad</h4>", unsafe_allow_html=True)

    col6, col7, col8, col9, col10 = st.columns([1,1,1,1,1])
        
    col6.markdown("<p style='text-align: center;  padding: 12px;'>Universitas PGRI ADI BUANA SURABAYA</p>", unsafe_allow_html=True)

    col7.markdown("<p style='text-align: center;  padding: 12px;'>Universitas Pembangunan Nasional “Veteran” Jawa Timur</p>", unsafe_allow_html=True)

    col8.markdown("<p style='text-align: center;  padding: 12px;'>Universitas Jenderal Soedirman</p>", unsafe_allow_html=True)

    col9.markdown("<p style='text-align: center;  padding: 12px;'>Universitas Ivet Semarang</p>", unsafe_allow_html=True)

    col10.markdown("<p style='text-align: center;  padding: 12px;'>Universitas Pembangunan Nasional “Veteran” Jawa Timur</p>", unsafe_allow_html=True)

