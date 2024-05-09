import streamlit as st
import pandas as pd
import os
#from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_community.llms import OpenAI
import random
import time
import tempfile
from langchain.agents import load_tools 
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

#=======================================================================================================================#
load_dotenv()

# Initialize session state

if 'data' not in st.session_state:
    st.session_state.data = None

if 'agent' not in st.session_state:
    st.session_state.agent = None

st.set_page_config(
    page_title="Ask your data",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

#=======================================================================================================================#

#------------------ Sidebar ------------------#


#=======================================================================================================================#

#------------------ Main Page ------------------#

st.title('Netlogo + LLM')


st.write('Go to the **Netlogo Interface** page')

