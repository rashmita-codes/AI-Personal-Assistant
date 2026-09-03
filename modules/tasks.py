from database.database import get_connection


def add_task(title, description="", priority="Medium", due_date=None):
    """Add a new task to the database."""

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO tasks
        (title, description, priority, due_date)
        VALUES (?, ?, ?, ?)
    """, (title, description, priority, due_date))

    connection.commit()
    connection.close()


def get_tasks():
    """Get all tasks from the database."""

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, title, description, priority,
               due_date, status, created_at
        FROM tasks
        ORDER BY id DESC
    """)

    tasks = cursor.fetchall()

    connection.close()

    return tasks


def complete_task(task_id):
    """Mark a task as completed."""

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE tasks
        SET status = 'Completed'
        WHERE id = ?
    """, (task_id,))

    connection.commit()
    connection.close()


def delete_task(task_id):
    """Delete a task."""

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM tasks
        WHERE id = ?
    """, (task_id,))

    connection.commit()
    connection.close()