from Class5 import Time


def get_valid_time_from_user(prompt):
    while True:
        user_input = input(prompt).strip()

        if ":" not in user_input:
            print("Ошибка: строка должна содержать двоеточие (формат ЧЧ:ММ).")
            continue

        parts = user_input.split(':')
        if len(parts) != 2:
            print("Ошибка: формат должен быть строго ЧЧ:ММ (одно двоеточие).")
            continue

        try:
            h = int(parts[0])
            m = int(parts[1])
        except ValueError:
            print("Ошибка: часы и минуты должны быть целыми числами.")
            continue

        if not (0 <= h < 24) or not (0 <= m < 60):
            print("Ошибка: часы должны быть от 0 до 23, минуты от 0 до 59.")
            continue

        return user_input


string_t1 = get_valid_time_from_user("Введите время для t1 (ЧЧ:ММ): ")
string_t2 = get_valid_time_from_user("Введите время для t2 (ЧЧ:ММ): ")

t1 = Time(string_t1)
t2 = Time(string_t2)

result_time = t1.subtract_time(t2)
print(f"\nsubtract_time: {result_time}")

print(f"int: {int(result_time)}")
print(f"bool: {bool(result_time)}")


while True:
    try:
        sub_mins = int(input("Введите минуты для вычитания: "))
        if sub_mins < 0:
            print("Введите положительное число.")
            continue
        break
    except ValueError:
        print("Неверное значение")

print(f"{result_time} - {sub_mins} мин: {result_time - sub_mins}")
print(f"t1({t1}) + t2({t2}): {t1 + t2}")