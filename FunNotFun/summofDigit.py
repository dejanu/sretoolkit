
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
        
