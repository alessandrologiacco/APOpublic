def main():
    word = input()
    # for each possible length of substring (i)
    for i in range(1, len(word)):
        # for each starting point (j)
        for j in range(len(word)):
            # only if substring of length (i) is possible from j
            if j + i <= len(word):
                print(word[j:j+i])


if __name__ == "__main__":
    main()
