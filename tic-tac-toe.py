
matrix = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# Functions
def result(player: str) -> None:

    print(f"\n\n\tResult: {player} Wins\n\n\t\t{matrix[0]}\n\t\t{matrix[1]}\n\t\t{matrix[2]}")
    return

def check_all_matrix() -> bool:

    if " " in matrix:
        return False
    else:
        return True

def check_vertical() -> bool:

    if (((matrix[0][0] == matrix [1][1] == matrix[2][2]) and matrix[0][0] != " ") or
            ((matrix[0][2] == matrix[1][1] == matrix[2][0]) and matrix[0][2] != " ")):
        return True
    return False

def check_column(index: int) -> bool:

    if matrix[0][index] == matrix[1][index] == matrix[2][index] and matrix[0][index] != " ":
        return True
    return False

def check_line(index: int)-> bool:

        if matrix[index][0] == matrix[index][1] == matrix[index][2] and matrix[index][0] != " ":
            return True
        return False

def check_game() -> bool:

    for line in range(0, 2):
        if check_line(line) or check_column(line) or check_vertical():
            return True
    return False

def mark_pos(player: str, mark_sign: str) -> None:

    position = marked_line = int(0)

    print(f"\n\t\t{matrix[0]}\n\t\t{matrix[1]}\n\t\t{matrix[2]}")
    position = int(input(f"\nWhat's the position for {player}: "))

    while position > 3:
        marked_line += 1
        position -= 3

    marked_column = position - 1

    if matrix[marked_line][marked_column] == " ":
        matrix[marked_line][marked_column] = mark_sign
    else:
        print("Position already marked, choose another")
        mark_pos(player, mark_sign)

def menu() -> None:

    print("\n\t======================"
          "\n\t== Tic-Tac-Toe Game =="
          "\n\t======================")

    player1_name = str(input("\n\tWhat's the name of the Player 1: "))
    player2_name = str(input("\n\tWhat's the name of the Player 2: "))

    player1_mark = str(input(f"\nWhich one would be the sign of the player {player1_name}: "))
    player2_mark = str(input(f"\nWhich one would be the sign of the player {player2_name}: "))

    turn = 0

    while not check_all_matrix():

        if turn % 2 == 0:

            mark_pos(player1_name, player1_mark)

            if check_game():
                result(player1_name)
                return
        else:

            mark_pos(player2_name, player2_mark)

            if check_game():
                result(player2_name)
                return
        turn += 1

    print(f"\n\n\tResult: Draw\n\n\t\t{matrix[0]}\n\t\t{matrix[1]}\n\t\t{matrix[2]}")


# Main
menu()