###Project Euler Problem 1
###Find the sum of all multiples of 3 or 5 below 1000
def sum35(number):
    sum = 0
    for i in range(number):
        if i%3 == 0 or i%5 == 0:
            sum += i
    return sum
print('Total for sum of multiples of 3 or 5 is:', sum35(1000))









