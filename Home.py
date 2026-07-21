import streamlit as st
import streamlit.components.v1 as comp
import math

if "page" not in st.session_state:
    st.session_state.page = "Home"

col1, col2, col3 = st.columns([1,3,1])

# Home
if st.session_state.page == "Home":
    with col2:
        st.title("YoNo Islam")

    labels = ["Azkar", "Quraan", "Tasbih", "Treasure Hunt"]
    cols = st.columns(len(labels))

    for col, label in zip(cols, labels):
        with col:
            if label == "Azkar":
                st.image("images/Azkar.jpg", width=80)
            elif label == "Quraan":
                st.image("images/Quraan.jpg", width=80)
            elif label == "Tasbih":
                st.image("images/Tasbih.jpg", width=80)
            elif label == "Treasure Hunt":
                st.image("images/Treasure.jpg", width=80)

            if st.button(label):
                st.session_state.page = label
                st.rerun()

# Azkar
elif st.session_state.page == "Azkar":
    with col2:
        st.title("Azkar")

    if st.button("⬅ Home"):
        st.divider()
        st.session_state.page = "Home"
        st.rerun()
    
    else:
        st.divider()
        labels = ["Morning Azkar", "Evening Azkar"]
        cols = st.columns(len(labels))

        

        for col, label in zip(cols, labels):
            with col:
                if label == "Morning Azkar":
                    st.image("images/A.jpg", width=80)
                elif label == "Evening Azkar":
                    st.image("images/A.jpg", width=80)
                    
                if st.button(label):
                    if label == "Morning Azkar":
                        st.image("images/MA.png")
                    else:
                        st.image("images/EA.png")

# Quraan
elif st.session_state.page == "Quraan":
    with col2:
        st.title("Quraan")

    if st.button("⬅ Home"):
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

        
        for i, surah in enumerate(surahs, start=1):
            if st.button(surah):
                url = f"https://download.quranicaudio.com/quran/yasser_ad-dussary/{i:03}.mp3"
                st.audio(url, format="audio/mp3")



