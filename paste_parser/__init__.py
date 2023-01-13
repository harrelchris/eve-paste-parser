COLUMNS_2 = [
    "name",
    "quantity",
]

COLUMNS_3 = [
    "name",
    "group",
    "quantity",
]

COLUMNS_7 = [
    "name",
    "quantity",
    "group",
    "size",
    "slot",
    "volume",
    "value",
]


def parse(text: str) -> dict:
    if not text.strip():
        return {}

    # remove empty lines
    lines = [line for line in text.splitlines() if line]

    # First line of a fit is [Hull, Name]
    if text.startswith("["):
        return {n: parse_fit_line(line) for n, line in enumerate(lines)}
    else:
        return {n: parse_item_line(line) for n, line in enumerate(lines)}


def parse_fit_line(line: str) -> dict:
    if line.startswith("["):
        ship, *_ = line.strip("[]").split(",")
        return {"name": ship}
    else:
        column_line_split = line.split(",")
        columns = len(column_line_split)
        if columns == 1:
            return {"name": line.strip()}
        elif columns == 2:
            # TODO: handle this - need to get two dicts into the fit somehow
            weapon, charge = column_line_split
            return {
                "weapon": weapon,
                "charge": charge,
            }
        else:
            raise ValueError(f"{columns} column lines unhandled")


def parse_item_line(line: str) -> dict:
    tab_split_line = line.split("\t")
    columns = len(tab_split_line)
    if columns == 1:
        return {"name": line.strip()}
    elif columns == 2:
        return dict(zip(COLUMNS_2, tab_split_line))
    elif columns == 3:
        return dict(zip(COLUMNS_3, tab_split_line))
    elif columns == 7:
        return dict(zip(COLUMNS_7, tab_split_line))
    else:
        raise ValueError(f"{columns} column lines unhandled")
