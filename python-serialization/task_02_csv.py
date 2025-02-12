#!/usr/bin/env python3
'''csv
'''


import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Reads data from a CSV file and converts it into JSON format.

    Parameters:
    csv_filename (str): The name of the CSV file to read.

    Returns:
    bool: True if the conversion was successful, False otherwise.
    """
    try:
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            # Read CSV file and convert to dictionary
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)

        # Serialize to JSON and write to a file
        with open("data.json", mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        print(f"Error: File '{csv_filename}' not found.")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False
