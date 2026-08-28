import streamlit as st
import streamlit.components.v1 as comp
import math
import base64
from PIL import Image
import random
import time

if "selected_surah" not in st.session_state:
    st.session_state.selected_surah = 0

if "evening_started" not in st.session_state:
    st.session_state.evening_started = False

if "Key" not in st.session_state:
    st.session_state.Key = 0

if "morning_started" not in st.session_state:
    st.session_state.morning_started = False

if "printed" not in st.session_state:
    st.session_state.printed = False

if "zekr" not in st.session_state:
    st.session_state.zekr = 0

if "result" not in st.session_state:
    st.session_state.result = ""
    
if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False

if "page" not in st.session_state:
    st.session_state.page = "Home"

if "answered" not in st.session_state:
    st.session_state.answered = False

col1, col2, col3 = st.columns([1,3,1])

st.markdown(
    """
    <style>
    .stApp {
        background-color: #8A9A5B;
    }
    </style>
    """,
    unsafe_allow_html=True
)

string = ["Which companion was called \"Sayfo Allah Almaslool\" 🗡️", "Who was the first khalifa after the death of Profit Mohammad :crown:"]
if "num" not in st.session_state:
  st.session_state.num = 1

title = string[0]

@st.dialog(title)
def Q1():

    col1, col2 = st.columns([1,1])
    if st.session_state.num == 1:
        if st.session_state.answered == False:
            with col1:
                B1 = st.button("Khalid ibn al-Walid")
                B2 = st.button("Abu Bakr")
            with col2:
                B3 = st.button("Uthman ibn Affan")
                B4 = st.button("Ali ibn Abi Talib")

            if B1:
                st.session_state.answered = True
                st.text("Correct",text_alignment="center", width="stretch")
                time.sleep(2)
                st.rerun()
            elif B2:
                st.session_state.answered = True
                st.text("Incorrect",text_alignment="center", width="stretch")
                time.sleep(2)
                st.rerun()

            elif B3:
                st.session_state.answered = True
                st.text("Incorrect",text_alignment="center", width="stretch")
                time.sleep(2)
                st.rerun()
            elif B4:
                st.session_state.answered = True
                st.text("Incorrect",text_alignment="center", width="stretch")
                time.sleep(2)
                st.rerun()

        else:
            next = st.button("➡️ Next Question", type="primary", width="stretch")

            if next:
                st.session_state.answered = False
                st.session_state.num = 2
                st.rerun()

@st.dialog(string[1])
def Q2():
    col1, col2 = st.columns([1,1])
    if st.session_state.num == 2:
        if st.session_state.answered == False:
            with col1:
                B1 = st.button("Khalid ibn al-Walid")
                B2 = st.button("Abu Bakr")
            with col2:
                B3 = st.button("Uthman ibn Affan")
                B4 = st.button("Ali ibn Abi Talib")

            if B1:
                st.session_state.answered = True
                st.text("Incorrect",text_alignment="center", width="stretch")
            elif B2:
                st.session_state.answered = True
                st.text("Correct",text_alignment="center", width="stretch")

            elif B3:
                st.session_state.answered = True
                st.text("Incorrect",text_alignment="center", width="stretch")
            elif B4:
                st.session_state.answered = True
                st.text("Incorrect",text_alignment="center", width="stretch")


    
# Home
if st.session_state.page == "Home":
    with col2:
        st.title("Nona Islam")

    labels = ["Azkar", "Quraan", "Treasure Hunt"]
    cols = st.columns(len(labels))

    for col, label in zip(cols, labels):
        with col:
            if label == "Azkar":
                st.image("images/Azkar.jpg", width=80)
            elif label == "Quraan":
                st.image("images/Quraan.jpg", width=80)
            elif label == "Treasure Hunt":
                st.image("images/Treasure.jpg", width=80)

            if st.button(label):
                st.session_state.page = label
                st.rerun()

