#Recursive function to return gcd of a and b
def gcd(a,b):
    if a == 0:
        return b
    return gcd(b % a, a)

# Function to return LCM of two numbers
def lcm(a,b):
    return (a // gcd(a,b))* b

a = 15 
b = 20
print('LCM of', a, 'and', b, 'is', lcm(a, b))
print('GCD of',a,'and',b,'is',gcd(a,b))
