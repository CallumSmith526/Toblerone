#  Allow 2 players to sign in for a match

#  Explain the rules of the game to each player

#  Provide 3 characters for players to choose from

#  Coin toss - Winner gets first character choice, loser gets first turn to play

#  Players take turns to attack each other until one player loses all health and is defeated

#  It should take roughly 5 turns to each player for a round to be won/lost

#  Best of 3 rounds wins the entire match

#  Match winner gets a +1 win on the leaderboard

#create classes
#create log in System
#put into gui
#use gui to explain rules

# from classes import Character

# almond = Assualt("Almond",100,25,1.5)
# milk = Health("Milk",100,15,10)
# dark = Defence("Dark",100,5,10)

from guizero import Text, App, Window, Box, TextBox, PushButton
from rules import rules
users = []
file = open('users.csv', 'r')
for user in file:
    users.append(user.strip().split(','))
user_count = 0
file = open("roundcounterfile.txt","w")
file.write("1")
file.close()


def login_handler_p1(input_box_p1, input_pass_p1):
    global users, user_count, username_p1, username_p2
    for user in users:
        if input_box_p1.value == user[0].strip(
        ) and input_pass_p1.value == user[1].strip():
            authorize_text_p1.text_color = "green"
            authorize_text_p1.value = "Valid user!"
            username_p1 = input_box_p1.value
            password = input_pass_p1.value
            users.remove([username_p1, password])
            login_button_p1.enabled = False
            input_box_p1.enabled = False
            input_pass_p1.enabled = False
            user_count += 1
            if user_count == 2:
                rules(app, username_p1, username_p2)
            return
        else:
            authorize_text_p1.text_color = "red"
            authorize_text_p1.value = "Invalid user!"


def login_handler_p2(input_box_p2, input_pass_p2):
    global users, user_count, username_p1, username_p2
    for user in users:
        if input_box_p2.value == user[0].strip(
        ) and input_pass_p2.value == user[1].strip():
            authorize_text_p2.text_color = "green"
            authorize_text_p2.value = "Valid user!"
            username_p2 = input_box_p2.value
            password = input_pass_p2.value
            users.remove([username_p2, password])
            login_button_p2.enabled = False
            input_box_p2.enabled = False
            input_pass_p2.enabled = False
            user_count += 1
            if user_count == 2:
                rules(app, username_p1, username_p2)
            return
        else:
            authorize_text_p2.text_color = "red"
            authorize_text_p2.value = "Invalid user!"


app = App(width=400, height=400)
login = Window(app, width=400, height=400, bg="azure")
Text(login, text="Login", size=30, color="red")
login_area = Box(login, width=380, height=300)

p1_login_box = Box(login_area, align="left")
Text(p1_login_box, text="Player 1")
Text(p1_login_box, text="username")
input_box_p1 = TextBox(p1_login_box)
Text(p1_login_box, text="password")
input_pass_p1 = TextBox(p1_login_box, hide_text=True)

login_button_p1 = PushButton(
    p1_login_box,
    text="login",
    command=lambda: login_handler_p1(input_box_p1, input_pass_p1))

authorize_text_p1 = Text(p1_login_box, text="Invalid user!", color="red")

p2_login_box = Box(login_area, align="right")
Text(p2_login_box, text="Player 2")
Text(p2_login_box, text="username")
input_box_p2 = TextBox(p2_login_box)
Text(p2_login_box, text="password")
input_pass_p2 = TextBox(p2_login_box, hide_text=True)

login_button_p2 = PushButton(
    p2_login_box,
    text="login",
    command=lambda: login_handler_p2(input_box_p2, input_pass_p2))

authorize_text_p2 = Text(p2_login_box, text="Invalid user!", color="red")




# from chara_choice import chara_choice
# from coin_flip import coin_flip
# from game import game
# rules(app)
# coin_flip(app,"admin","test")

# game(app,Almond("username_p1",100,25,1.5),Dark("username_p2",100,5,10),"Player 1")

# round_count(app,Milk("username_p2",100,5,10),1)

# chara_choice(app,"admin","test","Player 1")
#rules= Window(app,title= "Rules of the game, bg="purple",height=300")
#rules.text_size=30
#rules.text_color="orange"

#Text(rules,text="RULES")
#Text(rules, text="There are two players, each must choose a class of character\n ATTACK, HEALTH OR DEFENSE")
