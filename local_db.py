# local_db.py
import sqlite3

DB_NAME = "raunak_erp.db"

def get_conn():
    return sqlite3.connect(DB_NAME)

def create_tables():
    conn = get_conn()
    cursor = conn.cursor()
    
    # Guests table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS guests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        room_number TEXT,
        checkin_date TEXT,
        checkout_date TEXT
    )
    """)
    
    # Staff table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS staff (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        role TEXT,
        attendance_status TEXT
    )
    """)
    
    # Events table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        date TEXT,
        description TEXT
    )
    """)
    
    # Reports table (placeholder)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reports (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        type TEXT,
        generated_date TEXT
    )
    """)
    
    conn.commit()
    conn.close()
