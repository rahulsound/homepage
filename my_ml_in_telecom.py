import streamlit as st


def run_ml_in_telecom():
    st.divider()

    st.markdown('''
    ### :blue[Overview:]

    ---
    #### :blue[Data Fuels AI:]
    -   Though one may be led to believe that every thought-experiement is realizable with AI, the story is very different for individual domains (Computer Vision, Natural Language Processing, Autonomous Driving, Finance, Telecommunications etc).

    -   Underneath a cosmetically beautiful (API driven) UI that mediates between a human and a machine learning model, is an interplay of database accesses, hardware accelerators, quagmire of networks of activation functions that squeeze and squish matrices of numbers created by millions of lines of boring software that clean, drop, impute, transform and read what we call as 'source' or 'raw' data.

    -   So prior to looking at applications and use cases of AI in Telecom, the story of data has its own place and needs to be told.    
    ---
    #### :blue[The background story:]
    ''')
    st.image('storyOfData.png', caption='Story of Data')

    st.divider()

    st.markdown('''
    #### :blue[The story of perspectives :]
    ''')
    st.image('storyOfPers.png', caption='Story of Perspectives')
    st.divider()

    st.markdown('''
    #### :blue[The story of AI/ML driven use cases :]
    ##### :green[Approach#1 Get the work done :]

    ''')
    st.image('appr1.png', caption='Approach#1')
    st.divider()

    st.markdown('''
    ##### :green[Approach#2 Need for 'alliances' :]

    ''')
    st.image('appr2.png', caption='Approach#2')
    st.divider()

    st.markdown('''
    ##### :green[Approach#3 Ride the AI Wave :]

    ''')
    st.image('appr3.png', width=800, caption='Approach#3')
    st.divider()

    st.markdown('''
    ###### Details of these approaches and further infomation -> In Progress...

    ''')


def run_study_of_research_papers():
    st.markdown(
        '''
### :blue[Motivation:]
###### To list out intersting research papers and a summarize learnings from them. 
---
#### :blue[Architectures:]
- Understanding O-RAN: Architecture, Interfaces, Algorithms, Security, and Research Challenges [[link]](https://ieeexplore.ieee.org/iel7/9739/10130694/10024837.pdf)
    - Summary on [medium](https://medium.com/@rahulsound/understanding-o-ran-architecture-978cc49deea7)
- ColO-RAN: Developing Machine Learning-based xApps for Open RAN Closed-loop Control on Programmable Experimental Platforms [[link]](https://ieeexplore.ieee.org/document/9814869)
    - summary

#### :blue[Energy Saving use case]:
- ScalO-RAN: Energy-aware Network Intelligence Scaling in Open RAN [[link]](https://arxiv.org/abs/2312.05096)
    - summary
- Energy Consumption of Machine Learning Enhanced Open RAN: A Comprehensive Review [[link]](https://yo-ran.org/wp-content/uploads/2024/06/Energy_Consumption_of_Machine_Learning_Enhanced_Open_RAN_A_Comprehensive_Review.pdf)
    - summary

#### :blue[Network Slicing use case:]

#### :blue[Traffic Steering use case:]
'''
    )


    