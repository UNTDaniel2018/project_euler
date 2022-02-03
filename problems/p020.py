import math

def sumDigits(in_num):
    
    sum_of_digits = 0
    in_num_str = str(in_num).replace('0','')

    for index in range(len(in_num_str)):
        sum_of_digits = sum_of_digits + int(in_num_str[index])

    return (sum_of_digits)


def findFactorial(in_num):
    return (math.factorial(in_num))


if __name__ == '__main__':

    numbers = [10, 100, 1000]
    answers = []

    for index in numbers:

        factorial_num = findFactorial(index)
        result = sumDigits(factorial_num)
        answers.append(result)

    print(numbers)
    print(answers)