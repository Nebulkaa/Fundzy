from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, Integer, String, Float, Text, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

DATABASE_URL = "sqlite:///donations.db"

Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

class Donation(Base):
    __tablename__ = "donations"

    id = Column(Integer, primary_key=True)
    streamer = Column(String(100), nullable=False)
    nick = Column(String(100), nullable=False)
    amount = Column(Float, nullable=False)
    currency = Column(String(10), nullable=False)
    network = Column(String(50), nullable=False)
    message = Column(Text)
    status = Column(String(20), default="pending")
    fee = Column(Float, default=0.0)
    date = Column(DateTime, default=datetime.utcnow)


def init_db():
    Base.metadata.create_all(bind=engine)


def save_donation(data):
    session = SessionLocal()
    donation = Donation(**data)
    session.add(donation)
    session.commit()
    session.refresh(donation)
    session.close()
    return donation

app = Flask(__name__)

@app.before_first_request
def setup():
    init_db()

@app.post("/donate")
def donate():
    data = request.json or {}
    donation = save_donation(data)
    return jsonify({"id": donation.id})

@app.get("/donations")
def get_donations():
    session = SessionLocal()
    donations = session.query(Donation).all()
    result = [
        {
            "id": d.id,
            "streamer": d.streamer,
            "nick": d.nick,
            "amount": d.amount,
            "currency": d.currency,
            "network": d.network,
            "message": d.message,
            "status": d.status,
            "fee": d.fee,
            "date": d.date.isoformat(),
        }
        for d in donations
    ]
    session.close()
    return jsonify(result)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
