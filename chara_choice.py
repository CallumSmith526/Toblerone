from guizero import Text, Window, Picture, PushButton, Box
from almond import Almond
from milk import Milk
from dark import Dark
from game import game

chosen = 0
player1chara = ""
player2chara = ""

def almond(username_p1, username_p2,winner,app):
    global chosen
    choose_almond = choice.yesno(title="continue?",
                                 text="do you want to continue with almond")
    if choose_almond is True and chosen != 2:
        chosen += 1
        almond_button.enabled = False
        the_chosen = "almond"
        who_first(username_p1, username_p2, winner, choice, the_chosen,app)


def milk(username_p1, username_p2,winner,app):
    global chosen
    choose_milk = choice.yesno(title="continue?",
                               text="do you want to continue with milk")
    if choose_milk is True and chosen != 2:
        chosen += 1
        milk_button.enabled = False
        the_chosen = "milk"
        who_first(username_p1, username_p2, winner, choice,the_chosen,app)


def dark(username_p1, username_p2,winner,app):
    global chosen
    choose_dark = choice.yesno(title="continue?",
                               text="do you want to continue with dark")
    if choose_dark is True and chosen != 2:
        chosen += 1
        dark_button.enabled = False
        the_chosen = "dark"
        who_first(username_p1, username_p2, winner, choice,the_chosen,app)


def who_first(username_p1, username_p2, winner, choice,the_chosen,app):
    global chosen,player1chara,player2chara
    if winner == "Player 1":
        # first_choice = username_p1
        if chosen == 1:
            if the_chosen == "almond":
              player1chara = Almond(username_p1,100,25,1.5)
            elif the_chosen == "milk":
              player1chara = Milk(username_p1,100,15,10) 
            elif the_chosen == "dark":
              player1chara = Dark(username_p1,100,5,10)
        elif chosen == 2:
            if the_chosen == "almond":
              player2chara = Almond(username_p2,100,25,1.5)
            elif the_chosen == "milk":
              player2chara = Milk(username_p2,100,15,10) 
            elif the_chosen == "dark":
              player2chara = Dark(username_p2,100,5,10)
    elif winner == "Player 2":
        if chosen == 1:
            if the_chosen == "almond":
              player2chara = Almond(username_p2,100,25,1.5)
            elif the_chosen == "milk":
              player2chara = Milk(username_p2,100,15,10) 
            elif the_chosen == "dark":
              player2chara = Dark(username_p2,100,5,10)
        elif chosen == 2:
            if the_chosen == "almond":
              player1chara = Almond(username_p1,100,25,1.5)
            elif the_chosen == "milk":
              player1chara = Milk(username_p1,100,15,10) 
            elif the_chosen == "dark":
              player1chara = Dark(username_p1,100,5,10)
    if chosen == 2:
      game(app,player1chara,player2chara,winner,)


def chara_choice(app, username_p1, username_p2, winner):
    global dark_button, milk_button, almond_button, choice
    choice = Window(app,
                    title="Choose your character",
                    width=600,
                    height=400,
                    layout="grid")

    left_box = Box(
        choice,
        grid=[0, 0],
        border=True,
        width=200,
        height=400,
    )

    left_box.bg = "royalblue3"
    middle_box = Box(choice, grid=[1, 0], border=True, width=200, height=400)
    middle_box.bg = "chocolate"
    right_box = Box(choice, grid=[2, 0], border=True, width=200, height=400)
    right_box.bg = "gray21"
    Text(left_box, text="Almond", color="ghost white", size=20)
    Text(middle_box, text="Milk", color="ghost white", size=20)
    Text(right_box, text="Dark", color="ghost white", size=20)
    Picture(left_box, image="tolberone/almond.png", height=200, width=150)
    Picture(middle_box, image="tolberone/milk.png", height=200, width=150)
    Picture(right_box, image="tolberone/dark.png", height=200, width=150)

    Text(left_box,
         text="Health●●●\nDamage●●●●●\n50% more Damage",
         color="ghost white")
    Text(middle_box,
         text="Health●●●●\nDamage●●●●\nRegens 10hp",
         color="ghost white")
    Text(right_box,
         text="Health●●●●●\nDamage●●●\nShield 10dmg",
         color="ghost white")
    almond_button = PushButton(left_box,
                               width=200,
                               height=100,
                               text="Choose almond!",
                               command=almond,args=[username_p1, username_p2,winner,app])
    almond_button.text_color = "ghost white"
    almond_button.bg = "blue4"
    milk_button = PushButton(middle_box,
                             width=200,
                             height=100,
                             text="Choose milk!",
                             command=milk,args=[username_p1,username_p2,winner,app])
    milk_button.text_color = "ghost white"
    milk_button.bg = "darkorange4"
    dark_button = PushButton(right_box,
                             width=200,
                             height=100,
                             text="Choose dark!",
                             command=dark,args=[username_p1, username_p2,winner,app])
    dark_button.text_color = "ghost white"
    dark_button.bg = "black"
