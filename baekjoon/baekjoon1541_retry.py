form_list = input().split('-')

result = 0
for i, form in enumerate(form_list):
    if i == 0:
        result = sum(map(int, form.split('+')))
    else:
        result -= sum(map(int, form.split('+')))
print(result)
