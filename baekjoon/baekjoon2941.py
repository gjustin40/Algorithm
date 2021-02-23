croatia_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
string = input()
count = 0

for cro in croatia_alpha:
    count += string.count(cro)
    string = string.replace(cro, ' ')
    
string = string.replace(' ', '')
count += len(string)
print(count)
