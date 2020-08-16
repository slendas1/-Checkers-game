import pygame
import sys


def inversion(a):
    if player == 2:
        if a == 1:
            return 3
        if a == 2:
            return 4
        if a == 3:
            return 1
        if a == 4:
            return 2
    return a



def necessary_moves():
    global necessary_moves_player_1
    global necessary_moves_player_2
    global limitation
    necessary_moves_player_1 = []
    necessary_moves_player_2 = []
    for first_pos_1 in range(8):
        for first_pos_2 in range(8):
             if field[first_pos_1][first_pos_2] == inversion(1) and (limitation == (first_pos_1, first_pos_2) or limitation == (-1, -1)):
                for k in range(4):
                    second_pos_1 = first_pos_1 + b[k][0]
                    second_pos_2 = first_pos_2 + b[k][1]
                    if second_pos_1 <= 7 and second_pos_1 >= 0 and second_pos_2 <= 7 and second_pos_2 >= 0:
                        if (field[first_pos_1 + a[k][0]][first_pos_2 + a[k][1]] == inversion(3) or field[first_pos_1 + a[k][0]][first_pos_2 + a[k][1]] == inversion(4)) and (field[second_pos_1][second_pos_2] == 0):
                            if player == 1:
                                necessary_moves_player_1.append((first_pos_1, first_pos_2, second_pos_1, second_pos_2))
                            else:
                                necessary_moves_player_2.append((first_pos_1, first_pos_2, second_pos_1, second_pos_2))
             if field[first_pos_1][first_pos_2] == inversion(2) and (limitation == (first_pos_1, first_pos_2)  or limitation == (-1, -1)):
                for direction in range(4):
                    check = 0
                    for k in range(direction, 28, 4):
                        r1 = first_pos_1 + c[k][0]
                        r2 = first_pos_2 + c[k][1]
                        if r1 <= 7 and r1 >= 0 and r2 <= 7 and r2 >= 0:
                            if check == 0:
                                if (field[r1][r2] == inversion(3) or field[r1][r2] == inversion(4)):
                                    check = 1
                                if (field[r1][r2] == inversion(1) or field[r1][r2] == inversion(2)):
                                    break
                            else:
                                if not field[r1][r2]:
                                    if player == 1:
                                        necessary_moves_player_1.append(
                                            (first_pos_1, first_pos_2, r1, r2))
                                    else:
                                        necessary_moves_player_2.append(
                                            (first_pos_1, first_pos_2, r1, r2))
                                else:
                                    break
    limitation = (-1, -1)


def possible_moves():
    global possible_moves_player_1
    global possible_moves_player_2
    possible_moves_player_1 = []
    possible_moves_player_2 = []
    for first_pos_1 in range(8):
        for first_pos_2 in range(8):
            if field[first_pos_1][first_pos_2] == inversion(1):
                for k in range(4):
                    second_pos_1 = first_pos_1 + a[k][0]
                    second_pos_2 = first_pos_2 + a[k][1]
                    if second_pos_1 <= 7 and second_pos_1 >= 0 and second_pos_2 <= 7 and second_pos_2 >= 0:
                        if (field[second_pos_1][second_pos_2] == 0):
                            if player == 1 and k <= 1:
                                possible_moves_player_1.append((first_pos_1, first_pos_2, second_pos_1, second_pos_2))
                            elif k >= 2:
                                possible_moves_player_2.append((first_pos_1, first_pos_2, second_pos_1, second_pos_2))
            if field[first_pos_1][first_pos_2] == inversion(2):
                for direction in range(4):
                    for k in range(direction, 28, 4):
                        r1 = first_pos_1 + c[k][0]
                        r2 = first_pos_2 + c[k][1]
                        if r1 <= 7 and r1 >= 0 and r2 <= 7 and r2 >= 0:
                            if not field[r1][r2]:
                                if player == 1:
                                    possible_moves_player_1.append(
                                        (first_pos_1, first_pos_2, r1, r2))
                                else:
                                    possible_moves_player_2.append(
                                        (first_pos_1, first_pos_2, r1, r2))
                            else:
                                break


