from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class Ship(Base):
    __tablename__ = "Ships"
    ship = Column(String, primary_key=True)
    weapon = Column(String)
    hull = Column(String)
    engine = Column(String)


class Weapon(Base):
    __tablename__ = "weapons"
    weapon = Column(String, primary_key=True)
    reload_speed = Column(Integer)
    rotational_speed = Column(Integer)
    diameter = Column(Integer)
    power_volley = Column(Integer)
    count = Column(Integer)


class Hull(Base):
    __tablename__ = "hulls"
    hull = Column(String, primary_key=True)
    armor = Column(Integer)
    type = Column(Integer)
    capacity = Column(Integer)


class Engine_(Base):
    __tablename__ = "engines"
    engine = Column(String, primary_key=True)
    power = Column(Integer)
    type = Column(Integer)
