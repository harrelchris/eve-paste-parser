from paste_parser import parse


def read_file(file_path: str) -> str:
    with open(file_path, "r") as file:
        return file.read()


def test_inventory():
    input_text = read_file("examples/inventory/details/1.txt")
    output_dict = {
        0: {
            "name": "Metal Scraps",
            "quantity": 1,
            "group": "Commodities",
            "size": None,
            "slot": None,
            "volume": "0.01 m3",
            "value": "994.05 ISK",
        },
        1: {
            "name": "Thorium Charge S",
            "quantity": 100,
            "group": "Hybrid Charge",
            "size": "Small",
            "slot": None,
            "volume": "0.25 m3",
            "value": "1,100.00 ISK",
        },
        2: {
            "name": "Veldspar",
            "quantity": 25,
            "group": "Veldspar",
            "size": None,
            "slot": None,
            "volume": "2.50 m3",
            "value": "260.75 ISK",
        },
    }
    assert parse(input_text) == output_dict
