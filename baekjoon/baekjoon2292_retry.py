N = int(input())
n = 0

while True:
    if N == 1:
        n = 1
        break
        
    elif 3*n**2 - 3*n + 2 > N:
        break
        
    else:
        n += 1
        
print(n)
## 나의 아이디어
## 계차수열로 풀었다...
## 근데 다른 사람들은 굳이 계차수열로 안 풀었더라구...
## 다시 풀어보자 나중에
