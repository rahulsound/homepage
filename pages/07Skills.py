import streamlit as st
import pandas as pd
st.set_page_config(page_title="Rahul Soundrarajan", layout="wide")
def run_sub_header(online=True):
    if online:    
        st.write('[ [A StartupFounder](https://rahulsound.streamlit.app/A_StartupFounder) | \
                [Consultancy](https://rahulsound.streamlit.app/Consultancy) | \
                [AI ML Projects](https://rahulsound.streamlit.app/AI_ML_Projects) | \
                [Research](https://rahulsound.streamlit.app/Research) | \
                [Patents](https://rahulsound.streamlit.app/Patents) |\
                [Skills](https://rahulsound.streamlit.app/Skills) ]')
    else:
        st.write('| [AIMLProjects](http://localhost:8501/AIMLProjects) | \
                [Expertise](http://localhost:8501/Expertise) | \
                [Explora](http://localhost:8501/Explora) | \
                [MLInTelecom](http://localhost:8501/MLInTelecom) | \
                [Patents](http://localhost:8501/Patents) | \
                [Research](http://localhost:8501/ResearchPapers) |\
                [Start-up](http://localhost:8501/Startup) ]')
 
def run_skills_and_interests():
    st.header(":blue[Skills & Expertise]")
    st.markdown(''' 
###### :violet[**I am passionate about fostering innovation in the intersection of Telecom & AI/ML, Computer Vision & Sensor Fusion domains | [[filed patents]](https://patents.justia.com/inventor/rahul-soundrarajan)**]
''')    
    st.write('Reskilling is essential to keep-up with Tech and figure out how to do things better...') 


    
    st.subheader('Machine Learning and AI')
    st.write('''
             - Reinforcement Learning (Deep-Q Learning) 
             - Computer Vision for custom object training, object detection, classification, segmentation (YOLO based models)
             - Sensor fusion algorithms (Radar + Camera): Fusion for object detection & velocity, distance tagging.
             - Supervised, Unsupervised Learning: Linear & Logistic Regressions, k-NN, Clustering, Neural Networks, CART,
             - Time Series analysis with several IPs in Throughput, HO Prediction and Optimization in 2/3/4G wireless networks.
             - NLP and NLTK on Wireless KPIs & logs
             - Exploring GenAI
            ''' )
    
    st.subheader('Telecom')
    st.write('''
            - 5G, O-RAN (WG2, WG3, WG4), NSA/SA architectures
            - Near-RT RIC, Non-RT RIC
            - 3G, 4G, 5G RAN System Architecture and Design | Protocols: RRC, PDCP, RLC, MAC
            - 3GPP contributions ''')

    st.subheader('Sensor Fusion Algorithms')
    st.write('''
             - Radar + Camera fusion, 
             - Experimented with early and late fusion architectures (Data, Feature, Decision fusion) on top of pre-trained computer vision models (YOLO)''')

    st.subheader('Statistical Methods')
    st.write('Descriptive & Predictive Analysis and applying Hypothesis testing, Confusion matrix in model evaluation')

    st.subheader('Programming Languages')
    st.write('C, C++, Python [pandas, numpy, sklearn, matplotlib, seaborn, nltk, plotly, bokeh')

    st.subheader('Tools')
    st.write('OpenAI Gym, Jupyter notebooks, Pycharm, Spyder, Matlab, Octave, Tableau')

    st.subheader('OS and Version Control')
    st.write('Unix, Linux, Git, Clearcase.')

    st.subheader('Media')
    st.write('[LinkedIn](https://www.linkedin.com/in/rahul-soundrarajan/), [Medium](https://medium.com/@rahulsound), [GitHub](https://github.com/rahulsound)')

    st.write("")
    st.subheader('Skill Development Graph')
    st.write('[**"One ounce of practice is worth a thousand pounds of theory"** ](https://vivekavani.com/harvard-qa-swami-vivekananda/)- _Swami Vivekananda_')
    st.write('I have been at the "Do-and-Learn" cycle for a while to figure out better ways of approaching problems that make an impact.')
    df = pd.read_csv('skill_progress.csv')
    st.table(df)


st.subheader(":blue[Rahul Soundrarajan]", anchor='#about')
st.markdown('''
###### [LinkedIn](https://www.linkedin.com/in/rahul-soundrarajan/) | [Medium](https://medium.com/@rahulsound) | [Contact](mailto:rahulsound@gmail.com)
                ''')
run_sub_header()
run_skills_and_interests()