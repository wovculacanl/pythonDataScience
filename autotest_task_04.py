'''
Задачі:

1 - Запросіть користувача ввести ціле число від 0 до 100. Збережіть це число в змінній num.
2 - Використовуйте цикл while для підрахунку суми всіх чисел від 1 до введеного числа включно.
3 - Збережіть результат у змінній sum.

Очікуваний результат:

Програма має вирахувати суму всіх чисел від 1 до num включно і зберегти цю суму в змінній sum.

Підказки:

Ініціалізуйте змінну sum значенням 0 перед початком циклу.
В циклі while зменшуйте значення num на 1 після кожного додавання до sum.
Використовуйте цикл while, який продовжується допоки num більше або дорівнює 0.
Тести:

При введеному числі 20, очікувана сума в змінній sum має бути 210.
При введеному числі 10, очікувана сума в змінній sum має бути 55.
При введеному числі 5, очікувана сума в змінній sum має бути 15.
При введеному числі 100, очікувана сума в змінній sum має бути 5050.
'''

num = int(input("Enter the integer (0 to 100): "))

sum_of_numbers = 0

while num >= 0:
    sum_of_numbers += num
    num -= 1
print(sum_of_numbers)

# Динамічний assert, який підлаштовується під те, що ввів користувач
# initial_num = num
# if initial_num == 20:
#     assert sum_of_numbers == 210
# elif initial_num == 10:
#     assert sum_of_numbers == 55
# elif initial_num == 5:
#     assert sum_of_numbers == 15
# elif initial_num == 100:
#     assert sum_of_numbers == 5050



# def calculate_sum(num):
#     sum_of_numbers = 0
#     while num >= 0:
#         sum_of_numbers     += num
#         num -= 1
#     return sum_of_numbers

# print(calculate_sum(num))

# assert calculate_sum(20) == 210
# assert calculate_sum(10) == 55
# assert calculate_sum(5) == 15
# assert calculate_sum(100) == 5050