def solution(col, row, puddles):
    result = []
    
    for i in range(row+1):
        if i == row:
            result.append([1]*(col+1))    
        else:
            result.append([0]*(col) + [1])
            
    for puddle in puddles:
        c, r = puddle
       
        if r == row:
            for j in range(1,c+1):
                result[r][j] = 0
                
        if c == col:
            for k in range(1, r+1):
                result[k][c] = 0
            
    for r in range(row, 0, -1):
        for c in range(col, 0, -1):
            coor = [c-1, r-1]
            
            if coor in puddles:
                result[r-1][c-1] = 0
                
            else:
                result[r-1][c-1] = result[r][c-1] + result[r-1][c]
                   
    return result[1][1] % 1000000007

# 1. 먼저 빈 깡통 만들고(array)
# 2. 맨 오른쪽과 아래는 1로 통일
# 3. 맨 오른쪽과 아래에서 1개라도 0이면 그 전 경로도 전부 0임
# 4. 집에서부터 계산해도 되는데 굳이 반대로 함(멍청이였네...)
# 5. 점화식 d[r-1, c-1] = d[r][c-1] + d[r-1][c]
