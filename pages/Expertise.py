import streamlit as st
import pandas as pd
st.set_page_config(page_title="Rahul Soundrarajan", layout="wide")
def run_sub_header(online=True):
    if online:    
        st.write('[ [AIMLProjects](https://rahulsound.streamlit.app/AIMLProjects) | \
                [Expertise](https://rahulsound.streamlit.app/Expertise) | \
                [Explora](https://rahulsound.streamlit.app/Explora) | \
                [MLInTelecom](https://rahulsound.streamlit.app/MLInTelecom) | \
                [Patents](https://rahulsound.streamlit.app/Patents) | \
                [Research](https://rahulsound.streamlit.app/ResearchPapers) |\
                [Start-up](https://rahulsound.streamlit.app/Startup) ]')
    else:
        st.write('| [AIMLProjects](http://localhost:8501/AIMLProjects) | \
                [Expertise](http://localhost:8501/Expertise) | \
                [Explora](http://localhost:8501/Explora) | \
                [MLInTelecom](http://localhost:8501/MLInTelecom) | \
                [Patents](http://localhost:8501/Patents) | \
                [Research](http://localhost:8501/ResearchPapers) |\
                [Start-up](http://localhost:8501/Startup) ]')
        

def run_skills_and_interests():
    st.header(":blue[Expertise]")
    st.write('''Foster innovation in the intersection of Telecom & AI/ML, Computer Vision & Sensor Fusion domains | [ [filed patents](https://patents.justia.com/inventor/rahul-soundrarajan) ] ''')
    
    st.subheader('Machine Learning and AI:')
    st.write('''
             - Reinforcement Learning (Deep-Q Learning) 
             - Computer Vision for custom object training, object detection, classification, segmentation (YOLO based models)
             - Sensor fusion algorithms (Radar + Camera): Fusion for object detection & velocity, distance tagging.
             - Supervised, Unsupervised Learning: Linear & Logistic Regressions, k-NN, Clustering, Neural Networks, CART,
             - Time Series analysis with several IPs in Throughput, HO Prediction and Optimization in 2/3/4G wireless networks.
             - NLP and NLTK on Wireless KPIs & logs
             - Exploring GenAI
            ''' )
    
    st.subheader('Telecom:')
    st.write('''
            - 5G, O-RAN (WG2, WG3, WG4), NSA/SA architectures
            - Near-RT RIC, Non-RT RIC
            - 3G, 4G, 5G RAN System Architecture and Design | Protocols: RRC, PDCP, RLC, MAC
            - 3GPP contributions ''')

    st.subheader('Sensor Fusion Algorithms:')
    st.write('''
             - Radar + Camera fusion, 
             - Experimented with early and late fusion architectures (Data, Feature, Decision fusion) on top of pre-trained computer vision models (YOLO)''')

    st.subheader('Statistical Methods:')
    st.write('Descriptive & Predictive Analysis and applying Hypothesis testing, Confusion matrix in model evaluation')

    st.subheader('Programming Languages:')
    st.write('C, C++, Python [pandas, numpy, sklearn, matplotlib, seaborn, nltk, plotly, bokeh')

    st.subheader('Tools:')
    st.write('OpenAI Gym, Jupyter notebooks, Pycharm, Spyder, Matlab, Octave, Tableau')

    st.subheader('OS and Version Control')
    st.write('Lnix, Linux, Clearcase, Git.')

    st.subheader('Media:')
    st.write('[LinkedIn](https://www.linkedin.com/in/rahul-soundrarajan/), [Medium](https://medium.com/@rahulsound), [GitHub](https://github.com/rahulsound)')

st.subheader(":blue[Rahul Soundrarajan]", anchor='#about')
st.markdown('''
###### [LinkedIn](https://www.linkedin.com/in/rahul-soundrarajan/) | [Medium](https://medium.com/@rahulsound) | [Contact](mailto:rahulsound@gmail.com)
                ''')
run_sub_header()
run_skills_and_interests()