from guizero import Window, Picture, Text, PushButton, Box
from leaderboard import Leaderboards
from almond import Almond
from milk import Milk
from dark import Dark
button_count=0
p1_button=""
p2_button=""

def p1button(roundcounter,roundCount):
  global p1_button,button_count
  button_count+=1
  p1_button.enabled=False
  if button_count == 2:
    file = open("roundcounterfile.txt","w")
    file.write(f"{roundcounter+1}")
    file.close()
    roundCount.hide()

def p2button(roundcounter,roundCount):
  global p2_button,button_count
  button_count+=1
  p2_button.enabled=False
  if button_count == 2:
    file = open("roundcounterfile.txt","w")
    file.write(f"{roundcounter+1}")
    file.close()
    roundCount.hide()


def round_count(app,current_winner,winners,p1,p2):
  global p1_button,p2_button,button_count
  #---------winners picture------
  # winner_pic="tolberone/milk.png"
  if isinstance(current_winner, Almond):
    winner_pic="tolberone/almond.png"
  elif isinstance(current_winner, Milk):
    winner_pic = "tolberone/milk.png"
  elif isinstance(current_winner, Dark):
    winner_pic = "tolberone/dark.png"
  #-------round counter------
  button_count=0
  file=open("roundcounterfile.txt","r")
  for number in file:
    roundcounter=int(number)
  file.close()
  if roundcounter == 1:
    currentround="Round 1/3"
  elif roundcounter == 2:
    currentround="Round 2/3"
  elif roundcounter == 3:
    currentround="Round 3/3"
    player1wins=0
    player2wins=0
  #--------Leaderboards---------------
    for players in winners:
      if players=="P1":
        player1wins+=1
      elif players=="P2":
        player2wins+=1
      if player2wins>player1wins:
        the3roundwinner=p1.name
      else:
        the3roundwinner=p2.name
    # READ ALL RECORDS IN SCORES.CSV
    leaderboard = []
    file = open("scores.csv", "r")
    for line in file:
      record = line.strip().split(",")
      record[1] = int(record[1])
      leaderboard.append(record)
    file.close()

    # UPDATE USERSCORE IF EXISTS
    updated_user_score = False
    for record in leaderboard:
      if record[0] == the3roundwinner:
        record[1] += 1
        updated_user_score = True

    # IF NOT EXIST ADD NEW SCORE
    if not updated_user_score:
      record = [the3roundwinner, 1]
      leaderboard.append(record)

    # SAVE OUR UPDATED LEADERBOARD
    file = open("scores.csv", "w")
    for record in leaderboard:
      str_record = f"{record[0]},{record[1]}\n"
      file.write(str_record)
    file.close()
    Leaderboards(app)
  #----------------Window-----------------
  roundCount=Window(app,title="Round Count",width=600,height=400, layout="grid")
  roundCount.bg="black"
  #-----------------rounds----------------
  roundbox=Box(roundCount,grid=[1,0])
  roundtext=Text(roundbox,text=currentround,color="magenta")
  #-----------------winning chara---------
  winning_chara=Picture(roundCount,image=winner_pic,grid=[1,1],width=300,height=300)
  #----------------ready button-----------
  p1_button=PushButton(roundCount, grid=[0,2],text = "Player 1 is ready",command=p1button,args=[roundcounter,roundCount])
  p1_button.bg="DeepSkyBlue2"
  p2_button=PushButton(roundCount,grid=[2,2],text="Player 2 is ready",command=p2button,args=[roundcounter,roundCount])
  p2_button.bg="dark orchid"  