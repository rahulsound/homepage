import streamlit as st


def run_ml_in_telecom():
    st.markdown('''
    #### :green[Data Fuels AI:]
    -   Though one may be led to believe that every thought-experiement is realizable with AI, the story is very different for individual domains (Computer Vision, Natural Language Processing, Autonomous Driving, Finance, Telecommunications etc).

    -   Underneath a cosmetically beautiful (API driven) UI that mediates between a human and a machine learning model, is an interplay of database accesses, hardware accelerators, quagmire of networks of activation functions that squeeze and squish matrices of numbers created by millions of lines of boring software that clean, drop, impute, transform and read what we call as 'source' or 'raw' data.

    -   So prior to looking at applications and use cases of AI in Telecom, the story of data has its own place and needs to be told.    
    ---
    #### :green[The background story:]
    ''')
    st.image('storyOfData.png', caption='Story of Data')

    st.divider()

    st.markdown('''
    #### :green[The story of perspectives :]
    ''')
    st.image('storyOfPers.png', caption='Story of Perspectives')
    st.divider()

    st.markdown('''
    #### :green[The story of AI/ML driven use cases :]
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
#### Summary by topic:

##### :green[O-RAN:]
- [**Technical summary on "Understanding O-RAN"**](https://medium.com/@rahulsound/understanding-o-ran-architecture-978cc49deea7) 
    -   From the paper: "Understanding O-RAN: Architecture, Interfaces, Algorithms, Security, and Research Challenges" [[full paper]](https://ieeexplore.ieee.org/iel7/9739/10130694/10024837.pdf)
- [**Technical summary on "xApps for O-RAN"**] 
    -   From the paper: "ColO-RAN: Developing Machine Learning-based xApps for Open RAN Closed-loop Control on Programmable Experimental Platforms | [[full paper]](https://ieeexplore.ieee.org/document/9814869)


##### :green[Energy Saving use case]:
- [**Technical summary on "Energy Aware Network Intelligence"**] 
    -   From the paper: "ScalO-RAN: Energy-aware Network Intelligence Scaling in Open RAN" [[full paper]](https://arxiv.org/abs/2312.05096)
- [**Technical summary on "Energy Consumtion in Open RAN"**] 
    -   From the paper: "Energy Consumption of Machine Learning Enhanced Open RAN: A Comprehensive Review" [[full paper]](https://yo-ran.org/wp-content/uploads/2024/06/Energy_Consumption_of_Machine_Learning_Enhanced_Open_RAN_A_Comprehensive_Review.pdf) by [YO-RAN](https://www.linkedin.com/company/yo-ran/about/) YOrkshire Open Radio Access Networks

##### :green[Network Slicing use case:]
- [**Technical summary on "Network Slicing "**] 
    -   From the paper: "Technical White Paper Network Slicing from Samsung" [[full paper]](https://images.samsung.com/is/content/samsung/assets/global/business/networks/insights/white-paper/network-slicing/200420_Samsung_Network_Slicing_Final.pdf)
- [**Technical summary on "Network Slicing Management"**] 
    -   From the paper: "Management of Network Slicing in 5G Radio Access Networks: Functional Framework and Information Models" [[full paper]](https://arxiv.org/abs/1803.01142)
- [**Technical summary on "Security KPIs for 5G slices"**] 
    -   From the paper: "Assessment of Security KPIs for 5G Network Slices for Special Groups of Subscribers" [[full paper]](https://www.mdpi.com/2504-2289/7/4/169)
- [**Technical summary on "AI based Network slicing"**] 
    -   From the paper: "AI-Based Resource Allocation in E2E Network Slicing with Both Public and Non-Public Slices" [[full paper]](https://www.mdpi.com/2076-3417/13/22/12505)
- [**Technical summary on "Network slicing framework"**] 
    -   From the paper: "An E2E Network Slicing Framework for Slice Creation and Deployment Using Machine Learning" [[full paper]](https://www.mdpi.com/1424-8220/23/23/9608)
- [**Technical summary on "DRLs for O-RAN slicing"**] 
    -   From the paper: "Safe and Accelerated Deep Reinforcement Learning-based O-RAN Slicing: A Hybrid Transfer Learning Approach" [[full paper]](https://ieeexplore.ieee.org/document/10329948)

##### :green[Traffic Steering use case:]
- [**Technical summary on "RL based xApp for Traffic Steering**](https://rahulsound.streamlit.app/~/+/AIMLProjects#near-rt-ric) 
    -   From the paper: "Programmable and Customized Intelligence for Traffic Steering in 5G Networks Using Open RAN Architectures" [[full paper]](https://arxiv.org/abs/2209.14171)
- [**Technical summary on "Traffic Steering use case**] 
    -   From the paper: "Toward Modular and Flexible Open RAN Implementations in 6G Networks: Traffic Steering Use Case and O-RAN xApps" [[full paper]](https://www.mdpi.com/1424-8220/21/24/8173)
'''
    )


    