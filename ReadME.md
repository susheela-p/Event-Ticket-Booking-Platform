#  Event Ticket Booking Platform – Backend (FastAPI + NeonDB)

# Project Overview

This project is a backend-focused Event Ticket Booking Platform, similar to a lite version of BookMyShow.
The main objective of this project is to design and implement correct backend business logic, secure authentication, and reliable seat booking while maintaining data consistency.

The system allows users to browse events and book seats, while admins can manage events and view bookings.
Special attention is given to preventing double booking and handling database transactions safely.

# Purpose of the Project

* This project was developed to demonstrate:

* Strong understanding of backend development

* Secure user authentication using JWT

* Proper relational database design

* Atomic seat booking logic using database transactions

* Clean API design and role-based access control

* The focus is on correctness and reliability, not UI or animations.

# Technology Stack

Backend Framework: FastAPI (Python)

Database: NeonDB (PostgreSQL)

Database Driver: psycopg2

Authentication: JWT (JSON Web Tokens)

Password Security: bcrypt hashing using passlib

API Documentation: Swagger UI (FastAPI built-in)

👥 User Roles and Permissions
👤 User (Customer)

Can sign up and log in

Can view available events

Can select seats for an event

Can book tickets

Can view their booking history

# Admin (Event Organizer)

Can create and manage events

Can define seat layouts for events

Can view bookings for events created by them

All permissions are strictly enforced at the API level using role checks.

# Authentication & Security

Users authenticate using JWT-based authentication

Passwords are never stored in plain text

Passwords are securely hashed using bcrypt

Protected routes require a valid JWT token

Role-based authorization ensures restricted access

# Database Design

The database follows a relational design with proper foreign key relationships.

# Main tables:

Users – stores user credentials and roles

Events – stores event details created by admins

Seats – stores seat information per event

Bookings – stores ticket booking records

Booking Seats – maps seats to a booking

Indexes and unique constraints are used to ensure data integrity.

#  Seat Booking Logic

Seat booking is handled using database transactions to ensure atomicity.

Booking flow:

User selects seats

System checks seat availability

Seats are locked within a transaction

Booking is created

Seats are marked as booked

Transaction is committed

If any seat is already booked, the entire transaction fails.
This prevents double booking and ensures consistency.

# Database Testing

The system was tested directly using SQL queries on NeonDB to verify:

Table creation

Correct data insertion

Booking-seat relationships

Seat availability updates

Double booking prevention

This confirms the backend behaves correctly under real-world conditions.

# API Design

The APIs are designed following REST principles:

Proper HTTP methods

Clear route naming

Input validation using Pydantic

Meaningful HTTP status codes

Error handling for failure cases

FastAPI’s Swagger UI is used for testing and documentation.

# Project Structure

The project follows a modular structure to separate concerns:

main.py – application setup and middleware

database.py – database connection logic

auth.py – authentication utilities

models.py – request/response schemas

routes/ – API route handlers

This structure improves readability and maintainability.

#  Assumptions & Limitations

Payment integration is intentionally excluded

Real-time seat locking is not implemented

UI is minimal; backend logic is the priority

Designed for learning and demonstration purposes

# Key Takeaways

Secure authentication implemented correctly

Clean relational database design

Atomic booking logic using transactions

Role-based authorization enforced

Backend-first, production-style approach

# Conclusion

This project demonstrates the implementation of a reliable backend ticket booking system with emphasis on:

Data integrity

Secure authentication

Business logic correctness

Real-world backend practices

It reflects a strong understanding of backend development concepts using FastAPI and NeonDB.

If you want, I can:

Shorten this for executive summary

Add ER diagram explanation

Convert it into PDF format

Review it as a team leader would


# Testing & Verification

The application was thoroughly tested using both Swagger UI and direct SQL queries on NeonDB to ensure correctness and data consistency.



# API Testing using Swagger UI

FastAPI provides an interactive Swagger UI, which was used to test all APIs:

User signup and login

JWT authentication and authorization

Event creation and listing

Seat creation and availability checks

Ticket booking and booking history

Swagger UI helped validate:

Request and response formats

Input validation

Error handling

Authorization behavior

# Swagger UI URL:  http://127.0.0.1:8000/docs



# Seat Booking Consistency Check

To verify double booking prevention:

The same seat was booked twice intentionally

First booking succeeded

Second booking failed

# SELECT seat_number, is_booked FROM seats WHERE event_id = 1;


# Testing Summary

* All APIs tested using Swagger UI

* Database tested using direct SQL queries

* Seat booking logic verified for correctness

* Data integrity maintained across all operations