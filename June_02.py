# VALID HEX CODE
# --------------------------------------------------------------------------------
# Create a function that determines whether a string is a valid hex code.
# A hex code must begin with a pound key # and is exactly 6 characters 
# in length. Each character must be a digit from 0-9 or an alphabetic character 
# from A-F. All alphabetic characters may be uppercase or lowercase.

def isValidHexCode(str):
    # Begins with '#'
    if(str[0] != '#'):
        return False
    # 6 characters in length
    if(not(len(str)) == 7):
        return False
    # 0-9, a-f, A-F
    for i in range(1, len(str)):
        if (not((str[i] >= '0' and str[i] <= '9') or (str[i] >= 'a' and str[i] <= 'f') or (str[i] >= 'A' or str[i] <= 'F'))):
            return False
    return True

if __name__ == "__main__":
    # Change to check
    str = "#CD5C58C"
    if(isValidHexCode(str)):
        # True
        print("Valid Hex Code")
    else:
        # False
        print("Not Valid Hex Code")

# RETURN NEXT PRIME
# --------------------------------------------------------------------------------
# Given an integer, create a function that returns the next prime. 
# If the number is prime, return the number itself.

def nextPrime(x):
    prime = x + 1
    for i in range(2, prime):
        if(prime % i == 0):
            prime = prime + 1
        else:
            print(prime)
x = int(input())
nextPrime(x)

# REORDER ARRAY
# --------------------------------------------------------------------------------
# Create a function that reorders the digits of each numerical element 
# in an array based on ascending (asc) or descending (desc) order.

# def reorderDigit(arr)
arr = [515, 341, 98, 44, 211]
# ASC
asc = arr.sort(reverse = False)
print(arr)
# DESC
desc = arr.sort(reverse = True)
print(arr)

# PARTITION ARRAY
# --------------------------------------------------------------------------------
# Write a function that returns true if you can partition an array into 
# one element and the rest, such that this element is equal 
# to the product of all other elements excluding itself.

# def canPartition(arr):


# ODDISH OR EVENISH
# --------------------------------------------------------------------------------
# Create a function that determines whether a number is Oddish or Evenish. 
# A number is Oddish if the sum of all of its digits is odd, 
# and a number is Evenish if the sum of all of its digits is even. 
# If a number is Oddish, return "Oddish". Otherwise, return "Evenish".

def oddishOrEvenish(x):
    if sum(map(int, str(x))) % 2:
        return 'Oddish'
    else:
        return 'Evenish'

print(oddishOrEvenish(43))


# REPLACE C1 W/ C2
# --------------------------------------------------------------------------------
# Write a function to replace all instances of 
# character c1 with character c2 and vice versa.

# def doubleSwap(str):
