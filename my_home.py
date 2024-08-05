import streamlit as st
from my_patents import run_patents
from my_skills_and_interests import run_skills_and_interests
from my_about import *


def run_home():
    # menu = ["About",
    #         "Patents", 
    #         "Skills and Interests" 
    #         ]

    # choice = st.sidebar.radio("Menu", menu)
    # if choice == "About":
    #     run_about()
    # elif choice == "Patents":
    #     run_patents()
    # elif choice == "Skills and Interests":
    #     run_skills_and_interests()

    #Needs to be a single word, #should have only small case & header in the page should be in double quotes ""
    st.sidebar.markdown('''
    # [Home](#about)
    ## [About](#about)
    ## [Patents](#patents) 
    ## [Expertise](#expertise)
    ''', unsafe_allow_html=True)

    run_about()
    st.divider()
    run_patents()
    st.divider()
    run_skills_and_interests()
    st.divider()

