import streamlit as st
from my_ml_in_telecom import run_ml_in_telecom

def run_papers():
    menu = ["ML in Telecom"
            ]

    choice = st.sidebar.radio("Menu", menu)
    if choice == "ML in Telecom":
        run_ml_in_telecom()


    st.divider()