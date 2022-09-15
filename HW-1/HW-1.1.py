import math 

def root_calculation(a,b,c):
    if a == 0:
        return 'The equation is not square'
    
    discr = b**2 - 4*a*c
    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2*a)
        x2 = (-b - math.sqrt(discr)) / (2*a)
        return x1, x2
    elif discr == 0:
        x = -b / (2 * a)
        return x,
    else:
        return None
   
assert(root_calculation(2,10,4)) 
assert(root_calculation(2,0,0))
assert(root_calculation(0,0,0))
print('OK')

