""" This is a sub program for game_engine.py that creates the board 
and defines legal/available moves for Othello """
def initialise_board(size=8):
    """ creates the othello board and defines the set size of 8
    as parameter and returns the board """
    board = [[None for _ in range(size)] for _ in range(size)]
    #insert the white and black in center
    board[3][3] = "White"
    board[4][4] = "White"
    board[4][3] = "Black"
    board[3][4] = "Black"
    return board
def print_board(board):
    """ prints the othello board to the terminal, 
    created by initialise board and passed as board """
    for row in board :
        for element in row:
            #iterates over row and column and checks whats in each space
            if element is None: # prints N followed by the 5 trailing spaces if value is None
                print("N", end="     ")
            else:
                print(element[0], end="     ")
                # prints first letter of the colour in that position if not None value
        print()
    return
def legal_move(colour, coord, board):
    """ defines legal moves using the given coordinates, 
    colour moving and game board spaces available, 
    all passed as parameters and returns if the move is legal, 
    along with the places to flip for that specific move """
    xcoord, ycoord = coord
    opponent = 'White' if colour == 'Black' else 'Black'
    # space must be None
    if board[xcoord][ycoord] is not None:
        return False, []
    places_to_flip = []
    # all 8 possible directions for a move to be taking pieces to check
    directions = [
        (-1, 0), (-1, 1), (0, 1), (1, 1),
        (1, 0), (1, -1), (0, -1), (-1, -1)
    ]
    for dx, dy in directions:
        x, y = xcoord + dx, ycoord + dy
        temp = []
        if not (0 <= x < 8 and 0 <= y < 8): # must be between 0 and 8 to be on the board
            continue
        if board[x][y] != opponent: # opponent square must be first
            continue
        # continues in direction
        while 0 <= x < 8 and 0 <= y < 8:
            if board[x][y] is None:
                break
            if board[x][y] == colour:
                #flip temp squares
                places_to_flip.extend(temp)
                break
            temp.append((x, y))
            x += dx # increments while loop
            y += dy
    # no direction made
    if not places_to_flip:
        return False, []
    return True, places_to_flip
