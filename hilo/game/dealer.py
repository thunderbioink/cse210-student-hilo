import random
from game.player import player


class dealer():

    def __init__(self):
        self.playing = True
        self.score = 300
        self.cards = []
        self.player = player()


    def start_game(self):
        while self.playing:
            self.draw_cards()
            self.player_input()
            self.update_score()
            self.game_output()


    def player_input(self):
        print(f'\nThe card is: {self.cards[0]}')
        self.player.player_guess()

    def draw_cards(self):
        self.cards.clear()
        for x in range(2):
            x = random.randint(1,13)
            self.cards.append(x)


    def update_score(self):
        if self.player.guess == 'h' and self.cards[0] < self.cards[1] or self.player.guess == 'l' and self.cards[0] > self.cards[1]:
            points = 100
        else:
            points = -75

        self.score += points

    
    def game_output(self):
        print(f'Next card was: {self.cards[1]}')
        print(f'Your score is: {self.score}')
        
        if self.score > 0:
            choice = input("Keep playing? [y/n] ")
            self.playing = (choice == "y")
        else:
            self.playing = False



# The card is: 11
# Higher or lower? [h/l] h
# Next card was: 13
# Your score is: 400
# Keep playing? [y/n] y
