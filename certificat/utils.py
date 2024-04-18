import json


def import_from_json(filename: str) -> list[dict]:
    with open(filename, "r", encoding="utf-8") as jsonfile:
        data = json.load(jsonfile)
    return data
