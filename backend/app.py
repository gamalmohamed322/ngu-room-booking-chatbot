from flask import Flask, request, jsonify
from database import init_db, is_room_available, create_booking
from rooms import get_all_rooms, is_valid_room
from validators import validate_booking_data

app = Flask(name)

# Create the database table when the app starts
init_db()


@app.route("/")
def home():
    return jsonify({
        "status": "success",
        "message": "NGU Room Booking Chatbot backend is running."
    })


@app.route("/rooms", methods=["GET"])
def rooms():
    return jsonify({
        "status": "success",
        "rooms": get_all_rooms()
    })


@app.route("/webhook/book-room", methods=["POST"])
def book_room():
    data = request.get_json(silent=True) or {}

    booking = {
        "room_type": data.get("room_type"),
        "room_name": data.get("room_name"),
        "booking_date": data.get("booking_date"),
        "booking_time": data.get("booking_time"),
        "student_name": data.get("student_name"),
        "student_email": data.get("student_email"),
        "phone": data.get("phone")
    }

    missing_fields = []

    for field, value in booking.items():
        if not value:
            missing_fields.append(field)

    if missing_fields:
        return jsonify({
            "status": "error",
            "message": "Some booking details are missing.",
            "missing_fields": missing_fields
        }), 400

    validation_errors = validate_booking_data(booking)

    if validation_errors:
        return jsonify({
            "status": "error",
            "message": "Some booking details are invalid.",
            "errors": validation_errors
        }), 400

    if not is_valid_room(booking["room_name"]):
        return jsonify({
            "status": "error",
            "message": "This room does not exist. Please choose one of the available NGU rooms."
        }), 400

    available = is_room_available(
        booking["room_name"],
        booking["booking_date"],
        booking["booking_time"]
    )

    if not available:
        return jsonify({
            "status": "error",
            "message": "Sorry, this room is already booked at this date and time. Please choose another room or time."
        }), 409

    booking_id = create_booking(booking)

    return jsonify({
        "status": "success",
        "message": "Your room booking has been confirmed successfully.",
        "booking_id": booking_id,
        "booking": booking
    }), 201


if name == "main":
    app.run(debug=True)
