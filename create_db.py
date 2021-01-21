import sys

import argparse

from src.db_app.db_creator import DbCreator


def main():
    parser = argparse.ArgumentParser(description="Create empty database")
    parser.add_argument("-p", "--path", type=str, default="test.db", help="path for db")
    params = parser.parse_args(sys.argv[1:])
    DbCreator(params.path).create_db()


if __name__ == "__main__":
    main()
