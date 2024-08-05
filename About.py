

##imports##
import streamlit as st

# Frontend using streamlit"
import streamlit as st
import os
from pages.Patents import run_patents
from pages.Expertise import run_skills_and_interests
from streamlit_option_menu import option_menu
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
        st.write('[ [AIMLProjects](https://rahulsound.streamlit.app/AIMLProjects) | \
                [Expertise](https://rahulsound.streamlit.app/Expertise) | \
                [Explora](https://rahulsound.streamlit.app/Explora) | \
                [MLInTelecom](https://rahulsound.streamlit.app/MLInTelecom) | \
                [Patents](https://rahulsound.streamlit.app/Patents) | \
                [ResearchPapers](https://rahulsound.streamlit.app/ResearchPapers) |\
                [Start-up](https://rahulsound.streamlit.app/Startup) ]')
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
        With over 23 years of diverse experience in telecom, machine learning, sensor fusion, and computer vision, I am an AI/ML technical consultant who designs and implements custom solutions for challenging problems that require cutting-edge technologies and deep domain knowledge.

        I hold multiple patents and publications in applied ML, specifically related to network optimization. In my previous role, I have designed and evaluated complex ML based solutions for O-RAN (Near and Non-RT RAN Intelligent Controller)

        Currently, I am working with Northeastern University and IMDEA Networks on EXPLORA, a framework that provides explainability of DRL-based control solutions for the Open RAN ecosystem.

        In my last role, as a founding member and VP of ML & SW Engineering at BlueFusion Inc., a Boston based start-up, I designed ML-based sensor fusion algorithms that helped demonstrate the capability and promise of the solution. This solution has applications for automotive, surveillance, UAVs, smart homes, V2X, and factory automation, and was in the start-up inception programs of Microsoft and Nvidia.

        I am passionate about creating innovative and impactful solutions that leverage the power of AI/ML and edge computing. 
        '''
          )
    st.write(md)
    st.divider()
    st.markdown('''
        ###### :blue[Feel free to check out the tabs at the top to explore my work.]
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
    run_sub_header
    run_about()
    # st.divider()
    # run_patents()
    # st.divider()
    # run_skills_and_interests()
    st.divider()
if __name__ == '__main__':
    #by default it will run at 8501 port
    run()