# Azkar
elif st.session_state.page == "Azkar":

    with col2:
        st.title("Azkar")

    if st.button("⬅ Home", type="primary"):
        st.session_state.page = "Home"
        st.session_state.morning_started = False
        st.session_state.zekr = 0
        st.rerun()

    st.divider()

    labels = ["Morning Azkar", "Evening Azkar"]
    cols = st.columns(len(labels))

    for col, label in zip(cols, labels):

        with col:

            if label == "Morning Azkar":
                st.image("images/A.jpg", width=80)
            else:
                st.image("images/A.jpg", width=80)

            if st.button(label, key=label):

                if label == "Morning Azkar":
                    st.session_state.evening_started = False
                    st.session_state.morning_started = True
                    st.session_state.zekr = 0
                    st.rerun()
                elif label == "Evening Azkar":
                    st.session_state.morning_started = False
                    st.session_state.evening_started = True
                    st.session_state.zekr = 0
                    st.rerun()

    if st.session_state.morning_started:
        azkar = [
            "🌅 أذكار الصباح",

            "1. آية الكرسي — مرة واحدة\n"
            "اللَّهُ لَا إِلَٰهَ إِلَّا هُوَ الْحَيُّ الْقَيُّومُ ۚ "
            "لَا تَأْخُذُهُ سِنَةٌ وَلَا نَوْمٌ...",

            "2. سورة الإخلاص — 3 مرات\n"
            "قُلْ هُوَ اللَّهُ أَحَدٌ ۝ اللَّهُ الصَّمَدُ ۝ "
            "لَمْ يَلِدْ وَلَمْ يُولَدْ ۝ "
            "وَلَمْ يَكُن لَّهُ كُفُوًا أَحَدٌ",

            "3. سورة الفلق — 3 مرات",

            "4. سورة الناس — 3 مرات",

            "5. أصبحنا وأصبح الملك لله\n"
            "أصبحنا وأصبح الملك لله، والحمد لله، لا إله إلا الله وحده لا شريك له، "
            "له الملك وله الحمد وهو على كل شيء قدير.",

            "6. سيد الاستغفار — مرة واحدة\n"
            "اللهم أنت ربي لا إله إلا أنت، خلقتني وأنا عبدك، "
            "وأنا على عهدك ووعدك ما استطعت، أعوذ بك من شر ما صنعت، "
            "أبوء لك بنعمتك عليَّ، وأبوء بذنبي، فاغفر لي، "
            "فإنه لا يغفر الذنوب إلا أنت.",

            "7. بسم الله الذي لا يضر — 3 مرات\n"
            "بسم الله الذي لا يضر مع اسمه شيء في الأرض ولا في السماء "
            "وهو السميع العليم.",

            "8. رضيت بالله ربًا — 3 مرات\n"
            "رضيت بالله ربًا، وبالإسلام دينًا، وبمحمد ﷺ نبيًا.",

            "9. اللهم إني أصبحت أشهدك — 4 مرات\n"
            "اللهم إني أصبحت أشهدك، وأشهد حملة عرشك، وملائكتك، "
            "وجميع خلقك، أنك أنت الله لا إله إلا أنت وحدك لا شريك لك، "
            "وأن محمدًا عبدك ورسولك.",

            "10. اللهم ما أصبح بي من نعمة\n"
            "اللهم ما أصبح بي من نعمة أو بأحد من خلقك فمنك وحدك "
            "لا شريك لك، فلك الحمد ولك الشكر.",

            "11. سبحان الله وبحمده — 100 مرة",

            "12. لا إله إلا الله وحده لا شريك له — 100 مرة\n"
            "لا إله إلا الله وحده لا شريك له، له الملك وله الحمد "
            "وهو على كل شيء قدير.",

            "13. اللهم عافني في بدني — 3 مرات\n"
            "اللهم عافني في بدني، اللهم عافني في سمعي، "
            "اللهم عافني في بصري، لا إله إلا أنت.",

            "14. اللهم إني أسألك العفو والعافية — 3 مرات\n"
            "اللهم إني أسألك العفو والعافية في الدنيا والآخرة.",

            "15. أعوذ بكلمات الله التامات — 3 مرات\n"
            "أعوذ بكلمات الله التامات من شر ما خلق."
        ]
        if st.session_state.zekr < len(azkar):
            st.markdown(
                f"""
                <p style="
                    color:#FFF8E7;
                    font-weight:bold;
                    font-size:24px;
                    text-align:center;
                ">
                    {azkar[st.session_state.zekr]}
                </p>
                """,
                unsafe_allow_html=True
            )

            if st.button(
                "Done",
                type="primary",
                width="stretch",
                key="done_morning"
            ):
                st.session_state.zekr += 1
                st.rerun()

        else:
            st.success("🌅 تم الانتهاء من أذكار الصباح")

    if st.session_state.evening_started:
        azkar_evening = [
                "🌙 أذكار المساء",

                "1. آية الكرسي — مرة واحدة\n"
                "اللَّهُ لَا إِلَٰهَ إِلَّا هُوَ الْحَيُّ الْقَيُّومُ ۚ "
                "لَا تَأْخُذُهُ سِنَةٌ وَلَا نَوْمٌ...",

                "2. سورة الإخلاص — 3 مرات\n"
                "قُلْ هُوَ اللَّهُ أَحَدٌ ۝ اللَّهُ الصَّمَدُ ۝ "
                "لَمْ يَلِدْ وَلَمْ يُولَدْ ۝ "
                "وَلَمْ يَكُن لَّهُ كُفُوًا أَحَدٌ",

                "3. سورة الفلق — 3 مرات",

                "4. سورة الناس — 3 مرات",

                "5. أمسينا وأمسى الملك لله\n"
                "أمسينا وأمسى الملك لله، والحمد لله، لا إله إلا الله وحده لا شريك له، "
                "له الملك وله الحمد وهو على كل شيء قدير.",

                "6. سيد الاستغفار — مرة واحدة\n"
                "اللهم أنت ربي لا إله إلا أنت، خلقتني وأنا عبدك، "
                "وأنا على عهدك ووعدك ما استطعت، أعوذ بك من شر ما صنعت، "
                "أبوء لك بنعمتك عليَّ، وأبوء بذنبي، فاغفر لي، "
                "فإنه لا يغفر الذنوب إلا أنت.",

                "7. بسم الله الذي لا يضر — 3 مرات\n"
                "بسم الله الذي لا يضر مع اسمه شيء في الأرض ولا في السماء "
                "وهو السميع العليم.",

                "8. رضيت بالله ربًا — 3 مرات\n"
                "رضيت بالله ربًا، وبالإسلام دينًا، وبمحمد ﷺ نبيًا.",

                "9. اللهم إني أمسيت أشهدك — 4 مرات\n"
                "اللهم إني أمسيت أشهدك، وأشهد حملة عرشك، وملائكتك، "
                "وجميع خلقك، أنك أنت الله لا إله إلا أنت وحدك لا شريك لك، "
                "وأن محمدًا عبدك ورسولك.",

                "10. اللهم ما أمسى بي من نعمة\n"
                "اللهم ما أمسى بي من نعمة أو بأحد من خلقك فمنك وحدك "
                "لا شريك لك، فلك الحمد ولك الشكر.",

                "11. سبحان الله وبحمده — 100 مرة",

                "12. لا إله إلا الله وحده لا شريك له — 100 مرة\n"
                "لا إله إلا الله وحده لا شريك له، له الملك وله الحمد "
                "وهو على كل شيء قدير.",

                "13. اللهم عافني في بدني — 3 مرات\n"
                "اللهم عافني في بدني، اللهم عافني في سمعي، "
                "اللهم عافني في بصري، لا إله إلا أنت.",

                "14. اللهم إني أسألك العفو والعافية — 3 مرات\n"
                "اللهم إني أسألك العفو والعافية في الدنيا والآخرة.",

                "15. أعوذ بكلمات الله التامات — 3 مرات\n"
                "أعوذ بكلمات الله التامات من شر ما خلق."
            ]

        if st.session_state.zekr < len(azkar_evening):
            st.markdown(
                f"""
                <p style="
                    color:#FFF8E7;
                    font-weight:bold;
                    font-size:24px;
                    text-align:center;
                ">
                    {azkar_evening[st.session_state.zekr]}
                </p>
                """,
                unsafe_allow_html=True
            )

            if st.button(
                "Done",
                type="primary",
                width="stretch",
                key="done_evening"
            ):
                st.session_state.zekr += 1
                st.rerun()

        else:
            col1,col2 = st.columns(2)
            with col2:
                st.success("🌙 تم الانتهاء من أذكار المساء")


