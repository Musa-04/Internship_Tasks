import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

st.set_page_config(page_title="LangChain Chatbot")

st.title("LangChain Chatbot")

openai_api_key = st.text_input("Enter OpenAI API Key", type="password")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display messages
for msg in st.session_state.messages:
    with st.chat_message(msg['role']):
        st.markdown(msg["content"])

# Chat input
if prompt := st.chat_input("Type your message..."):

    if not openai_api_key:
        st.error("Please enter API key")
    else:
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("user"):
            st.markdown(prompt)

        llm = ChatOpenAI(
            model="gpt-4o-mini",
            api_key=openai_api_key
        )

        prompt_template = ChatPromptTemplate.from_messages([
            ("system", "You are a helpful assistant."),
            ("user", "{question}")
        ])

        chain = prompt_template | llm | StrOutputParser()

        response = chain.invoke({"question": prompt})

        st.session_state.messages.append({
            "role": "assistant",
            "content": response
        })

        with st.chat_message("assistant"):
            st.markdown(response)