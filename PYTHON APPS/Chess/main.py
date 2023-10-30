import pygame as p
import engine


# square window for our game.
# can change screen size from here
screen_width = screen_height = 550
screen_caption = "Two Player Chess by Purna"
icon = p.image.load(r"Images\icon.png")

# rows and columns

dimensions = 8

# making sqaures in the screen to display chess board boxes
sq_size = screen_height // dimensions

fps = 30
# to pass as an argument in clock.tick
# adjust if game become laggy

images = {}

def load_images():

    # load all images once as it is cpu heavy task
    pieces = ["wp", "wR", "wN", "wB", "wQ", "wK", "bp", "bR", "bN", "bB", "bQ", "bK"]
    for piece in pieces:
        image_path = r"Images" + "\\" + piece + ".png"

        images[piece] = p.transform.scale(p.image.load(image_path).convert_alpha(), (sq_size, sq_size))

        # pygame.transform.scale to adjust the image

def main():
    p.init()
    
    

    # os.system("welcome.mp3")
    

    # setting screen with sizes

    # closing our face detection window
   

    screen = p.display.set_mode((screen_width,screen_height), p.HWSURFACE | p.DOUBLEBUF)
    
   
    
    p.display.set_caption(screen_caption)
    p.display.set_icon(icon)
    p.display.update()
    # clock object 
    clock = p.time.Clock()
    # fps change karega to limit CPU in clock.tick(15)

    screen.fill(p.Color("white"))
    # aise hi

    # creating a gamestate object joh ki constructor ko call karega apne
    # dot operator to call gamestate() in engine
    
    gs = engine.gamestate()


    # to store valid moves
    valid_moves = gs.getvalidmoves()


    # print(gs.board)
    move_made = False
    # to update valid moves only when a move is made
    
    # flag variable for when a move is made
    # loading the images "once"
    load_images()

    # running variable to check start and quit
    running = True
    # tuple to keep the last square selected
    sq_selected = ()
    # no square is selected at start
    # tuple: (row,col)
    # playerClicks = []

    # list to keep two inputs
    player_clicks = []
    # keep track of player clicks (two tuples: [(6, 4), (4, 4)])


    done = True
    
    chess = p.transform.scale_by(p.image.load(r"Images\chess.jpg"),0.25)
    screen.fill(p.Color("black"))
    while done:

        screen.blit(chess,p.Rect(200-5*sq_size + 180,200-5*sq_size + 200,10,10))
        screen.blit(p.transform.scale_by(icon,0.5),p.Rect(470-5*sq_size+15,screen_height/2-270,10,10))
        showtext(screen, "Welcome to Chess", (screen_height/2 - 230,screen_height/2 - 10), 40)
        showtext(screen, "Press any key to start the game", (screen_height/2 - 220,screen_height/2+50),25)
        
        
        p.display.flip()
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
            if event.type == p.KEYDOWN:
                done = False
                # showtext(screen, predicted_name + " is playing")




    
    # start of my gameloop
    while running:

        # lets keep a for loop to get events
        for event in p.event.get():
            # print(p.display.Info())
            # if the type of event is this
            
            if event.type == p.QUIT:
                # to exit the whileloop
                running = False
            elif event.type == p.MOUSEBUTTONDOWN:
                # mouse kaha h?
                mouse_location = p.mouse.get_pos() # (x,y) location of mouse
                # get x and y from list
                column = mouse_location[0]//sq_size
                row  = mouse_location[1]//sq_size
                
                
                # first click is select, second click is undo
                if sq_selected == (row,column):
                    # user clicks same sqaure again
                    sq_selected = () # undo
                    player_clicks = []
                else:
                    # store the square selected by the user now
                    sq_selected = (row,column)
                    player_clicks.append(sq_selected)
                    # first time it will append to empty list then it appends to list[0]
                    

                    # hume pata karna hai user ka first click hai ya second
                    if len(player_clicks)==2:

                        # do clicks hogye toh bolenge make move
                        # so call the move class constructor
                        move = engine.Move(player_clicks[0],player_clicks[1],gs.board)
                        print(move.getChessNotation())

                        # player_clicks[0] is our source
                        # player_clicks[1] is our piece's destination
                        for i in range(len(valid_moves)):

                        # only get valid move object
                        # so check for it

                            if move == valid_moves[i]:
                                
                                gs.makeMove(valid_moves[i])
                                user_choice = "Q"
                                while move.pawn_promotion:
                                    p.display.set_caption("Choose a piece to promote to")
                                    screen.fill(p.Color("black"))
                                    screen.blit(p.transform.scale_by(p.image.load(r"Images\PromotionMenu.jpg"),0.2),p.Rect(200-sq_size,200-sq_size,10,10))
                                    showtext(screen, "Enter the corresponding character of the piece you want to promote to :", (200,200),12)
                                    p.display.flip()
                                    user_choice = ""
                                    for event in p.event.get():
                                        if event.type == p.KEYDOWN:
                                            if event.key == p.K_q:
                                                gs.makePawnPromotion(move,"Q")
                                                move.pawn_promotion=False
                                                
                                            elif event.key == p.K_r:
                                                gs.makePawnPromotion(move,"R")
                                                move.pawn_promotion=False
                                                
                                            elif event.key == p.K_b:
                                                gs.makePawnPromotion(move,"B")
                                                move.pawn_promotion=False
                                            elif event.key == p.K_n:
                                                gs.makePawnPromotion(move,"N")
                                                move.pawn_promotion=False
                                            else:
                                                gs.makePawnPromotion(move,"Q")
                                                move.pawn_promotion=False
                                            p.display.set_caption("ChessAI")
                            
                                
                                
                                    
                                # argument to makemove is generated by the engine
                            
                                

                                move_made = True
                               
                                sq_selected = () # reset user clicks
                                player_clicks = []
                            
                            
                                
                                # reset the user clicks after making the move each time 
                        if not move_made:
                            player_clicks = [sq_selected]
                        
                            
                        #gs.makeMove(move)
                        # to make the move
                            
            elif event.type == p.KEYDOWN:
                if event.key == p.K_z:
                    gs.undoMove()

                    move_made = True
                    # when the user undoes a move the valid moves change
                    # so change the flag variable to true

                    # to update the valid moves
        if move_made:
            valid_moves = gs.getvalidmoves()
            move_made = False
    


        # calling the draw boardand pieces fn
        draw_game_state(screen,gs)
        clock.tick(fps)
        p.display.flip()
        # to update the display

