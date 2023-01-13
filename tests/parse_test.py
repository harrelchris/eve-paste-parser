from paste_parser import parse


def read_file(file_path: str) -> str:
    with open(file_path, "r") as file:
        return file.read()


def test_assets_contents_01():
    input_text = read_file("tests/examples/assets/contents/01.txt")
    output_dict = {
        0: {
            "name": "Scourge Cruise Missile",
            "group": "Cruise Missile",
            "quantity": "5300",
        },
        1: {
            "name": "Spike M",
            "group": "Advanced Railgun Charge",
            "quantity": "4277",
        },
        2: {
            "name": "Improved Blue Pill Booster Reaction Formula",
            "group": "Biochemical Reaction Formulas",
            "quantity": "1",
        },
        3: {
            "name": "Improved Blue Pill Booster Blueprint",
            "group": "Booster Blueprints",
            "quantity": "1",
        },
        4: {
            "name": "Cartography: The Art of Treasure Map Making",
            "group": "Commodities",
            "quantity": "1",
        },
        5: {
            "name": "22nd Tier Overseer's Personal Effects",
            "group": "Overseer Personal Effects",
            "quantity": "1",
        },
    }
    assert parse(input_text) == output_dict


def test_assets_station_01():
    input_text = read_file("tests/examples/assets/station/01.txt")
    output_dict = {
        0: {
            "name": "Loot",
            "quantity": "",
            "group": "Audit Log Secure Container",
            "size": "",
            "slot": "",
            "volume": "2,000,000 m3",
            "value": "45,300.64 ISK",
        },
        1: {
            "name": "Heavy Water",
            "quantity": "1,287,839",
            "group": "Ice Product",
            "size": "",
            "slot": "",
            "volume": "515,135.60 m3",
            "value": "201,302,114.09 ISK",
        },
        2: {
            "name": "Doc Harrel's Minmatar Shuttle",
            "quantity": "",
            "group": "Shuttle",
            "size": "",
            "slot": "",
            "volume": "5,000 m3",
            "value": "19,471.51 ISK",
        },
        3: {
            "name": "Minmatar Shuttle",
            "quantity": "1",
            "group": "Shuttle",
            "size": "",
            "slot": "",
            "volume": "500 m3",
            "value": "19,471.51 ISK",
        },
    }
    assert parse(input_text) == output_dict


def test_hangars_items_01():
    input_text = read_file("tests/examples/hangars/items/01.txt")
    output_dict = {
        0: {
            "name": "Loot",
        },
        1: {
            "name": "Station Container",
            "quantity": "3",
        },
        2: {
            "name": "Heavy Water",
            "quantity": "1287839",
        },
        3: {
            "name": "Electrolytes",
            "quantity": "253953",
        },
        4: {
            "name": "Oxygen",
            "quantity": "485932",
        },
        5: {
            "name": "Precious Metals",
            "quantity": "285586",
        },
        6: {
            "name": "Reactive Metals",
            "quantity": "44740",
        },
        7: {
            "name": "Toxic Metals",
            "quantity": "140100",
        },
        8: {
            "name": "Water",
            "quantity": "227474",
        },
    }
    assert parse(input_text) == output_dict


def test_hangars_ships_01():
    input_text = read_file("tests/examples/hangars/ships/01.txt")
    output_dict = {
        0: {
            "name": "Prowler",
        },
        1: {
            "name": "Huginn",
        },
        2: {
            "name": "Catalyst",
        },
        3: {
            "name": "Rapier",
        },
        4: {
            "name": "Noctis",
        },
        5: {
            "name": "Doc Harrel's Minmatar Shuttle",
        },
        6: {
            "name": "Minmatar Shuttle",
            "quantity": "1",
        },
    }
    assert parse(input_text) == output_dict


def test_inventory_details_01():
    input_text = read_file("tests/examples/inventory/details/01.txt")
    output_dict = {
        0: {
            "name": "Metal Scraps",
            "quantity": "1",
            "group": "Commodities",
            "size": "",
            "slot": "",
            "volume": "0.01 m3",
            "value": "994.05 ISK",
        },
        1: {
            "name": "Thorium Charge S",
            "quantity": "100",
            "group": "Hybrid Charge",
            "size": "Small",
            "slot": "",
            "volume": "0.25 m3",
            "value": "1,100.00 ISK",
        },
        2: {
            "name": "Veldspar",
            "quantity": "25",
            "group": "Veldspar",
            "size": "",
            "slot": "",
            "volume": "2.50 m3",
            "value": "260.75 ISK",
        },
    }
    assert parse(input_text) == output_dict


def test_inventory_icons_01():
    input_text = read_file("tests/examples/inventory/icons/01.txt")
    output_dict = {
        0: {
            "name": "Veldspar",
            "quantity": "25",
        },
        1: {
            "name": "Thorium Charge S",
            "quantity": "100",
        },
        2: {
            "name": "Metal Scraps",
            "quantity": "1",
        },
    }
    assert parse(input_text) == output_dict


def test_inventory_list_01():
    input_text = read_file("tests/examples/inventory/list/01.txt")
    output_dict = {
        0: {
            "name": "Metal Scraps",
            "quantity": "1",
            "group": "Commodities",
            "size": "",
            "slot": "",
            "volume": "0.01 m3",
            "value": "994.05 ISK",
        },
        1: {
            "name": "Thorium Charge S",
            "quantity": "100",
            "group": "Hybrid Charge",
            "size": "Small",
            "slot": "",
            "volume": "0.25 m3",
            "value": "1,100.00 ISK",
        },
        2: {
            "name": "Veldspar",
            "quantity": "25",
            "group": "Veldspar",
            "size": "",
            "slot": "",
            "volume": "2.50 m3",
            "value": "260.75 ISK",
        },
    }
    assert parse(input_text) == output_dict
