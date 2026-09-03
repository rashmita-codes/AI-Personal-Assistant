from database.database import get_connection


def add_note(title, content):
    """Add a new note to the database."""

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO notes (title, content)
        VALUES (?, ?)
    """, (title, content))

    connection.commit()
    connection.close()


def get_notes():
    """Get all saved notes."""

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, title, content, created_at
        FROM notes
        ORDER BY id DESC
    """)

    notes = cursor.fetchall()

    connection.close()

    return notes


def delete_note(note_id):
    """Delete a note from the database."""

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM notes
        WHERE id = ?
    """, (note_id,))

    connection.commit()
    connection.close()