from guizero import Window, Text, PushButton
from coin_flip import coin_flip


def rules(app, username_p1, username_p2):
    rules = Window(app,
                   title="Rules of the game",
                   bg="purple",
                   width=400,
                   height=400)
    rules.text_size = 10
    rules.text_color = "gold"

    title1 = Text(rules, text="RULES")
    title1.text_size = 15
    Text(rules, text="""
(1) There are two players,
each must choose a class of character
ATTACK, HEALTH OR DEFENSE
(2) You must battle using three modes of attack,
each deals different amounts of damage
(3) you have five rounds to battle it out,
the winner is the character with the most
amount of Health at the end or till the opponents
character is DEFEATED """)
    PushButton(rules,
               text="Understood",
               align="top",
               command=coin_flip,
               args=[app, username_p1, username_p2])
