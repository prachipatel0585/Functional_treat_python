print(input('please enter your choice:'))
num=int(input('enter a number to calculate its factorial:'))
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
print(factorial(5))
print(f'factorial of {num} is: {factorial(num)}')
