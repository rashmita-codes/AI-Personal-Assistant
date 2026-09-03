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
# AI CHAT
# -------------------------------

st.subheader("💬 Chat with AI")

message = st.text_input(
    "Enter your message",
    placeholder="Ask your AI assistant anything..."
)

if st.button("🤖 Ask AI"):

    if message.strip():

        with st.spinner("Thinking..."):

            try:
                response = ask_ai(message)

                st.write("### 🤖 Assistant")
                st.write(response)

            except Exception as e:
                st.error("Something went wrong while contacting the AI.")
                st.caption(str(e))

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
# NOTES MANAGER
# -------------------------------

st.divider()

st.subheader("📝 Notes Manager")


# Create a new note
with st.form("note_form"):

    note_title = st.text_input(
        "Note title",
        placeholder="Example: Python Important Concepts"
    )

    note_content = st.text_area(
        "Note content",
        placeholder="Write your note here..."
    )

    save_note = st.form_submit_button(
        "💾 Save Note"
    )

    if save_note:

        if note_title.strip() and note_content.strip():

            add_note(
                note_title,
                note_content
            )

            st.success("✅ Note saved successfully!")

        else:

            st.warning(
                "Please enter both a title and note content."
            )


# -------------------------------
# DISPLAY NOTES
# -------------------------------

st.write("### 📚 Your Notes")

notes = get_notes()


if not notes:

    st.info(
        "No notes yet. Create your first note above!"
    )

else:

    for note in notes:

        note_id = note[0]
        title = note[1]
        content = note[2]
        created_at = note[3]

        with st.container():

            col1, col2 = st.columns([5, 1])

            with col1:

                st.write(f"**{title}**")

                st.write(content)

                st.caption(
                    f"Created: {created_at}"
                )

            with col2:

                if st.button(
                    "🗑️ Delete",
                    key=f"delete_note_{note_id}"
                ):

                    delete_note(note_id)

                    st.rerun()

            st.divider()


# -------------------------------
# DATABASE STATUS
# -------------------------------

st.success("🗃️ SQLite database connected successfully!")