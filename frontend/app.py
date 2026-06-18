import streamlit as st
import requests

API = "https://your-render-app.onrender.com"


# st.set_page_config(
#     page_title="AWS Agreement Q&A",
#     layout="wide"
# )

st.title("AWS Agreement RAG Chatbot")

question = st.text_input(
    "Ask a question"
)

if st.button("Submit"):

    response = requests.post(
        f"{API}/ask",
        json={
            "query": question
        }
    )

    data = response.json()

    st.subheader("Answer")

    st.success(data["answer"])

    st.subheader("Sources")

    for source in data["sources"]:
        st.info(source)

st.divider()

st.header("Analytics")

if st.button("Load Analytics"):

    response = requests.get(
        f"{API}/analytics"
    )

    st.json(
        response.json()
    )