from pathlib import Path
import logging

from sqlalchemy import create_engine

from .model import Base


LOG_FORMAT = logging.Formatter(fmt="{asctime}:{levelname}:{name}: {message}", style="{")


class DbCreator:
    def __init__(self, path: str):
        self.db_path = path

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(LOG_FORMAT)
        self.logger = logging.getLogger("db_creator")
        self.logger.addHandler(console_handler)
        self.logger.setLevel(logging.DEBUG)

    def create_db(self):
        engine = create_engine(f"sqlite:///{self.db_path}", echo=True)
        if not Path(self.db_path).exists():
            Base.metadata.create_all(engine)
        else:
            self.logger.warning(f"Db {self.db_path} exists")
