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

    def utility(self, board):
        #todo

    def minimax(self, board, depth, symbol):
        if symbol == self.symbol:
            #maximizing player
        
        else:
            #minimizing player


    def get_move(self, board):
        #start timer
        start = time.time()

        #get best move
        best_move = self.minimax(board, 0, self.symbol)

        #end timer
        end = time.time()

        #print time
        print("Minimax " + self.symbol + " move took: " + str(end - start) + " seconds")

        return best_move
        

        



