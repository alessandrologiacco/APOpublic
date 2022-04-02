# Questa soluzione considera anche come massimo:
# - unico numero in una sequenza lunga 1
# - primo numero se maggiore del secondo
# - ultimo numero se maggiore del penultimo

def main():
    # there are no local maxima for now
    flag = False
    # read numbers and append to list
    num_list = []
    val_str = input()
    while val_str != "":
        num_list.append(int(val_str))
        val_str = input()
    # find local maxima
    for i in range(len(num_list)):
        # this checks: sequence of one number, max at beginning/end, max in the middle
        # right side of "OR" is not evaluated if left side is already true
        if (i == 0 or num_list[i] > num_list[i-1]) and \
                (i == len(num_list) - 1 or num_list[i] > num_list[i+1]):
            print("max in pos {}".format(i))
            flag = True
    if not flag:
        print("Local maxima are not present")


if __name__ == "__main__":
    main()
