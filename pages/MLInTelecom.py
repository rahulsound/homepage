import streamlit as st
st.set_page_config(page_title="AI-ML in Telecom", layout="wide")
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
        
def run_ml_in_telecom():
    st.markdown('''
    ### :blue[AI/ML in Telecom:]
    ###### This pages covers my perspectives on how AI/ML can be infused into Telecom domain.
                
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
    - [Technical summary on medium](https://medium.com/@rahulsound/understanding-o-ran-architecture-978cc49deea7)
- ColO-RAN: Developing Machine Learning-based xApps for Open RAN Closed-loop Control on Programmable Experimental Platforms [[link]](https://ieeexplore.ieee.org/document/9814869)
    - Technical summary

#### :blue[Energy Saving use case]:
- ScalO-RAN: Energy-aware Network Intelligence Scaling in Open RAN [[link]](https://arxiv.org/abs/2312.05096)
    - Technical summary
- Energy Consumption of Machine Learning Enhanced Open RAN: A Comprehensive Review [[link]](https://yo-ran.org/wp-content/uploads/2024/06/Energy_Consumption_of_Machine_Learning_Enhanced_Open_RAN_A_Comprehensive_Review.pdf)
    - By [YO-RAN](https://www.linkedin.com/company/yo-ran/about/) YOrkshire Open Radio Access Networks
    - Technical summary

#### :blue[Network Slicing use case:]
- Technical White Paper Network Slicing from Samsung [[link]](https://images.samsung.com/is/content/samsung/assets/global/business/networks/insights/white-paper/network-slicing/200420_Samsung_Network_Slicing_Final.pdf)
    - Technical summary 
- Management of Network Slicing in 5G Radio Access Networks: Functional Framework and Information Models [[link]](https://arxiv.org/abs/1803.01142)
    - Technical summary
- Assessment of Security KPIs for 5G Network Slices for Special Groups of Subscribers [[link]](https://www.mdpi.com/2504-2289/7/4/169)
    - Technical summary
- AI-Based Resource Allocation in E2E Network Slicing with Both Public and Non-Public Slices [[link]](https://www.mdpi.com/2076-3417/13/22/12505)
    - Technical summary
- An E2E Network Slicing Framework for Slice Creation and Deployment Using Machine Learning [[link]](https://www.mdpi.com/1424-8220/23/23/9608)
    - Technical summary
- Safe and Accelerated Deep Reinforcement Learning-based O-RAN Slicing: A Hybrid Transfer Learning Approach [[link]](https://ieeexplore.ieee.org/document/10329948)

#### :blue[Traffic Steering use case:]
- Programmable and Customized Intelligence for Traffic Steering in 5G Networks Using Open RAN Architectures [[link]](https://arxiv.org/abs/2209.14171)
    - Technical summary [[here]](https://rahulsound.streamlit.app/~/+/#near-rt-ric)
- Toward Modular and Flexible Open RAN Implementations in 6G Networks: Traffic Steering Use Case and O-RAN xApps [[link]](https://www.mdpi.com/1424-8220/21/24/8173)
    - Technical summary
'''
    )

st.subheader(":blue[Rahul Soundrarajan]", anchor='#about')
st.markdown('''
###### [LinkedIn](https://www.linkedin.com/in/rahul-soundrarajan/) | [Medium](https://medium.com/@rahulsound) | [Contact](mailto:rahulsound@gmail.com)
                ''')
run_sub_header()
run_ml_in_telecom()
run_study_of_research_papers()
    