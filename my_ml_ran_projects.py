import streamlit as st


def run_summary():  
    st.header(":blue[Summary]")  
    st.markdown('''
    - The list of projects covered here are mainly related to ML based network optimizations - an endeavor I have been involved for the last 10 years.
    - These projects are a mix of PoCs and field-trials and my intention is to describe the thought process without divulging proprietary information.
    - I believe a multi-discplinary skillset is necessary to marry AI/ML and a complex domain such as Telecom.   
    - The materials I have used are from public domain.
                ''')
    st.markdown("")

def run_near_rt_ric():
    st.markdown("")
    st.header(':blue[Near-RT RIC]')    
    st.markdown('''
                #### Overview:
                ##### :blue[Reinforcement Learning based Traffic Steering xApp to steer the UE to the best secondary cell that would maximize the UE Throughput.]
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
                ''')
    st.image('system-design.png', width=600, caption='https://arxiv.org/abs/2209.14171')
    st.markdown('''
                ---
                ##### :blue[RL Design]:
                - Out of the several variants of RL, an offline off-policy style of RL was chosen.  
                - Being off-policy helps collect training samples from different 'expert' policies available in ns3. 
                - It also gives an opportunity to train and evaluate a custom policy different from the ones used to gather training data samples.   
                - This is shown in the image below.
                ''')
    st.image('offlineOffpolicy.png', width=600, caption='https://arxiv.org/abs/2005.01643')
    st.markdown('''
                - This way the RL agent is deployed after training is completed.
                - It continues to collect samples [replay buffer] and is trainied in batches enabling it to customize its behaviour based on the mix of training data and new experiences seen after deployment.
                - A list of key aspects that make the RL framework:
                    - **State space**   : Consists of the E2SM KPMs from E2 nodes [total 8] consisting of UE, Cell and Nodel level data at a granularity of 100ms of simulation time.  
                    - **Action space**  : 7 : Handover to 6 other NR cells OR 'no handover' to continue remaining in the current NR cell.  
                    - **Reward**        : Exponential improvement in UE throughput - exponential decay \(alpha) times the time duration since last handover. The cost is to discourage the agent from taking too frequent handovers.
                - The replay buffer collected for training consists of this [S, A, R, S'] tuples where S' corresponds to the 'next state' after taking action A.  
                - The architecture of the RL agent includes other design aspects such as:  
                    - Deciding the order of Markov Decision Process [MDP] - single event to infinte horizon
                    - Exploration / Exploitation trade-off that accounts for the proportion of actions the agent should take based on historic data that maximizes cumulative reward v/s an exploratory action to discover the state-space.  
                    - Soft-updates deciding the frequency and weights for overwriting model weights.  
                    - Underlying architecture [Deep-Q Neural Network in this case] that defines the number of layers and number of neurons per layer.  
                    - Activation functions, connectivity, pooling, drop-off etc. within the DQN.  
                    - Learning Rate, batch-size and number of samples required for each training iteration.  
                    - Number of heads of the REM  [Random Ensemble Mixture], specifically implemented to ensure the model doesn't over-estimate Q-values for out-of-distribution samples; as shown below.  
                ''')
    st.image('dqn-rem.png', width=600, caption='arXiv:1907.04543v4 [cs.LG] 22 Jun 2020')
    st.markdown('''
                ##### :blue[Data Flow]:
                - Once deployed, the live E2 SM KPMs get ingested via the streaming pipeline, they undergo transformation [identical to the training phase] and get are fed into the input of the DQN network.  
                - The agent outputs the target cell that would maximize the UE's Throughput. This could be the same cell [meaning no handover].  
                - This cell-id is handled by the Near-RT RIC framework to prepare and invoke the E2 SM RC service that gets reflected in the ns3.  
                - The UE is now handed over to this target-cell OR continues to remain in the same cell depending on the cell-id.
                - There are other aspects to this flow related to E2 procedures such as:
                    - ASN.1 encoding of parameters 
                    - E2 procedures such as Setup, Subscription, Indication to facilitate this message exchange between E2 nodes and Near-RT RIC.
                ---
                ##### :blue[Evaluation]:
                - The RL agent was evaluated live during the [O-RAN PlugFest of 2021](https://www.mavenir.com/blog/building-the-worlds-first-o-ran-compliant-ai-powered-closed-loop-near-rt-ric/#Section_4_O-RAN_Plugfest_Demo_results)
                - The evaluation results are presented [here](https://www.mavenir.com/blog/building-the-worlds-first-o-ran-compliant-ai-powered-closed-loop-near-rt-ric/#Section_4_O-RAN_Plugfest_Demo_results)
                ''')
    st.markdown("")

def run_non_rt_ric():
    st.markdown("")
    st.header(':blue[Non-RT RIC]')    
    st.markdown('''
                #### Overview:
                #### :blue[MLB and MRO to reduce Handovers and improve UE throughput in a Tier-1 customer network]
                ---
                - Pubications:
                    -   [Network Optimization: Non-Real-Time RIC Trial Analysis](https://www.mavenir.com/resources/network-optimization-non-real-time-ric-trial-analysis/)
                ---
                ##### :blue[Bayesian Optimization based algorithm]:
                - Details to be filled.  
            ''')
    st.markdown("")

def run_node_profiling():
    st.markdown("")
    st.header(":blue[Node Profiling]")
    st.markdown('''
                ---
                #### Overview:
                #### :blue[Utilize Configuration Parameters and Performance Counters of a 4G network to profile eNBs]
                ---
                - IP:
                    -   [Node Profiling ](https://patents.justia.com/patent/10735287)
                ---
                ##### :blue[Details to be filled]:
                ---
                
            ''')
    st.markdown("")

def run_arima():
    st.markdown("")
    st.header(":blue[ARIMA]")
    st.markdown('''
                ---
                #### Overview:
                #### :blue[Utilize seasonlity in Wireless KPIs for ARIMA based forecasting]
                ---
                - IP:
                    -   [ARIMA based forecast](https://patents.justia.com/patent/20210224699)
                ---
                ##### :blue[Details to be filled]:
                ---
  ''')
    st.markdown("")

def run_kpi_prediction():
    st.markdown("")
    st.header(":blue[KPI Prediction]")
    st.markdown('''
                ---
                #### Overview:
                #### :blue[Utilize CMs and PMs in a wireless network for KPI prediction]
                ---
                - IP:
                    -   [KPI Prediction](https://patents.justia.com/patent/11115287)
                ---
                ##### :blue[Details to be filled]:
                ---
  ''')
    st.markdown("")
