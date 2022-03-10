def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

for i in range(5):
    print("{}!: {}".format(i+1, factorial(i+1)))