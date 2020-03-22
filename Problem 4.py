# A palindromic number reads the same both ways. The largest palindrome
# made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
import time
import math

# observation: presumably, the palindrome is 6 digits --> palindrome p = abccba
# abccba = a + 10b + 100c + 1000c + 10000b + 100000a
# abccba = 100001a + 10010b + 1100c
# abccba = 11(9091a + 910b + 100c) --> abccba = de, and either d or e must be divisible by 11

def main():
    start = int(round(time.time() * 1000))
    maxVal = 0
    for i in range(999, 0, -1):
        for j in range(999, 0, -1):
            product = i*j
            productList = [int(x) for x in str(product)]
            palindrome = True
            exitLoop = False
            for w in range(int(len(productList) / 2)):
                if productList[w] != productList[len(productList) - w - 1]:
                    palindrome = False
                    break
            if palindrome:
                if product > maxVal:
                    print(i)
                    print(j)
                    print(product)
                    maxVal = product
                break
        if exitLoop:
            break
    print("finished in " + str(int(round(time.time() * 1000)) - start) + "ms")
    # finished in ~1s, TODO improvements necessary...
main()