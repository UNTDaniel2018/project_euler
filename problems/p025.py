import math
import time


def check_length(n):

    if n > 0:
        digits = int(math.log10(n))+1
    elif n == 0:
        digits = 1
    else:
        digits = int(math.log10(-n))+2 # +1 if you don't count the '-' 

    return (digits)


def fib_seq():

    n1, n2 = 1, 1
    length = 0
    max_digits = 1000
    fib_list = []

    print("Fibonacci sequence:")
   
    while length <= max_digits:
        
        fib_list.append(n1)
        
        # DEBUG
        #print(n1) 

        if(length == max_digits):
            break

        nth = n1 + n2
        
        n1 = n2
        
        n2 = nth

        length = check_length(n1)

    return (fib_list)


if __name__ == '__main__':

    start_time = time.time()

    fib_list_result = fib_seq()

    #print(fib_list_result[-1])

    print(len(fib_list_result))

    print("\n--- %s seconds ---\n" % (time.time() - start_time))