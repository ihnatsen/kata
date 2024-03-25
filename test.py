def sieve_of_Eratosthenes(number):
    numbers = [True] * number
    numbers[0] = numbers[1] = False
    for k in range(2, number):
        if numbers[k]:
            for m in range(2*k, number, k):
                numbers[m] = False

    return numbers

print(sieve_of_Eratosthenes(10))