from easyinput import read
def product_of_digits(n):
    if n <= 9:
        print(f"The product of the digits of {n} is {n}.")     
    else:
        while n > 9:
            if n % 10 == 0:
                print(f"The product of the digits of {n} is {0}.")
                break
            else:
                total = 1
                n_ = n
                while n_ > 0:
                    total *= n_ % 10
                    n_ //= 10
                print(f"The product of the digits of {n} is {total}.")
                n = total
    print("----------")    
    

number = read(int)
while number is not None:
    product_of_digits(number)
    number = read(int)