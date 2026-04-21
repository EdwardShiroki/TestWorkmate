import csv

from reports import REPORTS


def read_rows_from_file(file_path: str) -> list[dict[str, str]]:
    with open(file_path, "r", newline="", encoding="utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)


def read_rows_from_files(files: list[str]) -> list[dict[str, str]]:
    result = []
    for file_path in files:
        result.extend(read_rows_from_file(file_path))
    return result


def proceed_all_files(files: list[str], method: str) -> list[list]:
    if method not in REPORTS:
        raise ValueError(f"There is no such report method: {method}")

    rows = read_rows_from_files(files)
    return REPORTS[method](rows)
