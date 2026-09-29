---
lab:
    title: "Generate an inventory reorder report with Python"
    description: "Implement a standard-library Python script that parses quoted CSV fields, filters below-level inventory, calculates units needed, and writes a verified reorder report."
    duration: 20
    level: 300
    islab: true
    status: "in-development"
    targetDate: "2026-09-29"
---

# Generate an inventory reorder report with Python

This exercise should take approximately **20** minutes to complete.

In this exercise, you will progressively implement a local Python script that reads inventory CSV data, calculates replenishment quantities, and writes a filtered report.

## Scenario

You support an operations team that needs a repeatable way to identify products requiring replenishment. The team supplies a small inventory CSV, and your script must produce a trustworthy reorder report without incorrectly splitting product names that contain commas. You will implement and verify the report so the team can act on shortages while excluding products already at or above their reorder level.

## Prior knowledge

- Basic Python syntax, functions, lists, dictionaries, and `if` statements.
- Familiarity with running a Python script from a terminal.

## Before you start

Before you start this exercise, make sure your environment is ready.

### Environment

- A local operating system with permission to read and write files in the exercise folder.
- Python 3.11 or later.

### Tools

- Python 3.11+: verify by running `python --version` or `python3 --version`.
- A text editor or Python-capable IDE.

### Exercise assets

- [Starter Python script](../../Labfiles/01-inventory-replenishment-python/python/reorder_report.py): incomplete script that you will implement.
- [Synthetic inventory CSV](../../Labfiles/01-inventory-replenishment-python/python/data/inventory.csv): input data containing below-level, exactly-at-level, above-level, and comma-containing product names.

### Verify your setup

1. Change to the `Labfiles/01-inventory-replenishment-python/python` folder.
1. Verify the Python version by running `python --version` or `python3 --version`.
1. Confirm that `reorder_report.py` and `data/inventory.csv` are present.
1. Inspect the first line of `data/inventory.csv` and confirm it is `product_id,product_name,quantity_on_hand,reorder_level`.

Your setup is ready when Python reports version 3.11 or later and both supplied files are readable. Do not continue until this check succeeds.

## Read inventory records with the CSV module

First, implement the input stage. The `csv` module handles quoted fields correctly, so the product named `Desk lamp, adjustable` remains one field.

1. Open `reorder_report.py` in your editor.
1. Replace the entire body of `read_inventory`, including the `return []` placeholder, with:

    ```python
    with path.open("r", encoding="utf-8", newline="") as file:
        return list(DictReader(file))
    ```

1. Save the file.
1. Add this temporary verification immediately after `records = read_inventory(INPUT_PATH)` in `main`:

    ```python
    print(records)
    ```

1. Run the script with `python reorder_report.py` or `python3 reorder_report.py`.
1. Confirm that the printed records include a single `product_name` value of `Desk lamp, adjustable`, not two separate fields.
1. Remove the temporary `print(records)` line and save the file.

> **Tip**: Opening CSV files with `newline=""` lets the `csv` module handle line endings as documented. `DictReader` maps each row to a dictionary using the header fields.

If the script cannot find the input file, run it from the folder containing `reorder_report.py`, or verify that `data/inventory.csv` exists relative to that script.

## Calculate reorder recommendations

Next, turn the input records into the smaller report shape and apply the strict below-level rule.

1. Replace the entire body of `build_reorder_rows`, including the `return []` placeholder, with:

    ```python
    reorder_rows = []

    for record in records:
        quantity_on_hand = int(record["quantity_on_hand"])
        reorder_level = int(record["reorder_level"])

        if quantity_on_hand < reorder_level:
            reorder_rows.append(
                {
                    "product_id": record["product_id"],
                    "product_name": record["product_name"],
                    "units_needed": reorder_level - quantity_on_hand,
                }
            )

    return reorder_rows
    ```

1. Save the file.
1. Add this temporary verification immediately after `reorder_rows = build_reorder_rows(records)` in `main`:

    ```python
    print(reorder_rows)
    ```

1. Run the script.
1. Confirm that the temporary output contains exactly three recommendations:
   - `P-1001` needs `6` units.
   - `P-1004` needs `5` units.
   - `P-1005` needs `2` units.
1. Confirm that `P-1002`, `P-1003`, and `P-1006` are absent. `P-1002` and `P-1006` are exactly at their reorder levels, and `P-1003` is above it.
1. Remove the temporary `print(reorder_rows)` line and save the file.

The comparison must be `<`, not `<=`. Using `<=` would incorrectly report products that already meet the reorder level.

## Write and verify the reorder report

Finish the script by writing a CSV with only the fields the operations team needs.

1. Replace the entire body of `write_report`, including the `pass` placeholder and its TODO comments, with:

    ```python
    fieldnames = ["product_id", "product_name", "units_needed"]

    with path.open("w", encoding="utf-8", newline="") as file:
        writer = DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    ```

1. Save the file.
1. Run the completed script with `python reorder_report.py` or `python3 reorder_report.py`.
1. Confirm the terminal reports `Wrote 3 reorder recommendation(s)`.
1. Open `reorder_report.csv` and confirm it contains:

    ```text
    product_id,product_name,units_needed
    P-1001,USB-C cable,6
    P-1004,Wireless mouse,5
    P-1005,Monitor stand,2
    ```

1. Confirm the report contains no rows for `P-1002`, `P-1003`, or `P-1006`, and the comma-containing product name was parsed correctly in the input stage.
1. For a final boundary check, temporarily change `P-1001` in `data/inventory.csv` from quantity `4` to `10`, run the script, and confirm the report now contains two rows. Restore the original `4` value when finished.

> **Tip**: `DictWriter.writeheader()` writes the selected column names, while `writerows()` writes the filtered dictionaries. The output file uses the same `newline=""` pattern as the input file.

If you see `ValueError: invalid literal for int()`, check that the input headers are spelled exactly as `quantity_on_hand` and `reorder_level`, and that those columns contain whole numbers. If the report contains extra columns, verify that `fieldnames` contains only `product_id`, `product_name`, and `units_needed`.

## Clean up

The script creates the local file `reorder_report.csv`.

1. Delete `reorder_report.csv` if you do not need to retain the sample output.
1. Restore `data/inventory.csv` to its original contents if you performed the boundary check.
