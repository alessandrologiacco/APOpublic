def main():
    # read table dimension
    n = int(input("Insert table dimension: "))
    # generate empty table
    table = [[0]*n for i in range(n)]
    # set first value
    table[0][0] = 1
    for i in range(n):
        for j in range(n):
            # check if there is a left cell
            if i > 0:
                table[i][j] += table[i-1][j]
            # check if there is an upper cell
            if j > 0:
                table[i][j] += table[i][j-1]
            # print cell
            print("{:{fill}}".format(table[i][j], fill=n), end="")
        # add new line
        print("")


if __name__ == "__main__":
    main()
