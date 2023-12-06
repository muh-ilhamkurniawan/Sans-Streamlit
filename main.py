import streamlit as st
import utils as utl
from views import home,about,options,configuration,info_tiktok,cek_review,cek_aplikasi
# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="SansAPK", page_icon=":tada:", layout="wide")
st.set_option('deprecation.showPyplotGlobalUse', False)
utl.inject_custom_css()
utl.navbar_component()
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-color: #ffff;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
color: black;
}}


[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

def navigation():
    route = utl.get_current_route()
    hide_streamlit_style = """
    <style>
        #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 0rem;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
    </style>

    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    if route == "home":
        home.load_view()
    elif route == "about":
        about.load_view()
    elif route == "info tiktok":
        info_tiktok.load_view()
    elif route == "cek review":
        cek_review.load_view()
    elif route == "cek aplikasi":
        cek_aplikasi.load_view()
    elif route == "options":
        options.load_view()
    elif route == "configuration":
        configuration.load_view()
    elif route == None:
        home.load_view()
        
navigation()