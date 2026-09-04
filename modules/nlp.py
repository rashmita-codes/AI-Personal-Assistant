import re
from datetime import datetime, timedelta


def detect_intent(message):
    """Detect the user's intention."""

    message = message.lower().strip()
    message = re.sub(r"\s+", " ", message)

    task_keywords = [
        "add a task",
        "add task",
        "create a task",
        "create task",
        "make a task",
        "make task",
        "new task",
        "remind me",
        "reminder",
        "todo",
        "to-do",
        "to do"
    ]

    note_keywords = [
        "add a note",
        "add note",
        "create a note",
        "create note",
        "make a note",
        "save a note",
        "save note",
        "new note",
        "remember this",
        "save this"
    ]

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

    list_note_keywords = [
        "show notes",
        "show my notes",
        "list notes",
        "list my notes",
        "my notes",
        "view notes",
        "view my notes"
    ]

    # Detect task commands
    task_pattern = r"\b(add|create|make)\s+(a\s+)?(high\s+priority\s+|medium\s+priority\s+|low\s+priority\s+)?task\b"

    if re.search(task_pattern, message):
        return "TASK"

# Existing task keywords
    if any(keyword in message for keyword in task_keywords):
        return "TASK"

    if any(keyword in message for keyword in note_keywords):
        return "NOTE"

    if any(keyword in message for keyword in list_task_keywords):
        return "LIST_TASKS"

    if any(keyword in message for keyword in list_note_keywords):
        return "LIST_NOTES"

    return "CHAT"


def extract_task(message):
    """Extract the task title."""

    original_message = message.strip()
    message_lower = original_message.lower()

    prefixes = [
        "add a task to ",
        "add task to ",
        "create a task to ",
        "create task to ",
        "make a task to ",
        "make task to ",
        "add a task ",
        "add task ",
        "create a task ",
        "create task ",
        "make a task ",
        "make task "
    ]

    for prefix in prefixes:

        if message_lower.startswith(prefix):
            return original_message[len(prefix):].strip()

    return original_message


def extract_task_details(message):
    """
    Extract task title, priority and due date.
    """

    original_message = message.strip()
    message_lower = original_message.lower()

    # -------------------------
    # DEFAULT VALUES
    # -------------------------

    priority = "Medium"
    due_date = None

    # -------------------------
    # PRIORITY
    # -------------------------

    if "high priority" in message_lower:
        priority = "High"

    elif "low priority" in message_lower:
        priority = "Low"

    elif "medium priority" in message_lower:
        priority = "Medium"

    # -------------------------
    # DUE DATE
    # -------------------------

    today = datetime.now().date()

    if "tomorrow" in message_lower:
        due_date = today + timedelta(days=1)

    elif "today" in message_lower:
        due_date = today

    # -------------------------
    # TASK TITLE
    # -------------------------

    task_title = original_message

    prefixes = [
        "add a task to ",
        "add task to ",
        "create a task to ",
        "create task to ",
        "make a task to ",
        "make task to ",
        "add a task ",
        "add task ",
        "create a task ",
        "create task ",
        "make a task ",
        "make task "
    ]

    for prefix in prefixes:

        if message_lower.startswith(prefix):
            task_title = original_message[len(prefix):].strip()
            break

    # -------------------------
    # REMOVE PRIORITY
    # -------------------------

    task_title = re.sub(
        r"\b(high|medium|low)\s+priority\b",
        "",
        task_title,
        flags=re.IGNORECASE
    )

    # -------------------------
    # REMOVE DATE
    # -------------------------

    task_title = re.sub(
        r"\btomorrow\b",
        "",
        task_title,
        flags=re.IGNORECASE
    )

    task_title = re.sub(
        r"\btoday\b",
        "",
        task_title,
        flags=re.IGNORECASE
    )

    # -------------------------
    # CLEAN TITLE
    # -------------------------

    task_title = re.sub(
        r"\s+",
        " ",
        task_title
    ).strip()

    task_title = re.sub(
        r"^to\s+",
        "",
        task_title,
        flags=re.IGNORECASE
    )

    # Convert date to string
    if due_date:
        due_date = due_date.strftime("%Y-%m-%d")

    return task_title, priority, due_date