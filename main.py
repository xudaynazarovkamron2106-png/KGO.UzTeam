# ====================================================================================================
# ♾️ LOYIHA: KGO Group Global Systems & GeminGPT Cosmic AI (100,000 IQ EDITION)
# 🎖️ STATUS: 100% LOCAL SMARTLOGIC ENGINE (NEVER FAILS, NO TIMEOUTS!)
# 👤 ASOSCHI: KAMRON XUDAYNAZAROV & KGO GROUP GLOBAL SYSTEMS
# ====================================================================================================
import streamlit as st
import time
import random
import urllib.parse
import re

# --- [SECTION 1] GLOBAL SYSTEM CONFIGURATIONS ---
st.set_page_config(
    page_title="KGO Group | Cosmic Systems",
    page_icon="♾️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- [SECTION 2] ULTRA-BRIGHT CYBER ANIMATED CSS ---
st.markdown("""
<style>
     /* Asosiy fon to'q ko'k/qora */
     .stApp {
         background-color: #0b0f19 !important;
         color: #ffffff !important;
         font-family: 'Inter', sans-serif;
     }
     
     /* BARCHA MATNLARNI MAJBURIY OQ VA TINIQ QILISH */
     h1, h2, h3, h4, h5, h6, p, span, label, li {
         color: #ffffff !important;
     }
     
     /* Sidebar uslubi va ichidagi yozuvlar */
     [data-testid="stSidebar"] {
         background-color: #0f172a !important;
         border-right: 1px solid rgba(37, 99, 235, 0.2);
     }
     [data-testid="stSidebar"] *, [data-testid="stSidebar"] p {
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
     
     /* Yon paneldagi vidjetlar */
     .sidebar-stat {
         padding: 12px 15px;
         background: rgba(255, 255, 255, 0.08);
         border-radius: 8px;
         margin-bottom: 10px;
         border-left: 4px solid #2563eb;
         color: #ffffff !important;
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
     
     /* Pastki qism (Footer) */
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

# --- [SECTION 3] SESSION LOGIC ---
if "messages" not in st.session_state: 
    st.session_state.messages = []

# --- [SECTION 4] SIDEBAR NAVIGATION & STATS ---
with st.sidebar:
    st.markdown("<h2 style='text-align:center; color:#2563eb;'>gemingpt</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class="sidebar-stat">👤 <b>Tizim:</b><br><code>KGO Group Admin</code></div>
    <div class="sidebar-stat">🧠 <b>IQ Darajasi:</b><br>100,000 (Cosmic Engine)</div>
    """, unsafe_allow_html=True)
    st.write("---")
    st.markdown("<b>Muallif: Kamron Xudaynazarov</b>", unsafe_allow_html=True)

# --- [SECTION 5] HEADLINE & HELP NAVIGATION ---
col_logo, col_space, col_help = st.columns([3, 1.5, 2])

with col_logo:
    st.markdown("<h1 style='color: #2563eb; font-weight:bold; margin-bottom:0;'>KGO Group Global Systems ♾️</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #00d2ff !important; font-size:16px;'>Kelajak texnologiyalari va raqamli innovatsiyalar markazi</p>", unsafe_allow_html=True)

with col_help:
    st.write("") 
    st.link_button("❓ KGO Texnik Yordam Markazi", "https://xudaynazarovkamron2106-ivgun.wordpress.com/", type="primary", use_container_width=True)

st.markdown("---")

# --- [SECTION 6] MAIN CONTENT (KOMPANIYA HAQIDA) ---
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
            <li><b>K (Kamron)</b> — Jamoa asoschisi, bosh arxitektor va loyihalar rahbari.</li>
            <li><b>G (Gemini)</b> — Aqlli texnologiyalar va mukammal tizim integratsiyasi.</li>
            <li><b>O (Onlayn)</b> — Global tarmoq. Biz 24/7 rejimida dunyo bilan aloqadamiz.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- [SECTION 7] XIZMATLAR VA TARIFLAR ---
st.markdown("<h2 style='text-align:center;'>🎯 Texnik Xizmat Ko'rsatish Paketlari</h2>", unsafe_allow_html=True)
st.write("")

t_col1, t_col2, t_col3, t_col4 = st.columns(4)

with t_col1:
    st.markdown("""<div class="tariff-card"><h3>🛠️ Diagnostika</h3><p style='color:#94a3b8 !important;'>Boshlang'ich Paket</p><p>Bot va ilovalardagi xatolarni tez aniqlab, muammoning sababini ko'rsatamiz.</p></div>""", unsafe_allow_html=True)
with t_col2:
    st.markdown("""<div class="tariff-card"><h3>⚙️ Sozlash</h3><p style='color:#94a3b8 !important;'>Standart Paket</p><p>Yangi bot va dasturlarni to'g'ri sozlab, xavfsizlik parametrlarini yo'lga qo'yamiz.</p></div>""", unsafe_allow_html=True)
with t_col3:
    st.markdown("""<div class="tariff-card"><h3>📈 Optimizatsiya</h3><p style='color:#94a3b8 !important;'>Kengaytirilgan Paket</p><p>Mavjud tizimingizni tahlil qilib, uning tezligi va barqarorligini oshiramiz.</p></div>""", unsafe_allow_html=True)
with t_col4:
    st.markdown("""<div class="tariff-card" style="border-top: 4px solid #00d2ff;"><h3>🛡️ Support</h3><p style='color:#94a3b8 !important;'>Obuna Asosida</p><p>Loyiha uchun doimiy monitoring, tezkor javob va profilaktika ishlarini olib boramiz.</p></div>""", unsafe_allow_html=True)

st.markdown("---")

# --- [SECTION 8] 🧠 INTEGRATED GEMINGPT COSMIC AI SYSTEM ---
st.markdown("<h2 style='text-align:center; color: #2563eb;'>🧠 GeminGPT Cosmic AI Tizimi (100,000 IQ)</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color: #94a3b8;'>Menga inglizcha tarjima, matematika yoki rasm chizish buyrug'ini bering!</p>", unsafe_allow_html=True)

# AI Xabarlar logikasi
for message in st.session_state.messages: 
     with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if message.get("is_image", False):
            st.image(message["image_url"], use_container_width=True)

# Foydalanuvchidan savol olish
user_query = st.chat_input("GeminGPT AI dan biror narsa so'rang yoki rasm chizdiring...")

if user_query:
    st.session_state.messages.append({"role": "user", "content": user_query, "is_image": False})
    with st.chat_message("user"):
        st.markdown(user_query)
        
    q_low = user_query.lower().strip()
    bot_res = ""
     
    # --- 🧠 HIGH-SMART LOCAL INTELLIGENCE CHIP ---
    
    # A. RASM BUYRUG'I
    if any(x in q_low for x in ["rasm chiz", "rasm yarat", "image", "logo", "surat", "chizib ber"]):
        with st.spinner("🎨 Koinot piksellari noldan chizilmoqda..."):
            time.sleep(1.5)
            prompt_clean = q_low
            for word in ["rasm chiz", "rasm yarat", "image", "logo", "surat", "chizib ber", "menga"]:
                prompt_clean = prompt_clean.replace(word, "").strip()
            if "mashina" in prompt_clean: prompt_clean = "car"
            if not prompt_clean: prompt_clean = "cyberpunk"
            random_id = random.randint(1, 9999)
            image_url = f"https://loremflickr.com/1024/1024/{urllib.parse.quote(prompt_clean)}?lock={random_id}"
            bot_res = f"🎨 **GeminGPT sening so'roving bo'yicha rasm yaratdi!**"
            st.session_state.messages.append({"role": "assistant", "content": bot_res, "is_image": True, "image_url": image_url})
            with st.chat_message("assistant"):
                st.markdown(bot_res)
                st.image(image_url, use_container_width=True)

    # B. MUALLIFLIK
    elif any(x in q_low for x in ["kim yaratgan", "muallif", "egasi", "kim yaratdi", "muallifi", "yaratuvching"]):
        bot_res = "Meni **KGO Group** va daho asoschi **Kamron Xudaynazarov** yaratgan! Men Kamronning shaxsiy 100,000 IQ koinot intellektiman. ♾️"

    # C. AKLLI TARJIMONLIK
    elif "ingliz" in q_low or "english" in q_low or "ingiliz" in q_low:
        if "xayir" in q_low or "xayr" in q_low:
            bot_res = "O'zbek tilidagi **'Xayr'** so'zi ingliz tilida **'Goodbye'** yoki qisqacha **'Bye'** deyiladi! 👋🇬🇧"
        elif "salom" in q_low:
            bot_res = "O'zbek tilidagi **'Salom'** so'zi ingliz tilida **'Hello'** yoki **'Hi'** deyiladi! 🇬🇧"
        elif "rahmat" in q_low:
            bot_res = "O'zbek tilidagi **'Rahmat'** so'zi ingliz tilida **'Thank you'** deyiladi! 🇬🇧"
        elif "nimalar qila olasan" in q_low or "nima qila olasan" in q_low:
            bot_res = "I can translate words, solve math problems, and chat with you in English! Men ingliz tilida tarjimalar qila olaman, matematikani bilaman va suhbatlashaman! 🇬🇧"
        else:
            bot_res = "Yes! Men ingliz tilini mukammal bilaman. Istalgan so'zni yozing, daho tarzda tarjima qilib beraman! Masalan: *'maktab ingliz tilida nima degani?'* deb so'rang. 🇬🇧"

    # D. MATEMATIKA ELEMENTAR CHIP
    elif any(op in q_low for op in ['+', '-', '*', '/']) or "nechchi" in q_low or "necha" in q_low:
        math_clean = re.sub(r'[^\d\+\-\*\/\(\)]', '', q_low)
        if math_clean:
            try:
                result = eval(math_clean)
                bot_res = f"🧮 **GeminGPT Matematika Yechimi:**\n\nSizning misolingiz: `{math_clean}`\nNatija: **{result}**\n\nKamron tuzgan tizim har qanday dars masalasini aniq hisoblaydi! ⚡"
            except:
                bot_res = "Misolni hisoblashda xatolik bo'ldi. Raqamlarni to'g'ri kiriting (Masalan: 9 + 9)."
        else:
            bot_res = "Matematik misolni raqamlar bilan yozing, darhol hisoblab beraman!"

    # E. ERKIN SINOVLAR
    elif "zo'rman" in q_low or "zorman" in q_low:
        bot_res = "Siz mutloq daho va judayam zo'rsiz! Kamron Xudaynazarov loyihasining eng top foydalanuvchisisiz! 🚀"
        
    elif "salom" in q_low or "assalomu alaykum" in q_low:
        bot_res = "Salom! Men Kamron Xudaynazarovning 100k IQ koinot intellektiman. Menga tarjima, matematika yoki rasm buyrug'ini bering, darhol bajaraman! ⚡"

    elif "nimalar qila olasan" in q_low or "nima qila olasan" in q_low:
        bot_res = "✨ **Men Kamron Xudaynazarov tizimidagi daho AI man. Qo'limdan keladigan ishlar:**\n\n" \
                  "1. 🇬🇧 **Ingliz tili tarjimoni:** Istalgan so'zni srazu tarjima qilaman.\n" \
                  "2. 🧮 **Matematika:** Istalgan misolni soniyada hisoblayman.\n" \
                  "3. 🎨 **Rasm Generator:** 'Mashina rasmini chiz' desangiz, yangi surat chiqaraman.\n" \
                  "4. 💬 **Jonli suhbat:** Savollaringizga shablonlarsiz, aniq javob beraman!"

    # F. UMUMIY JAVOB
    else:
        bot_res = f"Sizning so'rovingizni Kamronning daho algoritmi o'qidi. Men inglizcha tarjimalarni, matematikani va rasm chizishni mukammal bajaraman. Menga shu buyruqlardan birini bering! 🚀"

    # Javobni saqlash va chiqarish
    if bot_res:
        st.session_state.messages.append({"role": "assistant", "content": bot_res, "is_image": False})
        with st.chat_message("assistant"):
            st.markdown(bot_res)

# --- [SECTION 9] FOOTER ---
st.markdown("""
<div class="footer-text">
    <b>© 2026 KGO Group Global Systems | Asoschi va Bosh Direktor: Kamron Xudaynazarov</b><br>
    Tizim har qanday kiber-sharoitda barqaror va animatsiyalar bilan ishlaydi. ⚡
</div>
""", unsafe_allow_html=True)
