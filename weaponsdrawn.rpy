label weaponsdrawn:
scene weaponsdrawn
play music weaponsdrawn
talk "Добро пожаловать в \"Преступление и Рисование\"!"
talk "Я рассказчица! Давай я расскажу тебе предысторию этой игры с твоим же участием."
talk "Круто, правда?"
talk "Итак!"
talk "Жил был ты. Ну и короче появились и другие пердунчики."
talk "Ну вот жили были вы пердунчики и одному из вас дали оружие."
talk "Если быть точнее то нарисованное в Paint'е оружие."
talk "А один из вас потом всех перестреляет и каждый должен определить кто кого убил."
talk "Я пока рассказывала историю даже не заметила как тайно объяснила правила игры."
talk "Ладно! Лорд Типпет! Веди игру."
lt "Окей! Сейчас начнём."
lt "Итак! Дайте-ка я нарисую оружие."
lt "Как там? А точно! Win + R и mspaint."
lt "Фух! Ну погнали!"
scene black
stop music
"Спустя два часа..."
scene weaponsdrawn
play music weaponsdrawn
lt "Отлично! Теперь кому бы мне его дать?"
if renpy.android:
    lt "[playera] или [playera]?"
else:
    lt "[player] или [player]?"
lt "Тяжёлый выбор!"
lt "Столько много игроков!"
lt "И как тут не запутаться?"
lt "Ладно!"
lt "Выдам например..."
if renpy.android:
    lt "[playera]!"
    lt "Держи оружие, [playera]."
    show paintgunandroid
else:
    lt "[player]!"
    lt "Держи оружие, [player]."
    show paintgun
play sound grabbed
"Вы получили \"Нарисованное оружие\"."
lt "Шедевр!"
lt "Теперь выбери кого убить!"
lt "А хотя..."
lt "Выбора особо-то нет."
lt "Ведущих убить нельзя."
lt "Поэтому я добавлю троечку ботов."
lt "Итак!"
show bot:
    xalign 0.0
    yalign 1.0
lt "Бот номер раз!"
show bot2:
    xalign 0.5
    yalign 1.0
lt "Бот номер два!"
show bot3:
    xalign 1.0
    yalign 1.0
if renpy.android:
    hide paintgunandroid
    show paintgunandroid
else:
    hide paintgun
    show paintgun
lt "И бот номер три!"
lt "Отлично!"
lt "А теперь выбери кого убить!"
menu:
    "Бот 1":
        jump wd_bot1
    "Бот 2":
        jump wd_bot2
    "Бот 3":
        jump wd_bot3
label wd_bot1:
hide bot
play sound shot
lt "Уф! Вот это экшен!"
stop music
"Вы чувствуете, что вам тоже нравится ваш выстрел и вы хотите ещё."
lt "Так стоп!"
lt "Это что ещё такое?"
lt "Как так-то?"
lt "Каким боком?"
lt "Жертву уже убили! У нас должно быть расследование!"
"ВЫБИРАЙ УЖЕ КОГО УБИТЬ!!!"
play music jackattack
menu:
    "Бот 2":
        jump wd_bot12
    "Бот 3":
        jump wd_bot13
label wd_bot12:
hide bot2
play sound shot
lt "Пожалуйста, остановись!"
"НЕ СЛУШАЙ ЕГО!!! ПРОДОЛЖАЙ УБИВАТЬ!!!"
hide bot3
play sound shot
"Отлично!"
"Теперь займись рассказчицой!"
lt "НЕТ! НЕ НАДО!"
talk "Что здесь происходит?"
lt "Они собираются убить тебя!"
talk "Что? Чё ты несёшь?"
"СТРЕЛЯЙ!"
play sound shot
stop music
talk "Ах!"
lt "НЕТ!"
"Убей Типпета!"
"УБЕЙ!"
lt "Какая там команда для кика?"
lt "А точно!"
if renpy.android:
    lt "/kick [playera]"
else:
    lt "/kick [player]"
jump picker_afterwd
label wd_bot13:
hide bot3
play sound shot
lt "Пожалуйста, остановись!"
"НЕ СЛУШАЙ ЕГО!!! ПРОДОЛЖАЙ УБИВАТЬ!!!"
hide bot2
play sound shot
"Отлично!"
"Теперь займись рассказчицой!"
lt "НЕТ! НЕ НАДО!"
talk "Что здесь происходит?"
lt "Они собираются убить тебя!"
talk "Что? Чё ты несёшь?"
"СТРЕЛЯЙ!"
play sound shot
stop music
talk "Ах!"
lt "НЕТ!"
"Убей Типпета!"
"УБЕЙ!"
lt "Какая там команда для кика?"
lt "А точно!"
if renpy.android:
    lt "/kick [playera]"
