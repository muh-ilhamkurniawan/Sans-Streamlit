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
def load_view():    
    st.title('Cek Aplikasi')
    # Main Streamlit app
    st.header("Play Store Reviews Apk")

    # Input link aplikasi dari pengguna
    app_link = st.text_input("Masukkan link aplikasi")
    app_number = st.slider("Masukkan jumlah", 1, 100)
    def extract_package_name(url):
        pattern = r'id=([^\&]+)'
        match = re.search(pattern, url)
        
        if match:
            return match.group(1)

        return None
    app_link = extract_package_name(app_link)
    # Tombol untuk memulai review dan informasi aplikasi
    if st.button("Mulai Review"):
        # Memeriksa apakah input kosong
        if not app_link:
            st.error("Link Aplikasi diperlukan. Silakan masukkan link aplikasi.")
        else:
            # Implementasi fungsi reviews
            result_reviews, continuation_token = reviews(
                app_link,
                lang='id',
                country='id',
                sort=Sort.MOST_RELEVANT,
                count=app_number,
                filter_score_with=None
            )

            # Implementasi fungsi app
            result_app = app(
                app_link,
                lang='id',
                country='id',
            )

            # DataFrame untuk hasil reviews
            df_reviews = pd.DataFrame(np.array(result_reviews), columns=['review'])
            df_reviews = df_reviews.join(pd.DataFrame(df_reviews.pop('review').tolist()))
            sorted_df_reviews = df_reviews[['userName', 'score', 'at', 'content']]

            # DataFrame untuk hasil app
            df_app = pd.DataFrame.from_dict(result_app, orient='index', columns=['value'])
            st.subheader("Informasi Aplikasi:")
            st.dataframe(df_app)

            # Menampilkan hasil review
            st.subheader("Daftar Review:")
            st.dataframe(sorted_df_reviews)

            # Menambahkan kolom clean_teks pada tabel sorted_df_reviews
            sorted_df_reviews['clean_teks'] = sorted_df_reviews['content'].apply(text_preprocessing_process)

            # Hasil dari penentuan polaritas sentimen tweet
            results = sorted_df_reviews['clean_teks'].apply(sentiment_analysis_lexicon_indonesia)
            results = list(zip(*results))
            sorted_df_reviews['polarity_score'] = results[0]
            sorted_df_reviews['polarity'] = results[1]

            tab1, tab2, tab3 = st.tabs(["Clean Text", "WordCloud", "Pie Chart"])

            with tab1:
                 # Menampilkan hasil review setelah preprocessing dan analisis sentimen
                st.subheader("Daftar Review setelah Preprocessing Data dan Pengecekan Sentimen Analisis:")
                st.dataframe(sorted_df_reviews[['userName', 'score', 'at', 'content', 'clean_teks', 'polarity_score', 'polarity']])

            with tab2:
                # Tampilkan WordCloud dari kolom 'clean_teks'
                if 'clean_teks' in sorted_df_reviews.columns:
                    clean_text_combined = ' '.join(' '.join(map(str, text)) for text in sorted_df_reviews['clean_teks'])
                    wordcloud = generate_wordcloud(clean_text_combined)

                    # Tampilkan WordCloud menggunakan Matplotlib
                    st.subheader("WordCloud Review:")
                    fig, ax = plt.subplots(figsize=(10, 5))
                    ax.imshow(wordcloud, interpolation='bilinear')
                    ax.axis('off')
                    st.pyplot(fig)
                    plt.close()  # Tutup plot Matplotlib
                else:
                    st.warning("Kolom 'clean_teks' tidak ditemukan dalam DataFrame.")

            with tab3:
                # Hitung jumlah masing-masing nilai di kolom 'polarity'
                polarity_counts = sorted_df_reviews['polarity'].value_counts()

                # Fungsi untuk membuat pie chart
                def create_pie_chart(polarity_counts):
                    fig, ax = plt.subplots()
                    ax.pie(polarity_counts, labels=polarity_counts.index, autopct='%1.1f%%', startangle=90)
                    ax.axis('equal')  # Memastikan pie chart berbentuk lingkaran
                    return fig

                # Main Streamlit app
                st.subheader("Diagram Pie dari Distribusi Sentimen Analis Review")

                # Menampilkan pie chart
                st.pyplot(create_pie_chart(polarity_counts))
