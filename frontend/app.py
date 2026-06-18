import streamlit as st
import requests

API = "https://your-fastapi-app.onrender.com"

st.title("AWS Agreement RAG Chatbot")

question = st.text_input("Ask a question")

if st.button("Submit"):
    if not question:
        st.warning("Please enter a question")
    else:
        # Initialize data as None to prevent NameError
        data = None 
        
        with st.spinner("Querying the RAG engine... (This may take a moment if the server is waking up)"):
            try:
                response = requests.post(
                    f"{API}/ask",
                    json={"query": question},
                    timeout=120  # Increased to 120 seconds for cold starts
                )

                if response.status_code == 200:
                    data = response.json()
                else:
                    st.error(f"API Error ({response.status_code}): {response.text}")

            except requests.exceptions.Timeout:
                st.error("The request timed out. The server might be taking too long to process the document.")
            except Exception as e:
                st.error(f"Connection error: {e}")

        # Only process data if it was successfully retrieved
        if data:
            st.subheader("Answer")
            st.success(data.get("answer", "No answer found"))

            st.subheader("Sources")
            for source in data.get("sources", []):
                st.info(source)