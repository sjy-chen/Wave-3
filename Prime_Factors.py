#receiving input from user
n = input("Enter an integer (2 or greater): ")

#error checking for letters, floats, and numbers less than two
if n.isalpha() == True:
    print("Please enter an integer 2 or greater.")
    exit()
elif float(n) % 1 != 0:
    print("Please enter an integer 2 or greater.")
    exit()
elif float(n) < 2:
    print("Please enter an integer 2 or greater.")
    exit()
else:
    print("The prime factors of", n, "are: ")

#converting n to an integer
n = int(n)

#displaying prime numbers
factor = 2
while factor <= n:
    if n % factor == 0:
        print(factor)
        n /= factor
    else:
        factor = factor + 1