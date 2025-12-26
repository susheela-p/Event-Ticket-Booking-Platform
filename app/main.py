from fastapi import FastAPI
from app.routes import auth, events, bookings
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Event Ticket Booking System")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all (OK for assignment)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




app.include_router(auth.router)
app.include_router(events.router)
app.include_router(bookings.router)



