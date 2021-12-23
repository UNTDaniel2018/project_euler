def prime_factors(in_num):
    factors = []
    d = 2
    while in_num > 1:
        while in_num % d == 0:
            factors.append(d)
            in_num /= d
        
        d += 1
    return (factors)


if __name__ == "__main__":
    
    pfs = prime_factors(13195)
        
    print(max(pfs)) 
