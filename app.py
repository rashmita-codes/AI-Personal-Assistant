import streamlit as st

from database.database import create_tables
from modules.tasks import (
    add_task,
    get_tasks,
    complete_task,
    delete_task
)


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


st.divider()


# -------------------------------
# TASK MANAGER
# -------------------------------

st.subheader("✅ Task Manager")


# Add task
with st.form("task_form"):

    task_title = st.text_input(
        "Task title",
        placeholder="Example: Complete Python assignment"
    )

    task_description = st.text_area(
        "Description",
        placeholder="Add some details about the task..."
    )

    col1, col2 = st.columns(2)

    with col1:
        priority = st.selectbox(
            "Priority",
            ["Low", "Medium", "High"]
        )

    with col2:
        due_date = st.date_input(
            "Due date"
        )

    submit_task = st.form_submit_button(
        "➕ Add Task"
    )


    if submit_task:

        if task_title.strip():

            add_task(
                task_title,
                task_description,
                priority,
                str(due_date)
            )

            st.success("✅ Task added successfully!")

        else:

            st.warning("Please enter a task title.")


# -------------------------------
# DISPLAY TASKS
# -------------------------------

st.write("### 📋 Your Tasks")

tasks = get_tasks()


if not tasks:

    st.info("No tasks yet. Add your first task above!")

else:

    for task in tasks:

        task_id = task[0]
        title = task[1]
        description = task[2]
        priority = task[3]
        due_date = task[4]
        status = task[5]

        with st.container():

            col1, col2, col3 = st.columns([5, 2, 1])

            with col1:

                st.write(f"**{title}**")

                if description:
                    st.caption(description)

                st.caption(
                    f"Priority: {priority} | Due: {due_date}"
                )

            with col2:

                if status == "Completed":
                    st.success("Completed")
                else:
                    st.warning("Pending")

            with col3:

                if status != "Completed":

                    if st.button(
                        "✅",
                        key=f"complete_{task_id}"
                    ):

                        complete_task(task_id)
                        st.rerun()

                if st.button(
                    "🗑️",
                    key=f"delete_{task_id}"
                ):

                    delete_task(task_id)
                    st.rerun()

            st.divider()


# -------------------------------
# DATABASE STATUS
# -------------------------------

st.success("🗃️ SQLite database connected successfully!")