# method to draw sqs on board and graphics of a current gamestate
def draw_game_state(screen,gs):

    # to draw squares on the board
    drawboard(screen)

    #board-->pieces order ofc matter karega nhi toh pieces piche chip jayenge 

    # to draw pieces
    drawpieces(screen,gs.board) # board from engine gamestate ka object gs , isliye dot

def drawboard(screen):
    # lets draw squares
    # white and grey alternate
    # make list to store white and grey switch karna easy hoga
    # colors = [p.Color("white"), p.Color("dark gray")]
    images = [p.image.load(r"images\ltb.jpg").convert_alpha(),p.image.load(r"images\dtb.jpg").convert_alpha()]

    for rows in range(dimensions):
        for columns in range(dimensions):
            # [00,10,20,30,40,50,60,70]
            # [01,11,21,31,41,51,61,71]
            # [02,12,22,32,42,52,62,72]
            # [03,13,23,33,43,53,63,73]
            # [04,14,24,34,44,54,64,74]
            # [05,15,25,35,45,55,65,75]
            # [06,16,26,36,46,56,66,76]
            # [07,17,27,37,47,57,67,77]

            # trend we see here is that if we add rows and columns
            # dark sqaures are odd
            # light sqaures are even

            # color = colors[(rows+columns)%2]
            image = images[(rows+columns)%2]
            # even --> colors[0] --> white
            # odd --> colors[1] --> black
            
            # smpart

            # just draw rectangle (surface,color,)
            custom_img = p.Surface((sq_size,sq_size))
            
            screen.blit(image,p.Rect(columns*sq_size,rows*sq_size,sq_size,sq_size))
            
            # p.draw.rect(screen, color, p.Rect(columns*sq_size,rows*sq_size, sq_size, sq_size))

def drawpieces(screen,board):
    for rows in range(dimensions):
        for columns in range(dimensions):
            pieces = board[rows][columns]
            if pieces != "--":
                screen.blit(images[pieces],p.Rect(columns*sq_size,rows*sq_size,sq_size,sq_size))
            # accessing our gs.board multi dim list by using [][]
            # to assign each square a piece

# function to show a menu an ask the user the piece to promote to in pawn promotion



    
            
    


def showtext(screen,text,location,fontsize):
    font = p.font.SysFont("Copperplate gothic", fontsize, True, False)
    textObject = font.render(text, 0, p.Color('White'))
    location1 = p.Rect(location, location)
    # textLocation = p.Rect(0, 0, screen_width, screen_height).move(screen_width / 2 - textObject.get_width() / 2, screen_height / 2 - textObject.get_height() / 2)
    # white = p.Color("black")
    # screen.blit(white,p.rect(textLocation,textLocation,200,200))
    screen.blit(textObject, location1)

    






# if we import something in the main code we need to do this cause it wont run otherwise
# THIS CODE WE HAVE TO RUN AS THIS IS OUR MAIN CODE AND WE IMPORT OTHER MODULES IN THIS CODE
# SO WE WRITE THIS
# The if __name__ == "__main__": construct is used to 
# ensure that a specific block of code only runs when the Python script is executed directly,
# not when it's imported as a module in another script.
if __name__=="__main__":
    main()