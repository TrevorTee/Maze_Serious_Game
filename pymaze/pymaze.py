##################################################
# Design by whole TUANJIE Team
# Code by Yunfeng & Zibo
# 雍正护体 没有BUG
# 2020 / 12 / 10
##################################################


import turtle as t
from random import shuffle
import pyaudio
import wave
import sys
import pygame
import os

pygame.mixer.init()
pygame.mixer.music.load('bg music.wav')
pygame.mixer.music.play(-1)

mz = t.Screen()
mz.setup(700, 700)
mz.bgcolor('darkolivegreen')
mz.title('Monster Maze')
mz.register_shape('wall.gif')
mz.register_shape('pr.gif')
mz.register_shape('pl.gif')
mz.register_shape('e.gif')
mz.register_shape('gold.gif')
mz.register_shape('coin.gif')
mz.register_shape('wall2.gif')
mz.tracer(0)

levels = []
level_1 = [
    "BBBBBBBBBBBBBBBBBBBBBBBB",
    "BXXXXXXXXXXXOXXXOOOOXXXB",
    "BPOOSOOSOOOXOOOOOXXOOOOB",
    "BXXXXXXXXXOXOXXXXXXXXXOB",
    "BOOOSOOSOOOXGXOOOOGXOOOB",
    "BXOXXXXXXXXXXXOXXXXXOXOB",
    "BXGXOXOOOOOOOOOXOOOOOXOB",
    "BXOXOXOXXXOXXXOXXXXXXXOB",
    "BXOOOOOXOXOXOXOXOOOOOOOB",
    "BXOXXXXXOXOXOXOXXOXXXXXB",
    "BXOOOOOOOXXXOXOXOOXGOOOB",
    "BXOXXXXXXXOOOXOXOXXXXOXB",
    "BXOXOOOOXOOOOOOXOXOXOOOB",
    "BXOXGOXOOOXOXXOOOXOXOXOB",
    "BXOXXXXXXXXOOXXXXXOXXXOB",
    "BXOOOOOOOXGOOXGXXOOOOOOB",
    "BXXXXOXXOXXXXXOXOOXXXXOB",
    "BOOOXOXXXXOOOOOXOXXONXOB",
    "BOXOXOOOOXOXXOXXOXOOXXOB",
    "BOXOOOXXOXOOXOOOOXXGXOOB",
    "BOXOXXXOOXXOXOXOXXXOXOXB",
    "BOXOOGXXOXOOXOXXXOXOXOXB",
    "BOXXXXXOOOOXXOOOOOXOOOXB",
    "BBBBBBBBBBBBBBBBBBBBBBBB"
]

level_2 = [
    "BBBBBBBBBBBBBBBBBBBBBBBB",
    "BXOOOOXOOOOGOOOOOOGOOONB",
    "BOOXXOXOXXXXXXXXXXXXXXXB",
    "BOXXXOXOXOOOGXOOOGOOOXXB",
    "BOXGXOXOXOXXXXOXXXXXOXOB",
    "BOXOXOXOXOOOOOOXOOOOOXGB",
    "BOXOXGXOXOOXXXXXOXXXOXOB",
    "BOXOXXXOXOOOOOOOOOOXOXOB",
    "BOXOOOXOXXXXXXXXXXOXOXOB",
    "BOXOXOOOOXOOGOOOOOOXOXOB",
    "BOXOXXXXOXOXXXOXOXXXOOOB",
    "BOXOOOGXOXOOPXOXOOOOOXOB",
    "BOXXXXXXOXXXXXOXOXOXXXXB",
    "BOOXGOOOOOOOOOOXOXOOOOOB",
    "BXOXXOXXXXXXXXXXOXOXXXOB",
    "BXOOXOOXOOOOXOOOOXXXOXOB",
    "BXXOXOOXOXXOXOXXXXOOOXOB",
    "BGXOXXOXOGXOXOOOGXOXGXOB",
    "BOXOOXOXXXXOXXXXXXOXXXOB",
    "BOXXOXOOXOOOOOXOOOOOOOOB",
    "BOOXOXXOXOXXXOXOXXXXXXXB",
    "BXOOOOXOOOOOXXXOOOOOOOGB",
    "BXXXXOOOXXXOOOOOXXXXXXXB",
    "BBBBBBBBBBBBBBBBBBBBBBBB"
]

levels.append(level_1)
levels.append(level_2)


