import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(file))
DB_PATH = os.path.join(BASE_DIR, "bookings.db")


def get_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            room_type TEXT NOT NULL,
            room_name TEXT NOT NULL,
            booking_date TEXT NOT NULL,
            booking_time TEXT NOT NULL,
            student_name TEXT NOT NULL,
            student_email TEXT NOT NULL,
            phone TEXT NOT NULL,
            status TEXT DEFAULT 'confirmed',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()


def is_room_available(room_name, booking_date, booking_time):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT COUNT(*) AS count
        FROM bookings
        WHERE LOWER(room_name) = LOWER(?)
        AND booking_date = ?
        AND booking_time = ?
        AND status = 'confirmed'
    """, (room_name, booking_date, booking_time))

    result = cursor.fetchone()
    connection.close()

    return result["count"] == 0


def create_booking(booking):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO bookings (
            room_type,
            room_name,
            booking_date,
            booking_time,
            student_name,
            student_email,
            phone
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        booking["room_type"],
        booking["room_name"],
        booking["booking_date"],
        booking["booking_time"],
        booking["student_name"],
        booking["student_email"],
        booking["phone"]
    ))

    booking_id = cursor.lastrowid

    connection.commit()
    connection.close()

    return booking_id

def get_all_bookings():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM bookings
        ORDER BY created_at DESC
    """)

    rows = cursor.fetchall()
    connection.close()

    bookings = []

    for row in rows:
        bookings.append({
            "id": row["id"],
            "room_type": row["room_type"],
            "room_name": row["room_name"],
            "booking_date": row["booking_date"],
            "booking_time": row["booking_time"],
            "student_name": row["student_name"],
            "student_email": row["student_email"],
            "phone": row["phone"],
            "status": row["status"],
            "created_at": row["created_at"]
        })

    return bookings
