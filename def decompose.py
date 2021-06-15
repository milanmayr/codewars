def decompose(n):
    from math import sqrt, floor
    result = []
    total = n ** 2
    
    result.append(floor(sqrt(total-1)))
    total -= floor(sqrt(total-1)) ** 2
        
    while total >= 1:
        next = floor(sqrt(total))
        while floor(sqrt(total - next ** 2)) < 2 and floor(sqrt(total - next ** 2)) > 0:
            next -= 1
        result.append(next)
        total -= next ** 2
    
    result.reverse()
    
    if result.count(1) > 1:
        return None
    else:
        return result

print(decompose(4622188))