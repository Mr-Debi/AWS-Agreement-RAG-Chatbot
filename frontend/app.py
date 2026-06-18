import streamlit as st
import requests

API = "https://aws-agreement-rag-chatbot.streamlit.app/"


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
        json={"query": question}
    )

    st.write("Status Code:", response.status_code)
    st.write("Response Text:", response.text)

    if response.status_code == 200:
        data = response.json()

        st.success(data["answer"])

        if "sources" in data:
            st.subheader("Sources")
            for source in data["sources"]:
                st.info(source)
    else:
        st.error(f"API Error: {response.text}")

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