import streamlit as st
import requests

API = "https://your-render-app.onrender.com"

st.title("AWS Agreement RAG Chatbot")

question = st.text_input(
    "Ask a question"
)

if st.button("Submit"):

    if not question:
        st.warning("Please enter a question")
    else:
        try:
            response = requests.post(
                f"{API}/ask",
                json={"query": question},
                timeout=60
            )

            st.write("Status Code:", response.status_code)

            if response.status_code == 200:

                data = response.json()

                st.subheader("Answer")
                st.success(data.get("answer", "No answer found"))

                st.subheader("Sources")

                for source in data.get("sources", []):
                    st.info(source)

            else:
                st.error(
                    f"API Error: {response.text}"
                )

        except Exception as e:
            st.error(f"Connection error: {e}")


st.divider()

st.header("Analytics")

if st.button("Load Analytics"):

    try:
        response = requests.get(
            f"{API}/analytics",
            timeout=60
        )

        if response.status_code == 200:
            st.json(response.json())
        else:
            st.error(response.text)

    except Exception as e:
        st.error(f"Analytics error: {e}")