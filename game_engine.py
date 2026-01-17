"""This program starts a game of othello inside the python terminal"""
import components
from components import legal_move

def cli_coords_input():
    """takes input of x and y coordinates to make the current move and 
    return the players current move coordinate"""
    while True:
        try:
            print("\n (Input your move coordinates in the format ' (x,y) ' : ")
            input_position = input()
            x = int(input_position[1]) # saving their input to usable variables
            y = int(input_position[3])
            if 0 <= x < 8:
                if 0 <= y < 8: # checking if both coordinates are on the actual board
                    print("That move position is valid!")
                    coord_tuple = (x, y) # creates the coordinate tuple
                    return coord_tuple
                print("Your Y coordinate is not valid!")
                continue
            print("Your X coordinate is not valid!")
            continue
        except ValueError:#a worse case fail safe for if an error occurs
            print("Invalid input.")
def simple_game_loop():
    """ starts the game of othello and eventually outputs the winner and ends the game """
    print("Welcome to the begininng of your game of Othello!")
    # declare the most important starting values
    board = components.initialise_board()
    move_counter = 60
    player = 'Black' # starting player is always black in othello
    def available_move_check(colour, board): # needs to check if their is available moves
        legal_coords = []
        length = 8
        for row in range(length):
            for column in range(length): # loops through every element in the board
                if board[row][column] is None:
                    if components.legal_move(colour, [row, column], board)[0]:
                        legal_coords.append((row, column)) # if the current element is empty and
                        # a legal move its added to legal coords list
        return legal_coords
    def make_move(colour, coord, board):
        legal = legal_move(colour, coord, board)[0]#stores boolean value if the move is legal
        pieces_to_swap = legal_move(colour, coord, board)[1] #stores list of pieces to
        #swap from the given coords
        if legal is False: #is move legal
            return False # move not valid
        #places the piece and flips relevenat pieces
        board[coord[0]][coord[1]] = colour
        for row, column in pieces_to_swap: #loops through changing all values
            #to flip from legal move function output
            board[row][column] = colour
        return True # valid move and pieces changed succesfully
    def player_changer(player): # changes player colour/turn
        if player == 'White':
            next_player = 'Black'
        else:
            next_player = 'White'
        return next_player
    def win_sequence(board):
        white_count = 0
        black_count = 0
        for row in board:
            for element in row: # loops through every element in every row
                if element == 'Black':
                    black_count = black_count + 1
                elif element == 'White':
                    white_count = white_count + 1
        return white_count, black_count # returns total black and white pieces on board
    while move_counter > 0: # ensures their is moves left to play
        print()
        components.print_board(board)
        print("It is currently " + player + "'s turn.")
        player_moves = available_move_check(player, board)
        if not player_moves: # ensures their is moves left to play
            print("No moves for " + player + ".")
            other = player_changer(player) # opponents colour value
            other_moves = available_move_check(other, board) #checks if opponent has possible moves
            if not other_moves: # if neither player has possible moves
                print("No legal moves for either player")
                break
            print("Skipping turn. Now its " + other + "'s turn.")
            player = other # changes current player to opponent/other
            continue
        while True:
            coords = cli_coords_input() # input from player
            if make_move(player, coords, board): # if move coords are valid
                move_counter = move_counter - 1 # one less total move as a valid move has happened
                player = player_changer(player) # swaps player because move is complete
                break # stop loop
            print("Illegal move. Try one of these moves.")
            print(player_moves) # prints available moves for current player
    white_score, black_score = win_sequence(board)
    print("Game over!")
    if white_score > black_score: # compates scores and prints the winner
        print("The winner is White!")
    elif black_score > white_score:
        print("The winner is Black!")
    else:
        print("Their is no certain winner.")
    print("White had " + str(white_score) + " counters")
    print("Black had " + str(black_score) + " counters")
# starts simple game loop, which starts the entire program
if __name__ == "__main__":
    simple_game_loop()
