label theend:
show chara
play music thefallenchild
wtf "Здравствуй!"
if renpy.android:
    chua "Я [playera]"
    chua "Ты прошёл этот пак."
    chua "Ты молодец, но ты ещё не знаешь, что ты устроил на самом деле!"
    chua "Ты один из тех кто повёлся на эту уловку."
    chua "Ничего бесплатного в этом мире не существует."
    chua "Скачав пиратскую игру ты подтверждаешь, то что ты жадный."
    chua "Тебе не хочется поддержать, не важно, маленькую или крупную студию."
    chua "Тебе лишь бы повеселиться."
    chua "Ладно!"
    chua "Тебя ещё можно понять."
    chua "Денег там нет например или просто проверить тянет ли игра или нет."
    chua "Но всё же пиратство это большой грех!"
    stop music
    play sound jackvoice
    wtf "Jackbox Games!"
    play sound jackvoice
    wtf "Jackbox Games!"
    stop sound
    chua "Что простите?"
    play sound jackvoice
    wtf "Jackbox Games!"
    stop sound
    menu:
        "Я знаю, что можно сделать, чтобы его понять!":
            pass
    chua "И что же?"
    menu:
        "Установить русификатор!":
            pass
    chua "Гениально!"
    menu:
        "Установить русификатор на незнакомца (текст)":
            pass
    $ renpy.movie_cutscene("videos/loading.mpg")
    hide chara
    "Русификатор установлен. Отматываем игру..."
    show chara
    play sound jackvoice
    wtf "А ну разойдитесь!"
    stop sound
    chua "Так-то лучше!"
    chua "Не уйдём!"
    play sound jackvoice
    wtf "Вам будет очень плохо если вы осмелитесь остаться здесь!"
    stop sound
    chua "Да не уйдём мы!"
    play sound jackvoice
    wtf "Ах так!"
    stop sound
    show jackbox:
        xalign 1.0
        yalign 1.0
    play music jackattack
    j "Я Джек и я тут!"
    j "Я одновременно и создатель, и основатель, и издатель, и разработчик, и сценарист, и программист, но не композитор."
    j "Я использовал самые популярные треки от самого популярного композитора самой популярной игры."
    j "Ну и из обычного лицензионного джекбокса тоже треки брал."
    j "Это всё же тоже как бы моё владение."
    j "Из треков к этой игре я написал только тему играющую на фоне."
    j "Это моя злодейская тема."
    chua "И тема устраивания геноцида в \"Преступлении и рисовании\"."
    menu:
        "То есть тем голосом в моей голове был ты?":
            pass
    chua "Точнее ты."
    chua "Я это ты."
else:
    chu "Я [player]."
    chu "Ты прошёл этот пак."
    chu "Ты молодец, но ты ещё не знаешь, что ты устроил на самом деле!"
    chu "Ты один из тех кто повёлся на эту уловку."
    chu "Ничего бесплатного в этом мире не существует."
    chu "Скачав пиратскую игру ты подтверждаешь, то что ты жадный."
    chu "Тебе не хочется поддержать, не важно, маленькую или крупную студию."
    chu "Тебе лишь бы повеселиться."
    chu "Ладно!"
    chu "Тебя ещё можно понять."
    chu "Денег там нет например или просто проверить тянет ли игра или нет."
    chu "Но всё же пиратство это большой грех!"
    stop music
    play sound jackvoice
    wtf "Jackbox Games!"
    play sound jackvoice
    wtf "Jackbox Games!"
    stop sound
    chu "Что простите?"
    play sound jackvoice
    wtf "Jackbox Games!"
    stop sound
    menu:
        "Я знаю, что можно сделать, чтобы его понять!":
            pass
    chu "И что же?"
    menu:
        "Установить русификатор!":
            pass
    chu "Гениально!"
    menu:
        "Установить русификатор на незнакомца (текст)":
            pass
    $ renpy.movie_cutscene("videos/loading.mpg")
    hide chara
    "Русификатор установлен. Отматываем игру..."
    show chara
    play sound jackvoice
    wtf "А ну разойдитесь!"
    stop sound
    chu "Так-то лучше!"
    chu "Не уйдём!"
    play sound jackvoice
    wtf "Вам будет очень плохо если вы осмелитесь остаться здесь!"
    stop sound
    chu "Да не уйдём мы!"
    play sound jackvoice
    wtf "Ах так!"
    stop sound
    show jackbox:
        xalign 1.0
        yalign 1.0
    play music jackattack
    j "Я Джек и я тут!"
    j "Я одновременно и создатель, и основатель, и издатель, и разработчик, и сценарист, и программист, но не композитор."
    j "Я использовал самые популярные треки от самого популярного композитора самой популярной игры."
    j "Ну и из обычного лицензионного джекбокса тоже треки брал."
    j "Это всё же тоже как бы моё владение."
    j "Из треков к этой игре я написал только тему играющую на фоне."
    j "Это моя злодейская тема."
    chu "И тема устраивания геноцида в \"Преступлении и рисовании\"."
    menu:
        "То есть тем голосом в моей голове был ты?":
            pass
    chu "Точнее ты."
    chu "Я это ты."
