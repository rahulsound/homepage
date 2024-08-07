

##imports##
import streamlit as st

# Frontend using streamlit"
import streamlit as st
import os

st.set_page_config(page_title="Rahul Soundrarajan", layout="wide", )
online_flag = True
from streamlit import session_state as ss

if 'sidebar_state' not in ss:
    ss.sidebar_state = 'collapsed'

    # st.sidebar.markdown('''
    # # Sections
    # - [Section 1](#section-1)
    # - [Section 2](#section-2)
    # ''', unsafe_allow_html=True)

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
        
    
def run_about():
    st.header(":blue[About]", anchor='#about')
    md = ('''
        I am passionate about creating innovative and impactful solutions that leverage the power of AI/ML and edge computing. 

        With over 23 years of diverse experience in telecom, machine learning, sensor fusion, and computer vision, I am an AI/ML technical consultant who designs and implements custom solutions for challenging problems that require cutting-edge technologies and deep domain knowledge.

        My idea of creating this site is to share my thoughts and learn.

        I hold multiple [patents](https://rahulsound.streamlit.app/Patents) and publications in applied ML, specifically related to network optimization. In my previous role, I have designed and evaluated complex ML based solutions for O-RAN (Near and Non-RT RAN Intelligent Controller)

        Currently, I am working with Northeastern University and IMDEA Networks on [EXPLORA](https://rahulsound.streamlit.app/Consultancy), a framework that provides explainability of DRL-based control solutions for the Open RAN ecosystem.

        In my last role was a [founding member and VP ](https://rahulsound.streamlit.app/~/+/A_StartupFounder#overview) of [BlueFusion Inc.](https://bluefusion.tech/), a Boston based start-up. I designed ML-based sensor fusion algorithms that helped demonstrate the capability and promise of the solution. This solution has applications for automotive, surveillance, UAVs, smart homes, V2X, and factory automation, and BlueFusion was in the start-up incubation ecosystem of **Microsoft For Startups** and **NVIDIA Inception Program**.
          
        '''
          )
    st.write(md)
    st.divider()
    st.markdown('''
        ###### :blue[To learn more about my research, projects check the links above.]
                ''')
    
def run():
#     def streamlit_menu():
#         selected = option_menu(
#             menu_title=None,  # required
#             options=["About", "Patents", "Expertise"],  # required
#             icons=["house", "mortarboard", "asterisk"],  # optional
#             menu_icon="cast",  # optional
#             default_index=0,  # optional
#             orientation="horizontal",
#         )
#         return selected
    
#     st.header(":blue[Rahul Soundrarajan]", anchor='#about')
#     st.markdown('''
# ##### [LinkedIn](https://www.linkedin.com/in/rahul-soundrarajan/) | [Medium](https://medium.com/@rahulsound) | [Contact](mailto:rahulsound@gmail.com)
#                 ''')
    
#     selected = streamlit_menu()
#     run_sub_header()
#     if selected == "Patents":
#         run_patents()
#     elif selected == "Expertise":
#         run_skills_and_interests()
#     else:
#         run_about()
#         st.divider()
#         run_patents()
#         st.divider()
#         run_skills_and_interests()
#         st.divider()

    st.header(":blue[Rahul Soundrarajan]", anchor='#about')
    st.markdown('''
##### [LinkedIn](https://www.linkedin.com/in/rahul-soundrarajan/) | [Medium](https://medium.com/@rahulsound) | [Contact](mailto:rahulsound@gmail.com)
                ''')
    run_sub_header()
    run_about()
    # st.divider()
    # run_patents()
    # st.divider()
    # run_skills_and_interests()
    st.divider()
if __name__ == '__main__':
    #by default it will run at 8501 port
    run()

