
##Division (/) always returns a float.
##To do floor division and get an integer result (discarding any fractional result) you can use the // operator;
##to calculate the remainder you can use %:

def summ (number):
    """summa of digits in a number"""
    summa = 0
    if (number<=9):
        last_digit = number % 10
        summa = last_digit
    else:
        #for i in range(1,number):
        while number:
            last_digit = number % 10
            number = number //10
            summa+=last_digit
    return summa
        
#  number  is created by concatenating the string   n*p times so the initial 
def superDigit(n, k):
    #if len(n)==1:
    #     return n
    # else:
    #     # multiply str by constant
    #     new_n=k*n
    #     while len(new_n)>1:
    #         s = digitsum(int(new_n))
    #         new_n = str(s)
    # return s
    if len(n) == 1:
        return int(n)
    res = 0
    for num in n:
        res += int(num)
    return superDigit(str(res*k),1)