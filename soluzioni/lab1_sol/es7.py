def main():
    # request name of text file
    filename = input("Insert name of text file: ")
    # open file and read line by line
    with open(filename, 'r') as infile:
        word_dict = {}
        for line in infile:
            # split on space
            words = line.split(" ")
            # remove newlines and empty lines
            words = [word.strip() for word in words if word]
            # create dict with key = word and value = occurrences
            for word in words:
                # remove punctuation
                for c in word:
                    if not c.isalpha():
                        word = word.replace(c, "")
                if word not in word_dict:
                    word_dict[word] = 1
                else:
                    word_dict[word] += 1
    # create list of tuples (occurrences, word) from word_dict
    word_list = [(occurrences, word) for word, occurrences in word_dict.items()]
    # sort list of tuples (sorts by occurrences and then by word)
    word_list.sort(reverse=True)
    # print first 100 words
    for _, word in word_list[:100]:
        print(word, end=" ")
    print("")


if __name__ == "__main__":
    main()
