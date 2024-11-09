# Голосок сансары
init python:
    def sansaravoice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("audio/sounds/sans.ogg")
        elif event == "slow_done":
            renpy.sound.stop()

# Голосок коробочного чела))
init python:
    def jackvoice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("audio/sounds/jackvoice.ogg")
        elif event == "slow_done":
            renpy.sound.stop()

# Удаление сейвов
init python:
    def clear_all_persistents():
        save_addon_idx = persistent.addon_idx
        safe_runtime = persistent.runtime
        safe_voicelines_path = persistent.voicelines_path
        persistent._clear(progress = True)
        persistent.addon_idx = save_addon_idx
        persistent.runtime = safe_runtime
        persistent.voicelines_path = safe_voicelines_path
        
        persistent.unlocked_endings = set()


    def delete_all_saves():
        for savegame in renpy.list_saved_games(fast=True):
            renpy.unlink_save(savegame)

# Определение персонажей игры.
define wtf = Character('???', color='#ffffff')
define dh = Character('Сова', color="#ffffff")
define duo = Character('Дуо', color="#00ff00") 
define wheel = Character('Колесо невероятных масштабов', color="#ffd700")
define god1 = Character('Бог 1', color="#ffffff")
define god2 = Character('Бог 2', color="#ffffff")
define god3 = Character('Бог 3', color="#ffffff")
define god4 = Character('Бог 4', color="#ffffff")
define msc = Character('Миссис Кулер', color="#1e90ff")
define sans = Character('санс', color="#ffffff", callback=sansaravoice, 
who_font="gui/fonts/comicsansmspixel.ttf",
what_font="gui/fonts/comicsansmspixel.ttf")
define talk = Character('Рассказчица', color="#ffffff")
define lt = Character('Лорд Типпет', color="#ffffff")
define ch = Character('Чара', color="#ffff00",
who_font="gui/fonts/determination.otf",
what_font="gui/fonts/determination.otf")
define chu = Character('[player]', color="#ffff00",
who_font="gui/fonts/determination.otf",
what_font="gui/fonts/determination.otf")
define chua = Character('[playera]', color="#ffff00",
who_font="gui/fonts/determination.otf",
what_font="gui/fonts/determination.otf")
define j = Character('Джек', color="#ffffff", callback=jackvoice)

# Музыка и звуки
define error.audio = ("audio/sounds/error.ogg")
define javoice.audio = ("audio/sounds/javoice.ogg")
define grabbed.audio = ("audio/sounds/grabbed.ogg")
define skeletron.audio = ("audio/sounds/skeletron.ogg")
define shot.audio = ("audio/sounds/shot.ogg")
define jackvoice.audio = ("audio/sounds/jackvoice.ogg")
define drawfullobby.audio = ("audio/music/drawfullobby.ogg")
define nyehhehheh.audio = ("audio/music/nyehhehheh.ogg")
define thewheel.audio = ("audio/music/thewheel.ogg")
define jobjob.audio = ("audio/music/jobjob.ogg")
define thepollmine.audio = ("audio/music/thepollmine.ogg")
define weaponsdrawn.audio = ("audio/music/weaponsdrawn.ogg")
define jackattack.audio = ("audio/music/jackattack.ogg")
define thefallenchild.audio = ("audio/music/thefallenchild.ogg")

# Дисклеймер смачный
image disclaimerundertale = ("images/other/disclaimer.jpg")

# Фоны
image drawfulanimate = ("images/bgs/drawfulanimate.jpg")
image thewheel = ("images/bgs/thewheel.jpg")
image msc = ("images/bgs/msc.jpg")
image thepollmine = ("images/bgs/thepollmine.jpg")
image thepollminenofuckel = ("images/bgs/thepollminenofuckel.jpg")
image weaponsdrawn = ("images/bgs/weaponsdrawn.jpg")
image thewheelofmsc = ("images/bgs/thewheelofmsc.jpg")

# Спрайты
image duo = ("images/sprites/duo.png")
image sprite = ("images/sprites/sprite.png")
image sans = ("images/sprites/sans.png")
image paintgun = ("images/sprites/paintgun.png")
image paintgunandroid = ("images/sprites/paintgunandroid.png")
image bot = ("images/sprites/bot.png")
image bot2 = ("images/sprites/bot2.png")
image bot3 = ("images/sprites/bot3.png")
image chara = ("images/sprites/chara.png")

# Юзернейм
init python:
    import os
    player = os.environ.get("USERNAME")

# Заставка
label splashscreen:
$ renpy.movie_cutscene('videos/developerintro.mpg')
scene black
scene disclaimer with fade
pause(5)
scene black with fade
return