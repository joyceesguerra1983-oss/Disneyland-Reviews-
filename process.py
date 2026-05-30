import csv


def load_csv(filename):
    data = []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                data.append(row)

    except FileNotFoundError:
        print(f"Error: {filename} was not found.")

    return data
