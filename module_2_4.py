numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes =[]

for num in numbers[1:]:
        is_prime = True
        for div in range(2,num):
            if num % div == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        else:
            not_primes.append(num)

print('primes:',primes)
print('not_primes:',not_primes)







