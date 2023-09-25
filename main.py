print("Пройди викторину о видеоиграх")
score = 0
questions = ["1. Какая игра считается самой продаваемой в истории?",
             "2. Какой персонаж является главным героем серии игр \"The Legend of Zelda?\"",
             "3. Какая игра стала первой в истории, в которую можно было играть онлайн?",
             "4. Какой жанр игр является самым популярным?",
             "5. Какая игра считается первой в истории видеоигр?",
             "6. Какая компания разработала игры серии \"Assassin's Creed\"?",
             "7. Какая игра стала первой в истории, получившей статус \"эксклюзива\" для консоли PlayStation 4?",
             "8. Какой персонаж является главным героем серии игр \"Super Mario\"?",
             "9. Какая игра стала первой в истории, получившей статус \"эксклюзива\" для консоли Xbox One?",
             "10. Какая игра считается самой популярной в жанре шутеров от первого лица?"]
answers = ["Minecraft", "Линк", "Ultima Online", "Экшен", "Pong", "Ubisoft", "Bloodborne", "Марио", "Ryse: Son of Rome",
           "Call of Duty: Modern Warfare"]

print(questions[0])
user_answer = input("Введите свой ответ: ")
if user_answer.lower() == answers[0].lower():
    score = score + 1
    print("Правильно")
else:
    print("Неправильно")

print(questions[1])
user_answer = input("Введите свой ответ: ")
if user_answer == answers[1]:
    score = score + 1
    print("Правильно")
else:
    print("Неправильно")

print(questions[2])
user_answer = input("Введите свой ответ: ")
if user_answer == answers[2]:
    score = score + 1
    print("Правильно")
else:
    print("Неправильно")

print(questions[3])
user_answer = input("Введите свой ответ: ")
if user_answer == answers[3]:
    score = score + 1
    print("Правильно")
else:
    print("Неправильно")

print(questions[4])
user_answer = input("Введите свой ответ: ")
if user_answer == answers[4]:
    score = score + 1
    print("Правильно")
else:
    print("Неправильно")

print(questions[5])
user_answer = input("Введите свой ответ: ")
if user_answer == answers[5]:
    score = score + 1
    print("Правильно")
else:
    print("Неправильно")

print(questions[6])
user_answer = input("Введите свой ответ: ")
if user_answer == answers[6]:
    score = score + 1
    print("Правильно")
else:
    print("Неправильно")

print(questions[7])
user_answer = input("Введите свой ответ: ")
if user_answer == answers[7]:
    score = score + 1
    print("Правильно")
else:
    print("Неправильно")

print(questions[8])
user_answer = input("Введите свой ответ: ")
if user_answer == answers[8]:
    score = score + 1
    print("Правильно")
else:
    print("Неправильно")

print(questions[9])
user_answer = input("Введите свой ответ: ")
if user_answer == answers[9]:
    score = score + 1
    print("Правильно")
else:
    print("Неправильно")

print("Ты ответил правильно на", score, "вопросов из 10")
if score > 8:
    print("Да ты настоящий геймер!")
elif score > 5:
    print("Ты следишь за игровой индустрией!")
else:
    print("Ты недавно начал увлекаться играми!")
