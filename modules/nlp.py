import re


def detect_intent(message):
    """
    Detect the user's intention from their message.
    """

    message = message.lower().strip()

    # Remove extra spaces
    message = re.sub(r"\s+", " ", message)

    # -----------------------------
    # TASK INTENT
    # -----------------------------

    task_keywords = [
        "add a task",
        "create a task",
        "make a task",
        "new task",
        "add task",
        "create task",
        "make task",
        "remind me",
        "reminder",
        "todo",
        "to-do",
        "to do"
    ]

    # -----------------------------
    # NOTE INTENT
    # -----------------------------

    note_keywords = [
        "add a note",
        "create a note",
        "make a note",
        "save a note",
        "new note",
        "add note",
        "create note",
        "save note",
        "remember this",
        "save this"
    ]

    # -----------------------------
    # LIST TASKS
    # -----------------------------

    list_task_keywords = [
        "show tasks",
        "show my tasks",
        "list tasks",
        "list my tasks",
        "my tasks",
        "pending tasks",
        "view tasks",
        "view my tasks"
    ]

    # -----------------------------
    # LIST NOTES
    # -----------------------------

    list_note_keywords = [
        "show notes",
        "show my notes",
        "list notes",
        "list my notes",
        "my notes",
        "view notes",
        "view my notes"
    ]

    # Check TASK first
    if any(keyword in message for keyword in task_keywords):
        return "TASK"

    # Check NOTE
    if any(keyword in message for keyword in note_keywords):
        return "NOTE"

    # Check LIST TASKS
    if any(keyword in message for keyword in list_task_keywords):
        return "LIST_TASKS"

    # Check LIST NOTES
    if any(keyword in message for keyword in list_note_keywords):
        return "LIST_NOTES"

    # Otherwise, normal AI chat
    return "CHAT"