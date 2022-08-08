from socket import gaierror
import pygame
import random
pygame.init()

blocks = [ 
    [[1,4,7],[3,4,5]], #straight
    [[1,3,4,5,7]], #cross
    [[0,1,4,5],[1,3,4,6]], # two on two ones
    [[1,2,3,4],[0,3,4,7]],
    [[0,1,3,6],[0,1,2,5],[2,5,7,8],[3,6,7,8]],
    [[1,2,5,8],[5,6,7,8],[0,3,6,7],[0,1,2,3]],
    [[4,6,7,8],[0,3,4,6],[0,1,2,4],[2,4,5,8]]
]

colours = [
    (122,78,0),
    (0,255,0),
    (100,60,200),
    (100,50,100),
    (50,100,200),
    (255,0,0),
    (0,0,255)
]

class Block:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.type = random.randint(0,len(blocks) - 1)
        self.rotation = 0
        self.colour = colours[random.randint(0,len(colours) -1)]
    
    def shape(self):
        return blocks[self.type][self.rotation]

def draw_block(screen, block, grid_size, x_gap, y_gap):
    for y in range(3):
        for x in range(3):
            if y * 3 + x in block.shape():
                pygame.draw.rect(screen,block.colour,
                                [(x + block.x) * grid_size + x_gap + 1, 
                                (y + block.y) * grid_size + y_gap + 1,grid_size - 2,grid_size - 2])
    
def collides(block,rows,cols,game_board,ny):
    collision = False
    for y in range(3):
        for x in range(3):
            if y * 3 + x in block.shape():
                if y + block.y + ny > rows - 1 or y + block.y + ny < 0:
                    collision = True
                    break
                if x + block.x > cols - 1 or x + block.x < 0:
                    collision = True
                    break
                if game_board[x + block.x][y + block.y + ny] != (0,0,0):
                    collision = True
                    break
    return collision

def rotate(block,rows,cols,game_board):
    last_rotate = block.rotation
    block.rotation = (block.rotation + 1)%len(blocks[block.type])
    can_rotate = True
    for y in range(3):
        for x in range(3):
            if y * 3 + x in block.shape():
                if collides(block,rows,cols,game_board,ny=0):
                    can_rotate = False
    if not can_rotate:
        block.rotation = last_rotate


def drawGrid(screen,rows,cols,x_gap,y_gap,grid_size,game_board):
    for y in range(rows):
        for x in range(cols):
            pygame.draw.rect(screen,(100,100,100),[x * grid_size + x_gap,y * grid_size + y_gap,grid_size,grid_size],1)
            pygame.draw.rect(screen,game_board[x][y],[x * grid_size + x_gap + 1,y * grid_size + y_gap + 1,grid_size - 2,grid_size - 2])

def dropBlock(block,rows,cols,game_board):
    can_drop = True
    for y in range(3):
        for x in range(3):
            if y * 3 + x in block.shape():
                if collides(block,rows,cols,game_board,ny=1):
                    can_drop = False
    if can_drop:
        block.y += 1
    else:
        for y in range(3):
            for x in range(3):
                if y * 3 + x in block.shape():
                    game_board[x + block.x][y + block.y] = block.colour
    return can_drop


def sideMove(block,cols,dx):
    can_move = True
    for y in range(3):
        for x in range(3):
            if y * 3 + x in block.shape():
                if block.x + x >= cols - 1 and dx == 1:
                    can_move = False
                elif block.x + x < 1 and dx == -1:
                    can_move = False
    if can_move:
        block.x += dx

def findLines(rows,cols,game_board):
    lines = 0
    for y in range(rows):
        empty = 0
        for x in range(cols):
            if game_board[x][y] == (0,0,0):
                empty += 1
        if empty == 0:
            lines += 1
            for y2 in range(y,1,-1):
                for x2 in range(cols):
                    game_board[x2][y2] = game_board[x2][y2 - 1]
    return lines

def main():
    screen = pygame.display.set_mode((300,600))
    pygame.display.set_caption('Tetris')
    grid_size = 30
    cols = screen.get_width() // grid_size
    rows = screen.get_height() // grid_size
    x_gap = (screen.get_width() - cols * grid_size) // 2
    y_gap = (screen.get_height() - rows * grid_size) // 2
    block = Block((cols - 1) // 2,0)
    game_over = False
    clock = pygame.time.Clock()
    fps = 8

    #game board setting black color
    game_board = []
    for i in range(cols):
        new_col = []
        for j in range(rows):
            new_col.append((0,0,0))
        game_board.append(new_col)
        
    score = 0
    font = pygame.font.SysFont('Arial', 25, True)
    font_quit = pygame.font.SysFont('Arial', 50, True)
    finished_text = font_quit.render('Game Over', True, (255,255,255))
    text_pos = [(screen.get_width() - finished_text.get_width())// 2, (screen.get_height() - finished_text.get_height()) // 2]
    game_finished = False
    while not game_over:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    rotate(block,rows,cols,game_board)
        if event.type == pygame.KEYDOWN:
            if block is not None:
                if event.key == pygame.K_LEFT:
                    sideMove(block,cols,-1)
                if event.key == pygame.K_RIGHT:
                    sideMove(block,cols,1)

        screen.fill((0,0,0))
        drawGrid(screen,rows,cols,x_gap,y_gap,grid_size,game_board)

        if block is not None:
            draw_block(screen, block, grid_size, x_gap, y_gap)
            if not dropBlock(block,rows,cols,game_board) and not game_finished:
                score += findLines(rows,cols,game_board)
                block = Block(random.randint(5,cols-5),0)
                if collides(block,rows,cols,game_board,ny=0):
                    game_finished = True

        text = font.render("Score: " + str(score), True, (255,255,255))
        screen.blit(text, [0,0])
        if game_finished == True:
            screen.blit(finished_text,text_pos)
        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()
