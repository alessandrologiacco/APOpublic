# alphabet set as lowercase letters (from ascii codes)
ALPHABET = {chr(65+i).lower() for i in range(26)}


def main():
    str1 = input("Insert first string: ")
    str2 = input("Insert second string: ")

    # transform to lowercase
    str1 = str1.lower()
    str2 = str2.lower()

    # transform to set and remove non ASCII
    str1_set = {c for c in str1 if c in ALPHABET}
    str2_set = {c for c in str2 if c in ALPHABET}

    union_set = set.union(str1_set, str2_set)
    diff_1 = str1_set - str2_set
    diff_2 = str2_set - str1_set
    comp = ALPHABET - str1_set - str2_set

    # print stuff
    print("union: {}".format(union_set if union_set else {}))
    print("str1 - str2: {}".format(diff_1 if diff_1  else {}))
    print("str2 - str1: {}".format(diff_2 if diff_2 else {}))
    print("complement: {}".format(comp if comp else {}))


if __name__ == "__main__":
    main()
