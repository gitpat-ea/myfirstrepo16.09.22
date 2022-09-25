import numpy as np
primes = np.array([-2,-3,-5,-7,-11,-13,-17,-19,-23,-29])
#primes = primes.reshape(10,1)
print(primes)
fib = np.array([1,1,2,3,5,8,13,21,34,55])
#fib = fib.reshape(10,1)
print(fib)
print(primes.dot(fib))