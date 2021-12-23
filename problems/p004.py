def check_palindrome(product):

    length = len(str(product))
    if (length % 2 != 0):
        return False

    half_len = int(length / 2)

    s_part = str(product)[:half_len]
    e_part = str(product)[half_len:]
    e_part = e_part[::-1]

    if (s_part == e_part):
        return True
    else:
        return False


def largest_palindrome():

    palindrome = []
    
    for index_1 in range(100, 1000):
        for index_2 in range(100, 1000):

            product = (index_1 * index_2)
            if (check_palindrome(product) == True and product not in palindrome):
                palindrome.append(product)

    return (palindrome)


if __name__ == "__main__":

    largest_palindrome_product = largest_palindrome()
    largest_palindrome_product.sort()

    print(max(largest_palindrome_product))
