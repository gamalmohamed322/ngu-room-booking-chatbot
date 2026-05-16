import re
from datetime import datetime


def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None


def is_valid_phone(phone):
    return phone.isdigit() and 10 <= len(phone) <= 15


def is_valid_date(date_text):
    try:
        datetime.strptime(date_text, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def validate_booking_data(booking):
    errors = []

    if not is_valid_email(booking["student_email"]):
        errors.append("Invalid email format.")

    if not is_valid_phone(booking["phone"]):
        errors.append("Invalid phone number. Phone number should contain only digits and be 10 to 15 digits long.")

    if not is_valid_date(booking["booking_date"]):
        errors.append("Invalid date format. Date should be written as YYYY-MM-DD.")

    return errors
