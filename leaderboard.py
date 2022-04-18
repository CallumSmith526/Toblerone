from guizero import Window, Text, Box


def Leaderboards(app):

    file = open("scores.csv", "r")
    winners = []
    for line in file:
        line = line.strip()
        line = line.split(",")
        line[1] = int(line[1])
        winners.append(line)
    file.close()

    def get_score(record):
        return record[1]

    winners = sorted(winners, key=get_score, reverse=True)

    def players_scores(winners):
        name1.value = winners[0][0]
        score1.value = winners[0][1]
        name2.value = winners[1][0]
        score2.value = winners[1][1]
        name3.value = winners[2][0]
        score3.value = winners[2][1]
        name4.value = winners[3][0]
        score4.value = winners[3][1]
        name5.value = winners[4][0]
        score5.value = winners[4][1]

    ldrbrd = Window(app,
                    title="Leaderboard",
                    bg="black",
                    width=400,
                    height=400)
    ldrbrd.text_size = 15

    title = Text(ldrbrd, text="Highest Scores:")
    title.text_color = "magenta"
    title.text_size = 15
    userbttn = Box(ldrbrd, align="left", layout="grid")
    name1 = Text(userbttn, text="player 1", grid=[0, 0], color="misty rose")
    name2 = Text(userbttn, text="player 2", grid=[0, 1], color="misty rose")
    name3 = Text(userbttn, text="player 3", grid=[0, 2], color="misty rose")
    name4 = Text(userbttn, text="player 4", grid=[0, 3], color="misty rose")
    name5 = Text(userbttn, text="player 5", grid=[0, 4], color="misty rose")
    scr = Box(ldrbrd, align="right", layout="grid")
    score1 = Text(scr, text="score 1", grid=[0, 0], color="white")
    score2 = Text(scr, text="score 2", grid=[0, 1], color="white")
    score3 = Text(scr, text="score 3", grid=[0, 2], color="white")
    score4 = Text(scr, text="score 4", grid=[0, 3], color="white")
    score5 = Text(scr, text="score 5", grid=[0, 5], color="white")
    players_scores(winners)
