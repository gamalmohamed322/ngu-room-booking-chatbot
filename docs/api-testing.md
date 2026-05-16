# API Testing Guide

This file explains how to test the NGU Room Booking Chatbot backend.

## 1. Home Route

URL:

GET /

Expected response:

{
  "status": "success",
  "message": "NGU Room Booking Chatbot backend is running."
}

## 2. Rooms Route

URL:

GET /rooms

This route returns all available rooms.

Expected response example:

{
  "status": "success",
  "rooms": [
    {
      "room_type": "study_room",
      "room_name": "Library Study Room 1"
    }
  ]
}

## 3. Book Room Route

URL:

POST /webhook/book-room

Example request body:

{
  "room_type": "study_room",
  "room_name": "Library Study Room 1",
  "booking_date": "2026-05-20",
  "booking_time": "2:00 PM",
  "student_name": "Gamal Mohamed",
  "student_email": "student@ngu.edu.eg",
  "phone": "01000000000"
}

Expected success response:

{
  "status": "success",
  "message": "Your room booking has been confirmed successfully.",
  "booking_id": 1
}

## 4. Missing Information Error

If some booking details are missing, the backend returns an error.

Example:

{
  "status": "error",
  "message": "Some booking details are missing.",
  "missing_fields": ["phone"]
}

## 5. Invalid Room Error

If the student enters a room that does not exist, the backend returns an error.

Example:

{
  "status": "error",
  "message": "This room does not exist. Please choose one of the available NGU rooms."
}

## 6. Room Already Booked Error

If the room is already booked at the same date and time, the backend returns an error.

Example:

{
  "status": "error",
  "message": "Sorry, this room is already booked at this date and time. Please choose another room or time."
}
