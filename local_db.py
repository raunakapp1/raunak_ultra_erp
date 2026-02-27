# local_db.py
import sqlite3
from sqlite3 import Error
import os

# Database file name
DB_NAME = "raunak_erp.db"

# Ensure database file is created in the current folder
DB_PATH = os.path.join(os.path.dirname(__file__), DB_NAME)

def get_conn():
    """
    Create a connection to the SQLite database.
    Returns:
        conn (sqlite3.Connection): SQLite connection object
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        return conn
    except Error as e:
        print(f"Error connecting to database: {e}")
        return None

def create_tables():
    """
    Create all required tables for the ERP system.
    """
    conn = get_conn()
    if conn is None:
        print("Failed to connect to database. Tables not created.")
        return
    
    cursor = conn.cursor()

    # Guests Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS guests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        room_number TEXT NOT NULL,
        check_in DATE,
        check_out DATE
    );
    """)

    # Staff Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS staff (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        role TEXT,
        attendance_count INTEGER DEFAULT 0
    );
    """)

    # Events Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        date DATE,
        location TEXT,
        description TEXT
    );
    """)

    # Attendance Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS attendance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        staff_id INTEGER,
        date DATE,
        status TEXT,
        FOREIGN KEY (staff_id) REFERENCES staff(id)
    );
    """)

    # Reports Table (PDF/Excel placeholder)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reports (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        report_name TEXT,
        created_on DATE
    );
    """)

    conn.commit()
    conn.close()
    print("✅ Database & tables created successfully!")
