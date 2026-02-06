# Automated Report Generator

try:
    total_sales = 0
    with open("sales.txt", "r") as file:
        for line in file:
            total_sales += int(line.strip())

    with open("report.txt", "w") as report:
        report.write("Daily Sales Report\n")
        report.write(f"Total Sales: {total_sales}")

    print("Report generated successfully")

except FileNotFoundError:
    print("Sales file is missing")
except ValueError:
    print("Invalid sales data")
