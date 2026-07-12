# Homework: Python Basics Module 3

This repository contains a set of scripts completed as part of a hands-on project to learn the basics of Python. The project consists of 4 separate tasks that demonstrate working with built-in modules, exception handling, and user interaction.

## Project structure

- `goit_algo_hw_03_task_01.py` — Calculate the number of days between a given date and the current date.


## Detailed task description

### Task 1: Calculating days from a given date (`goit_algo_hw_03_task_01.py`)

The script contains the function `get_days_from_today(date)`, which calculates the number of days between the user-entered date and today.

**main characteristics:**
* * **Input data:** A string in the format `YYYY-MM-DD` (for example, `2026-10-09`).
* **Output:** Integer (number of days). If the date entered is in the future, a negative number is returned.
* **Error handling:** A check for the correct format of the entered date has been implemented using the `try/except` block. In case of incorrect input, the program does not "crash", but prompts the user to try again.
* **Використані модулі:** `datetime`.

**Приклад використання:**
```bash
Введіть дату в форматі 'РРРР-ММ-ДД': 2021-05-05
Різниця у днях складає: 1894