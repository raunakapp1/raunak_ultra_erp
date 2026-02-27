import sqlite3

DB_NAME = "local_db.sqlite"

def get_conn():
    """Return SQLite connection"""
    conn = sqlite3.connect(DB_NAME)
    return conn

def init_db():
    """Create users table if not exists"""
    conn = get_conn()
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

# Initialize DB automatically
init_db()