j "Не ври!"
j "Ты думаешь я не играл в \"Undertale\" или не смотрел летсплеи по нему?"
j "Моим первым и любимым путём в твоей игре был геноцид!"
j "Я обожаю что-то злодейское!"
j "Я сам злодей в этой игре!"
if renpy.android:
    j "Ты не [playera], ты Чара!"
else:
    j "Ты не [player], ты Чара!"
ch "Ну ладно! Я Чара."
ch "Я думала ты тупой и ты играешь только в джекбокс и всё."
j "Так и есть, но иногда нет."
ch "Гениально!"
if renpy.android:
    ch "Да и тем более [playera] мог и не понять почему какой-то персонаж в игре это он сам."
else:
    ch "Да и тем более [player] мог и не понять почему какой-то персонаж в игре это он сам."
    ch "А точнее его пользователь в Windows."
ch "Может он-то и не играл в \"Undertale\"."
if renpy.android:
    ch "[playera], ты играл в \"Undertale\"?"
else:
    ch "[player], ты играл в \"Undertale\"?"
menu:
    "Да!":
        stop music
        ch "Правда?"
        ch "Тогда давай дружить!"
        j "СЕЙЧАС НЕ ВРЕМЯ ДРУЖИТЬ И ВЕСЕЛИТЬСЯ!"
        pass
    "Нет!":
        stop music
        ch "Вот видишь!"
        j "..."
        j "Забудь."
        pass
play music jackattack
if renpy.android:
    j "Короче, [playera]! Мне придётся тебя убить ЗДЕСЬ и СЕЙЧАС!"
else:
    j "Короче, [player]! Мне придётся тебя убить ЗДЕСЬ и СЕЙЧАС!"
ch "Может быть этим займусь я?"
j "НИКАК НЕТ!"
stop music
ch "..."
j "..."
ch "Можно было и не орать."
j "Ладно! Не буду."
play music jackattack
j "Я тебя убью! Ха-ха-ха..."
j "ХА-ХА-ХА!"
j "АХАХАХАХАХАХАХАХАХХАХХАХАХАХААХАХАХХАХАХАХАХАХАХХАХХАХАХАХАХААХАХАХАХАХААХХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХХАХАХАХАХАХАХАХААХХАХАХАХАХАХАХХАХАХАХХАХАХАХАХХААХХААХАХХАХАХХААХАХАХАХАХАХАХАХАХАХАХАХАХХААХХААХХАААХАХАХАХАХААХХАХААХАХАХАХХАХАХАХАХАХААХАХХААХАХАХАХАХААХАХАХАХААХАХАХАХАХХАХАХАХХАХХАХАХХАХХАХАХАХХ"
stop music
dh "Отвали от него!"
j "Чего?"
dh "Я сказала отвали!"
j "С каких это пор какая-то сова должна мне указывать?"
dh "А с таких!"
play music jackattack
dh "Отвали!"
show sans:
    xalign 0.0
    yalign 1.0
sans "серьёзно, бро. отвали!"
if renpy.android:
    lt "Хоть и [playera] меня чуть не убил, но всё равно отвали!"
else:
    lt "Хоть и [player] меня чуть не убил, но всё равно отвали!"
scene thewheel
show chara
show jackbox:
    xalign 1.0
    yalign 1.0
show sans:
    xalign 0.0
    yalign 1.0
wheel "Отвали от него!"
god1 "Отвали!"
god2 "Отвали!"
god3 "Отвали!"
god4 "Отвали!"
talk "Отвали от него!"
lt "Оу, рассказчица! Вы выжили?"
talk "Да, Типпи!"
lt "Не называйте меня так."
talk "Ладно!"
show duo:
    xalign 0.75
    yalign 1.0
duo "Отвали! А то убью, как ту сову."
dh "О! Привет, Дуо!"
duo "Здравствуй, крошка!"
scene thewheelofmsc
show chara
show jackbox:
    xalign 1.0
    yalign 1.0
show sans:
    xalign 0.0
    yalign 1.0
show duo:
    xalign 0.75
    yalign 1.0
msc "Отвали, коробочный!"
j "БОЖЕ, КАК ЖЕ ВЫ МЕНЯ ЗАДОЛБАЛИ!!!"
hide jackbox
"Джек убежал."
dh "А ну иди сюда!"
hide duo
duo "Меня подожди!"
lt "Рассказчица, пошли за мной."
talk "Я не против!"
hide sans
sans "я пожалуй тоже с вами."
god1 "И я!"
god2 "И я!"
god3 "И я!"
god4 "И я!"
msc "Покедово!"
scene thewheel
show chara
wheel "Меня подожди!"
scene black 
show chara
stop music
"Все убежали за Джеком."
"Вы остались наедине с Чарой."
ch "..."
ch "Э-эм."
ch "Так как я помощница Джека, то будьте добры сбросить ваш прогресс и удалить ваши сохранения."
ch "Только дайте мне сказать кое-что напоследок."
ch "Первый символ пароля: 8."
ch "А теперь..."
if renpy.android:
    ch "Пока, [playera]..."
else:
    ch "Пока, [player]..."
ch "Была рада познакомиться."
$ clear_all_persistents()
$ delete_all_saves()
$ renpy.quit()