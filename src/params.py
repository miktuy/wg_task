"""
Described params for database filling
"""
import random


MAX_ITEMS = {
    "ship": 200,
    "weapon": 20,
    "hull": 5,
    "engine": 6,
}
MIN_INTEGER_PARAM_VALUE = 1
MAX_INTEGER_PARAM_VALUE = 20
VALUE_RANGE = (MIN_INTEGER_PARAM_VALUE, MAX_INTEGER_PARAM_VALUE)
PARAMS_GEN = {
    "int": lambda: random.randint(*VALUE_RANGE),
    "ship": lambda n: f"Ship-{n}",
    "weapon": lambda n: f"Weapon-{n}",
    "hull": lambda n: f"Hull-{n}",
    "engine": lambda n: f"Engine-{n}",
}