from fastapi import APIRouter
from app.database import get_db
from app.schemas import Event, Seat

router = APIRouter()

@router.post("/events")
def create_event(event: Event):
    db = get_db()
    cur = db.cursor()

    cur.execute(
        "INSERT INTO events (title, venue, city, event_date) VALUES (%s, %s, %s, %s)",
        (event.title, event.venue, event.city, event.event_date)
    )

    db.commit()
    cur.close()
    db.close()
    return {"message": "Event created"}

@router.get("/events")
def list_events():
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM events")
    events = cur.fetchall()
    cur.close()
    db.close()
    return events

@router.post("/events/{event_id}/seats")
def add_seat(event_id: int, seat: Seat):
    db = get_db()
    cur = db.cursor()

    cur.execute(
        "INSERT INTO seats (event_id, seat_number, price) VALUES (%s, %s, %s)",
        (event_id, seat.seat_number, seat.price)
    )

    db.commit()
    cur.close()
    db.close()
    return {"message": "Seat added"}
