# ====================================================================================================
# ♾️ LOYIHA: KGO Group Global Systems & GeminGPT Cosmic AI
# 👤 ASOSCHI: KAMRON XUDAYNAZAROV & KGO UZTEAM
# ====================================================================================================
import streamlit as st
import time
import random
import urllib.parse
import re

# --- [SECTION 1] GLOBAL CONFIG ---
st.set_page_config(
    page_title="KGO Group | Cosmic Systems",
    page_icon="♾️",
    layout="wide"
)

# --- [SECTION 2] ULTRA-BRIGHT CYBER ANIMATED CSS ---
st.markdown("""
<style>
     /* Asosiy fon to'q ko'k/qora */
     .stApp {
         background-color: #0b0f19 !important;
         font-family: 'Inter', sans-serif;
     }
     
     /* BARCHA MATNLARNI MAJBURIY OQ VA TINIQ QILISH */
     h1, h2, h3, h4, h5, h6, p, span, label, li {
         color: #ffffff !important;
     }
     
     /* Kiber qutilar */
     .cyber-card {
         background: rgba(30, 41, 59, 0.7) !important;
         padding: 25px;
         border-radius: 15px;
         border: 2px solid #2563eb;
         box-shadow: 0 0 15px rgba(37, 99, 235, 0.3);
         margin-bottom: 20px;
     }
     
     /* Tariflar qutisi */
     .tariff-card {
         background: #111827 !important;
         padding: 20px;
         border-radius: 12px;
         border-top: 4px solid #ff007f;
         box-shadow: 0 4px 10px rgba(0,0,0,0.5);
         text-align: center;
     }

     /* Chat xabarlari matni tiniqligi */
     .stChatMessage {
         background-color: #1e293b !important;
         border-radius: 10px;
         margin-bottom: 10px;
         padding: 10px;
     }
     .stChatMessage p, .stChatMessage span, .stChatMessage div {
         color: #ffffff !important;
         font-size: 16px !important;
     }

     /* Chat kiritish oynasi */
     .stChatInputContainer textarea {
         color: #ffffff !important;
         background-color: #1e293b !important;
     }
     .stChatInputContainer {
        border: 2px solid #2563eb !important; 
        border-radius: 12px !important;
        background-color: #1e293b !important; 
        box-shadow: 0 0 15px rgba(37, 99, 235, 0.4) !important; 
     }
     
     /* 🔥 TUGMALAR USTIDAN O'TGANDA HARAKATLANISH VA NEON EFFEKTI (HOVER ANIMATION) */
     button, .stDownloadButton, .stLinkButton a {
         transition: all 0.3s ease-in-out !important;
     }
     button:hover, .stLinkButton a:hover {
         transform: scale(1.05) !important; /* Kattalashish harakati */
         box-shadow: 0 0 25px #00d2ff !important; /* Atrofida neon nur taralishi */
         border-color: #00d2ff !important;
     }
     
     /* Pastki qism */
     .footer-text {
         text-align: center; 
         color: #94a3b8 !important; 
         font-size: 14px; 
         margin-top: 50px;
         border-top: 1px solid rgba(255,255,255,0.1);
         padding-top: 20px;
     }
</style>
""", unsafe_allow_html=True)

# --- [SECTION 3] HEADLINE & HELP NAVIGATION ---
col_logo, col_space, col_help = st.columns([3, 1.5, 2])

with col_logo:
    st.markdown("<h1 style='color: #2563eb; font-weight:bold; margin-bottom:0;'>KGO Group Global Systems ♾️</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #00d2ff !important; font-size:16px;'>Kelajak texnologiyalari va raqamli innovatsiyalar markazi</p>", unsafe_allow_html=True)

with col_help:
    st.write("") 
    st.link_button("❓ KGO Texnik Yordam Markazi", "https://xudaynazarovkamron2106-ivgun.wordpress.com/", type="primary", use_container_width=True)

st.markdown("---")

# --- [SECTION 4] MAIN CONTENT (KOMPANIYA HAQIDA) ---
st.markdown("<h2 style='text-align:center;'>🚀 Kompaniya va Tizim Haqida</h2>", unsafe_allow_html=True)
st.write("")

col_left, col_right = st.columns(2)

with col_left:
    st.markdown("""
    <div class="cyber-card">
        <h3>🌌 KGO UzTeam Nima Bilan Shug'ullanadi?</h3>
        <p><b>KGO Group Global Systems</b> — zamonaviy dasturiy ta'minotlar, yuqori intellektli bot tizimlari, kiber-xavfsizlik yechimlari va murakkab veb-loyihalarni noldan yaratuvchi global raqamli shtabdir.</p>
        <p>Biz oddiy g'oyalarni eng mukammal kodlar yordamida haqiqatga aylantiramiz.</p>
    </div>
    """, unsafe_allow_html=True)

with col_right:
    st.markdown("""
    <div class="cyber-card">
        <h3>💡 Bizning Asosiy Tamoyillarimiz</h3>
        <ul>
            <li><b>K (Kamron)</b> — Jamoa asoschisi,
