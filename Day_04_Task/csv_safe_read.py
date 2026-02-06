import csv

try:
    with open("demo.csv", "r") as file:
        reader = csv.reader(file)
        header = next(reader)

        for row in reader:
            try:
                if float(row[2]) > 4.5:
                    print(row)
            except ValueError:
                print("Invalid numeric data:", row)

except FileNotFoundError:
    print("File not found")
except Exception as e:
    print("Unexpected error:", e)
