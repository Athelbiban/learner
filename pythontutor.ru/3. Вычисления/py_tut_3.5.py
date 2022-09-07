"""
Задача «Конец уроков»
Условие
В некоторой школе занятия начинаются в 9:00. Продолжительность урока — 45 минут,
после 1-го, 3-го, 5-го и т.д. уроков перемена 5 минут, а после 2-го, 4-го, 6-го и т.д. — 15 минут.

Дан номер урока (число от 1 до 10). Определите, когда заканчивается указанный урок.

Выведите два целых числа: время окончания урока в часах и минутах.
"""


number_lesson = int(input())
start_hour = 9
lesson_time = 45
timeout_1 = 5
timeout_2 = 15

if number_lesson % 2 == 0:
    m1 = lesson_time * number_lesson + number_lesson // 2 * timeout_1 + (number_lesson // 2 - 1) * timeout_2
    h = start_hour + m1 // 60
    m = m1 % 60
else:
    m1 = lesson_time * number_lesson + number_lesson // 2 * timeout_1 + number_lesson // 2 * timeout_2
    h = start_hour + m1 // 60
    m = m1 % 60

print(h)
print(m)
