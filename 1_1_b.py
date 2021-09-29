# Task_1_b

duration = int(input('Введите интервал в секундах '))
minutes = (duration // 60 % 60)
seconds = duration % 60
print('Ответ:', minutes, 'мин', seconds, 'сек')
