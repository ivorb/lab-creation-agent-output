from csv import DictReader, DictWriter
from pathlib import Path

INPUT_PATH = Path(__file__).with_name("data") / "inventory.csv"
OUTPUT_PATH = Path(__file__).with_name("reorder_report.csv")


def read_inventory(path):
    """Read inventory rows from a CSV file and return them as dictionaries."""
    # TODO: Open path with UTF-8 encoding and newline="", then return list(DictReader(file)).
    return []


def build_reorder_rows(records):
    """Return report rows for products below their reorder level."""
    # TODO: Convert quantity_on_hand and reorder_level to integers.
    # TODO: Keep only rows where quantity_on_hand is less than reorder_level.
    # TODO: Return product_id, product_name, and units_needed fields.
    return []


def write_report(path, rows):
    """Write report rows to a CSV file."""
    # TODO: Set the report field names, open path with UTF-8 encoding and newline="",
    #       create a DictWriter, write the header, and write all rows.
    pass


def main():
    records = read_inventory(INPUT_PATH)
    reorder_rows = build_reorder_rows(records)
    write_report(OUTPUT_PATH, reorder_rows)
    print(f"Wrote {len(reorder_rows)} reorder recommendation(s) to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
