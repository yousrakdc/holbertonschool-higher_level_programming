#!/usr/bin/env python3

import csv
import json


def convert_csv_to_json(csv_filename):
    try:
        with open(csv_filename, 'r') as csv_file:
            reader = csv.DictReader(csv.file)
            data = [row for row in reader]

        with open('data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except FileNotFoundError:
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
