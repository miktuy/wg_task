import sys

import argparse

from sqlalchemy.orm.session import Session

from src.db_app.db_creator import DbCreator
from src.db_app.model import Ship, Weapon, Hull, Engine_


def get_ship(session: Session, ship_num):
    return session.query(Ship).filter(Ship.ship.endswith(f"-{ship_num}")).one()


def get_weapon(session: Session, ship: Ship):
    weapon = session.query(Weapon).filter(
        Weapon.weapon == ship.weapon).one()
    return weapon


def get_hull(session: Session, ship: Ship):
    hull = session.query(Hull).filter(
        Hull.hull == ship.hull).one()
    return hull


def get_engine(session: Session, ship: Ship):
    hull = session.query(Engine_).filter(
        Engine_.engine == ship.engine).one()
    return hull


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Create empty database")
    parser.add_argument("-p", "--path", type=str, default='test.db', help="path for db")
    params = parser.parse_args(sys.argv[1:])
    DbCreator(params.path).create_db()

