from fastapi import APIRouter, HTTPException
from app.database import get_db
from app.schemas import Booking

router = APIRouter()

@router.post("/bookings")
def book_ticket(data: Booking):
    db = get_db()
    cur = db.cursor()

    cur.execute(
        "SELECT * FROM seats WHERE id = ANY(%s) AND is_booked=FALSE FOR UPDATE",
        (data.seat_ids,)
    )

    seats = cur.fetchall()
    if len(seats) != len(data.seat_ids):
        raise HTTPException(400, "Seat already booked")

    total = sum(seat["price"] for seat in seats)

    cur.execute(
        "INSERT INTO bookings (user_id, event_id, total_amount) VALUES (%s, %s, %s) RETURNING id",
        (1, data.event_id, total)
    )
    booking_id = cur.fetchone()["id"]

    for seat in seats:
        cur.execute("UPDATE seats SET is_booked=TRUE WHERE id=%s", (seat["id"],))
        cur.execute(
            "INSERT INTO booking_seats (booking_id, seat_id) VALUES (%s, %s)",
            (booking_id, seat["id"])
        )

    db.commit()
    cur.close()
    db.close()

    return {"message": "Booking successful", "total": total}
