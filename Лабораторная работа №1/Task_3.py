players = ["Антон", "Максим", "Андрей", "Матвей", "Александр",
            "Арсений", "Кирилл", "Павел", "Иван", "Евгений", "Марк", "Дмитрий", "Владислав",
           "Константин", "Валерий", "Акакий"]

count_players = len(players)

print(f"\nОбщее количество игроков = {count_players}\n")

middle_CP = count_players // 2

print(f"Команда 1: {players[:middle_CP]}\nКоманда 2: {players[middle_CP:]}")