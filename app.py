import streamlit as st
from graph import app
st.title("🤖 AI Research Agent")
st.caption("Ask me anything — I'll search the web for you!")
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask me anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Searching and thinking..."):
            from langchain_core.messages import HumanMessage
            result = app.invoke({"messages": [HumanMessage(content=prompt)]})
            response = result["messages"][-1].content
        st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})