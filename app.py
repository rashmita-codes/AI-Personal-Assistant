import streamlit as st

st.set_page_config(
    page_title="AI Personal Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Personal Assistant")

st.write(
    "Your personal AI assistant for chatting, "
    "managing tasks, and taking notes."
)

st.divider()

st.subheader("💬 Chat")

message = st.text_input(
    "Enter your message",
    placeholder="Ask your assistant something..."
)

if st.button("Send"):
    if message:
        st.info("AI functionality will be connected soon.")
    else:
        st.warning("Please enter a message.")