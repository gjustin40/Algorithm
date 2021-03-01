
n = int(input())

room = 1
n_sum = 1

while True:
    
    if n_sum >= n:
        break
        
    else:
        
        n_sum += 6*room
        room += 1

print(room)
