# Function: Sums multiples of 3 or 5 from 0 to given limit.
# RETURNS: sum of numbers (integer)
def calculate_sum(num_limit):

    # set/reset value to 0
    multiple_sum = 0

    # range starts at 0 goes to num_limit - 1
    # note 0 gets counted
    for value in range(num_limit):
        # check if value is a multple of 3 or 5
        if (value % 3 == 0 or value % 5 == 0):
            multiple_sum = multiple_sum + value
                    
    # prints results from function
    # print("Sum of all multiples under (%d): %d" % (num_limit, multiple_sum))
    return (multiple_sum)


if __name__ == "__main__":
    
    # problem value
    print(calculate_sum(1000))
    
    # given value, sum = 23
    calculate_sum(10)