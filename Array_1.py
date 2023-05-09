# problem 4:
# Given two arrays a and b of numbers and a target value t, find a number from each array whose sum is closest to t.
# Example: a=[9, 13, 1, 8, 12, 4, 0, 5],  b=[3, 17, 4, 14, 6],  t=20  ⇒  [13, 6] or [4, 17] or [5, 14]
# Time Complexity should be O(n)

def closest_sum(a, b, t):
    closest = float('inf')
    result = None
    hash_table = {}
    
    # populate hash table with values from first array
    for value in a:
        hash_table[value] = True
    
    # iterate over second array and find closest sum
    for value in b:
        complement = t - value
        if complement in hash_table:
            if abs(complement + value - t) < closest:
                closest = abs(complement + value - t)
                result = [complement, value]
    
    return result

def main():
    a = [9, 13, 1, 8, 12, 4, 0, 5]
    b = [3, 17, 4, 14, 6]
    t = 20
    print(closest_sum(a, b, t))

if __name__ == '__main__':
    main()
