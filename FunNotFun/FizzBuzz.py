# Generate list of numbers from 1 to 100 
# foreach multiple of 3 print Fizz instead of number
# foreach multiple of 5 print Buzz insteam of number
# for numbers multiple of both 3 and 5 print FizzBuzz

def fizzbuzz(x=100):
    y = []
    for i in range(1,100):
        if i%3 == 0:
            if i%5 ==0:
                y.append("FizzBuzz")
            else:
                y.append("Fizz")
        elif i%5 == 0:
            y.append("Buzz")
        else:
            y.append(i)
    return y



 def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        3 return 'FizzBuzz'
    elif n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        return 'Buzz'
    else:
        return str(n)
