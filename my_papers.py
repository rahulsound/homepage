import streamlit as st
from my_ml_in_telecom import *

def run_papers():
    menu = ["ML in Telecom - Overview",
            "A study of research papers"
            ]

    choice = st.sidebar.radio("Menu", menu)
    if choice == "ML in Telecom - Overview":
        run_ml_in_telecom()
    elif choice == "A study of research papers":
        run_study_of_research_papers()


    st.divider()