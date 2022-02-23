
def main(power):

    sum_of_digits = 0
    x = pow(2, power)
    x_str = str(x).replace('0','')

    for index in range(len(x_str)):
        sum_of_digits = sum_of_digits + int(x_str[index])

    return (sum_of_digits)

if __name__ == '__main__':

    answer = main(1000)
    print(answer)