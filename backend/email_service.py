import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()


def send_booking_confirmation(booking, booking_id):
    email_user = os.getenv("EMAIL_USER")
    email_password = os.getenv("EMAIL_PASSWORD")
    admin_email = os.getenv("ADMIN_EMAIL")

    if not email_user or not email_password or not admin_email:
        return {
            "sent": False,
            "message": "Email settings are missing. Email notification was skipped."
        }

    subject = f"New Room Booking #{booking_id}"

    body = f"""
A new room booking has been confirmed.

Booking ID: {booking_id}

Student Name: {booking["student_name"]}
Student Email: {booking["student_email"]}
Phone: {booking["phone"]}

Room Type: {booking["room_type"]}
Room Name: {booking["room_name"]}
Date: {booking["booking_date"]}
Time: {booking["booking_time"]}

Status: Confirmed
"""

    message = EmailMessage()
    message["Subject"] = subject
    message["From"] = email_user
    message["To"] = admin_email
    message.set_content(body)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(email_user, email_password)
            smtp.send_message(message)

        return {
            "sent": True,
            "message": "Email notification sent successfully."
        }

    except Exception as error:
        return {
            "sent": False,
            "message": f"Email notification failed: {str(error)}"
        }
