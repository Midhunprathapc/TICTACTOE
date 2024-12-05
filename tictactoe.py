def print_board(pattern):
    print(f" {pattern[0]} | {pattern[1]} | {pattern[2]} ")
    print("-----------")
    print(f" {pattern[3]} | {pattern[4]} | {pattern[5]} ")
    print("-----------")
    print(f" {pattern[6]} | {pattern[7]} | {pattern[8]} ")


def check_winner(pattern, player):

    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]             
    ]
    for combo in win_combinations:
        if pattern[combo[0]] == pattern[combo[1]] == pattern[combo[2]] == player:
            return True
    return False


def tic_tac_toe():
    playboard = [" "] * 9 
    players={"player 1":"x","player 2":"o"} 
    current_player = "player 1"

    for i in range(9):
        print_board(playboard)
        print(f"Player {current_player}'s turn ({players[current_player]}).")
        try:
            position = int(input("Enter a position (1-9): ")) - 1 
        except ValueError:
            print("invalid input.enter the position(1-9)")
            continue
        

        if position < 0 or position > 8 or playboard[position] != " ":
            print("Invalid move! Try again.")
            continue

        playboard[position] = players[current_player]

        
        if check_winner(playboard, players[current_player]):
            print_board(playboard)
            print(f"Player {current_player} wins!")
            return

        current_player = "player 2" if current_player == "player 1" else "player 1"

    print_board(playboard)
    print("It's a draw!")


tic_tac_toe()
