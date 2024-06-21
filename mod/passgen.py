import string
import random

def passgen():
    while True:
        try:
            length = int(input("Введите длину пароля (1-100): "))
            if length < 1 or length > 100:
                raise ValueError("Длина пароля должна быть от 1 до 100 символов")

            include_uppercase = input("Включать заглавные буквы? (да/нет) ").lower() == "да"
            include_lowercase = input("Включать строчные буквы? (да/нет) ").lower() == "да"
            include_digits = input("Включать цифры? (да/нет) ").lower() == "да"
            include_special_chars = input("Включать специальные символы? (да/нет) ").lower() == "да"

            exclude_chars = input("Введите символы, которые нужно исключить из пароля (Enter для пропуска): ")

            uppercase_chars = string.ascii_uppercase
            lowercase_chars = string.ascii_lowercase
            digit_chars = string.digits
            special_chars = string.punctuation

            char_set = ""
            if include_uppercase:
                char_set += uppercase_chars
            if include_lowercase:
                char_set += lowercase_chars
            if include_digits:
                char_set += digit_chars
            if include_special_chars:
                char_set += special_chars

            if exclude_chars:
                char_set = "".join(c for c in char_set if c not in exclude_chars)
            else:
                char_set = "".join(char_set)

            if not char_set:
                raise ValueError("Необходимо включить хотя бы один тип символов")

            password = "".join(random.choice(char_set) for _ in range(length))
            print(f"Сгенерированный пароль: {password}")
            return password
        except ValueError as e:
            print(f"Ошибка: {e}")
            print("Попробуйте еще раз.")