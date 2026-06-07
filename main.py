# ====================================================================================================
# ♾️ LOYIHA: GeminGPT - THE ULTIMATE COSMIC INTELLIGENCE (100,000 IQ EDITION)
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
    page_title="GeminGPT | Cosmic Sovereign",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- [SECTION 2] UI & DESIGN (BLUE-DARK ULTRA YANGILANGAN) ---
st.markdown("""
<style>
     /* Umumiy fon va matnlar tiniqligi */
     .stApp {
         background-color: #0b0f19 !important;
         color: #ffffff !important;
         font-family: 'Inter', sans-serif;
     }
     
     /* Sarlavhalar rangini majburiy oq qilish */
     h1, h2, h3, h4, h5, h6, p, span, label {
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
     
     /* Chat kiritish oynasi (Input) - Matn qora fonda oq ko'rinishi uchun */
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
</style>
""", unsafe_allow_html=True)

# --- [SECTION 3] SESSION LOGIC ---
if "messages" not in st.session_state: 
    st.session_state.messages = []

# --- [SECTION 4] MAIN APP (SIGN IN OLIB TASHLANDI) ---
with st.sidebar:
    st.markdown("<h2 style='text-align:center; color:#2563eb;'>gemingpt</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class="sidebar-stat">👤 <b>Tizim:</b><br><code>KGO Group Admin</code></div>
    <div class="sidebar-stat">🧠 <b>IQ Darajasi:</b><br>100,000 (Cosmic Engine)</div>
    """, unsafe_allow_html=True)
    st.write("---")
    st.markdown("<b>Muallif: Kamron Xudaynazarov</b>", unsafe_allow_html=True)
    
st.markdown("<h1 style='color: #2563eb; font-weight:bold;'>gemingpt ♾️</h1>", unsafe_allow_html=True)
st.markdown("<p style='color: #94a3b8;'>Kamron Xudaynazarov va KGO Group tomonidan yaratilgan eng daxshat intellekt tizimi.</p>", unsafe_allow_html=True)
st.markdown("---")

# Oldingi xabarlarni ekranga chiqarish
for message in st.session_state.messages: 
     with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if message.get("is_image", False):
            st.image(message["image_url"], use_container_width=True)

# Foydalanuvchidan savol olish
user_query = st.chat_input("Savol yozing yoki rasm chizdiring...")

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

st.markdown('<br><div style="text-align:center; color:#94a3b8; font-size:12px; margin-top: 60px;">© 2026 KGO Group Global Systems | Asoschi: Kamron Xudaynazarov</div>', unsafe_allow_html=True)
