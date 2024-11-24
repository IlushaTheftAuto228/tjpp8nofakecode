label start:
if renpy.android:
    $ playera = renpy.input("Как вас зовут?", length=12, allow="АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!#$%&*()_+-?,.\"' ")
    $ playera = playera.strip()
    "Вы уверены, что [playera] ваше имя?"
    menu:
        "Да":
            pass
        "Нет":
            jump start
else:
    pass
stop music
"Какую игру вы выберите?"
menu:
    "Рисовач: Анимач":
        jump drawful_animate
    "Колесо невероятных масштабов":
        jump picker_notthatgame
    "За работой":
        jump picker_notthatgame
    "Подземнения":
        jump picker_notthatgame
    "Преступление и рисование":
        jump picker_notthatgame
return
label picker_notthatgame:
play sound error
"Ошибка! Игры нужно начинать проходить в порядке сверху вниз."
"А то можно себе кое-что заспойлерить."
jump start
return
label picker_afterdrawful:
"Какую игру вы выберите теперь?"
menu:
    "Колесо невероятных масштабов":
        jump thewheel
    "За работой":
        jump picker_notthatgame2
    "Подземнения":
        jump picker_notthatgame2
    "Преступление и рисование":
        jump picker_notthatgame2
return
label picker_notthatgame2:
play sound error
"Ты что, забыл в каком порядке надо проходить игры?"
"Ах да!"
"Ты же мог и не читать ту самую ошибку."
"Ну ладно!"
"Я объясню."
"Игры нужно начинать проходить в порядке сверху вниз."
"А то можно себе кое-что заспойлерить."
jump picker_afterdrawful
return
label picker_afterthewheel:
"Какую игру вы выберите теперь?"
menu:
    "За работой":
        jump jobjob
    "Подземнения":
        jump picker_notthatgame3
    "Преступление и рисование":
        jump picker_notthatgame3
label picker_notthatgame3:
play sound error
"Хватит уже забывать нужный порядок прохождения!"
"Ой, точно!"
"Ты же мог его и не знать."
"Прости за мой гнев."
"Я не могу его контролировать."
"Ох..."
"Короче, нужно проходить все игры в порядке сверху вниз."
"Понял?"
menu:
    "Да":
        "Вот и отлично!"
        "А теперь иди и выбирай игру."
        jump picker_afterthewheel
    "Нет":
        "Да блин!"
        "Короче, я не хочу с тобой разбираться."
        "Поэтому, пожалуйста, сохраняйся после прохождения каждой игры."
        "Спасибо за понимание!"
        $ renpy.quit()
label picker_afterjobjob:
"Какую игру вы выберите теперь?"
menu:
    "Подземнения":
        jump thepollmine
    "Преступление и рисование":
        jump picker_notthatgame4
label picker_notthatgame4:
    play sound error
    "..."
    "Я предупреждал..."
    "Или ты не слышал в каком порядке надо проходить игры?"
    menu:
        "Слышал":
            "..."
            "Я не хочу с тобой разбираться."
            "Ты просто прикалываешься, да?"
            "А хотя чё я спрашиваю?"
            "Конечно прикалываешься!"
            "И это не обсуждается."
            "Пока."
            $ renpy.quit()
        "Не слышал":
            "Ладно!"
            "Короче игры нужно проходить в порядке сверху вниз."
            "Теперь можешь продолжать."
            jump picker_afterjobjob
label picker_afterthepollmine:
"Какую игру вы выберите теперь?"
"А хотя стоп."
"Выбирать не надо."
"Осталась последняя игра на прохождение."
"Поэтому желаю тебе удачи."
"А теперь иди, игрок."
jump weaponsdrawn
label picker_afterwd:
scene black
play sound error
"Мы сожалеем, но ведущий выгнал вас из игровой комнаты."
"Вы прошли все игры! Теперь можно выйти из па-, а хотя стоп."
"Поступило сообщение от сервера, о том что вышло новое важное обновление игры."
"Мы обязаны его немедленно установить."
$ renpy.movie_cutscene("videos/loading.mpg")
"Обновление установлено. Чтобы все изменения вступили в силу мы перезапустим игру."
"Все ваши сохранённые данные не будут утеряны."
$ renpy.movie_cutscene("videos/developerintro.mpg")
"Игра перезапущена."
"Какую игру вы выберите теперь?"
menu:
    "???":
        jump theend
    "???":
        jump theend
    "???":
        jump theend
    "???":
        jump theend
    "???":
        jump theend
