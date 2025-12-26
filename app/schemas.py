from pydantic import BaseModel
from datetime import datetime
from typing import List

class Signup(BaseModel):
    email: str
    password: str
    role: str

class Login(BaseModel):
    email: str
    password: str

class Event(BaseModel):
    title: str
    venue: str
    city: str
    event_date: datetime

class Seat(BaseModel):
    seat_number: str
    price: int

class Booking(BaseModel):
    event_id: int
    seat_ids: List[int]
