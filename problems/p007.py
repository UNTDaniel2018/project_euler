def list_primes():

    primes = [2]
    in_num = 3

    while (len(primes) <= 10001):

        is_prime = True

        for index in range(2, int(in_num/ 2)):
            if (in_num % index == 0):
                is_prime = False
                break

        if(is_prime == True):
            primes.append(in_num)

        in_num += 2

    return (primes)


if __name__ == "__main__":

    prime_num = list_primes()

    print(max(prime_num))
