# Chatbot Flow

This document explains the conversation flow for the NGU Room Booking Chatbot.

## Goal

The chatbot helps New Giza University students book university rooms such as study rooms, meeting rooms, lab rooms, or club activity rooms.

## Conversation Flow

### 1. Greeting

Bot:
Hello! Welcome to the NGU Room Booking Assistant. How can I help you today?

Student:
I want to book a room.

### 2. Ask for Room Type

Bot:
What type of room would you like to book?

Options:
- Study Room
- Meeting Room
- Lab Room
- Club Activity Room

### 3. Ask for Room Name or Preference

Bot:
Do you have a preferred room?

Example:
- Library Study Room 1
- Library Study Room 2
- CS Lab
- Meeting Room A

### 4. Ask for Date

Bot:
What date would you like to book the room?

Example:
2026-05-20

### 5. Ask for Time

Bot:
What time would you like to book the room?

Example:
2:00 PM

### 6. Ask for Student Name

Bot:
Please enter your full name.

### 7. Ask for Student Email

Bot:
Please enter your university email address.

### 8. Ask for Phone Number

Bot:
Please enter your phone number.

### 9. Confirm Booking Details

Bot:
Please confirm your booking details:

Room Type:
Room:
Date:
Time:
Name:
Email:
Phone:

Would you like to confirm this booking?

### 10. Booking Result

If the room is available:

Bot:
Your booking has been confirmed successfully.

If the room is already booked:

Bot:
Sorry, this room is already booked at that time. Please choose another time or room.

## Information Collected

The chatbot collects:

- Room type
- Room name
- Booking date
- Booking time
- Student name
- Student email
- Student phone number

## Future Improvements

- Add booking duration
- Add admin approval
- Add email confirmation
- Add database storage
- Add booking cancellation
- Add room availability checking
