import streamlit as st
from datetime import date

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

from modules.nlp import (
    detect_intent,
    extract_task,
    extract_task_details,
    extract_note
)


# =====================================================
# DATABASE
# =====================================================

create_tables()


# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="AI Personal Assistant",
    page_icon="🤖",
    layout="wide"
)


# =====================================================
# HEADER
# =====================================================

st.title("🤖 AI Personal Assistant")

st.write(
    "Your intelligent assistant for managing tasks, "
    "notes, calendar events and AI conversations."
)

st.divider()


# =====================================================
# LOAD DATA
# =====================================================

tasks = get_tasks()
notes = get_notes()


# =====================================================
# DASHBOARD STATISTICS
# =====================================================

total_tasks = len(tasks)

completed_tasks = sum(
    1 for task in tasks
    if task[5] == "Completed"
)

pending_tasks = total_tasks - completed_tasks

total_notes = len(notes)


# =====================================================
# DASHBOARD
# =====================================================

st.header("📊 Dashboard")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "📋 Total Tasks",
        total_tasks
    )

with col2:
    st.metric(
        "⏳ Pending Tasks",
        pending_tasks
    )

with col3:
    st.metric(
        "✅ Completed",
        completed_tasks
    )

with col4:
    st.metric(
        "📝 Notes",
        total_notes
    )


st.divider()


# =====================================================
# NAVIGATION
# =====================================================

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    [
        "🏠 Dashboard",
        "✅ Todo List",
        "📝 Notes",
        "📅 Calendar",
        "🤖 AI Chat"
    ]
)


# =====================================================
# TAB 1 — DASHBOARD
# =====================================================

with tab1:

    st.subheader("📊 Overview")

    if total_tasks == 0:

        st.info(
            "No tasks yet. Go to Todo List and add your first task."
        )

    else:

        progress = completed_tasks / total_tasks

        st.write("### Task Progress")

        st.progress(progress)

        st.write(
            f"{completed_tasks} of {total_tasks} tasks completed"
        )

        st.divider()

        st.write("### 🔥 Recent Tasks")

        for task in tasks[:5]:

            task_id = task[0]
            title = task[1]
            priority = task[3]
            due_date = task[4]
            status = task[5]

            if status == "Completed":
                icon = "✅"
            else:
                icon = "⏳"

            st.write(
                f"{icon} **{title}** — "
                f"Priority: {priority}"
            )

            if due_date:
                st.caption(
                    f"📅 Due: {due_date}"
                )


# =====================================================
# TAB 2 — TODO LIST
# =====================================================

with tab2:

    st.subheader("✅ Todo List")

    # ---------------------------------------------
    # ADD TASK
    # ---------------------------------------------

    st.write("### ➕ Add New Task")

    with st.form("task_form"):

        title = st.text_input(
            "Task",
            placeholder="Example: Study Python"
        )

        description = st.text_area(
            "Description",
            placeholder="Optional description"
        )

        col1, col2 = st.columns(2)

        with col1:

            priority = st.selectbox(
                "Priority",
                [
                    "Low",
                    "Medium",
                    "High"
                ]
            )

        with col2:

            due_date = st.date_input(
                "Due Date",
                value=None
            )

        submitted = st.form_submit_button(
            "➕ Add Task"
        )

        if submitted:

            if title.strip():

                add_task(
                    title,
                    description,
                    priority,
                    str(due_date)
                )

                st.success(
                    f"✅ Task added: {title}"
                )

                st.rerun()

            else:

                st.warning(
                    "Please enter a task."
                )


    st.divider()


    # ---------------------------------------------
    # DISPLAY TASKS
    # ---------------------------------------------

    st.write("### 📋 Your Tasks")

    if not tasks:

        st.info(
            "No tasks available."
        )

    else:

        for task in tasks:

            task_id = task[0]
            title = task[1]
            description = task[2]
            priority = task[3]
            due_date = task[4]
            status = task[5]

            with st.container(border=True):

                col1, col2, col3 = st.columns(
                    [5, 2, 2]
                )

                with col1:

                    if status == "Completed":

                        st.markdown(
                            f"### ✅ ~~{title}~~"
                        )

                    else:

                        st.markdown(
                            f"### 📋 {title}"
                        )

                    if description:

                        st.write(
                            description
                        )

                    if due_date:

                        st.caption(
                            f"📅 Due: {due_date}"
                        )

                with col2:

                    if priority == "High":

                        st.error(
                            "🔥 High"
                        )

                    elif priority == "Low":

                        st.info(
                            "🟢 Low"
                        )

                    else:

                        st.warning(
                            "🟡 Medium"
                        )

                with col3:

                    if status != "Completed":

                        if st.button(
                            "✅ Complete",
                            key=f"complete_{task_id}"
                        ):

                            complete_task(
                                task_id
                            )

                            st.rerun()

                    if st.button(
                        "🗑️ Delete",
                        key=f"delete_{task_id}"
                    ):

                        delete_task(
                            task_id
                        )

                        st.rerun()


