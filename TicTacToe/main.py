from tictactoe import TicTacToe

game = TicTacToe()

print(r'''

  _______ _        _______           _______         
 |__   __(_)      |__   __|         |__   __|        
    | |   _  ___     | | __ _  ___     | | ___   ___ 
    | |  | |/ __|    | |/ _` |/ __|    | |/ _ \ / _ \
    | |  | | (__     | | (_| | (__     | | (_) |  __/
    |_|  |_|\___|    |_|\__,_|\___|    |_|\___/ \___/
                                                     
''')

off = False
while not off:
    GAME_OVER = False
    player_symbol = input("Enter your choice of game piece (X or O): ").upper()
    game.assign_symbol(player_symbol)
    go_first_choice = input("Would you like to go first (Yes or No): ").lower()

    #Play
    while not GAME_OVER:
        game.clear_screen()
        game.grid()

        if go_first_choice == "yes":
            game.player_plays()
            if game.review_grid() == True:
                print("You win!")
                GAME_OVER = True
            else:
                game.computer_plays()
                if game.review_grid() == True:
                    print("You lose!")
                    GAME_OVER = True
        else:
            game.computer_plays()
            if game.review_grid() == True:
                print("You lose!")
                GAME_OVER = True
            else:
                game.player_plays()
                if game.review_grid() == True:
                    print("You win!")
                    GAME_OVER = True

    game.reset_grid()
    if input("Do you want to play again? (Yes or No): ").lower() == "no":
        off=True