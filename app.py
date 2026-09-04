import streamlit as st

from database.database import create_tables

from modules.tasks import (
    add_task,
    get_tasks,
    complete_task,
    delete_task
)

from modules.notes import (
    add_note,
    get_notes,
    delete_note
)

from modules.ai import ask_ai
from modules.nlp import detect_intent, extract_task , extract_task_details


# Create database tables
create_tables()


# Page configuration
st.set_page_config(
    page_title="AI Personal Assistant",
    page_icon="🤖",
    layout="wide"
)


# -------------------------------
# HEADER
# -------------------------------

st.title("🤖 AI Personal Assistant")

st.write(
    "Your personal AI assistant for chatting, "
    "managing tasks, and taking notes."
)

st.divider()


# -------------------------------
# CHAT
# -------------------------------

# -------------------------------
# AI CHAT + NLP
# -------------------------------

st.subheader("💬 Chat with AI")

message = st.text_input(
    "Enter your message",
    placeholder="Ask your AI assistant anything..."
)

if st.button("🤖 Ask AI"):

    if message.strip():

        intent = detect_intent(message)

        st.caption(f"Detected intent: {intent}")

        if intent == "CHAT":

            with st.spinner("🤖 Thinking..."):

                response = ask_ai(message)

                st.write("### 🤖 Assistant")
                st.write(response)

        elif intent == "TASK":

            task_title, priority, due_date = extract_task_details(message)

            if task_title:

                add_task(
                    task_title,
                    "Created using AI Assistant",
                    priority,
                    due_date
                )

                st.success(
                    f"✅ Task added: {task_title}"
                )

                st.write(f"🔥 **Priority:** {priority}")

                if due_date:
                    st.write(f"📅 **Due date:** {due_date}")
                else:
                    st.write("📅 **Due date:** Not specified")

        elif intent == "NOTE":

            st.info("📝 Note detected.")

        elif intent == "LIST_TASKS":

            st.info("📋 Task list detected.")

        elif intent == "LIST_NOTES":

            st.info("📝 Notes list detected.")

    else:

        st.warning("Please enter a message.")