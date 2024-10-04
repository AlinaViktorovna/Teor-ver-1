# Задача 2.
# На входной двери подъезда установлен кодовый замок, содержащий десять кнопок с
# цифрами от 0 до 9. Код содержит три цифры, которые нужно нажать одновременно.
# Какова вероятность того, что человек, не знающий код, откроет дверь с первой
# попытки?

import math

buttons = 10
code_digits = 3

total_combinations = math.comb (buttons, code_digits)
probability_first_try = 1/ total_combinations

print (f"Вероятность угадать код с первой попытки {probability_first_try: .5f}")
