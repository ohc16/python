#3. Реализовать функцию my_func(), которая принимает три
# позиционных аргумента и возвращает сумму наибольших двух аргументов.

def my_func(arg1 , arg2, arg3):
    my_list = [arg1, arg2, arg3]
    try:
        my_list.remove(min(my_list))
    except TypeError or ValueError or NameError:  #не понимаю почему не срабатывает
        return "Вводите только числа!"
    return sum(my_list)

print(f'Cумма наибольших двух аргументов - {my_func(int(input("Введите первый аргумент: ")), int(input("Введите второй аргумент: ")), int(input("Введите третий аргумент: ")))}')