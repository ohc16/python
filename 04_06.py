#Реализовать два небольших скрипта:
#а) бесконечный итератор, генерирующий целые числа,
#начиная с указанного,
#б) бесконечный итератор, повторяющий элементы
#некоторого списка, определенного заранее.
#Подсказка: использовать функцию count() и cycle()
#модуля itertools.


from itertools import count, cycle

my_count = count(7)
my_cycle = cycle("ABC")

for _ in range(5):
    print("(my_count, my_cycle) = ({},{})".format(next(my_count), next(my_cycle)))

