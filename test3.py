money = int(input("Введите сумму:"))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
x=int((per_cent["ТКБ"])*(money/100))
x1=int((per_cent["СКБ"])*(money/100))
x2=int((per_cent["ВТБ"])*(money/100))
x3=int((per_cent["СБЕР"])*(money/100))
deposit = [x, x1, x2, x3]
print("Доход по депозиту:",deposit)
i = max(deposit)
print("Максимальная сумма, которую Вы можете заработать:",i)