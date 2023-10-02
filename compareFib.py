import time
import math

inputArray = [1,2,3,4,5,6,7,8,9,10,25,30,35,40]

def fib1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib1(n-1) + fib1(n-2)


def fib2(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        f = [0] * (n+1)
        f[0] = 0
        f[1] = 1
        for i in range(2, n+1):
            f[i] = f[i-1] + f[i-2]
        return f[n]



def fibWithGoldenRatio(n):
    phi = (1 + math.sqrt(5)) / 2
    return round((phi**n - (1 - phi)**n) / math.sqrt(5))

for input in inputArray:

    start = time.time()
    fib1Result = fib1(input)
    end  = time.time()
    fib1Time = (end - start) *1000

    start = time.time()
    fib2Result = fib2(input)
    end = time.time()
    fib2Time = (end - start)*1000

    start = time.time()
    fibGoldenRatioResult = fibWithGoldenRatio(input)
    end  = time.time()
    fibGoldenRatioTime = (end - start)*1000

    print(f"\n\nInput: {input}")
    print(f"fib1: {fib1Time}   fib2: {fib2Time}   fibGR: {fibGoldenRatioTime}")       
    print(f"fib1Result: {fib1Result}               fib2Result: {fib2Result}                  fibGRresult: {fibGoldenRatioResult}")