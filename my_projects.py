import streamlit as st
from my_startup import run_startup
from my_interests import run_interests
from my_about import run_about
from my_explora import run_explora
from my_papers import run_papers
from my_ml_ran_projects import *

def run_projects():
    # menu = [
    #         "Summary",
    #         "EXPLORA | AI Explainability", 
    #         "AI/ML | Near-RT RIC",
    #         "AI/ML | Non-RT RIC",
    #         "Node-Profiling using CM and PM",
    #         "ARIMA for KPI forecast",
    #         "KPI Prediction" 
    #         ]

    # choice = st.sidebar.radio("Menu", menu)
    # if choice == "Summary":
    #     st.divider()
    #     run_summary()
    # elif choice == "EXPLORA | AI Explainability":
    #     run_explora()
    # elif choice == "AI/ML | Near-RT RIC":
    #     run_near_rt_ric()
    # elif choice == "AI/ML | Non-RT RIC":
    #     run_non_rt_ric()
    # elif choice == "Node-Profiling using CM and PM":
    #     run_node_profiling()
    # elif choice == "ARIMA for KPI forecast":
    #     run_arima()
    # elif choice == "KPI Prediction":
    #     run_kpi_prediction()

    st.sidebar.markdown('''
        # Home
        ## [Summary](#summary)
        ## [EXPLORA](#explora)
        ## [Near RT RIC](#ric-1)
        ## [Non RT RIC](#ric-2)
        ## [Node Profiling](#node-profiling)
        ## [ARIMA](#arima)
        ## [KPI Prediction](#kpi-prediction)               
        ''', unsafe_allow_html=True)

    st.divider()
    run_summary()
    st.divider()
    run_explora()
    st.divider()
    run_near_rt_ric()
    st.divider()
    run_non_rt_ric()
    st.divider()
    run_node_profiling
    st.divider()
    run_arima()
    st.divider()
    run_kpi_prediction()