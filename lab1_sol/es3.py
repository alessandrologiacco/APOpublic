# enter your file path
DATA_PATH = "./lab1/data"

# file names
IN_FILE = "input.txt"
OUT_FILE = "output.txt"


def main():
    lines = []
    # open input file
    with open("{}/{}".format(DATA_PATH, IN_FILE), "r") as file:
        # reach each line
        for line in file:
            # print removing newline
            print(line.strip())
            # append to table
            lines.append(line)
    # invert line order
    lines = lines[-1::-1]
    # open output file
    with open("{}/{}".format(DATA_PATH, OUT_FILE), "w") as file:
        for line in lines:
            file.write(line)


if __name__ == "__main__":
    main()
