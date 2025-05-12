import random
import time

def print_pause(message, delay=1):
    print(message)
    time.sleep(delay)

def ask_question(question, answer_func, player_asking, player_answering):
    print_pause(f"\n{player_asking} задает вопрос {player_answering}:")
    print_pause(question)
    user_answer = input("Введи ответ: ")
    return answer_func(user_answer)

# Вопрос 1: Степенная сумма (n² + n³ + n⁴)
def power_sum_answer(answer):
    try:
        n = int(answer)
        return n**2 + n**3 + n**4
    except ValueError:
        return None

# Вопрос 2: Фильтрация чисел до первого отрицательного
def filter_positive_numbers(answer):
    try:
        numbers = list(map(int, answer.split()))
        filtered = []
        for num in numbers:
            if num >= 0:
                filtered.append(num)
            else:
                break
        return filtered
    except ValueError:
        return None

# Вопрос 3: Приближение дроби к 9.75
def fraction_approximation(answer):
    try:
        numerator, denominator = map(int, answer.split('/'))
        approx = numerator / denominator
        return abs(approx - 9.75) < 0.01  # Проверка с округлением
    except (ValueError, ZeroDivisionError):
        return None

# Вопрос 4: Форматирование времени (минуты → дни:часы:минуты)
def format_time(answer):
    try:
        total_minutes = int(answer)
        days = total_minutes // 1440
        remaining = total_minutes % 1440
        hours = remaining // 60
        minutes = remaining % 60
        return f"{days}:{hours}:{minutes}"
    except ValueError:
        return None

# Вопрос 5: Проверка делимости на 5
def check_divisibility(answer):
    try:
        number = int(answer)
        return number % 5 == 0
    except ValueError:
        return None

# Вопрос 6: Конвертация км ↔ мили
def km_to_miles(answer):
    try:
        km = float(answer)
        miles = km * 0.621371
        return f"{km} км = {miles:.2f} миль"
    except ValueError:
        return None

def miles_to_km(answer):
    try:
        miles = float(answer)
        km = miles / 0.621371
        return f"{miles} миль = {km:.2f} км"
    except ValueError:
        return None

def play_game():
    player1 = input("Имя первого игрока: ")
    player2 = input("Имя второго игрока: ")
    score1, score2 = 0, 0

    print_pause(f"\n{player1} vs {player2}! Начинаем игру!")

    # Раунд 1: Степенная сумма
    n = random.randint(1, 5)
    question1 = f"Какая сумма {n}² + {n}³ + {n}⁴?"
    correct_answer1 = n**2 + n**3 + n**4
    user_answer1 = ask_question(question1, lambda x: int(x) if x.isdigit() else None, player1, player2)
    if user_answer1 == correct_answer1:
        print_pause(f"Верно! {player2} получает 1 очко.")
        score2 += 1
    else:
        print_pause(f"Неверно! Правильный ответ: {correct_answer1}")

    # Раунд 2: Фильтрация чисел
    question2 = "Введи список чисел через пробел (напр., '3 1 -2 5'). Выведи все положительные до первого отрицательного."
    sample_list = " ".join(map(str, [random.randint(-5, 5) for _ in range(4)]))
    print_pause(f"Пример: {sample_list}")
    user_answer2 = ask_question(question2, filter_positive_numbers, player2, player1)
    if user_answer2 is not None:
        print_pause(f"Твой ответ: {user_answer2}")
        # Проверка вручную, так как правильный ответ зависит от ввода
        print_pause(f"{player1}, проверь ответ {player2} и скажи, верно ли (да/нет).")
        if input().lower() == "да":
            score1 += 1
    else:
        print_pause("Ошибка формата!")

    # Раунд 3: Дробь к 9.75
    question3 = "Найди дробь вида a/b, приближенную к 9.75 (например, 39/4). Введи в формате 'a/b'."
    user_answer3 = ask_question(question3, fraction_approximation, player2, player1)
    if user_answer3:
        print_pause(f"Верно! 9.75 ≈ {user_answer3}")
        score1 += 1
    else:
        print_pause("Неверный формат или ответ!")

    # Раунд 4: Форматирование времени
    minutes = random.randint(100, 10000)
    question4 = f"Переведи {minutes} минут в 'дни:часы:минуты'."
    user_answer4 = ask_question(question4, format_time, player1, player2)
    correct_answer4 = f"{minutes // 1440}:{(minutes % 1440) // 60}:{minutes % 60}"
    if user_answer4 == correct_answer4:
        print_pause(f"Верно! {player2} получает 1 очко.")
        score2 += 1
    else:
        print_pause(f"Неверно! Правильно: {correct_answer4}")

    # Раунд 5: Делимость на 5
    number = random.randint(1, 100)
    question5 = f"Делится ли {number} на 5 без остатка? (да/нет)"
    user_answer5 = ask_question(question5, lambda x: x.lower(), player2, player1)
    correct_answer5 = "да" if number % 5 == 0 else "нет"
    if user_answer5 == correct_answer5:
        print_pause("Верно!")
        score1 += 1
    else:
        print_pause(f"Неверно! Ответ: {correct_answer5}")

    # Раунд 6: Конвертация км ↔ мили
    km = round(random.uniform(1, 10), 2)
    question6 = f"Переведи {km} км в мили (округли до 2 знаков)."
    user_answer6 = ask_question(question6, km_to_miles, player1, player2)
    miles = km * 0.621371
    if user_answer6 and abs(float(user_answer6.split()[-2]) - miles) < 0.01:
        print_pause(f"Верно! {player2} получает 1 очко.")
        score2 += 1
    else:
        print_pause(f"Неверно! Правильно: {km} км = {miles:.2f} миль")

    # Итог
    print_pause("\n=== Результаты ===")
    print_pause(f"{player1}: {score1} очков")
    print_pause(f"{player2}: {score2} очков")
    if score1 > score2:
        print_pause(f"Победил {player1}!")
    elif score2 > score1:
        print_pause(f"Победил {player2}!")
    else:
        print_pause("Ничья!")

# Запуск игры
play_game()