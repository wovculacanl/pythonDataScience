
'''

Перше завдання

Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.

Вимоги до завдання:

1 - Функція приймає один параметр: date — рядок, що представляє дату у форматі 'РРРР-ММ-ДД' (наприклад, '2020-10-09').
2 - Функція повертає ціле число, яке вказує на кількість днів від заданої дати до поточної. Якщо задана дата пізніша за поточну, результат має бути від'ємним.
3 - У розрахунках необхідно враховувати лише дні, ігноруючи час (години, хвилини, секунди).
4 - Для роботи з датами слід використовувати модуль datetime Python.


Рекомендації для виконання:

1 - Імпортуйте модуль datetime.
2 - Перетворіть рядок дати у форматі 'РРРР-ММ-ДД' у об'єкт datetime.
3 - Отримайте поточну дату, використовуючи datetime.today().
4 - Розрахуйте різницю між поточною датою та заданою датою.
5 - Поверніть різницю у днях як ціле число.


Критерії оцінювання:

Коректність роботи функції: функція повинна точно обраховувати кількість днів між датами.
Обробка винятків: функція має впоратися з неправильним форматом вхідних даних.
Читабельність коду: код повинен бути чистим і добре документованим.


'''
import datetime

user_input = input("Введіть дату в форматі 'РРРР-ММ-ДД': ")

# --- Main function block ---

def get_days_from_today(date: str) -> int | None:
    '''
    Calculates the number of days between a given date and the current date.
    Returns an integer number of days, or None if the date format is invalid.

    '''
    try:

        # Convert user input to a datetime.date object and calculate the difference in days
        
        target_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        today = datetime.date.today()
        difference = today - target_date  # According to the condition — if the given date is later than the current date, the result must be negative.
        return difference.days
        
        # If the date format is invalid, a ValueError is raised, and the function returns None and the code continues execution

    except ValueError:
        return None 

# --- User interaction block ---

while True:

    # To re-ask the user for the date if the date format is incorrect

    result = get_days_from_today(user_input)
    
    if result is not None:
        print(f"Різниця у днях складає: {result}")
        break
    else:
        print("Некоректний формат дати. Будь ласка, використовуйте формат 'РРРР-ММ-ДД'.")
        print("-" * 100)
        user_input = input("Введіть дату в форматі 'РРРР-ММ-ДД' щe раз: ")