class Gold(t.Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.shape('gold.gif')
        self.speed(0)
        self.penup()


class Coin(t.Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.shape('coin.gif')
        self.speed(0)
        self.penup()


class NPC(t.Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.shape('e.gif')
        self.speed(0)
        self.penup()


class Owall(t.Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.shape('wall2.gif')
        self.speed(0)
        self.penup()


class Player(t.Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.shape('pr.gif')
        self.speed(0)
        self.penup()

    def go_right(self):
        go_x = self.xcor() + 24
        go_y = self.ycor()
        self.shape('pr.gif')
        self.move(go_x, go_y)

    def go_left(self):
        go_x = self.xcor() - 24
        go_y = self.ycor()
        self.shape('pl.gif')
        self.move(go_x, go_y)

    def go_up(self):
        go_x = self.xcor()
        go_y = self.ycor() + 24
        self.move(go_x, go_y)

    def go_down(self):
        go_x = self.xcor()
        go_y = self.ycor() - 24
        self.move(go_x, go_y)

    def move(self, go_x, go_y):
        if (go_x, go_y) not in walls and (go_x, go_y) not in Owalls:
            self.goto(go_x, go_y)
            self.look_for_gold(go_x, go_y)
            self.look_for_coin(go_x, go_y)
            self.look_for_NPC(go_x, go_y)
        else:
            print('Wow，hitting wall')
            playsound('hit.wav')

    def look_for_gold(self, go_x, go_y):

        # global i   #i 是一个从0开始的数字
        for g in golds:
            if g.distance(player) == 0:
                global current_question
                current_question = read_question_msg(g)
                show_msgbox(current_question, 'Press A, B, C, or D to answer')

                g.ht()
                golds.remove(g)

                playsound('yes.wav')
        if not golds:
            print("金币吃完啦！快去找怪物进入下一关！")

    def look_for_coin(self, go_x, go_y):
        for c in coins:
            if c.distance(player) == 0:
                print("吃掉了一个教程币")
                # w = coins.index(c)
                # print(w)
                global coin_index
                global tutorial_pointer

                show_msgbox(read_tutorial_msg('t', tutorial_pointer), 'Press Enter to continue')
                c.ht()
                coins.remove(c)
                playsound('yes.wav')

                if tutorial_pointer < coin_index:
                    tutorial_pointer += 1

    def look_for_NPC(self, go_x, go_y):
        for c in npcs:
            if c.distance(player) == 0:
                print("找到了npc！")
                global score
                global target_score
                global current_level
                if score is target_score:
                    score_celebrate = 'Your Score is ' + str(score)
                    if current_level is 2:
                        show_msgbox('You have won! ' + score_celebrate, 'You can quit this game now.')
                    else:
                        show_msgbox('You will enter the Level 2. ' + score_celebrate,
                                    'Press the N to enter the next level.')
                else:
                    show_msgbox('You need to collect all golds!', 'Press Enter to continue')
                # npcs.remove(c)
                # c.ht()


class Pen(t.Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.shape('wall.gif')
        self.speed(0)
        self.penup()

    def make_maze(self):
        level = levels[current_level - 1]
        for i in range(len(level)):
            row = level[i]
            for j in range(len(row)):
                screen_x = -288 + 24 * j
                screen_y = 288 - 24 * i
                char = row[j]
                if char == 'X':
                    self.goto(screen_x, screen_y)
                    self.stamp()
                    walls.append((screen_x, screen_y))  # tuple
                elif char == 'B':
                    owall = Owall()
                    owall.goto(screen_x, screen_y)
                    owall.stamp()
                    Owalls.append((screen_x, screen_y))
                elif char == 'P':
                    player.goto(screen_x, screen_y)
                    player.st()
                elif char == 'G':
                    gold = Gold()
                    golds.append(gold)
                    gold.goto(screen_x, screen_y)
                    gold.st()

                    gold_index = golds.index(gold)
                    golds_question_dict[gold] = test_bank[gold_index]

                    global target_score
                    target_score += 1
                elif char == 'S':
                    global coin_index
                    coin_index += 1

                    coin = Coin()
                    coins.append(coin)
                    coin.goto(screen_x, screen_y)
                    coin.st()
                elif char == 'N':
                    npc = NPC()
                    npcs.append(npc)
                    npc.goto(screen_x, screen_y)
                    npc.st()


current_level = 1

msg_pen = t.Turtle()


def show_msgbox(title, msg):
    msg_pen.ht()
    msg_pen.speed(0)
    msg_pen.penup()
    msg_pen.goto(-300, -300)
    msg_pen.fillcolor('dimgray')
    msg_pen.begin_fill()
    for i in range(4):
        msg_pen.fd(600)
        msg_pen.left(90)
    msg_pen.end_fill()
    msg_pen.goto(-190, -90)
    msg_pen.color('white')
    msg_pen.write(title, align='left', font=('Arial', 13, ''))
    msg_pen.goto(-190, -185)
    msg_pen.write(msg, align='left', font=('Arial', 12, 'bold'))


def next_level():
    global current_level
    global target_score
    global score

    if score == target_score:
        current_level = current_level + 1
        msg_pen.clear()
    else:
        show_msgbox("You need to collect all golds!", "Press Enter to continue!")
        return

    global coin_index
    global tutorial_pointer
    global test_bank
    global golds_question_dict

    score = 0
    target_score = 0
    coin_index = 0
    tutorial_pointer = 0
    test_bank = test_bank_build(current_level)
    golds_question_dict = {}

    for c in npcs:
        c.ht()
    npcs.clear()

    pen.clear()
    walls.clear()
    golds.clear()
    Owalls.clear()
    pen.make_maze()


def playsound(file):
    chunk = 1024
    wf = wave.open(file, 'rb')
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    data = wf.readframes(chunk)
    while len(data) > 0:
        stream.write(data)
        data = wf.readframes(chunk)
    stream.stop_stream()
    stream.close()
    p.terminate()


def read_tutorial_msg(m, t):
    with open(f'{m}{t}.txt', 'r') as f:
        return f.read()


def read_question_msg(gold):
    global golds_question_dict
    global current_level
    global current_answer

    quest = golds_question_dict[gold]
    answer = quest.split('_')[2]
    current_answer = answer[0]  # record the current answer
    path = 'test_bank/level_' + str(current_level) + '/' + quest
    with open(path) as f:
        return f.read()


# load the test bank for current level (Note: the questions are shuffled here)
def test_bank_build(currentLevel):
    files = os.listdir('test_bank/level_' + str(currentLevel))
    test_bank = []
    for file in files:
        test_bank.append(file)
    # shuffle(test_bank)

    return test_bank


def check_answer_a():
    global msg_pen
    global score
    if current_answer is 'a':
        msg_pen.clear()

        score += 1
        print(f"current score is {score}")
    else:
        show_msgbox('Your answer is Wrong!', 'Press Space to Continue')


def check_answer_b():
    global msg_pen
    global score
    if current_answer is 'b':
        msg_pen.clear()

        score += 1
        print(f"current score is {score}")
    else:
        show_msgbox('Your answer is Wrong!', 'Press Space to Continue')


def check_answer_c():
    global score
    global msg_pen
    if current_answer is 'c':
        msg_pen.clear()

        score += 1
        print(f"current score is {score}")
    else:
        show_msgbox('Your answer is Wrong!', 'Press Space to Continue')


def check_answer_d():
    global msg_pen
    global score
    if current_answer is 'd':
        msg_pen.clear()

        score += 1
        print(f"current score is {score}")
    else:
        show_msgbox('Your answer is Wrong!', 'Press Space to Continue')


def reshow_question():
    global current_question
    show_msgbox(current_question, 'Press A, B, C, or D to answer')


goal_num = [6, 6]
score = 0
target_score = 0
i = 0
pen = Pen()
player = Player()
walls = []
Owalls = []
golds = []
coins = []
coin_index = 0  # record the index of tutorial
tutorial_pointer = 0
enemies = []
npcs = []
test_bank = test_bank_build(current_level)
golds_question_dict = {}  # build the dictionary for questions and golds
current_answer = 'p'
current_question = ''

pen.make_maze()

mz.listen()
mz.onkey(player.go_right, 'Right')
mz.onkey(player.go_left, 'Left')
mz.onkey(player.go_up, 'Up')
mz.onkey(player.go_down, 'Down')
mz.onkey(msg_pen.clear, 'Return')
mz.onkey(check_answer_a, 'a')
mz.onkey(check_answer_b, 'b')
mz.onkey(check_answer_c, 'c')
mz.onkey(check_answer_d, 'd')
mz.onkey(reshow_question, 'space')
mz.onkey(next_level, 'n')

while True:
    mz.update()

mz.mainloop()
