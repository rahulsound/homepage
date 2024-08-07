import streamlit as st
#from MLInTelecom import run_ml_in_telecom, run_study_of_research_papers
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Research Papers", layout="wide")
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

def run_study_of_research_papers():
    st.markdown(
        '''
#### :violet[Technical Summaries:]

##### :green[O-RAN:]
- [**Technical summary on "Understanding O-RAN"**](https://medium.com/@rahulsound/understanding-o-ran-architecture-978cc49deea7) 
    -   From the paper: "Understanding O-RAN: Architecture, Interfaces, Algorithms, Security, and Research Challenges" [[full paper]](https://ieeexplore.ieee.org/iel7/9739/10130694/10024837.pdf)
- [**Technical summary on "xApps for O-RAN"**] 
    -   From the paper: "ColO-RAN: Developing Machine Learning-based xApps for Open RAN Closed-loop Control on Programmable Experimental Platforms | [[full paper]](https://ieeexplore.ieee.org/document/9814869)

##### :green[Traffic Steering use case:]
- [**Technical summary on "RL based xApp for Traffic Steering**](https://rahulsound.streamlit.app/~/+/AIMLProjects#near-rt-ric) 
    -   From the paper: "Programmable and Customized Intelligence for Traffic Steering in 5G Networks Using Open RAN Architectures" [[full paper]](https://arxiv.org/abs/2209.14171)
- [**Technical summary on "Traffic Steering use case**] 
    -   From the paper: "Toward Modular and Flexible Open RAN Implementations in 6G Networks: Traffic Steering Use Case and O-RAN xApps" [[full paper]](https://www.mdpi.com/1424-8220/21/24/8173)

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


'''
    )
def run_ml_in_telecom():
    st.markdown('''
    #### :violet[My Articles:]
                
    ##### :green[The story of Data in Telecom:]
    - [**Part1 - An Introduction & Perspectives**](https://medium.com/@rahulsound/the-story-of-ai-ml-driven-use-cases-for-telecom-0527067f1d60) 
        -   _Though one may be led to believe that every thought-experiement is realizable with AI, the story is very different for individual domains (Computer Vision, Natural Language Processing, Autonomous Driving, Finance, Telecommunications etc). So prior to looking at applications and use cases of AI in Telecom, the story of data has its own place and needs to be told. Underneath a cosmetically beautiful (API driven) UI that mediates between a human and a machine learning model, is an interplay of database accesses, hardware accelerators, quagmire of..._   

    ''')
    st.image('storyOfData.png', width=500, caption='https://medium.com/@rahulsound/the-story-of-ai-ml-driven-use-cases-for-telecom-0527067f1d60')

    #st.image('storyOfPers.png', width=500 , caption='Story of Perspectives')
    st.divider()

    st.markdown('''
    - [**Part2 - The Approach(1): Get the work done!**](https://medium.com/@rahulsound/the-story-of-ai-ml-driven-use-cases-for-telecom-59e1198d991b)
        -   _This approach looks at data and possibilities from a Telecom operator's point of view as they already have the data albeit not in a form that readily renders itself for data or ML-driven insights...._

    ''')
    #st.image('appr1.png',width=500, caption='Approach#1')
    st.image('son2.png',width=500, caption='https://www-file.huawei.com/-/media/corporate/pdf/mbb/next-gene-ation-son-for-5g.pdf?la=en')
    st.divider()

    st.markdown('''
    - [**Part2 - The Approach(2): Need for Alliances**](https://medium.com/@rahulsound/the-story-of-ai-ml-driven-use-cases-for-telecom-b2fbb2876e97)
        -   _Following the previous line of thought, there are different players in this field each having different strengths and weaknesses. So this part covers the foundations of such alliances — the mission, objective, gain and...._

    ''')
    st.image('appr2.png' , width=500, caption='Approach#2')
    st.divider()

    st.markdown('''
    - [**Part3 - The Approach(3): Ride the AI Wave!**]

    ''')
    st.image('appr3.png', width=500, caption='Approach#3')
    st.divider()

    # st.markdown('''
    # ###### Details of these approaches and further infomation -> In Progress...

    # ''')
    st.markdown('''
    - [**The Knowledge Transfer - Principles to take from Sherlock Holmes to Analytics & from Computing to Behavioral Science**](https://medium.com/@rahulsound/the-knowledge-transfer-principles-you-take-from-sherlock-holmes-to-analytics-and-from-computing-c4380ef17b09)
        -   _Introspection: I have noticed that certain lines I read or hear just jump out at me and make me pause and look up at the ceiling munching and ruminating over its implications in different contexts. I realized that I can strip out the context and relate to it from totally ...._

    ''')
    st.markdown('''
    - [**5 Tips for a Budding Data Scientist:**](https://medium.com/@rahulsound/notes-to-a-budding-data-science-enthusiast-ce47720b679b)
        -   _When you read the sentence ‘Mercury is hot’ — you immediately want to find out if the word ‘mercury’ here refers to the planet or liquid metal. Why don’t we do this when we come across words like ‘cluster’ or ‘model’ in a data science context? It is easy to lose ourselves in this heap of ...._

    ''')
 
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

def run_medium():
        st.markdown(
        '''
Here are some of my articles related to AI/ML in Telecom:
1. [Understanding O-RAN Architecture](https://medium.com/@rahulsound/understanding-o-ran-architecture-978cc49deea7)
2. [The story of AI/ML driven use cases for Telecom: Part1](https://medium.com/@rahulsound/the-story-of-ai-ml-driven-use-cases-for-telecom-0527067f1d60)

---
''')
        
st.subheader(":blue[Rahul Soundrarajan]", anchor='#about')
st.markdown('''
###### [LinkedIn](https://www.linkedin.com/in/rahul-soundrarajan/) | [Medium](https://medium.com/@rahulsound) | [Contact](mailto:rahulsound@gmail.com)
                ''')

#run_medium()
def streamlit_menu():
    selected = option_menu(
        menu_title=None,  # required
        options=["All", "Technical Summaries", "My Articles"],  # required
        #icons=["house", "mortarboard", "asterisk"],  # optional
        menu_icon="cast",  # optional
        default_index=0,  # optional
        orientation="horizontal",
    )
    return selected

selected = streamlit_menu()
run_sub_header()
st.header(":blue[Research Interests]", anchor='#research-interests')

st.markdown(
        '''
##### Using AI/ML to optimise Telecom Networks is one of my core interests. 
##### To learn and collaborate, I prepare summaries of research papers and also share my personal views as articles on [Medium](https://medium.com/@rahulsound). 
---
''')

if selected == 'Technical Summaries':
    run_study_of_research_papers()
elif selected == 'My Articles':
    run_ml_in_telecom()
else:
    col1, col2 = st.columns(2)
    with col1:
        run_study_of_research_papers()
    with col2:
        run_ml_in_telecom()


