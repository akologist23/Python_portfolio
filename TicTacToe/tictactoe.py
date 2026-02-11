import time
import random

from fontTools.pens.basePen import NullPen


class TicTacToe:
    def __init__(self):
        self.grid_dic = {
            "a": " ",
            "b": " ",
            "c": " ",
            "d": " ",
            "e": " ",
            "f": " ",
            "g": " ",
            "h": " ",
            "i": " "
        }
        self.player_symbol = None
        self.computer_symbol = None

    def grid(self):
        l = self.grid_dic
        print(f'''

        Reference                     Game
      a  |  b  |  c              {l['a']}  |  {l['b']}  |  {l['c']}   
    -----|-----|-----          -----|-----|-----   
      d  |  e  |  f              {l['d']}  |  {l['e']}  |  {l['f']}   
    -----|-----|-----          -----|-----|-----
      g  |  h  |  i              {l['g']}  |  {l['h']}  |  {l['i']}   

        ''')

    def reset_grid(self):
        #global self.grid_dic
        for key in self.grid_dic.keys():
            self.grid_dic[key] = " "

    def clear_screen(self):
        print("\n" * 10)

    def assign_symbol(self, player_choice):
        if player_choice == "X":
            self.player_symbol = "X"
            self.computer_symbol = "O"
        else:
            self.player_symbol = "O"
            self.computer_symbol = "X"
    
    def check_game_end(self):
        total = 0
        for key in self.grid_dic.keys():
            if self.grid_dic[key] == " ":
                total += 1
        if total == 0:
            return True
        else:
            return False
    
    def check_score(self):
        if (self.grid_dic['a'] == self.grid_dic['b'] == self.grid_dic['c']) and self.grid_dic['a'] != " ":
            return True
        elif self.grid_dic['d'] == self.grid_dic['e'] == self.grid_dic['f'] and self.grid_dic['d'] != " ":
            return True
        elif self.grid_dic['g'] == self.grid_dic['h'] == self.grid_dic['i'] and self.grid_dic['g'] != " ":
            return True
        elif self.grid_dic['a'] == self.grid_dic['d'] == self.grid_dic['g'] and self.grid_dic['a'] != " ":
            return True
        elif self.grid_dic['b'] == self.grid_dic['e'] == self.grid_dic['h'] and self.grid_dic['b'] != " ":
            return True
        elif self.grid_dic['c'] == self.grid_dic['f'] == self.grid_dic['i'] and self.grid_dic['c'] != " ":
            return True
        elif self.grid_dic['a'] == self.grid_dic['e'] == self.grid_dic['i'] and self.grid_dic['a'] != " ":
            return True
        elif self.grid_dic['g'] == self.grid_dic['e'] == self.grid_dic['c'] and self.grid_dic['g'] != " ":
            return True
        else:
            return False

    def review_grid(self):
        if self.check_score() == True:
            return True
        elif self.check_game_end() == True:
            return True
        else:
            return False

    def computer_plays(self):
        #global self.grid_dic
        print("Computer is thinking...")
        time.sleep(2)
        free_letters = []
        for letter in self.grid_dic:
            if self.grid_dic[letter] == " ":
                free_letters.append(letter)
        opponent_choice = random.choice(free_letters)
        self.grid_dic[opponent_choice] = self.computer_symbol
        self.clear_screen()
        self.grid()

    def player_plays(self):
        #global self.grid_dic
        success = False
        while not success:
            letter = input("Select a free letter to play:  ").lower()
            if letter not in ["a", "b", "c", "d", "e", "f", "g", "h", "i"]:
                print("Please enter a valid letter.")
            else:
                success = True
                self.grid_dic[letter] = self.player_symbol
                self.clear_screen()
                self.grid()