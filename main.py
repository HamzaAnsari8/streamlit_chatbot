import os
from dotenv import load_dotenv
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# load env variables
load_dotenv()

# streamlit page setup
st.set_page_config(
    page_title="Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Chatbot")

# initiate chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# display chat history
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# initialize Gemini LLM 
llm = ChatGoogleGenerativeAI(
    model="gemini-flash-latest",
    temperature=0.7
)

# user input
user_prompt = st.chat_input("Ask Chatbot...")

if user_prompt:
    # show user message
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append(
        {"role": "user", "content": user_prompt}
    )

    # invoke model 
    response = llm.invoke(  
        [
            SystemMessage(content="You are a helpful assistant"),
            *[
                HumanMessage(content=m["content"]) if m["role"] == "user"
                else AIMessage(content=m["content"])
                for m in st.session_state.chat_history
            ]
        ]
        )

    assistant_response = response.content

    # save assistant message
    st.session_state.chat_history.append(
        {"role": "assistant", "content": assistant_response}
    )

    # display assistant message
    with st.chat_message("assistant"):
        st.markdown(assistant_response)
