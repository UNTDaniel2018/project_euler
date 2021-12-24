def square_of_sum(in_num):
    value = 0

    for index in range(1, in_num + 1):
        value = value + pow(index, 2)

    return (value)


def sum_of_squares(in_num):
    value = 0

    for index in range(1, in_num + 1):
        value = value + index

    return (pow(value, 2))


if __name__ == "__main__":

    print(sum_of_squares(100) - square_of_sum(100))
