import streamlit as st
import requests

# Replace this with your actual deployed backend URL (e.g., on Render or Railway)
API = "http://127.0.0.1:8000"

st.title("AWS Agreement RAG Chatbot")

question = st.text_input("Ask a question")

if st.button("Submit"):
    if not question:
        st.warning("Please enter a question.")
    else:
        # Using a try-except block to catch connection issues
        try:
            with st.spinner("Querying the RAG engine..."):
                response = requests.post(
                    f"{API}/ask", 
                    json={"query": question}, 
                    timeout=120
                )

            # Check if the response is successful (Status 200)
            if response.status_code == 200:
                data = response.json()
                st.subheader("Answer")
                st.success(data.get("answer", "No answer found"))

                st.subheader("Sources")
                for source in data.get("sources", []):
                    st.info(source)
            else:
                # If the server returned an error, display it clearly
                st.error(f"Backend Error ({response.status_code}): {response.text}")

        except requests.exceptions.RequestException as e:
            st.error(f"Connection error: {e}")

st.divider()
st.header("Analytics")

if st.button("Load Analytics"):
    try:
        response = requests.get(f"{API}/analytics")
        if response.status_code == 200:
            st.json(response.json())
        else:
            st.error(f"Failed to load analytics: {response.status_code}")
    except Exception as e:
        st.error(f"Error fetching analytics: {e}")