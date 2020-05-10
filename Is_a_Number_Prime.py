#defining number_isPrime function
def number_isPrime(number):
    if number <= 1: 
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

#checking if the inputted integer is prime
n = input("Please input an integer: ")
if n.isalpha() == True:
    print("Please input an integer.")
    exit()
elif float(n) % 1 != 0:
    print("Please input an integer.")
    exit()
else:
    n = int(n)
if number_isPrime(n):
    print(n, "is prime.")
else:
    print(n, "is not prime.")