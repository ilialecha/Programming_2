def sum_of_digits(n):
    if 0<=n<=9: return n
    else: return n%10 + sum_of_digits(n//10)

def is_multiple_3(n):
    return sum_of_digits(n)%3==0
