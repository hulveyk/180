# This is a python Program to Calculate the fibonacci sequence. Create the fibonacci sequence and store it in a list.
def fib(n):
    if n == 0:
        return [0] 
    elif n == 1:
        return [0, 1]
    else:
        x = fib(n-1)
        x.append(sum(x[:-2:-1]))
        return x
n = int(input("Enter the number of terms: "))

print(fib(n))

# Output: Enter the number of terms: 10
 print([0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
     

