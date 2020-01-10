# Conway's Game of Life

import sys, pygame
import pygame.locals

def gameOfLifeAlgo(old):
    for i in range (len(old)):
        for j in range (len(old[i])):
            checkNeighbors(old, i, j)

    for i in range (len(old)):
        for j in range (len(old[i])):
            finalUpdate(old, i, j)

def checkNeighbors(board, row, col):
    n = [-1, 0, 1]
    count = 0
    for i in range (3):
        for j in range (3):
            currY = row + n[i]
            currX = col + n[j]
            if currY == -1 and currX == -1:
                break
            elif currX > len(board[j]) - 1 or currY > len(board) - 1:
                break
            elif currY == -1 or currX == -1 or (currY == row and currX == col):
                continue
            val = board[currY][currX]
            if val == 1 or val == 6 or val == 7 or val == 8:
                count = count + 1
    updateBoard(board, row, col, count)

def updateBoard(board, r, c, count):
    if board[r][c] == 0:
        if count < 2:
            board[r][c] = 2
        elif count == 2:
            board[r][c] = 3
        elif count == 3:
            board[r][c] = 4
        elif count > 3:
            board[r][c] = 5
    else:
        if count < 2:
            board[r][c] = 6
        elif count == 2 or count == 3:
            board[r][c] = 7
        elif count > 3:
            board[r][c] = 8

def finalUpdate(board, r, c):
    val = board[r][c]
    if val == 2 or val == 3 or val == 5 or val == 6 or val == 8:
        board[r][c] = 0
    else:
        board[r][c] = 1

pygame.init()

# Initializing the Size and Screen of the GUI
size = width, height = 360, 360
const = 8

bWidth, bHeight = int(width / const), int(height / const)
board = [[0] * (bWidth) for _ in range(bHeight)]

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Game of Life')
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 205)
silver = (192, 192, 192)

play = False
clock = pygame.time.Clock()
while 1:
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                x, y = event.pos
                board[int(y/const)][int(x/const)] = 1
        elif event.type == pygame.locals.KEYDOWN:
            if event.key == pygame.K_SPACE:
                play = not play

    for i in range (width):
        for j in range (height):
            pygame.draw.rect(screen, silver, (i * const, j * const, const, const), 1)
    
    for i in range (len(board)):
        for j in range (len(board[i])):
            if board[i][j] == 1:
                pygame.draw.rect(screen, blue, (j * const, i * const, const, const))

    pygame.display.flip()
    clock.tick(60)
    if play:
        gameOfLifeAlgo(board)