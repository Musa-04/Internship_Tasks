# Task: File data counter

def file_counter(filename):
    with open(filename, "r") as f:
        lines = f.readlines()

    words = sum(len(line.split()) for line in lines)
    characters = sum(len(line) for line in lines)

    return len(lines), words, characters

# Example:
# print(file_counter("sample.txt"))
