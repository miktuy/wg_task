from pathlib import Path

import pytest

from src.db_app.model import Base
from src.db_utils.db_filler import DbFiller
from src.db_utils.db_randomizer import DBRandomizer


@pytest.fixture(scope="session")
def setup_databases():
    filler = DbFiller("fleet.db")
    if not Path("fleet.db").exists():
        Base.metadata.create_all(filler.engine)
        filler.fill_db()
    filled_db_session = filler.session

    randomized_db = DBRandomizer(filler.session)
    randomized_db.copy_db()
    yield filled_db_session, randomized_db.session
    filled_db_session.close()
    randomized_db.session.close()
