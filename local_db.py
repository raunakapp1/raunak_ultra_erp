# local_db.py
import sqlite3

DB_FILE = "raunak_erp.db"

def get_conn():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    conn = get_conn()
    cursor = conn.cursor()
    
    # Staff Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS staff (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT,
            role TEXT NOT NULL
        )
    """)
    
    # Guest Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS guests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT,
            pax INTEGER,
            category TEXT,
            entry_date TEXT,
            added_by_staff_id INTEGER,
            FOREIGN KEY(added_by_staff_id) REFERENCES staff(id)
        )
    """)
    
    # Attendance Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            staff_id INTEGER,
            date TEXT,
            status TEXT,
            FOREIGN KEY(staff_id) REFERENCES staff(id)
        )
    """)
    
    conn.commit()
    conn.close()
