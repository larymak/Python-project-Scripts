

class gamestate():
    def __init__(self):
        # 2D 8x8 list, each element has 2 characters.
        # The first character represents the color of the piece
        # The second character represents the type of the piece
        # "--" represents an empty space with no piece
        # "wp" represents a white pawn
        # "bR" represents a black rook
        # "bK" represents a black king
        # "wQ" represents a white queen
        # and so on
        self.board = [
            ["bR","bN","bB","bQ","bK","bB","bN","bR"],
            ["bp","bp","bp","bp","bp","bp","bp","bp"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["wp","wp","wp","wp","wp","wp","wp","wp"],
            ["wR","wN","wB","wQ","wK","wB","wN","wR"]]
        
        # dictionary to map pieces to their respective move functions
        # so that proper function is called for each piece

        self.moveFunctions = {'p':self.getPawnMoves,'R':self.getRookMoves,'N':self.getKnightMoves,
                              'B':self.getBishopMoves,'Q':self.getQueenMoves,'K':self.getKingMoves}
        

        # we dont have to write 6 different functions for each piece


        
        
        self.whitemove=True
        self.moveLog = []
        self.whiteKingLocation = (7,4)
        self.blackKingLocation = (0,4)
        self.checkmate = False
        self.stalemate = False
        self.enpassantPossible = () # coordinates for the square where en passant capture is possible
        self.currentCastlingRights = castleRights(True,True,True,True)
        self.castleRightsLog = [castleRights(self.currentCastlingRights.wks,self.currentCastlingRights.bks,self.currentCastlingRights.wqs,self.currentCastlingRights.bqs)]

        # pawn promotion is if white pawn reaches row 0
        # or if a black pawn reaches row 7

    def makePawnPromotion(self,move,user_choice):
        if move.pawn_promotion:
            # place queen of same color at pawn's place
            self.board[move.endRow][move.endCol] = move.pieceMoved[0] + user_choice
    
    
    

    def makeMove(self,move):
        # make the move and update the board
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.moveLog.append(move)
        # swap turns after move
        self.whitemove = not self.whitemove
        if move.pieceMoved == 'wK':
            self.whiteKingLocation = (move.endRow,move.endCol)
        if move.pieceMoved == 'bK':
            self.blackKingLocation = (move.endRow,move.endCol)

        if move.enpassantPossible:
            self.board[move.startRow][move.endCol] = "--" 
            # capturing the pawn
        #update enpassantPossible variable

        # only if the pawn moves two squares ahead
        # used abs so that it works for both white and black pawns
        # both up the board and down the board
        if move.pieceMoved[1] == 'p' and abs(move.startRow - move.endRow) == 2:
            self.enpassantPossible = ((move.startRow + move.endRow)//2,move.startCol)
        else:
            # reset enpassantPossible
            self.enpassantPossible = ()

        # updateCastleRights(move)


        if move.isCastleMove:
            if move.endCol - move.startCol == 2:
                # king side castle move
                self.board[move.endRow][move.endCol-1] = self.board[move.endRow][move.endCol+1]
                self.board[move.endRow][move.endCol+1] = "--"
            else:
                # queen side castle move
                self.board[move.endRow][move.endCol+1] = self.board[move.endRow][move.endCol-2]
                self.board[move.endRow][move.endCol-2] = "--"
        

        # castling
        # if king moves two squares to the right
        # then rook moves one square to the left
        # and vice versa
        self.updateCastleRights(move)
        self.castleRightsLog.append(castleRights(self.currentCastlingRights.wks,self.currentCastlingRights.bks,self.currentCastlingRights.wqs,self.currentCastlingRights.bqs))

        # update casting rights whenever it is a rook or a king move
        # if a rook or a king moves from its starting position
        # then we have to update the castling rights
    
    

    
        



        # pawn promotion
        
    

    
    def undoMove(self):
        # to make sure that there is a move to undo
        if len(self.moveLog) != 0:
            # pop returns and removes the last element from the list
            move = self.moveLog.pop()

            self.board[move.startRow][move.startCol] = move.pieceMoved
            # undoing the move
            self.board[move.endRow][move.endCol] = move.pieceCaptured
            # to make sure the piece captured is not empty
            # switch turns back
            self.whitemove = not self.whitemove
            if move.pieceMoved == 'wK':
                self.whiteKingLocation = (move.startRow,move.startCol)
            if move.pieceMoved == 'bK':
                self.blackKingLocation = (move.startRow,move.startCol)

            # undo enpassantPossible
            if move.enpassantPossible:
                self.board[move.endRow][move.endCol] = "--"
                # leave the landing square blank
                self.board[move.startRow][move.endCol] = move.pieceCaptured
                # redo the enpassant capture
                # if i undo the move, i have to set the enpassantPossible to the square where the enpassant capture was possible
                self.enpassantPossible = (move.endRow,move.endCol)
            # undo 2 square pawn advance
            if move.pieceMoved[1] == 'p' and abs(move.startRow - move.endRow) == 2:
                self.enpassantPossible = ()
            self.castleRightsLog.pop()
            self.currentCastlingRights = self.castleRightsLog[-1]
            self.currentCastlingRights = castleRights(self.currentCastlingRights.wks,self.currentCastlingRights.bks,self.currentCastlingRights.wqs,self.currentCastlingRights.bqs)
            # undo castling rights
            # if a rook or a king moves from its starting position
            # then we have to update the castling rights
            # if a rook or a king moves from its starting position
            # then we have to update the castling rights
            if move.isCastleMove:
                if move.endCol - move.startCol == 2:
                    # king side castle move
                    self.board[move.endRow][move.endCol+1] = self.board[move.endRow][move.endCol-1]
                    self.board[move.endRow][move.endCol-1] = "--"
                else:
                    # queen side castle move
                    self.board[move.endRow][move.endCol-2] = self.board[move.endRow][move.endCol+1]
                    self.board[move.endRow][move.endCol+1] = "--"
                self.checkmate = False
                self.stalemate = False

    def updateCastleRights(self,move):
        if move.pieceMoved == 'wK':
            self.currentCastlingRights.wks = False
            self.currentCastlingRights.wqs = False
        elif move.pieceMoved == 'bK':
            self.currentCastlingRights.bks = False
            self.currentCastlingRights.bqs = False
        elif move.pieceMoved == 'wR':
            if move.startRow == 7:
                if move.startCol == 0:
                    self.currentCastlingRights.wqs = False
                elif move.startCol == 7:
                    self.currentCastlingRights.wks = False
        elif move.pieceMoved == 'bR':
            if move.startRow == 0:
                if move.startCol == 0:
                    self.currentCastlingRights.bqs = False
                elif move.startCol == 7:
                    self.currentCastlingRights.bks = False
    def getvalidmoves(self):
        for log in self.moveLog:
            print(log.getChessNotation())
        # to store a copy of the enpassantPossible variable
        temp_enpassantPossible = self.enpassantPossible
        tempCastleRights = castleRights(self.currentCastlingRights.wks,self.currentCastlingRights.bks,self.currentCastlingRights.wqs,self.currentCastlingRights.bqs)
        # 1. generate all possible moves
        moves = self.getAllPossibleMoves()

        # 2. for each move, make the move

        if self.whitemove:
            self.getCastleMoves(self.whiteKingLocation[0],self.whiteKingLocation[1],moves)
        else:
            self.getCastleMoves(self.blackKingLocation[0],self.blackKingLocation[1],moves)


        # while removing an element from a list, we have to traverse the list backwards
        # because the indexes change after removing the element

        
        
        for i in range(len(moves)-1,-1,-1):

            # make move
            self.makeMove(moves[i])

            # 3. generate all possible moves for the opponent
            # 4. for each of your opponent's move, see if they attack your king
            self.whitemove = not self.whitemove
            if self.inCheck():
                moves.remove(moves[i])
            self.whitemove = not self.whitemove
            self.undoMove()


        # 3. generate all possible moves for the opponent
        # 4. for each of your opponent's move, see if they attack your king
        if len(moves) == 0:
            if self.inCheck():
                self.checkmate = True
            else:
                self.stalemate = True
        # if we undo the move, we have to set the checkmate and stalemate to false
        else:
            self.checkmate = False
            self.stalemate = False

        # because we are not making any move
        # we have to reset the enpassantPossible variable
        # to its original value
        
        self.enpassantPossible = temp_enpassantPossible

         
        # reset
        self.currentCastlingRights = tempCastleRights


        return moves
    
    def inCheck(self):
        if self.whitemove:
            return self.squareUnderAttack(self.whiteKingLocation[0],self.whiteKingLocation[1])
        else:
            return self.squareUnderAttack(self.blackKingLocation[0],self.blackKingLocation[1])
        
    def squareUnderAttack(self,r,c):
        self.whitemove = not self.whitemove
        opp_moves = self.getAllPossibleMoves()
        self.whitemove = not self.whitemove
        for move in opp_moves:
            if move.endRow == r and move.endCol == c:
                return True
        return False





    
    # all moves without considering checks
    def getAllPossibleMoves(self):

        # 
        


        # empty list for storing all possible moves 
        poss_moves = []
        # loop through all the squares in the board using nested for loop
        for rows in range(len(self.board)):
            for columns in range(len(self.board[rows])):

                # checking the first char of pieces
                # assigning moves to pieces according to their color
                turn = self.board[rows][columns][0]
                if (turn == 'w' and self.whitemove) or (turn == 'b' and not self.whitemove):
                    # if the piece is a pawn
                    # because each piece has its own set of rules
                    piece = self.board[rows][columns][1]
                    self.moveFunctions[piece](rows,columns,poss_moves)
                    # calls the proper function for each piece



        return poss_moves

    def getPawnMoves(self,rows,columns,poss_moves):
        # if white pawn
        #
        if self.whitemove:
            # if the square in front of the pawn is empty
            if self.board[rows-1][columns] == "--":
                # going a row ahead not diagonal so column reamins the same
                poss_moves.append(Move((rows,columns),(rows-1,columns),self.board))

                # if the pawn is in its starting position
                # for pawns first move
                # we can move two squares ahead
                # so append move rows-2

                # check two conditions for this
                # 1. the square two squares ahead is empty
                # pawn is at row 6 (its starting position)
                if rows == 6 and self.board[rows-2][columns] == "--":
                    poss_moves.append(Move((rows,columns),(rows-2,columns),self.board))
                    # mark this square by photo



            if columns-1 >= 0:
                if self.board[rows-1][columns-1][0] == 'b':
                    poss_moves.append(Move((rows,columns),(rows-1,columns-1),self.board))
                elif (rows-1,columns-1) == self.enpassantPossible:
                    # if the square is the enpassant square
                    # then we can capture the pawn
                    # so we have to add the move
                    poss_moves.append(Move((rows,columns),(rows-1,columns-1),self.board,enpassantPossible = True))
            if columns+1 <= 7:
                if self.board[rows-1][columns+1][0] == 'b':
                    poss_moves.append(Move((rows,columns),(rows-1,columns+1),self.board))
                elif (rows-1,columns+1) == self.enpassantPossible:
                    # if the square is the enpassant square
                    # then we can capture the pawn
                    # so we have to add the move
                    poss_moves.append(Move((rows,columns),(rows-1,columns+1),self.board,enpassantPossible = True))
        else:
            if self.board[rows+1][columns] == "--":
                poss_moves.append(Move((rows,columns),(rows+1,columns),self.board))
                if rows == 1 and self.board[rows+2][columns] == "--":
                    poss_moves.append(Move((rows,columns),(rows+2,columns),self.board))
            if columns-1 >= 0:
                if self.board[rows+1][columns-1][0] == 'w':
                    poss_moves.append(Move((rows,columns),(rows+1,columns-1),self.board))
                elif (rows+1,columns-1) == self.enpassantPossible:
                    # if the square is the enpassant square
                    # then we can capture the pawn
                    # so we have to add the move
                    poss_moves.append(Move((rows,columns),(rows+1,columns-1),self.board,enpassantPossible = True))
            if columns+1 <= 7:
                if self.board[rows+1][columns+1][0] == 'w':
                    poss_moves.append(Move((rows,columns),(rows+1,columns+1),self.board))
                elif (rows+1,columns+1) == self.enpassantPossible:
                    # if the square is the enpassant square
                    # then we can capture the pawn
                    # so we have to add the move
                    poss_moves.append(Move((rows,columns),(rows+1,columns+1),self.board,enpassantPossible = True))
    def getRookMoves(self,rows,columns,poss_moves):

        # to get the direction like vector without changing the value of the original tuple
        # back row,back column,forward row,forward column
        directions = ((-1,0),(0,-1),(1,0),(0,1))
        # white rook --> wR
        # black rook --> bR
        # so we can use the first character to check the color of the piece
        # and the second character to check the type of the piece
        # so we can use the second character to check the type of the piece
        # so we can use the second character to check the type of the piece
        enemy_color = "b" if self.whitemove else "w"
        for d in directions:
            for i in range(1,8):

                # direction into magnitude
                endRow = rows + d[0]*i

                # kaha into kitne se
                endCol = columns + d[1]*i
                # if the square is on the board

                if 0 <= endRow < 8 and 0 <= endCol < 8:
                    # square is on the board
                    endPiece = self.board[endRow][endCol]
                    # if the square is empty

                    # append the moves till the squares are empty
                    if endPiece == "--":
                        poss_moves.append(Move((rows,columns),(endRow,endCol),self.board))
                    elif endPiece[0] == enemy_color:
                        # move to capture the piece
                        poss_moves.append(Move((rows,columns),(endRow,endCol),self.board))
                        break
                        # cant go over the enemy piece
                    else:
                        # cant capture alsi
                        break
                        # cant go over your own piece
                else:
                    # all squares are out of board
                    break
        

    def getKnightMoves(self,rows,columns,poss_moves):
        knight_moves = ((-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1))
        ally_color = "w" if self.whitemove else "b"
        for m in knight_moves:
            endRow = rows + m[0]
            endCol = columns + m[1]
            if 0 <= endRow < 8 and 0 <= endCol < 8:
                
                endPiece = self.board[endRow][endCol]
                if endPiece[0] != ally_color:
                    # enemy hai kya
                    # nahi na
                    # toh move
                    poss_moves.append(Move((rows,columns),(endRow,endCol),self.board))

        
    def getBishopMoves(self,rows,columns,poss_moves):
        # bishop can move diagonally
        # left diagonal down, left diagonal up, right diagonal down, right diagonal up
        directions = ((-1,-1),(-1,1),(1,-1),(1,1))
        enemy_color = "b" if self.whitemove else "w"
        for d in directions:
            # maximum square limit
            for i in range(1,8):
                endRow = rows + d[0]*i
                endCol = columns + d[1]*i
                if 0 <= endRow < 8 and 0 <= endCol < 8:
                    endPiece = self.board[endRow][endCol]
                    if endPiece == "--":
                        poss_moves.append(Move((rows,columns),(endRow,endCol),self.board))
                    elif endPiece[0] == enemy_color:
                        poss_moves.append(Move((rows,columns),(endRow,endCol),self.board))
                        break
                    else:
                        break
                else:
                    break

        
    def getQueenMoves(self,rows,columns,poss_moves):

        self.getBishopMoves(rows,columns,poss_moves)
        self.getRookMoves(rows,columns,poss_moves)
       
    def getKingMoves(self,rows,columns,poss_moves):
        # all squares surrounding the king
        directions = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))

        # but just one move

        ally_color = "w" if self.whitemove else "b"
    
        for d in directions:
            # traversing for all possible moves
        
            endRow = rows + d[0]
            endCol = columns + d[1]

            # filtering out the moves that are out of board
            if 0 <= endRow < 8 and 0 <= endCol < 8:

                endPiece = self.board[endRow][endCol]

                # not running on a ally piece
                if endPiece[0] != ally_color:
                    poss_moves.append(Move((rows,columns),(endRow,endCol),self.board))

        # self.getCastleMoves(rows,columns,poss_moves)


    def getCastleMoves(self,rows,columns,poss_moves):
        if self.squareUnderAttack(rows,columns):
            return
        if (self.whitemove and self.currentCastlingRights.wks) or (not self.whitemove and self.currentCastlingRights.bks):
            self.getKingSideCastleMoves(rows,columns,poss_moves)
        if (self.whitemove and self.currentCastlingRights.wqs) or (not self.whitemove and self.currentCastlingRights.bqs):
            self.getQueenSideCastleMoves(rows,columns,poss_moves)

    def getKingSideCastleMoves(self,rows,columns,poss_moves):
        if self.board[rows][columns+1] == '--' and self.board[rows][columns+2] == '--':
            if not self.squareUnderAttack(rows,columns+1) and not self.squareUnderAttack(rows,columns+2):
                poss_moves.append(Move((rows,columns),(rows,columns+2),self.board,isCastleMove = True))


    def getQueenSideCastleMoves(self,rows,columns,poss_moves):
        if self.board[rows][columns-1] == '--' and self.board[rows][columns-2] == '--' and self.board[rows][columns-3] == '--':
            if not self.squareUnderAttack(rows,columns-1) and not self.squareUnderAttack(rows,columns-2):
                poss_moves.append(Move((rows,columns),(rows,columns-2),self.board,isCastleMove = True))


