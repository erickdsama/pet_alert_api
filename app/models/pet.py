from sqlalchemy import Column, String, Integer, DECIMAL, BOOLEAN
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


from app import db


class Pet(db.Model):
    __tablename__ = "pet"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    breed = Column(String(100))
    color = Column(String(100))
    size = Column(String(20))
    age = Column(DECIMAL)
    weight = Column(DECIMAL)
    sex = Column(Integer)
    diseases = Column(String)
    medicates = Column(String)
    photo = Column(String(200))
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'))
    active = Column(BOOLEAN, default=False)
    date_registered = db.Column(db.DateTime(timezone=True), server_default=func.now())

    pet = relationship("Owner")




