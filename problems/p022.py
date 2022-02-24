def open_file(input_location):

    content = ''

    input_f = open(input_location, "r")

    content = input_f.read()

    input_f.close()

    return (content)


def calculate_name_value(name):

    value = 0

    for letter in name:
        value = value + (ord(letter) - 64)

    return (value)


def name_value(name_list):

    value_list = []

    index_i = 1

    for index in name_list:

        index = index.replace('"', '')

        tmp_value = (calculate_name_value(index) * index_i)
        
        value_list.append(tmp_value)

        index_i += 1

    return (value_list)


def get_max(name_list, value_list):

    max_index = value_list.index(max(value_list))

    print(name_list[max_index], value_list[max_index])


def get_total(value_list):

    result = 0

    for value in value_list:
        result = result + value

    return (result)


if __name__ == '__main__':

    input_location = '../project_euler/input_files/p022_names.txt'

    name_list = []

    value_list = []

    raw_file = open_file(input_location)

    name_list = sorted(raw_file.split(','))

    value_list = name_value(name_list)

    print('Total:', get_total(value_list))
    