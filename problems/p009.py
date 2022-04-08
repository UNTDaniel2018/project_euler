import time

def count_coin_sum():

    counter = 0

    for a in range(3):
        # number of 50p coins
            for b in range(int(1+(200-100*a)/50)):
                # number of 20p coins
                    for c in range(int(1+(200-100*a-50*b)/20)):
                        # number of 10p coins
                            for d in range(int(1+(200-100*a-50*b-20*c)/10)):
                                # number of 5p coins
                                    for e in range(int(1+(200-100*a-50*b-20*c-10*d)/5)):
                                        # number of 2p coins
                                            for f in range(int(1+(200-100*a-50*b-20*c-10*d-5*e)/2)):
                                                counter += 1

    return (counter)



if __name__ == '__main__':

    start_time = time.time()

    solution = count_coin_sum()
    print (solution)


    print("\n--- %s seconds ---\n" % (time.time() - start_time))
