label thewheel:
scene thewheel
play music thewheel
wheel "Добро пожаловать в игру под названием  \"Колесо невероятных масштабов\"."
wheel "Я Колесо Невероятных Масштабов и я буду вести эту викторину."
wheel "Если что представляться не надо я знаю как тебя зовут."
if renpy.android:
    wheel "[playera] же, да?"
    wheel "Ладно! Не говори мне."
    wheel "Я знаю, что это твоё имя."
    wheel "Небеса говорят что это правда."
    menu:
        "Точнее скрипт игры":
            pass
    wheel "Как тебе не стыдно такое говорить?"
    wheel "Дай угадаю!"
    wheel "Тебе так сказала ведущая рисовача?"
    menu:
        "Ну вообще да":
            pass
else:
    wheel "[player] же, да?"
    wheel "Ладно! Не говори мне."
    wheel "Я знаю, что это твоё имя."
    wheel "Небеса говорят что это правда."
    menu:
        "Точнее мой компьютер":
            pass
    wheel "Как тебе не стыдно такое говорить?"
    wheel "Дай угадаю!"
    wheel "Тебе так сказала ведущая рисовача?"
    menu:
        "Ну вообще да":
            pass
wheel "Я так и знал"
wheel "Ой, точнее небеса так и знали!"
wheel "Ха-ха!"
if renpy.android:
    wheel "Ладно, [playera]!"
else:
    wheel "Ладно, [player]!"
wheel "Давай начнём игру!"
wheel "Как там говорилось в одной песне про меня?"
wheel "Ах точно!"
wheel "\"Выше всех богов, выше всяких облаков!\""
stop music
god1 "М-да! Лживая какая-то песня."
wheel "Ну не всех!"
god2 "Непросто не всех, а..."
god3 "вообще ни один бог ниже тебя не стоял!"
god4 "И это я могу смело подтвердить."
if renpy.android:
    wheel "Э-э! Л-ладно, [playera]! Т-ты п-прошёл игру!"
    god1 "Да, [playera]! Можешь уходить."
else:
    wheel "Э-э! Л-ладно, [player]! Т-ты п-прошёл игру!"
    god1 "Да, [player]! Можешь уходить."
menu:
    "Ладно! До свидания!":
        pass
scene black
"Поздравляем!"
"Вы прошли игру \"Колесо невероятных масштабов\"."
jump picker_afterthewheel
return