def step(first_pos1, first_pos2, second_pos1, second_pos2):
    global player
    global player_win
    global field, limitation, move
    move =  False
    arr = [first_pos1, first_pos2, second_pos1, second_pos2]
    step1 = (arr[0],arr[1], arr[2], arr[3])
    necessary_moves()
    possible_moves()
    if player == 1:
        if necessary_moves_player_1:
            if step1 in necessary_moves_player_1:
                direction_1 = (arr[2] - arr[0])//abs(arr[2] - arr[0])
                direction_2 = (arr[3] - arr[1])//abs(arr[3] - arr[1])
                checker = field[arr[0]][arr[1]]
                field[arr[0]][arr[1]] = 0
                cell_1 = arr[0] + direction_1
                cell_2 = arr[1] + direction_2
                while cell_1 != arr[2]:
                    if (field[cell_1][cell_2] == 3) or (field[cell_1][cell_2] == 4):
                        field[cell_1][cell_2] = 0
                    cell_1 += direction_1
                    cell_2 += direction_2
                field[arr[2]][arr[3]] = checker
                if (arr[2], arr[3]) in edge_1:
                    field[arr[2]][arr[3]] = 2
                limitation = (arr[2], arr[3])
                necessary_moves()

                if not necessary_moves_player_1:
                    player = 2
                else:
                    limitation = (arr[2], arr[3])
                move = True
        elif possible_moves_player_1:
            if step1 in possible_moves_player_1:
                field[arr[2]][arr[3]] = field[arr[0]][arr[1]]
                field[arr[0]][arr[1]] = 0
                if (arr[2], arr[3]) in edge_1:
                    field[arr[2]][arr[3]] = 2
                player = 2
                move = True
        else:
            player_win = 2
    else:
        if necessary_moves_player_2:
            if step1 in necessary_moves_player_2:
                direction_1 = (arr[2] - arr[0])//abs(arr[2] - arr[0])
                direction_2 = (arr[3] - arr[1])//abs(arr[3] - arr[1])
                checker = field[arr[0]][arr[1]]
                field[arr[0]][arr[1]] = 0
                cell_1 = arr[0] + direction_1
                cell_2 = arr[1] + direction_2
                while cell_1 != arr[2]:
                    if (field[cell_1][cell_2] == 1) or (field[cell_1][cell_2] == 2):
                        field[cell_1][cell_2] = 0
                    cell_1 += direction_1
                    cell_2 += direction_2
                field[arr[2]][arr[3]] = checker
                if (arr[2], arr[3]) in edge_2:
                    field[arr[2]][arr[3]] = 4
                limitation = (arr[2], arr[3])
                necessary_moves()
                if not necessary_moves_player_2:
                    player = 1
                else:
                    limitation = (arr[2], arr[3])
                move = True
        elif possible_moves_player_2:
            if step1 in possible_moves_player_2:
                field[arr[2]][arr[3]] = field[arr[0]][arr[1]]
                field[arr[0]][arr[1]] = 0
                if (arr[2], arr[3]) in edge_2:
                    field[arr[2]][arr[3]] = 4
                player = 1
                move = True
        else:
            player_win = 1


def quantity_of_checkers():
    global player_win
    count = 0
    for i in range(8):
        for j in range(8):
            if field[i][j] == inversion(1) or field[i][j] == inversion(2):
                count = 1
    if count == 0:
        if player == 1:
            player_win = 2
        else:
            player_win = 1