class castleRights():
    def __init__(self,wks,bks,wqs,bqs):
        self.wks = wks
        self.bks = bks
        self.wqs = wqs
        self.bqs = bqs
        # white king side, black king side, white queen side, black queen side
        


        

        




class Move():
    # map position from rows and columns to ranks and files in chess


    # so using dictionaries to map
    ranksToRows = {"1":7,"2":6,"3":5,"4":4,
                     "5":3,"6":2,"7":1,"8":0}
    
    # reversing the above dictionary
    rowsToRanks = {v:k for k,v in ranksToRows.items()}


    # using for converting columns to files
    filesToCols = {"a":0,"b":1,"c":2,"d":3,
                        "e":4,"f":5,"g":6,"h":7}
    colsToFiles = {v:k for k,v in filesToCols.items()}


    # fn with optional parameter
    def __init__(self,start_sq,end_sq,board,enpassantPossible = False,isCastleMove = False):
        # start_sq
        # source

        # end_sq
        # destination

        # board state passed to validate the move and store information about the move
        # what piece was captured? --> information

        # for first tuple that is sq_selected in player_clicks
        self.startRow = start_sq[0]
        self.startCol = start_sq[1]

        # for second tuple that is sq_selected in player_clicks
        self.endRow = end_sq[0]
        self.endCol = end_sq[1]

        # refers to pos in board
        self.pieceMoved = board[self.startRow][self.startCol] # piece moved
        
        # refers to pos in board
        self.pieceCaptured = board[self.endRow][self.endCol] # piece captured
        self.moveID = self.startRow*1000 + self.startCol*100 + self.endRow*10 + self.endCol

        # default value for flag
        self.pawn_promotion = False
        # conditions of location and piece for pawn promotion 
        if (self.pieceMoved == "wp" and self.endRow == 0) or (self.pieceMoved == "bp" and self.endRow == 7):
            self.pawn_promotion = True

        # flag for en passant move
        self.enpassantPossible = enpassantPossible
        if self.enpassantPossible:
            self.pieceCaptured = 'wp' if self.pieceMoved == 'bp' else 'bp'

        self.isCastleMove = isCastleMove
        # if pawn is moving two squares ahead
        # if self.pieceMoved[1] == 'p' and abs(self.startRow - self.endRow) == 2:
        #     self.isEnpassantMove = True
        # if pawn is moving two squares ahead
        # if the pawn moves two squares ahead





        # self.promotionChoice = "Q"   
        
        # we could write pawn promotion flags in the getpawnmoves itself but we chose this because of less new code to be written here
        print(self.moveID)
    

    def __eq__(self, other):
        # comparing this object to another object

        # to ensure that we are comparing two move objects and not some other class object
        if isinstance(other,Move):
            return self.moveID == other.moveID
        return False

    def getChessNotation(self):
        # you can add to make this like real chess notation
        return self.pieceMoved + "to" + self.getRankFile(self.startRow,self.startCol) + self.getRankFile(self.endRow,self.endCol)
    
    def getRankFile(self,rows,columns):
        return self.colsToFiles[columns] + self.rowsToRanks[rows]
    
    # castling
    # king cannot move to a square that is under attack
    # sqs clear
    # sqs cannot be under attack
    # king didnt move
    # king not in check
    # first move of king and rook