print("Данный код определяет какие Петя задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого есть две подсказки: сумма этих чисел S и их произведение P.")

S = int(input('Введите сумму чисел: '))
P = int(input('Введите произведение чисел: '))

X = (S - int((S ** 2- 4 * P) ** 0.5)) // 2
Y = S - X
if X <= 1000 and Y <= 1000:

    print('Петя задумал другие числа.')
print(f'Числа, которые загадал Петя: {X, Y}')
