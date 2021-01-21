import argparse
import logging
import sys

from pathlib import Path
from sqlalchemy.exc import IntegrityError

from src.db_app.model import Base
from src.db_utils.db_filler import DbFiller


def main():
    parser = argparse.ArgumentParser(description="Fill empty database.")
    parser.add_argument("-p", "--path", type=str, default="test.db", help="path for db")
    parser.add_argument(
        "-e", "--existed", type=bool, default=False, help="should db be existed"
    )
    params = parser.parse_args(sys.argv[1:])

    filler = DbFiller(f"/{params.path}")
    if params.existed and not Path(params.path).exists():
        logging.error(f"Database `{params.path}` does not exist")
        exit(1)
    elif not Path(params.path).exists():
        Base.metadata.create_all(filler.engine)
    try:
        filler.fill_db()
    except IntegrityError:
        logging.warning(f"Database `{params.path}` exists and filled")


if __name__ == "__main__":
    main()
