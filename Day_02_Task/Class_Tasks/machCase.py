# Write a program for match case by using the months like jan, feb, ... dec

month = input("Enter a month (jan, feb, mar, ... dec): ").lower()

match month:
    case "jan":
        print("January has 31 days")
    case "feb":
        print("February has 28 or 29 days")
    case "mar":
        print("March has 31 days")
    case "apr":
        print("April has 30 days")
    case "may":
        print("May has 31 days")
    case "jun":
        print("June has 30 days")
    case "jul":
        print("July has 31 days")
    case "aug":
        print("August has 31 days")
    case "sep":
        print("September has 30 days")
    case "oct":
        print("October has 31 days")
    case "nov":
        print("November has 30 days")
    case "dec":
        print("December has 31 days")
    case _:
        print("Invalid month entered")
