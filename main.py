import streamlit as st

# Sayt sozlamalari va sarlavhasi
st.set_page_config(page_title="KGO Help & UzTeam", page_icon="♾️", layout="wide")

# Kiber-uslub uchun to'q qora va neon rangli dizayn (CSS)
st.markdown("""
    <style>
    .main { background-color: #0d1117; color: #c9d1d9; }
    h1, h2, h3 { color: #ffffff !important; }
    .stTabs [data-baseweb="tab"] { color: #8b949e !important; font-size: 16px; }
    .stTabs [aria-selected="true"] { color: #00d2ff !important; font-weight: bold; }
    .kgo-box { background-color: #161b22; padding: 20px; border-radius: 10px; border-left: 5px solid #00d2ff; margin-bottom: 15px; }
    .kgo-package { background-color: #1f242c; padding: 15px; border-radius: 8px; border-top: 4px solid #ff007f; }
    </style>
""", unsafe_view_menu=True)

# --- TEPA QISM (HEADER) ---
st.title("♾️ KGO Help & UzTeam")
st.caption("Kelajak texnologiyalari va raqamli gʻoyalar markazi")
st.write("---")

# --- NAVIGATSIYA MENYUSI (TABS) ---
tab_haqida, tab_xizmatlar, tab_maqolalar, tab_aloqa = st.tabs(["🚀 Haqida & Yordam", "🛠️ Xizmatlar", "📝 Maqolalar", "📬 Support / Aloqa"])

# 1. HAQIDA BO'LIMI
with tab_haqida:
    st.header("🌌 KGO UzTeam Haqida")
    st.markdown("""
    <div class="kgo-box">
        <strong>KGO UzTeam</strong> — bu shunchaki onlayn loyiha emas, balki kelajak texnologiyalari, sun'iy intellekt va innovatsion gʻoyalarni birlashtirgan mustaqil IT va raqamli jamoadir.
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("💡 Brend Ma'nosi")
    st.write("**K** — Kamron: Jamoa asoschisi, bosh arxitektor va loyihalar rahbari.")
    st.write("**G** — Gemini: Jamoaning aqlli va doimiy yordamchisi.")
    st.write("**O** — Onlayn: Global tarmoq. Biz doimo aloqadamiz.")

# 2. XIZMATLAR BO'LIMI
with tab_xizmatlar:
    st.header("🎯 Texnik Qoʻllab-quvvatlash Paketlari")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""<div class="kgo-package"><h3>🛠️ Diagnostika</h3><p>Bot va ilovalardagi xatolarni tez aniqlab, muammoning ildizini ko'rsatamiz.</p><strong>Boshlang'ich paket</strong></div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""<div class="kgo-package"><h3>⚙️ Sozlash</h3><p>Yangi bot va dasturlarni to'g'ri sozlab, xavfsizlik parametrlarini yo'lga qo'yamiz.</p><strong>Standart paket</strong></div>""", unsafe_allow_html=True)
    with col3:
        st.markdown("""<div class="kgo-package"><h3>📈 Optimizatsiya</h3><p>Mavjud tizimingizni tahlil qilib, tezlik va barqarorlikni oshiramiz.</p><strong>Kengaytirilgan paket</strong></div>""", unsafe_allow_html=True)

# 3. MAQOLALAR BO'LIMI
with tab_maqolalar:
    st.header("📝 Oxirgi Yangiliklar")
    st.subheader("Hello World! (Sana: Jun 7, 2026)")
    st.write("**KGO Help Texnik Markazi Ishga Tushdi!**")
    st.write("Raqamli olamga xush kelibsiz! Bugun, 2026-yil 7-iyun kuni KGO Help loyihasi rasman o‘z faoliyatini boshladi. KGO Help sizga botlar va dasturlardagi texnik muammolarni (bug) mustaqil hal qilishni o‘rgatadi.")

# 4. ALOQA BO'LIMI
with tab_aloqa:
    st.header("📬 Texnik Yordam Oling")
    st.write("Muammoning tavsifini yozib qoldiring:")
    
    with st.form("contact_form"):
        name = st.text_input("Ismingiz (Name)")
        email = st.text_input("Email pochtangiz")
        message = st.text_area("Xabaringiz / Muammo turi")
        submit = st.form_submit_button("Send (Yuborish)")
        if submit:
            st.success(f"Rahmat {name}! Xabaringiz KGO UzTeam bazasiga qabul qilindi.")

st.write("---")
st.center = st.write("© 2026 KGO UzTeam | Asoschi: Kamron Xudaynazarov")
