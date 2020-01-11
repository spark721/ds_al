
# [3, 5, 12, 5, 13] # => True


def findPythagoreanTriplets(nums):
    """
    Takes in a list and return boolean 
    if it contains pythagorean triplets.
    """
    for a in nums:
        for b in nums:
            for c in nums:
                if a*a + b*b == c*c:
                    return True
    return False

def findPythagoreanTriplets2(nums):
    """
    Takes in a list and return boolean 
    if it contains pythagorean triplets.
    """
    squares = set([n*n for n in nums])

    for a in nums:
        for b in nums:
            if a * a + b * b in squares:
                return True
    return False


li = [3, 5, 12, 5, 13]
print(findPythagoreanTriplets2(li))
