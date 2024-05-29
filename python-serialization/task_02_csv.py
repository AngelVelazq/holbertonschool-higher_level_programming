import csv
import json


def convert_csv_to_json(csv_filename):
    try:
        with open(csv_filename, 'r', newline='') as csvfile:
            # Read CSV file using DictReader
            reader = csv.DictReader(csvfile)
            data = list(reader)

        # Serialize data to JSON
        json_data = json.dumps(data, indent=4)

        # Write JSON data to data.json
        with open('data.json', 'w') as jsonfile:
            jsonfile.write(json_data)

        return True

    except FileNotFoundError:
        print("File not found!")
        return False


# Example usage
if __name__ == "__main__":
    csv_filename = 'example.csv'
    success = convert_csv_to_json(csv_filename)
    if success:
        print("Conversion successful. JSON data written to data.json")
    else:
        print("Conversion failed.")
