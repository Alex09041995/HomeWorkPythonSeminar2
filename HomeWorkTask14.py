print("Данный код выводит все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.")

n = int(input('Введите число: '))
m = 1
flag = True

while flag:
        if(m < n):
            if (m * 2 > n):
                flag = False
            else:
                m = m * 2
                print(m)
