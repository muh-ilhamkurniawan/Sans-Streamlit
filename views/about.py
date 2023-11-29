# about.py
import streamlit as st
import cv2

def load_view():    
    st.markdown("<h1 style='text-align: center; margin-bottom: 30px; color: #034832;'>Meet Our Team</h1>", unsafe_allow_html=True)

    img = cv2.imread('profil.png')

    col1, col2, col3, col4, col5 = st.columns([1,1,1,1,1])
    col1.image(img, use_column_width=True)
    col1.markdown("<h4 style='text-align: center; color: #034832;'>Hafiz</h4>", unsafe_allow_html=True)
    col1.markdown("<p style='text-align: center;'>Universitas</p>", unsafe_allow_html=True)
    col2.image(img, use_column_width=True)
    col2.markdown("<h4 style='text-align: center;'>Tata</h4>", unsafe_allow_html=True)
    col2.markdown("<p style='text-align: center;'>Universitas</p>", unsafe_allow_html=True)
    col3.image(img, use_column_width=True)
    col3.markdown("<h4 style='text-align: center;'>Muhammad Ilham Kurniawan</h4>", unsafe_allow_html=True)
    col3.markdown("<p style='text-align: center;'>Universitas Jenderal Soedirman</p>", unsafe_allow_html=True)
    col4.image(img, use_column_width=True)
    col4.markdown("<h4 style='text-align: center;'>Fajar</h4>", unsafe_allow_html=True)
    col4.markdown("<p style='text-align: center;'>Universitas</p>", unsafe_allow_html=True)
    col5.image(img, use_column_width=True)
    col5.markdown("<h4 style='text-align: center;'>Fathur</h4>", unsafe_allow_html=True)
    col5.markdown("<p style='text-align: center;'>Universitas</p>", unsafe_allow_html=True)
