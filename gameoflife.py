"""
    Conway's Game of Life Visualization Project
    Charles Ezra Cabauatan
    Description: This project focuses on creating a way to visualize the game of life problem which
    is structured around overpopulation. This algorithm will attempt to show how the populations will
    move which depends on the amount of neighbors they have.
    Technologies: Python and Pygame
"""

# Necessary Imports for the Project
import sys, pygame
import pygame.locals

# Class for the Main Algorithm that will update the board
class Algorithm():
    def __init__(self, board):
        self.board = board

    def gameOfLifeAlgo(self) -> None:
        for i in range (len(self.board)):
            for j in range (len(self.board[i])):
                self.checkNeighbors(i, j)

        for i in range (len(self.board)):
            for j in range (len(self.board[i])):
                self.finalUpdate(i, j)
    
    def checkNeighbors(self, row, col) -> None:
        n = [-1, 0, 1]
        count = 0
        for i in range (3):
            for j in range (3):
                currY = row + n[i]
                currX = col + n[j]
                if currY == -1 and currX == -1:
                    break
                elif currX > len(self.board[j]) - 1 or currY > len(self.board) - 1:
                    break
                elif currY == -1 or currX == -1 or (currY == row and currX == col):
                    continue
                val = self.board[currY][currX]
                if val == 1 or val == 6 or val == 7 or val == 8:
                    count = count + 1
        self.updateBoard(row, col, count)

    def updateBoard(self, r, c, count) -> None:
        if self.board[r][c] == 0:
            if count < 2:
                self.board[r][c] = 2
            elif count == 2:
                self.board[r][c] = 3
            elif count == 3:
                self.board[r][c] = 4
            elif count > 3:
                self.board[r][c] = 5
        else:
            if count < 2:
                self.board[r][c] = 6
            elif count == 2 or count == 3:
                self.board[r][c] = 7
            elif count > 3:
                self.board[r][c] = 8
    
    def finalUpdate(self, r, c) -> None:
        val = self.board[r][c]
        if val == 2 or val == 3 or val == 5 or val == 6 or val == 8:
            self.board[r][c] = 0
        else:
            self.board[r][c] = 1
            self.board[r][c] = 1

''' Start of Pygame Impelementation for the Visualization '''

# Global Variables that are needed for the visualization
size = width, height = 500, 500
NUM_ROWS = 50
board_width, board_height = NUM_ROWS, NUM_ROWS
board = [[0] * (board_width) for _ in range(board_height)]

# Colors that will be used in the Visualization
WHITE = (255, 255, 255)
BLUE = (0, 0, 205)
SILVER = (192, 192, 192)

# This function updates the board that is in display
# By checking over the board 2D array and looking for a 1 
# If there is a 1 encountered, the display will create a blue rectangle there
def updateDisplayBoard(window, sizeBtwn):
    for i in range (len(board)):
        for j in range (len(board[i])):
            if board[i][j] == 1:
                pygame.draw.rect(window, BLUE, (j * sizeBtwn, i * sizeBtwn, sizeBtwn, sizeBtwn))

# This function draws the grid of the overall display
def drawGrid(window):
    sizeBtwn = width // NUM_ROWS
    x = 0
    y = 0
    for i in range(NUM_ROWS):
        x = x + sizeBtwn
        y = y + sizeBtwn
        pygame.draw.line(window, SILVER, (x,0), (x,width))
        pygame.draw.line(window, SILVER, (0,y), (width, y))
    updateDisplayBoard(window, sizeBtwn)

# This function updates the window of the visualization
def updateWindow(window):
    window.fill(WHITE)
    drawGrid(window)
    pygame.display.flip()

# Main function, where the main while loop for the pygame is found
def main():
    window = pygame.display.set_mode(size)
    pygame.display.set_caption('Game of Life')

    flag = True
    play = False
    clock = pygame.time.Clock()
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = pygame.mouse.get_pos()
                    sizeBtwn = width // NUM_ROWS
                    board[y // sizeBtwn][x // sizeBtwn] = 1
            elif event.type == pygame.locals.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    play = not play
        
        pygame.time.delay(50)
        clock.tick(60)
        updateWindow(window)
        
        if play:
            algo = Algorithm(board)
            algo.gameOfLifeAlgo()
    pass

main()