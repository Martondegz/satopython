"""
Create a function that:
	1. Halves even numbers
	2. Doubles odd numbers
	3. Returns the sum of all
"""
numbers = [12,13,15]
def super_sum(num):
#initialize an empty variable for even and odd numbers
    even = 0
    odd = 0
#for loop through my function list
    for i in num:
#if the number is even double the number
        if(i % 2 == 0):
            even = even + (int(i) / 2)
# for the odd numbers return double the number
        elif(i % 2 != 0):
            odd = odd + (int(i) * 2)
            result = odd + even
#return sum of the odd and even
    return result

print super_sum(numbers)