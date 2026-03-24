import sqlite3

DB_NAME = "feedback.db"


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            message TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def add_feedback(name, message):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO feedback (name, message) VALUES (?, ?)",
        (name, message)
    )

    conn.commit()
    conn.close()


def get_all_feedback():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM feedback ORDER BY id DESC")
    rows = cursor.fetchall()

    conn.close()
    return rows