else:
    lt "/kick [player]"
jump picker_afterwd
label wd_bot2:
hide bot2
play sound shot
lt "Уф! Вот это экшен!"
stop music
"Вы чувствуете, что вам тоже нравится ваш выстрел и вы хотите ещё."
lt "Так стоп!"
lt "Это что ещё такое?"
lt "Как так-то?"
lt "Каким боком?"
lt "Жертву уже убили! У нас должно быть расследование!"
"ВЫБИРАЙ УЖЕ КОГО УБИТЬ!!!"
play music jackattack
menu:
    "Бот 1":
        jump wd_bot21
    "Бот 3":
        jump wd_bot23
label wd_bot21:
hide bot
play sound shot
lt "Пожалуйста, остановись!"
"НЕ СЛУШАЙ ЕГО!!! ПРОДОЛЖАЙ УБИВАТЬ!!!"
hide bot3
play sound shot
"Отлично!"
"Теперь займись рассказчицой!"
lt "НЕТ! НЕ НАДО!"
talk "Что здесь происходит?"
lt "Они собираются убить тебя!"
talk "Что? Чё ты несёшь?"
"СТРЕЛЯЙ!"
play sound shot
stop music
talk "Ах!"
lt "НЕТ!"
"Убей Типпета!"
"УБЕЙ!"
lt "Какая там команда для кика?"
lt "А точно!"
if renpy.android:
    lt "/kick [playera]"
else:
    lt "/kick [player]"
jump picker_afterwd
label wd_bot23:
hide bot3
play sound shot
lt "Пожалуйста, остановись!"
"НЕ СЛУШАЙ ЕГО!!! ПРОДОЛЖАЙ УБИВАТЬ!!!"
hide bot
play sound shot
"Отлично!"
"Теперь займись рассказчицой!"
lt "НЕТ! НЕ НАДО!"
talk "Что здесь происходит?"
lt "Они собираются убить тебя!"
talk "Что? Чё ты несёшь?"
"СТРЕЛЯЙ!"
play sound shot
stop music
talk "Ах!"
lt "НЕТ!"
"Убей Типпета!"
"УБЕЙ!"
lt "Какая там команда для кика?"
lt "А точно!"
if renpy.android:
    lt "/kick [playera]"
else:
    lt "/kick [player]"
jump picker_afterwd
label wd_bot3:
hide bot3
play sound shot
lt "Уф! Вот это экшен!"
stop music
"Вы чувствуете, что вам тоже нравится ваш выстрел и вы хотите ещё."
lt "Так стоп!"
lt "Это что ещё такое?"
lt "Как так-то?"
lt "Каким боком?"
lt "Жертву уже убили! У нас должно быть расследование!"
"ВЫБИРАЙ УЖЕ КОГО УБИТЬ!!!"
play music jackattack
menu:
    "Бот 1":
        jump wd_bot31
    "Бот 2":
        jump wd_bot32
label wd_bot31:
hide bot
play sound shot
lt "Пожалуйста, остановись!"
"НЕ СЛУШАЙ ЕГО!!! ПРОДОЛЖАЙ УБИВАТЬ!!!"
hide bot2
play sound shot
"Отлично!"
"Теперь займись рассказчицой!"
lt "НЕТ! НЕ НАДО!"
talk "Что здесь происходит?"
lt "Они собираются убить тебя!"
talk "Что? Чё ты несёшь?"
"СТРЕЛЯЙ!"
play sound shot
stop music
talk "Ах!"
lt "НЕТ!"
"Убей Типпета!"
"УБЕЙ!"
lt "Какая там команда для кика?"
lt "А точно!"
if renpy.android:
    lt "/kick [playera]"
else:
    lt "/kick [player]"
jump picker_afterwd
label wd_bot32:
hide bot2
play sound shot
lt "Пожалуйста, остановись!"
"НЕ СЛУШАЙ ЕГО!!! ПРОДОЛЖАЙ УБИВАТЬ!!!"
hide bot
play sound shot
"Отлично!"
"Теперь займись рассказчицой!"
lt "НЕТ! НЕ НАДО!"
talk "Что здесь происходит?"
lt "Они собираются убить тебя!"
talk "Что? Чё ты несёшь?"
"СТРЕЛЯЙ!"
play sound shot
stop music
talk "Ах!"
lt "НЕТ!"
"Убей Типпета!"
"УБЕЙ!"
lt "Какая там команда для кика?"
lt "А точно!"
if renpy.android:
    lt "/kick [playera]"
else:
    lt "/kick [player]"
jump picker_afterwd