# Quraan
elif st.session_state.page == "Quraan":
    with col2:
        st.title("Quraan")

    if st.button("⬅ Home", type="primary"):
        st.divider()
        st.session_state.page = "Home"
        st.rerun()
    else:
        st.divider()
        surahs = [
            "Al-Fatihah", "Al-Baqarah", "Aal-E-Imran", "An-Nisa", "Al-Ma'idah",
            "Al-An'am", "Al-A'raf", "Al-Anfal", "At-Tawbah", "Yunus",
            "Hud", "Yusuf", "Ar-Ra'd", "Ibrahim", "Al-Hijr",
            "An-Nahl", "Al-Isra", "Al-Kahf", "Maryam", "Ta-Ha",
            "Al-Anbiya", "Al-Hajj", "Al-Mu'minun", "An-Nur", "Al-Furqan",
            "Ash-Shu'ara", "An-Naml", "Al-Qasas", "Al-Ankabut", "Ar-Rum",
            "Luqman", "As-Sajdah", "Al-Ahzab", "Saba", "Fatir",
            "Ya-Sin", "As-Saffat", "Sad", "Az-Zumar", "Ghafir",
            "Fussilat", "Ash-Shura", "Az-Zukhruf", "Ad-Dukhan", "Al-Jathiyah",
            "Al-Ahqaf", "Muhammad", "Al-Fath", "Al-Hujurat", "Qaf",
            "Adh-Dhariyat", "At-Tur", "An-Najm", "Al-Qamar", "Ar-Rahman",
            "Al-Waqi'ah", "Al-Hadid", "Al-Mujadilah", "Al-Hashr", "Al-Mumtahanah",
            "As-Saff", "Al-Jumu'ah", "Al-Munafiqun", "At-Taghabun", "At-Talaq",
            "At-Tahrim", "Al-Mulk", "Al-Qalam", "Al-Haqqah", "Al-Ma'arij",
            "Nuh", "Al-Jinn", "Al-Muzzammil", "Al-Muddaththir", "Al-Qiyamah",
            "Al-Insan", "Al-Mursalat", "An-Naba", "An-Nazi'at", "'Abasa",
            "At-Takwir", "Al-Infitar", "Al-Mutaffifin", "Al-Inshiqaq", "Al-Buruj",
            "At-Tariq", "Al-A'la", "Al-Ghashiyah", "Al-Fajr", "Al-Balad",
            "Ash-Shams", "Al-Layl", "Ad-Duha", "Ash-Sharh", "At-Tin",
            "Al-'Alaq", "Al-Qadr", "Al-Bayyinah", "Az-Zalzalah", "Al-'Adiyat",
            "Al-Qari'ah", "At-Takathur", "Al-'Asr", "Al-Humazah", "Al-Fil",
            "Quraysh", "Al-Ma'un", "Al-Kawthar", "Al-Kafirun", "An-Nasr",
            "Al-Masad", "Al-Ikhlas", "Al-Falaq", "An-Nas"
        ]

        col1,col2,col3 = st.columns(3)

        with col2: 
            sheikhs = st.selectbox("Select your favorite sheikh: ",
                                [
                                    "yasser_ad-dussary",
                                    "Abdul Basit Abdul Samad"
                                ])

        with st.container(height=250, border=True, width="stretch"):
            for i, surah in enumerate(surahs, start=1):
                if st.button(surah, width="stretch"):
                    st.session_state.selected_surah = i
        if "selected_surah" in st.session_state and st.session_state.selected_surah != 0:
            i = st.session_state.selected_surah
            if sheikhs == "yasser_ad-dussary":
                url = f"https://download.quranicaudio.com/quran/yasser_ad-dussary/{i:03}.mp3"
                st.audio(url, format="audio/mp3")
            else:
                url = f"https://download.quranicaudio.com/quran/abdulbaset_mujawwad/{i:03}.mp3"
                st.audio(url, format="audio/mp3")

# Treasure Hunt
elif st.session_state.page == "Treasure Hunt":
    with col2:
        st.title("Treasure Hunt")
    with st.container():
        home = st.button("⬅ Home", type="primary")
        if home:
            st.divider()
            st.session_state.page = "Home"
            st.rerun()
        
    if home != True:
        st.divider()
        st.image("images/TH.png", width = 600)
        st.write("\n\n")
        st.image("images/TH2.png", width = 600)



    if st.button(":closed_lock_with_key: start Adventure", type="primary"):
        st.session_state.quiz_started = True
        st.session_state.num = 1
        st.session_state.answered = False
        st.rerun()

    if st.session_state.quiz_started:
        if st.session_state.num == 1:
            Q1()
        else:
            Q2()
        
