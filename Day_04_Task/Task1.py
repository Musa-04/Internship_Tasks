# Count errors and store error lines separately

def count_errors(filename):
    error_lines = []
    count = 0

    with open(filename, "r") as file:
        for line in file:
            if "error" in line.lower():
                count += 1
                error_lines.append(line)

    with open("error_log.txt", "w") as log:
        log.writelines(error_lines)

    return count

print("Total Errors:", count_errors("log.txt"))
