#Fibonaci Sequence

print('Input a number')
number = input()
number = int(number)

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1)+fibonacci(n-2))

if number <= 0:
    print('Please input a positive number')
else:
    print('Fibonaci Sequence:')
    for i in range(number):
        print(fibonnacci(i))
