SALARY = 5000  # Ежемесячная зарплата
SPEND = 6000  # Траты за первый месяц
MONTHS = 10  # Количество месяцев, которое планируется протянуть без долгов
INCREASE = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
money_capital = 0
current_spend = SPEND

for month in range(MONTHS):
    if month > 0:  # Увеличение расходов на 3% с второго месяца
        current_spend *= (1 + INCREASE)
    # Расчет необходимой суммы из подушки безопасности
    needed_from_capital = current_spend - SALARY
    # Обновление подушки безопасности
    money_capital += needed_from_capital

print(f"Подушка безопасности, чтобы протянуть {MONTHS} месяцев без долгов:", int(money_capital))
