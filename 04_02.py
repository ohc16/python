# Представлен список чисел. Необходимо вывести элементы
# исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить
# в виде списка. Для формирования списка использовать генератор.

from random import randint

my_list = [randint(0, 100) for _ in range(0, randint(2, 20))]
my_new_list = [num for i, num in enumerate(my_list[1:]) if num > my_list[i]]
print(f'Исходный список {my_list}')
print(f'Новый список {my_new_list}')
