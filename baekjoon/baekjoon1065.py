n = int(input())

def nums(x):
    if x < 100:
        return x
    
    elif x>=100:
        num = 99
        for i in range(100,x+1):
            
            x_str = str(i)
        
            sub1 = int(x_str[0]) - int(x_str[1])
            sub2 = int(x_str[1]) - int(x_str[2])
        
            if sub1==sub2:
                num += 1
        return num
    
num = nums(n)
print(num)
