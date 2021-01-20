"""
Class provides changing values in existed database with data by random values
"""
import random

from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm.session import sessionmaker, Session

from src.db_app.model import Base, Ship, Weapon, Hull, Engine_
from src.params import MAX_ITEMS, PARAMS_GEN


class DBRandomizer:
    def __init__(self, existed_db_session: Session):
        self.parent_db_session = existed_db_session

        engine: Engine = create_engine("sqlite://")
        Base.metadata.create_all(engine)
        self._session: Session = sessionmaker(bind=engine)()

    @property
    def session(self):
        return self._session

    def copy_ships_table_with_random_changes(self):
        for ship in self.parent_db_session.query(Ship).all():
            new_ship = Ship(
                ship=ship.ship, weapon=ship.weapon, hull=ship.hull, engine=ship.engine
            )
            attr = random.choice(["weapon", "hull", "engine"])
            new_value = PARAMS_GEN[attr](random.randint(1, MAX_ITEMS[attr]))
            setattr(new_ship, attr, new_value)
            self.session.add(new_ship)
        self.session.commit()

    def copy_weapons_table_with_random_changes(self):
        for weapon in self.parent_db_session.query(Weapon).all():
            new_weapon = Weapon(
                weapon=weapon.weapon,
                reload_speed=weapon.reload_speed,
                rotational_speed=weapon.rotational_speed,
                diameter=weapon.diameter,
                power_volley=weapon.power_volley,
                count=weapon.count,
            )
            attr = random.choice(
                [
                    "reload_speed",
                    "rotational_speed",
                    "diameter",
                    "power_volley",
                    "count",
                ]
            )
            new_value = PARAMS_GEN["int"]()
            setattr(new_weapon, attr, new_value)
            self.session.add(new_weapon)
        self.session.commit()

    def copy_engines_table_with_random_changes(self):
        for engine in self.parent_db_session.query(Engine_).all():
            new_engine = Engine_(
                engine=engine.engine,
                power=engine.power,
                type=engine.type,
            )
            attr = random.choice(
                [
                    "power",
                    "type",
                ]
            )
            new_value = PARAMS_GEN["int"]()
            setattr(new_engine, attr, new_value)
            self.session.add(new_engine)
        self.session.commit()

    def copy_hulls_table_with_random_changes(self):
        for hull in self.parent_db_session.query(Hull).all():
            new_hull = Hull(
                hull=hull.hull,
                armor=hull.armor,
                type=hull.type,
                capacity=hull.capacity,
            )
            attr = random.choice(
                [
                    "armor",
                    "type",
                    "capacity",
                ]
            )
            new_value = PARAMS_GEN["int"]()
            setattr(new_hull, attr, new_value)
            self.session.add(new_hull)
        self.session.commit()

    def copy_db(self):
        self.copy_weapons_table_with_random_changes()
        self.copy_engines_table_with_random_changes()
        self.copy_hulls_table_with_random_changes()
        self.copy_ships_table_with_random_changes()
