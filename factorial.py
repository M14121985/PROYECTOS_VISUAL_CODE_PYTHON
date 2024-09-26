#factorial

def factorial(n):
    if n == 1:
        return 1
    else:
        return n* factorial(n-1)
    
print(factorial(5))#120
print(factorial(6))#720
print(factorial(7))#5040
print(factorial(8))#40320
print(factorial(9))#362880
print(factorial(10))#3628800
print(factorial(11))#39916800