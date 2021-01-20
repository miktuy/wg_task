import pytest

from src.app import get_ship, get_weapon, get_engine, get_hull
from src.db_app.model import Weapon, Engine_, Hull
from src.params import MAX_ITEMS


@pytest.mark.parametrize("ship_num", range(1, MAX_ITEMS["ship"] + 1), scope="class")
class TestShip:
    @pytest.fixture()
    def setup_ship(self, setup_databases, ship_num):
        exp_db_session, current_db_session = setup_databases
        exp_ship = get_ship(exp_db_session, ship_num)
        current_ship = get_ship(current_db_session, ship_num)

        return exp_ship, current_ship

    def test_weapon(self, setup_databases, setup_ship):
        exp_db_session, current_db_session = setup_databases
        exp_ship, current_ship = setup_ship

        assert exp_ship.weapon == current_ship.weapon, (
            f"{current_ship.ship}, {current_ship.weapon}"
            f"\n\texpected {exp_ship.weapon}, was {current_ship.weapon}"
        )

        exp_weapon: Weapon = get_weapon(exp_db_session, exp_ship)
        current_weapon: Weapon = get_weapon(current_db_session, current_ship)

        errors = list()
        if exp_weapon.reload_speed != current_weapon.reload_speed:
            errors.append(
                f"reload speed: expected {exp_weapon.reload_speed}, was {current_weapon.reload_speed}"
            )
        if exp_weapon.rotational_speed != current_weapon.rotational_speed:
            errors.append(
                f"rotational speed: expected {exp_weapon.rotational_speed}, was {current_weapon.rotational_speed}"
            )
        if exp_weapon.diameter != current_weapon.diameter:
            errors.append(
                f"diameter: expected {exp_weapon.diameter}, was {current_weapon.diameter}"
            )
        if exp_weapon.power_volley != current_weapon.power_volley:
            errors.append(
                f"power volley: expected {exp_weapon.power_volley}, was {current_weapon.power_volley}"
            )
        if exp_weapon.count != current_weapon.count:
            errors.append(
                f"count: expected {exp_weapon.count}, was {current_weapon.count}"
            )
        errors = "\n\t".join(errors)
        assert not errors, f"{current_ship.ship}, {current_ship.weapon}" f"\n\t{errors}"

    def test_engine(self, setup_databases, setup_ship):
        exp_db_session, current_db_session = setup_databases
        exp_ship, current_ship = setup_ship

        assert exp_ship.engine == current_ship.engine, (
            f"{current_ship.ship}, {current_ship.engine}\n\t"
            f"expected {exp_ship.engine}, was {current_ship.engine}"
        )

        exp_engine: Engine_ = get_engine(exp_db_session, exp_ship)
        current_engine: Engine_ = get_engine(current_db_session, current_ship)

        errors = list()
        if exp_engine.power != current_engine.power:
            errors.append(
                f"power: expected {exp_engine.power}, was {current_engine.power}"
            )
        if exp_engine.type != current_engine.type:
            errors.append(
                f"type: expected {exp_engine.type}, was {current_engine.type}"
            )

        errors = "\n\t".join(errors)
        assert not errors, f"{current_ship.ship}, {current_ship.engine}" f"\n\t{errors}"

    def test_hull(self, setup_databases, setup_ship):
        exp_db_session, current_db_session = setup_databases
        exp_ship, current_ship = setup_ship

        assert exp_ship.hull == current_ship.hull, (
            f"{current_ship.ship}, {current_ship.hull}"
            f"\n\texpected {exp_ship.hull}, was {current_ship.hull}"
        )

        exp_hull: Hull = get_hull(exp_db_session, exp_ship)
        current_hull: Engine_ = get_hull(current_db_session, current_ship)

        errors = list()
        if exp_hull.armor != current_hull.armor:
            errors.append(f"armor: expected {exp_hull.armor}, was {current_hull.armor}")
        if exp_hull.type != current_hull.type:
            errors.append(f"type: expected {exp_hull.type}, was {current_hull.type}")
        if exp_hull.capacity != current_hull.capacity:
            errors.append(
                f"type: expected {exp_hull.capacity}, was {current_hull.capacity}"
            )

        errors = "\n\t".join(errors)
        assert not errors, f"{current_ship.ship}, {current_ship.hull}" f"\n\t{errors}"
