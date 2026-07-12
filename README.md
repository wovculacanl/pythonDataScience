# Homework: Python Basics Module 3

This repository contains a set of scripts completed as part of a hands-on project to learn the basics of Python. The project consists of 4 separate tasks that demonstrate working with built-in modules, exception handling, and user interaction.

## Project structure

- `task_01.py` — Calculate the number of days between a given date and the current date.
- `task_02.py` — Calculate the number of days between a given date and the current date.



## Detailed task description

### Task 1: Calculating days from a given date (`task_01.py`)

The script contains the function `get_days_from_today(date)`, which calculates the number of days between the user-entered date and today.

**main characteristics:**
* **Input data:** A string in the format `YYYY-MM-DD` (for example, `2026-10-09`).
* **Output:** Integer (number of days). If the date entered is in the future, a negative number is returned.
* **Error handling:** A check for the correct format of the entered date has been implemented using the `try/except` block. In case of incorrect input, the program does not "crash", but prompts the user to try again.
* **Modules used:** `datetime`.

**Example of use:**
```bash
Введіть дату в форматі 'РРРР-ММ-ДД': 2021-05-05
Різниця у днях складає: 1894
```



### Task 2: Lottery ticket number generator (`task_02.py`)

The script contains the function `get_numbers_ticket(min, max, quantity)`, which generates a set of unique random numbers for a lottery ticket within a specified range.

**main characteristics:**
* **Input data:** Three integers: `min` (minimum possible number, not less than 1), `max` (maximum possible number, not more than 1000), and `quantity` (amount of numbers to select).
* **Error handling:** Built-in validation ensures that the parameters fall within the allowed limits and that the requested `quantity` does not exceed the available range `(max - min + 1)`.
* **Modules used:** `random`.

**Test usage of the function:**
```python
lottery_numbers = get_numbers_ticket(1, 36, 6)
print("Ваші лотерейні числа:", lottery_numbers)
```
```bash
Ваші лотерейні числа: [4, 15, 23, 28, 37, 45]
```

### Task 3: Normalizing phone numbers (`task_03.py`)

The script contains the function `normalize_phone(phone_number)`, which sanitizes and normalizes phone numbers from various formats into a standard format required for SMS campaigns.

**Main characteristics:**
* **Input data:** A string representing a phone number in any format (e.g., `"    +38(050)123-32-34"` or `"0503451234"`).
* **Output:** A string containing the normalized phone number, consisting only of digits and a `+` symbol at the beginning. The standard international code `+38` (for Ukraine) is automatically added if missing.
* **Data processing:** The function utilizes the `re` (regular expressions) module to efficiently strip out all irrelevant characters such as spaces, hyphens, brackets, and invisible whitespace (like `\t` or `\n`).
* **Modules used:** `re`.

**Example of use:**
```python
raw_number = "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   "
sanitized_number = normalize_phone(raw_number)
print(sanitized_number)
```

```bash
Нормалізовані номери телефонів для SMS-розсилки: ['+380671234567', '+380952345678', '+380441234567', '+380501234567', '+380501233234', '+380503451234', '+380508889900', '+380501112222', '+380501112211']
```