from sqlalchemy.orm.session import Session

from src.db_app.model import Ship, Weapon, Hull, Engine_


def get_ship(session: Session, ship_num):
    return session.query(Ship).filter(Ship.ship.endswith(f"-{ship_num}")).one()


def get_weapon(session: Session, ship: Ship):
    weapon = session.query(Weapon).filter(Weapon.weapon == ship.weapon).one()
    return weapon


def get_hull(session: Session, ship: Ship):
    hull = session.query(Hull).filter(Hull.hull == ship.hull).one()
    return hull


def get_engine(session: Session, ship: Ship):
    hull = session.query(Engine_).filter(Engine_.engine == ship.engine).one()
    return hull
