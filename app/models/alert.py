from geoalchemy2 import Geography
from sqlalchemy import Column, String, Integer, BOOLEAN
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app import db


class Alert(db.Model):
    __tablename__ = "alert"

    id = Column(Integer, primary_key=True)
    description = Column(String)
    lost_point = Column(Geography(geometry_type='POINT', srid=4326))
    pet_id = db.Column(db.Integer, db.ForeignKey('pet.id'))
    active = Column(BOOLEAN, default=False)
    date_registered = db.Column(db.DateTime(timezone=True), server_default=func.now())
    date_finish = db.Column(db.DateTime(timezone=True), server_default=func.now())
    pet = relationship("Pet")


