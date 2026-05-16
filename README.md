# NGU Room Booking Chatbot

An AI-powered room booking assistant designed for New Giza University students.
## Screenshot

![NGU Room Booking Chatbot Screenshot](assets/chatbot-screenshot.png)

This project allows students to book university rooms such as study rooms, meeting rooms, lab rooms, and club activity rooms through a simple chatbot-style web interface.

## Project Idea

Many university students need to reserve rooms for studying, group work, club meetings, or lab activities. This project makes the booking process easier by allowing students to submit a room booking request through a web chatbot interface.

The backend checks whether the room exists, validates the student information, prevents duplicate bookings, stores the booking in a database, and returns a confirmation message.

## Features

- Chatbot-style web booking interface
- Room type and room name selection
- Student information collection
- Date and time booking
- Input validation
- Room availability checking
- Duplicate booking prevention
- SQLite database storage
- View all saved bookings through an API route
- Email notification service structure
- API documentation
- Chatbot flow documentation

## Tech Stack

- Python
- Flask
- SQLite
- HTML
- CSS
- JavaScript
- GitHub

## Project Structure

```text
ngu-room-booking-chatbot/
│
├── backend/
│   ├── app.py
│   ├── database.py
│   ├── email_service.py
│   ├── rooms.py
│   ├── validators.py
│   ├── requirements.txt
│   └── templates/
│       └── chat.html
│
├── docs/
│   ├── api-testing.md
│   └── chatbot-flow.md
│
├── .env.example
├── .gitignore
└── README.md
## How It Works

1. The student opens the chatbot page.
2. The student chooses a room type and room name.
3. The student enters the booking date, time, name, email, and phone number.
4. The Flask backend receives the request.
5. The backend validates the data.
6. The backend checks if the room is already booked at the same date and time.
7. If the room is available, the booking is saved in the SQLite database.
8. The system returns a booking confirmation response.

## API Routes

### Home Route

GET /

Returns a message confirming that the backend is running.

### Chatbot Page

GET /chat

Opens the chatbot-style room booking web interface.

### Rooms Route

GET /rooms

Returns all available rooms.

### Book Room Route

POST /webhook/book-room

Creates a new room booking.

### View Bookings Route

GET /bookings

Returns all saved bookings.

## Example Booking Request

{
  "room_type": "study_room",
  "room_name": "Library Study Room 1",
  "booking_date": "2026-05-20",
  "booking_time": "2:00 PM",
  "student_name": "Gamal Mohamed",
  "student_email": "student@ngu.edu.eg",
  "phone": "01000000000"
}

## How to Run the Project Locally

### 1. Open the backend folder

cd backend

### 2. Install the required packages

pip install -r requirements.txt

### 3. Run the Flask app

python app.py

### 4. Open the chatbot page

http://127.0.0.1:5000/chat

## Environment Variables

This project includes a .env.example file for email settings.

Example:

EMAIL_USER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
ADMIN_EMAIL=admin@example.com

The real .env file should not be uploaded to GitHub.

## Project Status

The project currently has a working backend, database, room validation, duplicate booking prevention, and chatbot-style web interface.

Future improvements may include:

- Admin dashboard
- Login system
- Booking cancellation
- Email confirmation to students
- Deployment online
- Integration with IBM Watson or another AI chatbot platform

## Credits

This project was inspired by the open-source AI Room Booking Chatbot using IBM Watson by Sarvesh Sharma.

I redesigned and extended the idea for a university room booking use case at New Giza University using Flask, SQLite, HTML, CSS, and JavaScript.

## Author

Gamal Mohamed  
Year 3 Student  
New Giza University
