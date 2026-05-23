def word_counter(filename):
    try:
        with open(filename, "r") as f:
            text = f.read()

        lines = text.splitlines()
        words = text.split()

        print("Lines:", len(lines))
        print("Words:", len(words))
        print("Characters:", len(text))

    except FileNotFoundError:
        print("File not found")

word_counter("summary.txt")
