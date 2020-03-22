# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# observation: 600851475143 = ab, where a is the smallest factor, and b is the largest factor
# find a, then b is easy to find
import time
import math
def main():
    start = int(round(time.time() * 1000))
    n = -1
    for i in range(int(math.sqrt(600851475143)+1), 3, -2):
        if 600851475143 % i == 0 and (isPrime(i)):
            n = 600851475143 / i
            print(i)
            break
    print("finished in " + str(int(round(time.time() * 1000)) - start) + "ms")
    # finished in ~45ms, TODO improvements necessary...
def isPrime(x):
    for i in range(3, int(math.sqrt(x)), 2):
        if x % i == 0:
            return False
    return True
main()