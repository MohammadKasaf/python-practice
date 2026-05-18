def check_prime_number(num):

    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True

num=int(input("enter a number :"))
if check_prime_number(num):
    print(f"{num} is prime")
else:
    print(f"{num} is not prime")