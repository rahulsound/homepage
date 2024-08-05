import streamlit as st
from my_ml_in_telecom import *
st.set_page_config(page_title="Research Papers", layout="wide")
def run_sub_header(online=True):
    if online:    
        st.write('| [AIMLProjects](https://rahulsound.streamlit.app/AIMLProjects) | \
                [Expertise](https://rahulsound.streamlit.app/Expertise) | \
                [Explora](https://rahulsound.streamlit.app/Explora) | \
                [MLInTelecom](https://rahulsound.streamlit.app/MLInTelecom) | \
                [Patents](https://rahulsound.streamlit.app/Patents) | \
                [Research](https://rahulsound.streamlit.app/ResearchPapers)\
                [Start-up](https://rahulsound.streamlit.app/Startup) |')
    else:
        st.write('| [AIMLProjects](http://localhost:8501/AIMLProjects) | \
                [Expertise](http://localhost:8501/Expertise) | \
                [Explora](http://localhost:8501/Explora) | \
                [MLInTelecom](http://localhost:8501/MLInTelecom) | \
                [Patents](http://localhost:8501/Patents) | \
                [Research](http://localhost:8501/ResearchPapers)\
                [Start-up](http://localhost:8501/Startup) |')

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
st.subheader(":blue[Rahul Soundrarajan]", anchor='#about')
st.markdown('''
###### [LinkedIn](https://www.linkedin.com/in/rahul-soundrarajan/) | [Medium](https://medium.com/@rahulsound) | [Contact](mailto:rahulsound@gmail.com)
                ''')
run_sub_header()
run_study_of_research_papers()