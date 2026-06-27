'''
Задачі:

Введіть кількість балів, які кандидат набрав у тесті, через функцію input та збережіть їх у змінній num як ціле число.
Використовуйте оператор контролю виконання if-else, щоб визначити, чи проходить кандидат до наступного туру. Якщо num більше або дорівнює 83, змінній is_next привласніть значення True. В іншому випадку привласніть їй значення False.
Очікуваний результат:

Програма повинна отримати кількість балів, набраних кандидатом, та вивести, чи проходить кандидат до наступного туру.

Підказки:

Використовуйте int() для перетворення рядкового введення в ціле число.
Умовний оператор if-else допомагає визначити, яку дію потрібно виконати, залежно від виконання умови.

'''

def check_pass(num):
    if num >= 83:
        return True
    else:
        return False

# Tests
assert check_pass(83) is True
assert check_pass(82) is False
assert check_pass(95) is True
assert check_pass(32) is False


user_input = int(input("Enter the number of points: "))
is_next = check_pass(user_input)
print("Does the candidate pass to the next round?", is_next)