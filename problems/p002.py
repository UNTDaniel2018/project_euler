# Function: calculates fibonacci sum of even terms.
# Returns: fibonacci sum (integer)
def generate_fibonacci(num_limit):

    current_value = 1
    fibonacci_sum = 0
    next_value = 0
    prev_value = 1

    while next_value < num_limit:
    
        if(current_value % 2 == 0):
            fibonacci_sum = fibonacci_sum + current_value

        next_value = current_value + prev_value
        prev_value = current_value
        current_value = next_value

    # print("Fibonacci sum: %d" % (fibonacci_sum))
    
    return (fibonacci_sum)
        

if __name__ == "__main__": 
    print(generate_fibonacci(4000000))
