# Given two arrays a and b of numbers and a target value t, find a number from each array whose sum is closest to t.
# Example: a=[9, 13, 1, 8, 12, 4, 0, 5],  b=[3, 17, 4, 14, 6],  t=20  ⇒  [13, 6] or [4, 17] or [5, 14]

def closest_sum(a, b, t):
    closest = float('inf')
    result = None
    
    for i in range(len(a)):
        for j in range(len(b)):
            sum = a[i] + b[j]
            if abs(sum - t) < closest:
                closest = abs(sum - t)
                result = [a[i], b[j]]
    
    return result

a = [9, 13, 1, 8, 12, 4, 0, 5]
b = [3, 17, 4, 14, 6]
t = 20

result = closest_sum(a, b, t)
print(result)