import streamlit as st
from streamlit_option_menu import option_menu
from pages.Current_Project_Explora import run_explora
st.set_page_config(page_title="AI-ML Projects", layout="wide")
# import sys
# sys.path.insert(0, '...')
# from About import online_flag, run_sub_header
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
            
def run_summary():  
    st.header(":blue[Summary]", anchor='summary-projects')  
    st.markdown('''
    - The list of projects covered here are mainly related to ML based network optimizations - an endeavor I have been involved for the last 10 years.
    - These projects are a mix of PoCs and field-trials and my intention is to describe the thought process without divulging proprietary information.
    - I believe a multi-discplinary skillset is necessary to marry AI/ML and a complex domain such as Telecom.   
    - The materials I have used are from public domain.
                ''')
    st.markdown("---")

def run_near_rt_ric():
    st.header(':blue[Near-RT RIC]', anchor='near-rt-ric')    
    st.markdown('''
                #### Overview:
                ##### :blue[Reinforcement Learning based Traffic Steering xApp to steer the UE to the best secondary cell that would maximize the UE Throughput.]
                ---
                ##### :blue[Publications]:
                -   Programmable and Customized Intelligence for Traffic Steering in 5G Networks Using Open RAN Architectures [[arXiv]](https://arxiv.org/abs/2209.14171), [[IEEE]](https://ieeexplore.ieee.org/document/10102369)
                -   Mavenir’s RAN Intelligent Controller (RIC) Solution [[whitepaper]](https://www.mavenir.com/resources/mavenirs-ran-intelligent-controller-ric-solution/)
                -   Building the World’s First O-RAN-Compliant, AI-Powered, Closed-Loop Near-RT RIC [[blog]](https://www.mavenir.com/blog/building-the-worlds-first-o-ran-compliant-ai-powered-closed-loop-near-rt-ric/)
                ---
                ##### :blue[References]:
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
                - The evaluation results are presented [here](https://www.mavenir.com/blog/building-the-worlds-first-o-ran-compliant-ai-powered-closed-loop-near-rt-ric/#Section_4_O-RAN_Plugfest_Demo_results)''')
    st.markdown("---")

def run_non_rt_ric():
    st.header(':blue[Non-RT RIC]', anchor='non-rt-ric')    
    st.markdown('''
                #### Overview:
                ##### :blue[MLB and MRO to reduce Handovers and improve UE throughput in a Tier-1 customer network]
                ---
                ##### :blue[Publications]:
                -   [Network Optimization: Non-Real-Time RIC Trial Analysis](https://www.mavenir.com/resources/network-optimization-non-real-time-ric-trial-analysis/)
                ---
                ##### :blue[Bayesian Optimization based algorithm]:
                - References:
                    - [BOTORCH: A Framework for Efficient Monte-Carlo Bayesian Optimization](https://proceedings.neurips.cc/paper_files/paper/2020/file/f5b1b89d98b7286673128a5fb112cb9a-Paper.pdf)
                    - [A Flexible Framework for Multi-Objective Bayesian Optimization using Random Scalarizations](https://arxiv.org/abs/1805.12168)
                    - [Multi-Task Bayesian Optimization](https://proceedings.neurips.cc/paper_files/paper/2013/file/f33ba15effa5c10e873bf3842afb46a6-Paper.pdf)
                ---
                ##### :blue[Overview]:
                -   This objective was to demonstrate a RIC based solution performs at par or better compared to a legacy RAN setup.  
                -   The trial was RIC solution was deployed in a cluster of cells and the KPIs were monitored for evaluation of performance.  
                -   This was a  MRO / MLB use case, KPIs monitored included distribution of RSRP, RSRQ, CQI, BLER, UE Throughput, HO statistics such as Attempts, Failures (including causes), Call Drop rate etc.  
                -   The configuration management (CM) paramters included A3 measurement Offset, Hysteresis, RS boost (Pa/Pb).
               ---
                ##### :blue[Evaluation and Tools used]:
                -   I used [glueviz](https://glueviz.org/) extensively in visualizing the KPIs to compare samples pre-and-post RIC depolyment.
                -   It has built-in capability to visualize multi-dimensional linked data that was handy to color the same cells pre and post RIC deployment.
                -   The paper has many plots that help in this evaluation especially the distribution of Timing Advance (TA) pre and post RIC deployment. It clearly shows the CM changes ensured UEs neither end-up in no-coverage zones OR in areas where multiple cells have a strong reference signals.
                -   The evaluation also shows decrease in PRB utilization and BLER, and improvement in SINR.    
                ---    
                ##### :blue[Objective and Design]:
                -   The objective was to tune the CMs to maximise specific KPIs such as user throughput and minimize KPIs as Call Drop Rate.
                -   Given the state space consisting of CMs  (including their ranges) and the KPIs, the problem was modelled as a joint optimization function that would find the right combination of parameter values in the CM feature space that would maxmise UE Throughpt KPI and reduce Call Drop KPI.
                ---    
                ##### :blue[Bayesian Optimization and BoTorch Algorithm]:
                -   Bayesian Optimization is a probabilistic model-based optimization technique used to find the minimum or maximum of a function that is expensive to evaluate. It is particularly useful for optimizing black-box functions where the objective function does not have a known form and its evaluations are noisy or costly.
            ''')
    st.write('- [[Reference: jonathan-guerne]](https://jonathan-guerne.medium.com/an-introduction-to-bayesian-optimization-for-hyperparameter-tuning-4561825bf47b)')
    st.image('bayesopt.png', caption='Bayesian Optimization breakdown')
    st.markdown('''
                -   BOTORCH is a modern programming framework for Bayesian optimization that combines Monte-Carlo (MC) acquisition functions, autodifferentiation, and variance reduction techniques. 
                -   BOTORCH’s modular design facilitates flexible specification and optimization of probabilistic models written in PyTorch, simplifying implementation of new acquisition functions. 
            ''')
    st.image('botorch.png', width=900, caption='https://proceedings.neurips.cc/paper_files/paper/2020/file/f5b1b89d98b7286673128a5fb112cb9a-Paper.pdf')
    st.markdown('''
                -   The acquisition function follows a strategy of _'exploration v/s exploitation'_ which could sound familiar to an angent in a Reinforcement Learning framework, attempting to maximise the long term return. 
                -   In the context of Bayesian Optimization, exploration-exploitation refers to the balance between two strategies when selecting the next point to evaluate:
                    -   **Exploration**: Involves searching in areas of the input space where the model's predictions are uncertain or where fewer evaluations have been conducted. The goal of exploration is to gather more information about the objective function across the entire search space. This helps in building a more accurate surrogate model, reducing uncertainty, and potentially discovering new regions that might contain better solutions.
                    -   **Exploitation**: Involves focusing on areas where the surrogate model predicts high performance based on current knowledge. The goal of exploitation is to make use of the information already gathered to find the optimum value more quickly by evaluating points that are likely to yield the best results according to the current model.
                    -   Balancing Exploration and Exploitation:
                        -   Too much exploitation can lead to local optima, where the search gets stuck in a region that is suboptimal because it ignores potentially better areas that have not been explored.
                        -   Too much exploration can lead to inefficient use of resources, where the optimization process spends too much time evaluating points in regions that do not yield significant improvements.
                ''')

    st.image('multi-obj-botorch.png', caption='https://jonathan-guerne.medium.com/multi-objective-bayesian-optimization-with-botorch-3c5cf348c63b')

    st.markdown('''
                -   As shown in the toy-example above, after 15 iterations (and the end of the optimization in this case) an optimal has been reached around x = -0.2. When looking at the graph we can see that this is in fact a zone where both functions reach minimum.
                -   Similarly, in the case of MLB/MRO optimization, BOTORCH helped identify the CM param values that resulted in reduction of HO failures and improvement of UE Throughput.
                ---
                ''')
         
    st.markdown("---")

