def smallest_multiple(in_num, in_range):

    multiples = []

    for index in range(in_range + 1, 1, -1):
        if (in_num % index == 0):
            multiples.append(index)
        else:
            return False

    return True


if __name__ == "__main__":

    is_done = True
    in_range = 20
    in_num = 2520

    while (is_done == True):

        if (smallest_multiple(in_num, in_range) == True):
            print(in_num)
            break

        in_num += 2520

