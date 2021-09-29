# Task_1_c

duration = int(input('Введите интервал в секундах '))
hour = (duration // (60 * 60))
minutes = (duration // 60 % 60)
seconds = duration % 60
print('Ответ:', hour, 'час', minutes, 'мин', seconds, 'сек')
