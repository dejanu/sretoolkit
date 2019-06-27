import math

def is_prime(x):
        if x<=3:
                return True
        sqr =int(math.sqrt(x)+1)
        for i in range(1,sqr):
                if  x%i != 0:
                        return False
                        break
        return True


def pris(a):
	for i in range(2,a//2):
		if a%i == 0:
			return False
	else:
		return True

def sieve_prime(n):
    """ generate firt n prime numbers"""
    primes = list(range(2,n+1))

    i = 2
    while (i <= int(math.sqrt(n))):
        # if i in list delete multiples
        if i in primes:
            # j will give multiples of i
            for j in range(i*2, n+1, i):
                if j in primes:
                    primes.remove(j)
        i+=1
    return primes

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0: 
                return False
        return True
    return False


#Euler 10  = return a list of all the primes no from start to infinity
def generator_primes(number):
    while True:
        if is_prime(number):
            yield number
        number += 1

if __name__ == "__main__":
        print(sieve_prime(100))
