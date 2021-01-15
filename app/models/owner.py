from sqlalchemy import Column, String, Integer

from app import db


class Owner(db.Model):
    __tablename__ = "owner"

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    last_name = Column(String(30))
    username = Column(String(100))
    email = Column(String(200), unique=True)
    phone = Column(String(14))
    f_user = Column(String(150))
    g_user = Column(String(150))
    photo = Column(String(200))
    age = Column(Integer)
    firebase_token = Column(String)
