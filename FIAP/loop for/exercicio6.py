max = 0
min = 0

'''#for i in range(10):
    num = int(input(f"Informe o {i+1}º numero ai: "))'''

for i in range(1,11):
    num = int(input(f"Informe o {i}º numero ai: "))
    if num > max:
        max = num
    elif num < min:
        min = num
print(f"O maior digitado é {max}\nO menor digitado foi {min}.")

