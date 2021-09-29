# Task_3

def declination(num):
    variant_1 = 'Процент'
    variant_2 = 'Процента'
    variant_3 = 'Процентов'
    numbs = {11, 12, 13, 14}
    if num in numbs:
        return str(num) + variant_3
    rem = num % 10
    if rem == 1:
        return str(num) + variant_1
    elif 1 < rem < 5:
        return str(num) + variant_2
    else:
        return str(num) + variant_3


for i in range(1, 101):
    print(declination(i))
