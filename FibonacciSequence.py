#Fibonaci Sequence

print('Input a number')
number = input()
number = int(number)

FiboList = []

def fibonacci(n):
    # Is the value in FiboList?
    length = len(FiboList)
    if length >= (n+1):
        # Value is in FiboList
        retval = FiboList[n]
        return retval

    # Value not in FiboList. Compute it.
    if n <= 1:
        retval = n
    else:
        retval = (fibonacci(n-2)+fibonacci(n-1))

    # Append to FiboList and return
    FiboList.append(retval)
    return retval

if number <= 0:
    print('Please input a positive number')
else:
    print('Fibonaci Sequence:')
    for i in range(number):
        print(fibonacci(i))
