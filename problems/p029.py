import time

def calculate_powers(min_num, max_num):

    powers_list = []

    for index_n in range(min_num, max_num + 1):

        offset = 0

        for index_p in range(min_num + offset, max_num + 1):

            product = pow(index_n, index_p)

            if (powers_list.count(product) == 0):

                powers_list.append(product)

            if (index_n != index_p):

                product_2 = pow(index_p, index_n)
                
                if (powers_list.count(product_2) == 0):

                    powers_list.append(product_2)

            # DEBUG
            #print(index_n, index_p)
    
        offset += 1

    return (sorted(powers_list))


if __name__ == '__main__':

    start_time = time.time()

    power_list = calculate_powers(2, 100)

    print(len(power_list))

    print("\n--- %s seconds ---\n" % (time.time() - start_time))
