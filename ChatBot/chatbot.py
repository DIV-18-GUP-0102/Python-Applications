import streamlit as st
import openai

st.title("Mini Chat Bot")

openai.api_key = st.secrets["OPENAI_API_KEY"]

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat app history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

# Assistant response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for response in openai.chat.completions.create(
            model = st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream = True,
        ):
            if response.choices[0].delta.content: full_response += response.choices[0].delta.content
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})

# OPENAI_API_KEY = "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"
# Network Hosted: http://10.12.55.69:8501