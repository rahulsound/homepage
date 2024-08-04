import streamlit as st


def run_summary():
    st.markdown('''
    #### :blue[Summary:]
    - The list of projects covered here are mainly related to ML based network optimizations - an endeavor I have been involved for the last 10 years.
    - These projects are a mix of PoCs and field-trials and my intention is to describe the thought process without divulging proprietary information.
    - I believe a multi-discplinary skillset is necessary to marry AI/ML and a complex domain such as Telecom.   
    - The materials I have used are from public domain.
                ''')

def run_near_rt_ric():
    st.markdown('''
                ---
                #### Overview:
                #### :blue[Reinforcement Learning based Traffic Steering xApp to steer the UE to the best secondary cell that would maximize the UE Throughput.]
                ---
                - Pubications:
                    -   Programmable and Customized Intelligence for Traffic Steering in 5G Networks Using Open RAN Architectures [[arXiv]](https://arxiv.org/abs/2209.14171), [[IEEE]](https://ieeexplore.ieee.org/document/10102369)
                    -   Mavenir’s RAN Intelligent Controller (RIC) Solution [[whitepaper]](https://www.mavenir.com/resources/mavenirs-ran-intelligent-controller-ric-solution/)
                    -   Building the World’s First O-RAN-Compliant, AI-Powered, Closed-Loop Near-RT RIC [[blog]](https://www.mavenir.com/blog/building-the-worlds-first-o-ran-compliant-ai-powered-closed-loop-near-rt-ric/)
                ---
                - References:
                    - Offline Reinforcement Learning: Tutorial, Review, and Perspectives on Open Problems [[arXiv]](https://arxiv.org/abs/2005.01643)
                    - An Optimistic Perspective on Offline Reinforcement Learning [[arXiv]](https://arxiv.org/abs/1907.04543)
                ---
                ##### :blue[Reinforcement Learning]:
                - Reinforcement Learning has been popularized by its effectiveness in fields like robotics and game-play.  
                - Though it is a sophisticated form of Machine learning, its adaptability to a changing environment make it suitable for a dynamic system such as a wireless network.  
                - The challenge to make it effective it to be able to represent the use case as a mathematical problem that can leverage the Reinforcement Learning principles.  
                ---
                
                ##### :blue[O-RAN Near-RT RIC]:
                - O-RAN WG2 specifies E2 interface with KPM (Key Performance Metrics) RC (RAN Control) Service Models that were utilized to build this soultion.  
                ---
                
                ##### :blue[System Design]:
                - The system is configured in NSA mode wherein the UE has an anchor LTE eNB cell and upto 7 NR cells.  
                - This is done using [[ns3]] (https://www.nsnam.org/)
                - There are about 20-100 UEs in the system doing full-buffer, bursty or a mix of full-buffer and bursty traffic.  
                - The UEs are moving between 2 and 4 m/s to simulate pedestrian/slow moving users.  
                - The E2 SM KPM implemented on the ns3 side streems UE, Cell and Node level KPMs to the Near-RT RIC.  
                - A data-ingestion pipeline within the Near-RT RIC processes incoming data stores it in an internal database.  
                - Cleaning, aggregation, null-value handling, interpolation etc. are othe procedures implemented within the ingestion pipeline.  
                ---
                

                ##### :blue[RL Design]:
                - Out of the several variants of RL, an offline off-policy style of RL was chosen.  
                - Being off-policy helps collect training samples from different 'expert' policies available in ns3. 
                - It also gives an opportunity to train and evaluate a custom policy different from the ones used to gather training data samples.   
                - This is shown in the image below.  
                - ![OfflineOffpolicy](offlineOffpolicy.png)

                ##### :blue[Data Flow]:

                ##### :blue[Evaluation]:

                The E2 node would stream KPM data with UE, Cell and Node specific information.  
                The RL model hosted in the Near-RT RIC cosumes these KPMs to 





                ''')
    

def run_non_rt_ric():
    st.write('run_non_rt_ric:')
    st.markdown('''
                ![link](./opendatacam.png)
                ''')

def run_node_profiling():
    st.write('run_node_profiling:')

def run_arima():
    st.write('run_arima:')

def run_kpi_prediction():
    st.write('run_kpi_prediction:')
