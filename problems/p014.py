def is_odd(in_num):
    return ((in_num * 3) + 1)

def is_even(in_num):
    return (in_num / 2)

def iterative_seq(in_num):

    seq = []
    seq.append(in_num)

    while (in_num != 1):
        if(in_num % 2 == 0):
            in_num = is_even(in_num)

        else:
            in_num = is_odd(in_num)

        seq.append(in_num)

    return (seq)


if __name__ == '__main__':
    
    collatz_list = []
    max_seq = 0
    max_num = 0

    for index in range(1, 1000000):

    #index = 13

        index_list = []
        index_list.append(index)

        sequence = iterative_seq(index)
        len_seq = len(sequence)

        index_list.append(len_seq)
        collatz_list.append(index_list)

        if (len_seq > max_seq):
            max_seq = len_seq
            max_num = index

    #print(sequence)
    
    #for index in range(len(collatz_list)):
    #    print(collatz_list[index])

    print(max_num)
    print(max_seq)

    