from guizero import Window,PushButton, Box, Picture,Text
from almond import Almond
from milk import Milk
from dark import Dark
from round_count import round_count
#(currenthp / totalhp) x width

is_p1_turn = True
info_text = ""
healthbar_p1_text = ""
healthbar_p2_text = ""
round_text = ""
p1=""
p2=""
winners=[]

def attack_move(attack,p1,p2,app):
  global is_p1_turn,info_text,healthbar_p2_text,healthbar_p1_text,round_text,winners
  if attack == "c":
    if is_p1_turn:
      info_text.value = p1.conservative_attack(p2)
    else:
      info_text.value = p2.conservative_attack(p1)
  elif attack == "b":
    if is_p1_turn:
      info_text.value = p1.balanced_attack(p2)
    else:
      info_text.value = p2.balanced_attack(p1) 
  elif attack == "a":
    if is_p1_turn:
      info_text.value = p1.aggressive_attack(p2) 
    else :
      info_text.value = p2.aggressive_attack(p1) 
  is_p1_turn = not is_p1_turn
  if is_p1_turn:
    round_text.value = p1.name
  else: 
    round_text.value = p2.name
  healthbar_p1_text.value = f"HP:{round(p1.game_health,1)}"
  healthbar_p2_text.value = f"HP:{round(p2.game_health,1)}"
  if p1.is_dead:
    p1.regenerate() 
    p2.regenerate()
    healthbar_p1_text.value = f"HP:{round(p1.game_health,1)}"
    healthbar_p2_text.value = f"HP:{round(p2.game_health,1)}"
    winners.append("P1")
    print(p2.game_health,p1.game_health)
    round_count(app,p2,winners,p1,p2)
    print("p1 is dead")

    #game_window.error(title="dead",text="p1 is dead")
  elif p2.is_dead:
    p1.regenerate() 
    p2.regenerate()
    healthbar_p1_text.value = f"HP:{round(p1.game_health,1)}"
    healthbar_p2_text.value = f"HP:{round(p2.game_health,1)}"    
    print(p2.game_health,p1.game_health)
    winners.append("P2")
    round_count(app,p1,winners,p1,p2)
    print("p2 is dead")
  


def game(app,player1chara,player2chara,winner):
  global is_p1_turn,info_text,healthbar_p2_text,healthbar_p1_text,round_text,p1,p1
  #-----------assignments-----------
  p1 = player1chara
  p2 = player2chara
  #Thank dan
  if isinstance(player1chara, Almond):
    chara1_pic="tolberone/almond.png"
  elif isinstance(player1chara, Milk):
    chara1_pic = "tolberone/milk.png"
  elif isinstance(player1chara, Dark):
    chara1_pic = "tolberone/dark.png"

  if isinstance(player2chara, Almond):
    chara2_pic="tolberone/almond.png"
  elif isinstance(player2chara, Milk):
    chara2_pic = "tolberone/milk.png"
  elif isinstance(player2chara, Dark):
    chara2_pic = "tolberone/dark.png"

    
  if winner == "Player 1":
    is_p1_turn = False
    first = p2.name
  else:
    is_p1_turn = True
    first = p1.name
  #----------------The window-------------------
  game_window = Window(app,title="Game",width=600,height=400,layout="grid")
  game_window.bg= "sky blue"
  #--------------Attack Buttons-------------------
  conservative_box = Box(game_window,align="bottom",grid=[0,2],width=200,height=50)
  conservative_attack = PushButton(conservative_box,text="Conservative Attack",command=attack_move,args=["c",p1,p2,app])
  conservative_attack.bg="yellow"
  balanced_box = Box(game_window,grid=[1,2],width=200,height=50)
  balanced_attack= PushButton(balanced_box,text = "Balanced Attack",command=attack_move,args=["b",p1,p2,app])
  balanced_attack.bg="orange"
  aggressive_box = Box(game_window,grid=[2,2],width=200,height=50)
  aggressive_attack = PushButton(aggressive_box,text="Aggressive Attack",command=attack_move,args=["a",p1,p2,app])
  aggressive_attack.bg="red"

  #---------------Chara images--------------------
  player1_chara = Picture(game_window,image=chara1_pic,grid=[0,1],width=200,height=200)
  player2_chara = Picture(game_window,image=chara2_pic,grid=[2,1],width=200,height=200)

  #----------------Health bars---------------------
  healthbar_p1 = Box(game_window,grid=[0,0])
  healthbar_p1_text=Text(healthbar_p1,text=f"HP:{p1.game_health}",color="red")
  healthbar_p2 = Box(game_window,grid=[2,0])
  healthbar_p2_text= Text(healthbar_p2,text=f"HP:{p2.game_health}",color="red")
  #----------------info box---------------------

  round_box = Box(game_window,grid = [1,0])
  round_text = Text(round_box,text=first)
  info_text = Text(game_window,text="",grid=[1,1],color="orange red")
  info_text.text_size=8
  
 #----------------round box---------------------
 
  
  