def initial_data():
    global field, player, necessary_moves_player_1
    global possible_moves_player_1, necessary_moves_player_2, possible_moves_player_2, player_win
    global limitation, move, x1, y1, x2, y2
    field = [[0, 3, 0, 3, 0, 3, 0, 3],
             [3, 0, 3, 0, 3, 0, 3, 0],
             [0, 3, 0, 3, 0, 3, 0, 3],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [1, 0, 1, 0, 1, 0, 1, 0],
             [0, 1, 0, 1, 0, 1, 0, 1],
             [1, 0, 1, 0, 1, 0, 1, 0]]
    player = 1
    necessary_moves_player_1 = []
    possible_moves_player_1 = []
    necessary_moves_player_2 = []
    possible_moves_player_2 = []
    player_win = -1
    limitation = (-1, -1)
    move = False
    x1 = -1
    y1 = -1
    x2 = -1
    y2 = -1
    grafic(-1, -1, -1, -1)


def grafic_of_win():
    f1 = pygame.font.Font(None, 100)
    text1 = f1.render("Белые выиграли", 1, RED)
    f2 = pygame.font.Font(None, 100)
    text2 = f1.render("Черные выиграли", 1, RED)
    if player_win == 1:
        win.blit(text1, (120, 350))
    else:
        win.blit(text2, (120, 350))
    pygame.display.update()


def grafic(x1, y1, x2, y2):
    clock.tick(FPS)
    global s
    global f1, g1
    global sign1, sign2
    win.fill(WHITE)
    k = 100
    x = 0
    for x in range(0, 800, 200):
        for y in range(100, 800, 200):
            pygame.draw.rect(win, BLACK, (y, x, 100, 100))
    for x in range(100, 800, 200):
        for y in range(0, 800, 200):
            pygame.draw.rect(win, BLACK, (y, x, 100, 100))
    for i in range(8):
        for j in range(8):
            if field[i][j] and (x2,y2) != (i, j):
                win.blit(checkers[field[i][j] - 1], (j*100, i * 100))
    if x1 != -1 and x2 != -1:
        if f1 != x2 * 100 or g1 != y2 * 100:
            win.blit(checkers[field[x2][y2] - 1], (g1, f1))
            f1 += sign1 * speed
            g1 += sign2 * speed
        else:
            win.blit(checkers[field[x2][y2] - 1], (y2 * 100, x2 * 100))
            s = False
    elif x1 != -1:
        pygame.draw.rect(win, GREEN, (y1 * 100, x1 * 100, 100, 100), 5)
    pygame.display.update()


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
RED = (255, 0, 0)
speed = 4
pygame.init()
win = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Chekers")
clock = pygame.time.Clock()
FPS = 60
checkers = [pygame.image.load('pictures/1b.gif'), pygame.image.load('pictures/1bk.gif'), pygame.image.load('pictures/1h.gif'), pygame.image.load('pictures/1hk.gif')]
a = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
b = [(-2, -2), (-2, 2), (2, 2), (2, -2)]
c = []
edge_1 = [(0, 1), (0, 3), (0, 5), (0, 7)]
edge_2 = [(7, 0), (7, 2), (7, 4), (7, 6)]
for i in range(1, 8):
    c.append((-i, -i))
    c.append((-i, i))
    c.append((i, i))
    c.append((i, -i))
initial_data()
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                if player_win != -1:
                    initial_data()
                else:
                    x = i.pos[0] // 100
                    y = i.pos[1] // 100
                    if field[y][x] == inversion(1) or field[y][x] == inversion(2):
                        x1 = y
                        y1 = x
                    elif x1 != -1:
                        x2 = y
                        y2 = x
    if x1 != -1:
        grafic(x1, y1, -1, -1)
    if x1 != -1 and x2 != -1:
        step(x1, y1, x2, y2)
        if move:
            s = True
            f1 = x1 * 100
            g1 = y1 * 100
            sign1 = (x2 - x1) // abs(x2 - x1)
            sign2 = (y2 - y1) // abs(y2 - y1)
            while s:
                grafic(x1, y1, x2, y2)
            x1 = -1
            y1 = -1
            x2 = -1
            y2 = -1
        else:
            x2 = -1
            y2 = -1
        quantity_of_checkers()
        if player_win != -1:
            grafic_of_win()