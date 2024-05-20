
# Función para imprimir el tablero de Tic-Tac-Toe de manera legible
def print_board(board):
    # Imprimir la cabecera con los números de columna
    print("  0 1 2")
    # Iterar sobre cada fila y su índice
    for i, row in enumerate(board):
        # Imprimir el índice de la fila y su contenido, separando los elementos con '|'
        print(f"{i} {'|'.join(row)}")
        # Si no es la última fila, imprimir la línea separadora
        if i < 2:
            print("  -----")

# Función para verificar si hay un ganador o un empate
def check_winner(board):
    # Verificar filas y columnas
    for i in range(3):
        # Verificar si una fila tiene el mismo valor y no está vacía
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        # Verificar si una columna tiene el mismo valor y no está vacía
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    # Verificar diagonales
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    # Verificar si hay empate (no hay espacios vacíos)
    for row in board:
        if " " in row:
            return None
    return "Tie"

# Función Minimax para encontrar la mejor jugada posible
def minimax(board, depth, is_maximizing):
    # Verificar el estado actual del juego
    winner = check_winner(board)
    if winner == "X":
        return -1  # El jugador humano gana
    elif winner == "O":
        return 1  # La IA gana
    elif winner == "Tie":
        return 0  # Empate

    # Si es el turno del Maximizing Player (IA)
    if is_maximizing:
        best_score = -float("inf")
        # Probar cada celda vacía en el tablero
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"  # Realizar la jugada
                    score = minimax(board, depth + 1, False)  # Llamada recursiva
                    board[i][j] = " "  # Deshacer la jugada
                    best_score = max(score, best_score)  # Obtener el mejor resultado
        return best_score
    # Si es el turno del Minimizing Player (jugador humano)
    else:
        best_score = float("inf")
        # Probar cada celda vacía en el tablero
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"  # Realizar la jugada
                    score = minimax(board, depth + 1, True)  # Llamada recursiva
                    board[i][j] = " "  # Deshacer la jugada
                    best_score = min(score, best_score)  # Obtener el mejor resultado
        return best_score

# Función para encontrar la mejor jugada para la IA
def best_move(board):
    best_score = -float("inf")
    move = None
    # Probar cada celda vacía en el tablero
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"  # Realizar la jugada
                score = minimax(board, 0, False)  # Llamada a Minimax
                board[i][j] = " "  # Deshacer la jugada
                if score > best_score:
                    best_score = score
                    move = (i, j)  # Actualizar la mejor jugada
    return move

# Función principal para jugar el juego
def play_game():
    # Inicializar el tablero vacío
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

    player = "X"  # Jugador humano
    ai = "O"      # Jugador IA

    for _ in range(9):
        if check_winner(board):
            break  # Salir del bucle si hay un ganador o empate
        
        if player == "X":
            # Pedir al jugador humano que ingrese su jugada
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter col (0-2): "))
            if board[row][col] == " ":
                board[row][col] = player  # Realizar la jugada del jugador humano
                player = ai  # Cambiar el turno a la IA
        else:
            move = best_move(board)  # Obtener la mejor jugada para la IA
            if move:
                board[move[0]][move[1]] = ai  # Realizar la jugada de la IA
                player = "X"  # Cambiar el turno al jugador humano
        
        print_board(board)  # Imprimir el tablero actual
        winner = check_winner(board)
        if winner:
            if winner == "Tie":
                print("It's a tie!")  # Anunciar empate
            else:
                print(f"The winner is {winner}!")  # Anunciar ganador
            break  # Salir del bucle si hay un ganador o empate

# Ejecutar la función principal para jugar el juego
play_game()

