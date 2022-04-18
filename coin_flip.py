from guizero import Window, PushButton, Picture, Box, Text
from chara_choice import chara_choice
from random import randint

animated_flipping = 0
count = 0
#add an extra screen to tell player who goes and who chooses first

def winner(coin, app, username_p1, username_p2):
    if p1 == coin:
        the_winner = "Player 1"
        name = username_p1
    elif p2 == coin:
        the_winner = "Player 2"
        name = username_p2
    # coinflip.info(title="selection",text=f"{name} will choose first")
    print(the_winner)
    app.after(2000, chara_choice, args=[app, username_p1, username_p2, the_winner])
    return the_winner


def the_coin(app, username_p1, username_p2):
    global animated_flipping, count
    # num=randint(1,2)
    if count == 0:
        count += 1
        coin.image = "coins/heads.png"
        results.value = "Heads"
    elif count == 1:
        count -= 1
        coin.image = "coins/tales.png"
        results.value = "Tales"
    animated_flipping += 1
    if animated_flipping == 10:
        coin.cancel(the_coin)
        num = randint(1, 2)
        if num == 1:
            coin.image = "coins/heads.png"
            the_winner=winner("heads", app, username_p1, username_p2)
            results.value = f"Heads\n{the_winner}"
        elif num == 2:
            coin.image = "coins/tales.png"
            the_winner=winner("tales", app, username_p1, username_p2)
            results.value = f"Tales\n{the_winner}"


def coin_flipping_p1(choice, app, username_p1, username_p2):
    global p1, p2
    heads_p1.enabled = False
    tales_p1.enabled = False
    heads_p2.enabled = False
    tales_p2.enabled = False
    if choice == "tales":
        p1 = "tales"
        p2 = "heads"
        choice_p1.value = "Tales"
        choice_p2.value = "Heads"
    elif choice == "heads":
        p1 = "heads"
        p2 = "tales"
        choice_p1.value = "Heads"
        choice_p2.value = "Tales"
    coin.repeat(300, the_coin, args=[app, username_p1, username_p2])


def coin_flipping_p2(choice, app, username_p1, username_p2):
    global p1, p2
    heads_p1.enabled = False
    tales_p1.enabled = False
    heads_p2.enabled = False
    tales_p2.enabled = False
    if choice == "tales":
        p1 = "heads"
        p2 = "tales"
        choice_p1.value = "Heads"
        choice_p2.value = "Tales"
    elif choice == "heads":
        p1 = "tales"
        p2 = "heads"
        choice_p1.value = "Tales"
        choice_p2.value = "Heads"
    coin.repeat(300, the_coin, args=[app, username_p1, username_p2])


def coin_flip(app, username_p1, username_p2):
    global heads_p1, tales_p1, heads_p2, tales_p2, choice_p1
    global choice_p2, coin, results
    coinflip = Window(app, title="Coin flip", width=400, height=400)
    coin = Picture(coinflip, image="coins/heads.png")
    results = Text(coinflip, text="choose", color="green")
    p1_box = Box(coinflip, layout="grid", align="left", width=200, height=150)
    invis_p1 = Box(p1_box, grid=[0, 0], height=10, width=50)
    Text(p1_box, text=username_p1, color="green", grid=[1, 0])
    heads_p1 = PushButton(p1_box,
                          text="Heads",
                          grid=[1, 1],
                          command=coin_flipping_p1,
                          args=["heads", app, username_p1, username_p2])
    tales_p1 = PushButton(p1_box,
                          text="tales",
                          grid=[1, 2],
                          command=coin_flipping_p1,
                          args=["tales", app, username_p1, username_p2])
    choice_p1 = Text(p1_box, text="choice", color="green", grid=[1, 3])

    p2_box = Box(coinflip, layout="grid", align="right", width=200, height=150)
    invis_p2 = Box(p2_box, grid=[0, 0], height=10, width=75)
    Text(p2_box, text=username_p2, color="green", grid=[1, 0])
    heads_p2 = PushButton(p2_box,
                          text="Heads",
                          grid=[1, 1],
                          command=coin_flipping_p2,
                          args=["heads", app, username_p1, username_p2])
    tales_p2 = PushButton(p2_box,
                          text="tales",
                          grid=[1, 2],
                          command=coin_flipping_p2,
                          args=["tales", app, username_p1, username_p2])
    choice_p2 = Text(p2_box, text="choice", color="green", grid=[1, 3])
