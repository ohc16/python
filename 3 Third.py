# 3. Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
n = int(input("Введите значение числа n:"))
n1 = n
n2 = int(str(n) + str(n))
n3 = int(str(n) + str(n)+ str(n))
summ = n1 + n2 + n3
print("У нас получается {}+{}+{}={}".format(n1, n2, n3, summ))
