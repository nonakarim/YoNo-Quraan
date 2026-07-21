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