def run_node_profiling():
    st.header(":blue[Node Profiling]", anchor='node-profiling')
    st.markdown('''
                #### Overview:
                #### :blue[Utilize Configuration Parameters and Performance Counters of a 4G network to profile eNBs]
                ---
                - IP:
                    -   [Node Profiling ](https://patents.justia.com/patent/10735287)
                ---
                ##### :blue[Details to be filled]:
                ---
                
            ''')
    st.markdown("---")

def run_arima():
    st.header(":blue[ARIMA]", anchor='arima')
    st.markdown('''
                #### Overview:
                #### :blue[Utilize seasonlity in Wireless KPIs for ARIMA based forecasting]
                ---
                - IP:
                    -   [ARIMA based forecast](https://patents.justia.com/patent/20210224699)
                ---
                ##### :blue[Details to be filled]:
                ---
  ''')
    st.markdown("---")

def run_kpi_prediction():
    st.header(":blue[KPI Prediction]", anchor='kpi-prediction')
    st.markdown('''
                #### Overview:
                #### :blue[Utilize CMs and PMs in a wireless network for KPI prediction]
                ---
                - IP:
                    -   [KPI Prediction](https://patents.justia.com/patent/11115287)
                ---
                ##### :blue[Details to be filled]:
                ---
  ''')
    st.markdown("---")

def streamlit_menu():
    selected = option_menu(
        menu_title=None,  # required
        options=["All", "Explora", "Near-RT RIC", "Non-RT RIC", "Node Profiling", "ARIMA", "KPI Prediction"],  # required
        #icons=["house", "mortarboard", "asterisk"],  # optional
        menu_icon="cast",  # optional
        default_index=0,  # optional
        orientation="horizontal",
    )
    return selected

st.subheader(":blue[Rahul Soundrarajan]", anchor='#about')
st.markdown('''
###### [LinkedIn](https://www.linkedin.com/in/rahul-soundrarajan/) | [Medium](https://medium.com/@rahulsound) | [Contact](mailto:rahulsound@gmail.com)
                ''')
    
selected = streamlit_menu()
run_sub_header()
if selected == "Explora":
    run_explora()
elif selected == "Near-RT RIC":
    run_near_rt_ric()
elif selected == "Non-RT RIC":
    run_non_rt_ric()
elif selected == "Node Profiling":
    run_node_profiling()
elif selected == "ARIMA":
    run_arima()
elif selected == "KPI Prediction":
    run_kpi_prediction()
else:
    run_summary()
    run_explora()    
    run_near_rt_ric()
    run_non_rt_ric()
    run_node_profiling()
    run_arima()
    run_kpi_prediction()
