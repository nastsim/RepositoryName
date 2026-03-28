salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Кол-во месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# Инициализация
total_cushion_needed = 0  # Общая сумма, нужная из подушки
current_spend = spend  # Текущие траты (начинаем с первого месяца)

# Расчет для каждого месяца
for month in range(1, months + 1):
    # Сколько нужно доплатить из подушки в этом месяце
    cushion_needed_this_month = current_spend - salary

    # Если зарплаты достаточно - доплата 0, иначе добавляем недостающую сумму
    if cushion_needed_this_month > 0:
        total_cushion_needed += cushion_needed_this_month

    # Увеличиваем траты на следующий месяц
    current_spend *= (1 + increase)

# Округляем до целого числа
money_capital = round(total_cushion_needed)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
