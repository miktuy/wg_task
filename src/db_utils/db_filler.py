import random

from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm.session import sessionmaker, Session

from src.db_app.model import Ship, Weapon, Hull, Engine_
from src.params import MAX_ITEMS, PARAMS_GEN


class DbFiller:
    def __init__(self, db_path: str):
        self._engine: Engine = create_engine(f"sqlite:///{db_path}")
        self._session: Session = sessionmaker(bind=self._engine)()

    @property
    def engine(self):
        return self._engine

    @property
    def session(self):
        return self._session

    def _create_weapons(self):
        weapons = list()
        for i in range(1, MAX_ITEMS["weapon"] + 1):
            weapons.append(
                Weapon(
                    weapon=PARAMS_GEN["weapon"](i),
                    reload_speed=PARAMS_GEN["int"](),
                    rotational_speed=PARAMS_GEN["int"](),
                    diameter=PARAMS_GEN["int"](),
                    power_volley=PARAMS_GEN["int"](),
                    count=PARAMS_GEN["int"](),
                )
            )
        self.session.add_all(weapons)
        self.session.commit()

    def _create_engines(self):
        engines = list()
        for i in range(1, MAX_ITEMS["engine"] + 1):
            engines.append(
                Engine_(
                    engine=PARAMS_GEN["engine"](i),
                    power=PARAMS_GEN["int"](),
                    type=PARAMS_GEN["int"](),
                )
            )
        self.session.add_all(engines)
        self.session.commit()

    def _create_hulls(self):
        hulls = list()
        for i in range(1, MAX_ITEMS["hull"] + 1):
            hulls.append(
                Hull(
                    hull=PARAMS_GEN["hull"](i),
                    armor=PARAMS_GEN["int"](),
                    type=PARAMS_GEN["int"](),
                    capacity=PARAMS_GEN["int"](),
                )
            )
        self.session.add_all(hulls)
        self.session.commit()

    def _create_ships(self):
        ships = list()
        for i in range(1, MAX_ITEMS["ship"] + 1):
            weapon = PARAMS_GEN["weapon"](random.randint(1, MAX_ITEMS["weapon"]))
            engine = PARAMS_GEN["engine"](random.randint(1, MAX_ITEMS["engine"]))
            hull = PARAMS_GEN["hull"](random.randint(1, MAX_ITEMS["hull"]))
            ship = PARAMS_GEN["ship"](i)
            ships.append(Ship(ship=ship, weapon=weapon, engine=engine, hull=hull))
        self.session.add_all(ships)
        self.session.commit()

    def fill_db(self):
        self._create_engines()
        self._create_weapons()
        self._create_hulls()
        self._create_ships()
