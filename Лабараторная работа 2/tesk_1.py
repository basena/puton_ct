money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
coll_mess=0
while salary+money_capital-spend>=0:
    coll_mess=coll_mess+1
    money_capital=money_capital+salary-spend
    spend=spend+spend*increase


print("Количество месяцев, которое можно протянуть без долгов:", coll_mess)
