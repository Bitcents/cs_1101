
def sum_harmonic(n):                     # function to sum up the first 
    sum = 0                              # n terms in the harmonic series
    for i in range(1,n):                 # fixed the division by zero error
        sum += 1/i                       # by starting the series from n = 1 rather than n = 0

    print(sum)

sum_harmonic(10)                         # call to function