###Project Euler Problem 3
###What is the Largest Prime Factor of the Number 600851475143
def largest_prime_factor(number): #Defining Function for Finding the Largest Prime Factor of a Number
    largestprime=0 #Initialize Largest Prime Variable
    while number%2==0: #While the number is even
        largestprime=2 #Largest Prime is 2 if a number is even
        number/=2 ##Divide the number by 2
    for i in range(3,int(number**.5)+1,2): #Iterate from 3 to the integer sqrt of number +1 by steps of 2 to skip even numbers as those are not prime
        while number%i==0: #While the number is divisible by i
            largestprime=i #Largest prime is set to i
            number/=i #Change number to number/i
    if number>2: #If the number is greater than two after the previous part
        largestprime=number #The number must be prime
    return(largestprime) #Return the value of the largest prime
print(largest_prime_factor(600851475143)) #Run Function on Desired Number
        
                    

                    

