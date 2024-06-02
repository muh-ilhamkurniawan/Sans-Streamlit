from altair import Orientation
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np 
from google_play_scraper import Sort, reviews, app  
import matplotlib.pyplot as plt
from datetime import datetime
from function import text_preprocessing_process, sentiment_analysis_lexicon_indonesia, generate_wordcloud
import re
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import os
import csv
# Load model yang sudah di-export
def load_view():    
    st.title('Cek Review')
    model = load_model('model.h5')
    # Load data yang digunakan saat melatih model (sebagai contoh)
    train_data = pd.read_csv('review_capcut.csv')
    st.header ('Prediksi Ulasan')
    # Contoh teks baru yang ingin diprediksi
    new_text = st.text_area("Masukkan teks yang ingin diprediksi:")

    # Tombol untuk memulai prediksi
    if st.button("Prediksi"):
        # Memeriksa apakah input kosong
        if not new_text:
            st.error("Ulasan diperlukan. Silakan masukkan ulasan yang ingin diprediksi")
        else:
            # Preprocessing teks baru menggunakan fungsi text_preprocessing_process
            processed_text = text_preprocessing_process(new_text)

            # Tokenisasi
            tokenizer = Tokenizer(num_words=5000, oov_token='<OOV>')
            tokenizer.fit_on_texts(train_data['clean_teks'])  # Menggunakan teks yang digunakan saat melatih model

            # Sequencing dan padding
            max_len = 100  # Sesuaikan dengan panjang yang digunakan saat melatih model
            new_text_seq = tokenizer.texts_to_sequences([processed_text])
            new_text_padded = pad_sequences(new_text_seq, maxlen=max_len, padding='post', truncating='post')

            # Prediksi probabilitas untuk setiap kelas
            predicted_probabilities = model.predict(new_text_padded)[0]


            # Mengambil indeks kelas dengan probabilitas tertinggi
            predicted_label = np.argmax(predicted_probabilities)

            # Mengubah label numerik menjadi label asli
            label_mapping = {0: 'negative', 1: 'neutral', 2: 'positive'}
            predicted_class = label_mapping[predicted_label]

            # Menampilkan hasil prediksi
            # st.write(f'Prediksi Sentimen Menggunakan Model: {predicted_class}')

            clean_text = text_preprocessing_process(new_text)
            # Melakukan analisis sentimen menggunakan fungsi yang telah Anda definisikan
            polarity_score, polarity = sentiment_analysis_lexicon_indonesia(clean_text)

            # Menampilkan hasil analisis sentimen
            # st.write(f'Prediksi Sentimen Menggunakan Polaritas: ({polarity_score})  {polarity}')
            st.write(f'Prediksi Sentimen : ({polarity_score})  {polarity}')