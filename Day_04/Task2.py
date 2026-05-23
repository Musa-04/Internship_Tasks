import csv

def filter_high_salary():
    try:
        with open("employees.csv", "r") as file:
            reader = csv.DictReader(file)
            high_salary = []

            for row in reader:
                if int(row["salary"]) > 50000:
                    high_salary.append(row)

        with open("high_salary.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=high_salary[0].keys())
            writer.writeheader()
            writer.writerows(high_salary)

        print("High salary employees saved")

    except FileNotFoundError:
        print("Employees file not found")
    except ValueError:
        print("Invalid salary value")

filter_high_salary()
