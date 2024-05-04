import time
'''
    Defines Player class, and subclasses Human and Minimax Player.
'''

class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    #PYTHON: use obj.symbol instead
    def get_symbol(self):
        return self.symbol
    
    #parent get_move should not be called
    def get_move(self, board):
        raise NotImplementedError()


class HumanPlayer(Player):
    def __init__(self, symbol):
        Player.__init__(self, symbol)

    def clone(self):
        return HumanPlayer(self.symbol)
    
    def valid_input(self, input):
        try:
            int(input)
            return True
        except ValueError:
            return False
        
#PYTHON: return tuple instead of change reference as in C++
    def get_move(self, board):
        print("Moves: ", board.get_legal_moves(self.symbol))
        col = -1
        row = -1
        try: # i dont like the way this is, but input() is an annoying function
            col = int(input("Enter column: "))
            row = int(input("Enter row: "))
        except:
            print("Invalid input")
        while (col, row) not in board.get_legal_moves(self.symbol):
            while not self.valid_input(col):
                col = int(input("Enter column: "))
            while not self.valid_input(row):
                row = int(input("Enter row: "))

        return col, row


class MinimaxPlayer(Player):

    def __init__(self, symbol):
        Player.__init__(self, symbol)
        if symbol == 'X':
            self.oppSym = 'O'
        else:
            self.oppSym = 'X'

        self.maxDepth = 5

    def clone(self):
        return MinimaxPlayer(self.symbol)

    def minimax(self, board, depth, symbol):
        sign = 1
        if symbol == self.oppSym:
            sign = -1

        best_eval = float('-inf') * sign
        best_move = None

        if depth == self.maxDepth:
            return board.count_score(self.symbol) * sign, None

        for move in board.get_legal_moves(symbol):
            newBoard = board.clone_of_board()
            newBoard.play_move(move[0], move[1], symbol)

            if symbol == self.symbol:
                eval, _ = self.minimax(newBoard, depth + 1, self.oppSym) #switch symbol
                if eval > best_eval:
                    best_eval = eval
                    best_move = move
            else:
                eval, _ = self.minimax(newBoard, depth + 1, self.symbol) #same
                if eval < best_eval:
                    best_eval = eval
                    best_move = move

        if best_move is None:
            return board.count_score(self.symbol) * sign, None
        
        return best_eval, best_move
    
    def get_move(self, board):
        #start timer
        start = time.time()

        #get best move
        s, best_move = self.minimax(board, 0, self.symbol)
        
        if best_move is None:
            print("No legal moves")
            return None
        
        #end timer
        end = time.time()

        #print time
        print("Minimax ", self.symbol, " took ", end - start, " seconds.")
        print("and chose ", best_move, " with score ", s)

        #if time is greater than 2 seconds, fuk it remove 1 from depth
        if end - start > 2:
            print("Trimming depth, took ", end - start, " seconds.")
            self.maxDepth -= 1

        return best_move
        

        



