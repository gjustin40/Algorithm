x = int(input())
n = 1
n_sum = 0
while True:
    n_sum += n
    
    if n_sum >= x:
        break
        
    else:
        n += 1
        
n_sum = n_sum - n
rest = x - n_sum

if n%2 == 0:
    son = rest
    mom = n - rest + 1
    
else:
    son = n - rest + 1
    mom = rest
    
print("{}/{}".format(son, mom))
