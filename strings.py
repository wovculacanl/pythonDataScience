s = "Hello world!"
print(s[0])# H
print(s[-1])# !

# s = "Hello world!"
# s[0] = "Q"# Тут буде викликано виняток (помилка) TypeError

# upper
s = "Hello world!"
print(s.upper())  # HELLO WORLD!

# lower
s = "Some Text"
print(s.lower())  # Виведе 'some text'
 
# startswith
s = "Bill Jons"
print(s.startswith("Bi"))  # Виведе True

# endswith
s = "hello.jpg"
print(s.endswith("jpg"))  # Виведе True

# capitalize
s = "hello world".capitalize()  # Результат: "Hello world"

# title
s = "hello world".title()  # Результат: "Hello World"

"123".isdigit()  # True
"hello".isalpha()  # True
" ".isspace()  # True

# format

name = 'John'
print('Hello, {}!'.format(name))

# Форматування з декількома аргументами
age = 25
print('Hello, {}. You are {} years old.'.format(name, age))

# Використання іменованих аргументів
print('Hello, {name}. You are {age} years old.'.format(name='Jane', age=30))

# Використання індексів для вказівки порядку аргументів
print('Hello, {1}. You are {0} years old.'.format(age, name))


