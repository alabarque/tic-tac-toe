# although the board is hard-coded to 3x3, this can be changed to have an NxN tic-tac-toe
# could be change to something like:
# ['_' for x in range(n) for y in range(n)]
board = [  
    ['_','_','_'],
    ['_','_','_'],
    ['_','_','_']
]

class WrongLocationError(Exception):
    "el valor esta fuera del rango"
    pass

class UsedLocationError(Exception):
    "el valor ya esta usado en esa ubicacion"
    pass

# main method, handles the game
def tateti():
    print(center_string("TA-TE-TI"))
    print("""   Como jugar: 
    Se debe ingresar el indice de la fila y de la columna.
    Las filas y las columnas estan representadas del 0 al 2
    Por ejemplo, el centro-arriba del tablero esta en la fila 0, columna 1""")
    i = 0
    while True:
        printBoard(board)
        location_x = receiveInt('escriba la fila donde ubicar su proxima jugada: ')
        location_y = receiveInt('escriba la columna donde ubicar su proxima jugada: ')
        try:
            place(board, location_x, location_y, i)
            i = i+1
        except IndexError:
            print('esa ubicacion esta fuera del tablero, seleccionar un valor entre 0 y 2')
        except WrongLocationError:
            print('esa ubicacion esta fuera del tablero, seleccionar un valor entre 0 y 2')
        except UsedLocationError:
            print('esa ubicacion ya esta usada, seleccionar otra')
        else:
            if(victory(board) or max_plays(board, i)):
                printBoard(board)
                return


def center_string(str):
    return str.center(60, '-')


# receives an input for the next play
def receiveInt(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print('solo se aceptan numeros, escribir un numero')

# places the play on the location x,y
def place(board, x, y, i):
    if(x < 0 or y < 0):
        raise WrongLocationError
    if ('X' in board[x][y] or 'O' in board[x][y]):
        raise UsedLocationError
    board[x][y] = x_o(i)

# gets the next char to play based on the turn i
def x_o(i):
    if(i % 2 == 0):
        return 'X'
    else:
        return 'O'

# checks if any of the players won
def victory(board):
    victory = False
    if check_victory(board, 'X'):
        print(center_string('Ganador jugador 1'))
        victory = True
    if check_victory(board, 'O'):
        print(center_string('Ganador jugador 2'))
        victory = True
    return victory

# checks if any player won on the rows, columns or diagonals
def check_victory(board, player):
    if (check_victory_rows(board, player) or
    check_victory_columns(board, player) or
    check_victory_diagonals(board, player)):
        return True
    return False

# checks if any of the rows have all the same elements as the player
def check_victory_rows(board, player):
    for x in board:
        if x.count(player) == len(x):
            return True

# checks if any of the columns have all the same elements as the player
def check_victory_columns(board, player):
    return check_victory_rows(transpose(board), player)

def transpose(board):
    return [list(x) for x in list(zip(*board))]

# checks if any of the diagonals have all the same elements as the player
def check_victory_diagonals(board, player):
    return check_victory_rows(diagonals(board), player)

def diagonals(board):
    aux_board = []
    aux_board.append([board[x][x] for x, r in enumerate(board)])
    aux_board.append([board[x][-1-x] for x, r in enumerate(board)])
    return aux_board

# prints the current state of the board
def printBoard(board):
    for r in board:
        print('|{}|'.format('|'.join(r)))

# checks if the game has reached it's, which is when it hits the matrix's size
def max_plays(board, i):
    tie = False
    if i == len(board)*len(board[0]):
        print('el juego ha terminado en empate')
        tie = True
    return tie


if __name__ == "__main__":
    tateti()