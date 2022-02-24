import time

# Equations from: https://www.educative.io/edpresso/how-to-solve-the-number-spiral-diagonals-problem

def diagonal_sum(dim):
    
    n = ((dim - 1) / 2)

    result = ((3 + 2 * n * (8 * n * n + 15 * n + 13)) / 3)

    return (result)


if __name__ == '__main__':

    start_time = time.time()

    dim = 5

    answer = int(diagonal_sum(dim))

    print(answer)

    print("\n--- %s seconds ---\n" % (time.time() - start_time))
