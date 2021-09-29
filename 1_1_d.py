# Task_1_d

duration = int(input('Введите интервал в секундах '))
day = (duration // (24 * 60 * 60))
hour = (duration // (60 * 60) - 24 * day)
minutes = (duration // 60 % 60)
seconds = duration % 60
print('Ответ:', day, 'дн', hour, 'час', minutes, 'мин', seconds, 'сек')
