# ====================================================================================================
# ♾️ LOYIHA: KGO Group Global Systems — Rasmiy Kompaniya Sayti
# 👤 ASOSCHI: KAMRON XUDAYNAZAROV & KGO UZTEAM
# ====================================================================================================
import streamlit as st

# --- [SECTION 1] GLOBAL CONFIG ---
st.set_page_config(
    page_title="KGO Group | Global Systems",
    page_icon="♾️",
    layout="wide"
)

# --- [SECTION 2] ULTRA-BRIGHT CYBER CSS (YOZUVLAR TINIQ KO'RINISHI UCHUN) ---
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
     
     /* Kiber qutilar (Kompaniya bo'limlari uchun) */
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
col_logo, col_space, col_help = st.columns([3, 2, 1.5])

with col_logo:
    st.markdown("<h1 style='color: #2563eb; font-weight:bold; margin-bottom:0;'>KGO Group Global Systems ♾️</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #00d2ff !important; font-size:16px;'>Kelajak texnologiyalari va raqamli innovatsiyalar markazi</p>", unsafe_allow_html=True)

with col_help:
    st.write("") # Tekislash uchun
    # Siz aytgan WordPress yordam markazi saytiga to'g'ridan-to'g'ri o'tish tugmasi
    st.link_button("❓ KGO Texnik Yordam Markazi", "https://xudaynazarovkamron2106-ivgun.wordpress.com/", type="primary", use_container_width=True)

st.markdown("---")

# --- [SECTION 4] MAIN CONTENT (KOMPANIYA HAQIDA) ---
st.markdown("<h2 style='text-align:center;'>🚀 Kompaniyamizga Xush Kelibsiz</h2>", unsafe_allow_html=True)
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
            <li><b>K (Kamron)</b> — Jamoa asoschisi, bosh arxitektor va loyihalar rahbari.</li>
            <li><b>G (Gemini)</b> — Aqlli texnologiyalar va mukammal tizim integratsiyasi.</li>
            <li><b>O (Onlayn)</b> — Global tarmoq. Biz 24/7 rejimida dunyo bilan aloqadamiz.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- [SECTION 5] XIZMATLAR VA TARIFLAR ---
st.markdown("<h2 style='text-align:center;'>🎯 Texnik Xizmat Ko'rsatish Paketlari</h2>", unsafe_allow_html=True)
st.write("")

t_col1, t_col2, t_col3, t_col4 = st.columns(4)

with t_col1:
    st.markdown("""
    <div class="tariff-card">
        <h3>🛠️ Diagnostika</h3>
        <p style='color:#94a3b8 !important;'>Boshlang'ich Paket</p>
        <p>Bot va ilovalardagi xatolarni tez aniqlab, muammoning sababini ko'rsatamiz.</p>
    </div>
    """, unsafe_allow_html=True)

with t_col2:
    st.markdown("""
    <div class="tariff-card">
        <h3>⚙️ Sozlash</h3>
        <p style='color:#94a3b8 !important;'>Standart Paket</p>
        <p>Yangi bot va dasturlarni to'g'ri sozlab, xavfsizlik parametrlarini yo'lga qo'yamiz.</p>
    </div>
    """, unsafe_allow_html=True)

with t_col3:
    st.markdown("""
    <div class="tariff-card">
        <h3>📈 Optimizatsiya</h3>
        <p style='color:#94a3b8 !important;'>Kengaytirilgan Paket</p>
        <p>Mavjud tizimingizni tahlil qilib, uning tezligi va barqarorligini oshiramiz.</p>
    </div>
    """, unsafe_allow_html=True)

with t_col4:
    st.markdown("""
    <div class="tariff-card" style="border-top: 4px solid #00d2ff;">
        <h3>🛡️ Support</h3>
        <p style='color:#94a3b8 !important;'>Obuna Asosida</p>
        <p>Loyiha uchun doimiy monitoring, tezkor javob va profilaktika ishlarini olib boramiz.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- [SECTION 6] ALOQA SHTABI ---
st.markdown("<h2 style='text-align:center;'>📬 KGO Group Bilan Bog'lanish</h2>", unsafe_allow_html=True)

col_form_space1, col_form, col_form_space2 = st.columns([1, 2, 1])

with col_form:
    with st.form("kgo_contact"):
        st.markdown("<p style='color:#94a3b8 !important;'>Savolingizni yoki loyiha taklifingizni qoldiring:</p>", unsafe_allow_html=True)
        name = st.text_input("Ismingiz / Kompaniya nomi")
        email = st.text_input("Email manzilingiz")
        message = st.text_area("Loyiha tavsifi yoki muammo turi")
        
        submit_btn = st.form_submit_button("Xabarni Yuborish ⚡", use_container_width=True)
        if submit_btn:
            if name and email and message:
                st.success(f"Rahmat {name}! Xabaringiz KGO Group tizimiga muvaffaqiyatli qabul qilindi.")
            else:
                st.error("Iltimos, barcha maydonlarni to'ldiring!")

# --- [SECTION 7] FOOTER ---
st.markdown("""
<div class="footer-text">
    <b>© 2026 KGO Group Global Systems | Asoschi va Bosh Direktor: Kamron Xudaynazarov</b><br>
    Tizim har qanday kiber-sharoitda barqaror ishlaydi. ⚡
</div>
""", unsafe_allow_html=True)
