###Project Euler Problem 2
###Find the sum of even-valued fibonacci sequence up to 4-million
def fibonaccievensum(num):
    val1 = 1
    val2 = 2
    total = 0
    while val1 <= num and val2 <=num:
        if val2%2 == 0:
            total += val2
        val1 = val1+val2
        if val1%2 == 0:
            total += val1
        val2 = val1+val2
    return total
print('Total for summing even fibonacci numbers is: ', fibonaccievensum(4000000))
