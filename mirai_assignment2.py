import streamlit as st

st.title("THE MULTIVERSE OF CHATBOTS")
st.write("Talk with AI Across Every Domain")

# Create chat history
if "history" not in st.session_state:
    st.session_state.history = []

# Sidebar
Domain = st.sidebar.selectbox("Select Domain",["Artificial Intelligence","Education","Career","Software Development","Motivational Coach","Stand-up Comedian","Fitness Trainer","Books","Sports","Programming Assistant","Health care","Food and Recipes","Movies"])

language = st.sidebar.selectbox("Select Language",["English","Kannada","Hindi","Tamil","Telugu","Malayalam","Marathi","Spanish"])

# Clear Chat Button
if st.sidebar.button("🗑 Clear Chat"):
    st.session_state.history = []
    st.rerun()

# Chat History
st.sidebar.subheader("📜 Chat History")

if st.session_state.history:
    for chat in reversed(st.session_state.history):
        st.sidebar.write(f"**You:** {chat['user']}")
        st.sidebar.write(f"**AI:** {chat['bot']}")
        st.sidebar.markdown("---")
else:
    st.sidebar.write("No chat history.")

from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

user_message = st.text_input("What do you want to know?")

if st.button("SEND"):
    if user_message:
        ai_instructions = (
            f"You are acting as a {Domain} chatbot. "
            f"Reply only in {language}. "
            f"User message: {user_message}"
        )

        with st.spinner("Connecting to the multiverse..."):
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=ai_instructions
            )

            st.success("Message received!")
            st.write(response.text)

            # saving chat history
            st.session_state.history.append({
                "user": user_message,
                "bot": response.text
            })

    else:
        st.warning("Please write the message first.")
    