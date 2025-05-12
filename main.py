import time

def print_pause(message, delay=1):
    print(message)
    time.sleep(delay)

def intro():
    print_pause("Ты стоишь перед древним храмом, затерянным в джунглях.")
    print_pause("Говорят, внутри спрятано сокровище, но путь к нему опасен...")
    print_pause("Ты решаешь войти...")

def make_choice(question, options):
    print_pause(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    while True:
        choice = input("Выбери номер (1-3): ")
        if choice in ["1", "2", "3"]:
            return int(choice)
        print("Нужно ввести 1, 2 или 3!")

def play_game():
    intro()
    
    # Первый выбор
    choice = make_choice(
        "\nПеред тобой три двери. Куда пойдешь?",
        ["Левая — покрыта странными символами.", "Центральная — выглядит надежно.", "Правая — из нее дует холодный ветер."]
    )
    
    if choice == 1:
        print_pause("\nТы вошел в комнату с древними письменами.")
        print_pause("На стене написано: 'Только мудрый найдет выход'.")
        print_pause("Ты пытаешься разгадать загадку, но ничего не понимаешь...")
        print_pause("Внезапно стены начинают сдвигаться! Ты погибаешь...")
        print_pause("Игра окончена. Попробуй еще раз!")
        return
    
    elif choice == 2:
        print_pause("\nТы входишь в просторный зал.")
        print_pause("Посередине стоит сундук. Открыть его?")
        
        second_choice = make_choice(
            "Что будешь делать?",
            ["Открыть сундук.", "Осмотреться вокруг.", "Уйти обратно."]
        )
        
        if second_choice == 1:
            print_pause("\nТы открываешь сундук...")
            print_pause("Внутри сверкает золото и драгоценные камни!")
            print_pause("Ты нашел сокровище! Победа!")
        elif second_choice == 2:
            print_pause("\nТы замечаешь скрытый механизм в стене.")
            print_pause("Нажимаешь на него — пол под тобой проваливается!")
            print_pause("Ты падаешь в бездну... Игра окончена.")
        else:
            print_pause("\nТы решаешь не рисковать и уходишь.")
            print_pause("Сокровище так и осталось ненайденным...")
    
    elif choice == 3:
        print_pause("\nТы входишь в ледяную пещеру.")
        print_pause("Перед тобой замерзшее озеро. Перейти по льду?")
        
        third_choice = make_choice(
            "Как поступишь?",
            ["Идти по льду.", "Искать обходной путь.", "Вернуться назад."]
        )
        
        if third_choice == 1:
            print_pause("\nЛед трескается! Ты проваливаешься в ледяную воду...")
            print_pause("Игра окончена.")
        elif third_choice == 2:
            print_pause("\nТы находишь узкий проход за сталактитами.")
            print_pause("Он ведет к потайной комнате с сокровищами!")
            print_pause("Ты победил!")
        else:
            print_pause("\nТы возвращаешься в главный зал.")
            print_pause("Но двери уже закрыты... Ты заперт навеки!")

# Запуск игры
play_game()