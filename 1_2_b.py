# Task_2_b

def sum_of_digits(i):
    summa = 0
    while i:
        summa += i % 10
        i //= 10
    return summa


answer_summa_1 = 0
answer_summa_2 = 0
mass_of_cubes = [i ** 3 for i in range(1, 1001, 2)]
print(mass_of_cubes)
for num in mass_of_cubes:
    new_num = num + 17
    if sum_of_digits(num) % 7 == 0:
        answer_summa_1 += num
    if sum_of_digits(new_num) % 7 == 0:
        answer_summa_2 += num
print(answer_summa_1)
print(answer_summa_2)
