#!/usr/bin/env python3

def print_fibonacci(length):
    fib =[]
    for i in range(length):
        if i == 0:
            fib.append(0)
        elif i == 1:
            fib.append(1)
        else:
            fib.append(fib[i-1] + fib[i-2])
    print(fib)
        
    