# =====================================================
# TAB 3 — NOTES
# =====================================================

with tab3:

    st.subheader("📝 Notes")

    # ---------------------------------------------
    # ADD NOTE
    # ---------------------------------------------

    st.write("### ➕ Create Note")

    with st.form("note_form"):

        note_content = st.text_area(
            "Write your note",
            placeholder="Example: Revise Python before Monday."
        )

        save_note = st.form_submit_button(
            "💾 Save Note"
        )

        if save_note:

            if note_content.strip():

                add_note(
                    "AI Assistant Note",
                    note_content
                )

                st.success(
                    "📝 Note saved successfully!"
                )

                st.rerun()

            else:

                st.warning(
                    "Please write something first."
                )


    st.divider()


    # ---------------------------------------------
    # DISPLAY NOTES
    # ---------------------------------------------

    st.write("### 📚 Saved Notes")

    if not notes:

        st.info(
            "No notes available."
        )

    else:

        for note in notes:

            note_id = note[0]
            content = note[1]

            with st.container(border=True):

                st.write(
                    f"📝 {content}"
                )

                if len(note) > 2:

                    st.caption(
                        f"Created: {note[2]}"
                    )

                if st.button(
                    "🗑️ Delete Note",
                    key=f"delete_note_{note_id}"
                ):

                    delete_note(
                        note_id
                    )

                    st.rerun()


# =====================================================
# TAB 4 — CALENDAR
# =====================================================

with tab4:

    st.subheader("📅 Calendar")

    selected_date = st.date_input(
        "Select a date",
        value=date.today()
    )

    selected_date_string = str(
        selected_date
    )

    st.write(
        f"### 📅 Tasks for {selected_date_string}"
    )

    found_tasks = False

    for task in tasks:

        task_id = task[0]
        title = task[1]
        priority = task[3]
        due_date = task[4]
        status = task[5]

        if due_date == selected_date_string:

            found_tasks = True

            if status == "Completed":

                st.success(
                    f"✅ {title}"
                )

            else:

                if priority == "High":

                    st.error(
                        f"🔥 {title} — High Priority"
                    )

                elif priority == "Low":

                    st.info(
                        f"🟢 {title} — Low Priority"
                    )

                else:

                    st.warning(
                        f"🟡 {title} — Medium Priority"
                    )


    if not found_tasks:

        st.info(
            "No tasks scheduled for this date."
        )


# =====================================================
# TAB 5 — AI CHAT
# =====================================================

with tab5:

    st.subheader("🤖 Chat with AI")

    message = st.text_input(
        "Enter your message",
        placeholder="Ask your assistant anything...",
        key="ai_message"
    )

    if st.button(
        "🤖 Ask AI",
        key="ai_chat_button"
    ):

        if message.strip():

            # Detect intent FIRST
            intent = detect_intent(message)

            st.caption(
                f"Detected intent: {intent}"
            )

            # =====================================
            # CHAT
            # =====================================

            if intent == "CHAT":

                with st.spinner("🤖 Thinking..."):

                    try:

                        response = ask_ai(message)

                        st.write("### 🤖 Assistant")

                        st.write(response)

                    except Exception as e:

                        st.error("AI request failed.")

                        st.caption(str(e))


            # =====================================
            # TASK
            # =====================================

            elif intent == "TASK":

                task_title, priority, due_date = (
                    extract_task_details(message)
                )

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

                    st.write(
                        f"🔥 **Priority:** {priority}"
                    )

                    if due_date:

                        st.write(
                            f"📅 **Due date:** {due_date}"
                        )

                    else:

                        st.write(
                            "📅 **Due date:** Not specified"
                        )


            # =====================================
            # NOTE
            # =====================================

            elif intent == "NOTE":

                note_content = extract_note(message)

                if note_content:

                    add_note(
                        "AI Assistant Note",
                        note_content
                    )

                    st.success(
                        f"📝 Note saved: {note_content}"
                    )

                else:

                    st.warning("Please provide note content.")


            # =====================================
            # LIST TASKS
            # =====================================

            elif intent == "LIST_TASKS":

                st.write("### 📋 Your Tasks")

                current_tasks = get_tasks()

                if current_tasks:

                    for task in current_tasks:

                        task_id = task[0]
                        title = task[1]
                        priority = task[3]
                        due_date = task[4]
                        status = task[5]

                        st.write(
                            f"• **{title}** — "
                            f"{priority} — {status}"
                        )

                        if due_date:

                            st.caption(
                                f"📅 Due: {due_date}"
                            )

                else:

                    st.info("You don't have any tasks yet.")


            # =====================================
            # LIST NOTES
            # =====================================

            elif intent == "LIST_NOTES":

                st.write("### 📝 Your Notes")

                current_notes = get_notes()

                if current_notes:

                    for note in current_notes:

                        st.write(
                            f"• 📝 {note[1]}"
                        )

                else:

                    st.info("You don't have any notes yet.")

        else:

            st.warning(
                "Please enter a message."
            )