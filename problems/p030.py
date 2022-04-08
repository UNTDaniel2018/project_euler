from ast import Num
import time


def fifth_powers():

    solution = 0

    #for loop to loop till 5(10-1)^5
    for i in range(2,5*9**5+1):

        if sum([int(x)**5 for x in str(i)]) == i:
            solution += i

    #printing the solution
    return(solution)


if __name__ == '__main__':

    start_time = time.time()

    answer = fifth_powers()

    print(answer)

    print("\n--- %s seconds ---\n" % (time.time() - start_time))
