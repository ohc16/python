'''
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и dict.
'''

list_season = ("зима", "весна", "лето", "осень")
season_dict = {1: "зима", 2: "весна", 3: "лето", 4: "осень"}
month = int(input("Введите месяц по номеру: "))
while True:
    if month <= 0 or month > 13:
        print("Такого месяца не существует. Значения должны быть от 1 до 12.")
        month = int(input("Введите месяц по номеру: "))
    if month == 1 or month == 12 or month == 2:
        print(season_dict.get(1))
        print(list_season[0])
    elif month == 3 or month == 4 or month == 5:
        print(season_dict.get(2))
        print(list_season[1])
    elif month == 6 or month == 7 or month == 8:
        print(season_dict.get(3))
        print(list_season[2])
    elif month == 9 or month == 10 or month == 11:
        print(season_dict.get(4))
        print(list_season[3])
    break
