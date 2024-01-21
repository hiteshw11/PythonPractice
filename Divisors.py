# Find Divisor Of A Number

#13 is a divisor of 26 because 26 / 13 has no remainder.

abc=int(input('Enter The Number '))
divisors=[]


for i in range(1,abc+1):
    if abc%i==0:
        divisors.append(i)

print(f'The Divisors of number {abc} are ')
print(divisors)