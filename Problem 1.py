# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# observation: multiples of 3 include 3, 6, 9, ... 999 --> 3(n), n in [1, 333]
# observation: multiples of 5 include 5, 10, 15, ... 995 --> 5(n), n in [1, 199]
# observation: must subtract those counted twice --> 15(n), n in [1, 66]

import time

def main():
    # method one - iterate through loops
    start = int(round(time.time() * 1000))
    sum = 0
    for i in range(333):
        sum += 3*(i+1)
    for i in range(199):
        sum += 5*(i+1)
    for i in range(66):
        sum -= 15*(i+1)
    print(sum)
    print("finished in " + str(int(round(time.time() * 1000)) - start) + "ms")

    # finished in 0ms, no improvements necessary...
main()