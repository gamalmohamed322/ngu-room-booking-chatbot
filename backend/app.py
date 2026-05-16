from flask import Flask, request, jsonify

app = Flask(name)


@app.route("/")
def home():
    return jsonify({
        "status": "success",
        "message": "NGU Room Booking Chatbot backend is running."
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

    return jsonify({
        "status": "success",
        "message": "Your booking request has been received successfully.",
        "booking": booking
    })


if name == "main":
    app.run(debug=True)
