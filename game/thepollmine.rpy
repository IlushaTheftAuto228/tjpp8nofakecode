label thepollmine:
scene thepollmine
play music thepollmine
"..."
menu:
    "Ау!":
        pass
"..."
menu:
    "Здесть кто-нибудь есть?":
        pass
"..."
"Сколько бы вы не кричали..."
"никто не откликался..."
"..."
"Вы видели только темноту и логотип играемой игры."
"Ну и пару факелов рядом с ним."
scene thepollminenofuckel
play sound grabbed
"Вы решили взять один."
"Он сразу пропал с логотипа."
"Вы решили пойти по темноте."
"Но поняли, что это всего лишь JPEG картинка."
"Вы были очень разачарованы в этом."
"И не только в этом, но и в том, что игры не будет."
"Вы уже грустными хотели развернуться и выбрать другую игру, как вдруг..."
stop music
play sound skeletron
"..."
"Вы слышите какой-то неизвестный голос..."
wtf "Человек..."
"Вы думаете, что это ведущий."
"Но ведущий так и не приходил и не представлялся."
"Вы думаете, что вам показалось."
"Но голос становился всё громче и громче и этот голос дополняли шаги."
"Вы в страхе хотели убежать, но потом вспомнили, что вы в JPEG картинке."
scene black with fade
"Вы, который уже готов умереть, закрыли свои глаза."
"И тут пришёл он..."
wtf "Человек..."
wtf "Тебя не учили здороваться с новым приятелем?"
wtf "Повернись и пожми мне руку..."
"Вы повернулись."
"С закрытыми глазами вы нашли твёрдую руку приятеля и пожали её."
"Как вдруг!"
$ renpy.movie_cutscene("videos/sans.mpg")
scene thepollminenofuckel
show sans
play music sans
sans "хех! трюк с подушкой-пердушкой никогда не прекращает быть смешным."
sans "я санс. скелет санс"
sans "было приятно познакомиться с тобой, человек."
sans "добро пожаловать, в подземелье!"
stop music
sans "точнее в подземнения..."
play music sans
sans "но не суть."
sans "и ещё, чел! верни факел, пожалуйста!"
menu:
    "Положить факел на место":
        pass
scene thepollmine
show sans
play sound grabbed
sans "так-то лучше!"
sans "таак. о чём это я?"
sans "а вспомнил!"
sans "короче мы щас в пиратском джекбоксе."
sans "не знаю какого фига джек вообще запихнул нас."
stop music
j "ДА ВЫ ТУТ ВСЕ ИЗДЕВАЕТЕСЬ ЧТО-ЛИ?!"
sans "чел, ты не волан-де морт!"
j "Да причём тут Гарри Поттер вообще?"
sans "иди своей дорогой, лысый."
sans "опозвоночься."
j "..."
j "Не смешно..."
sans "да ты вообще шуток не понимаешь."
sans "свали!"
sans "а ты игрок не суй не в своё дело нос и уходи играть в последнюю игру."
sans "я уверен, у тебя всё получится."
scene black
"Поздравляем!"
"Вы прошли игру \"Подземнения\"."
jump picker_afterthepollmine