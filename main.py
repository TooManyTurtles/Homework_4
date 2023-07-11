# 1. Користувач вводить рядок з клавіатури. Порахуйте кількість літер, цифр у рядку.
# Виведіть обидві кількості на екран. (використовувати цикл)
# 2. Користувач вводить з клавіатури рядок та символ для пошуку.
# Порахуйте скільки разів у рядку зустрічається потрібний символ. Отримане число виведіть на екран.
# 3. Користувач вводить з клавіатури рядок, слово для пошуку, слово для заміни.
# Зробіть у рядку заміну одного слова на інше. Отриманий рядок на екрані.
# 4. Дано рядок. (зробити зрізи)
# - Спершу виведіть третій символ цього рядка.
# - У другому рядку виведіть передостанній символ цього рядка.
# - У третьому рядку виведіть перші п'ять символів цього рядка.
# - У четвертому рядку виведіть весь рядок, крім двох останніх символів.
# - У п'ятому рядку виведіть усі символи з парними індексами
# (вважаючи, що індексація починається з 0, тому символи виводяться з першого).
# - У шостому рядку виведіть усі символи з непарними індексами, тобто, починаючи з другого символу рядка.
# - У сьомому рядку виведіть усі символи у зворотному порядку.
# - У восьмому рядку виведіть усі символи рядка через один у зворотному порядку, починаючи з останнього.
# - У дев'ятому рядку виведіть довжину цього рядка.

# Додатково:
# Є певний текст. Реалізуйте наступну функціональність:
# ■ Змінити текст таким чином, щоб кожна пропозиція починалася з великої літери;
# ■ Порахуйте скільки разів цифри зустрічаються у тексті;
# ■ Порахуйте скільки разів розділові знаки зустрічаються в тексті;
# ■ Порахуйте кількість знаків оклику в тексті.

# 1. Користувач вводить рядок з клавіатури. Порахуйте кількість літер, цифр у рядку.
# Виведіть обидві кількості на екран. (використовувати цикл)
#
# try:
#     while True:
#         digit_count = 0
#         alpha_count = 0
#         sentence = input("Input any sentence: ")
#         for letter in sentence:
#             if letter.isdigit():
#                 digit_count += 1
#             elif letter.isalpha():
#                 alpha_count += 1
#         print("The number digit symbols is =", digit_count)
#         print("The number of alphabetical symbols is =", alpha_count)
#         break
# except Exception as random_error:
#     print(random_error)

# 2. Користувач вводить з клавіатури рядок та символ для пошуку.
# Порахуйте скільки разів у рядку зустрічається потрібний символ. Отримане число виведіть на екран.

# try:
#     while True:
#         digit_count = 0
#         alpha_count = 0
#         sentence = input("Input any sentence: ")
#         for letter in sentence:
#             if letter.isdigit():
#                 digit_count += 1
#             elif letter.isalpha():
#                 alpha_count += 1
#         print("The number digit symbols is =", digit_count)
#         print("The number of alphabetical symbols is =", alpha_count)
#         break
# except Exception as random_error:
#     print(random_error)


# 3. Користувач вводить з клавіатури рядок, слово для пошуку, слово для заміни.
# Зробіть у рядку заміну одного слова на інше. Отриманий рядок на екрані.

# try:
#     while True:
#         sentence = input("Input any sentence:")
#         word_to_find = input("Input word you want to find:")
#         word_to_change = input("Input word you change on:")
#
#         if sentence.find(word_to_find):
#             sentence = sentence.replace(word_to_find, word_to_change)
#             print(sentence)
#             break
#         else:
#             print("There is no such a word in sentence")
#             break
# except Exception as random_error:
#     print(random_error)

