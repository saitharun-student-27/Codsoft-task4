import random as r
import time

class RPS:
    def __init__(self):
        self.user_score = 0
        self.computer_score = 0
        self.choices = ['rock', 'paper', 'scissors']
        self.round = 0

    def user_choice(self):
        self.user = input('Enter your choice (rock, paper, scissors):\n').lower()
        if self.user in self.choices:
            return self.user
        else:
            print('Invalid input, please enter again.\n')
            return self.user_choice()  # ask again if invalid

    def computer_choice(self):
        self.computer = r.choice(self.choices)
        return self.computer

    def game(self, computer, user):
        if user == computer:
            return 'tie'
        elif (user == 'rock' and computer == 'scissors') or \
             (user == 'scissors' and computer == 'paper') or \
             (user == 'paper' and computer == 'rock'):
            self.user_score += 1
            return 'user_wins'
        else:
            self.computer_score += 1
            return 'computer_wins'

    def play_game(self, computer, user, result):
        print(f'\nYOUR CHOICE: {user}')
        print(f'COMPUTER CHOICE: {computer}\n')
        print('READY! SET! GO!\n')
        time.sleep(1)
        print(f'THE RESULTS OF ROUND {self.round}\n')
        time.sleep(1)

        if result == 'tie':
            print('IT\'S A TIE THIS ROUND!\n')
        elif result == 'user_wins':
            print('YOU WON THIS ROUND! GREAT JOB!\n')
        elif result == 'computer_wins':
            print('COMPUTER WON THIS ROUND!\n')

        print(f'SCORE -> YOUR SCORE: {self.user_score} | COMPUTER SCORE: {self.computer_score}\n')

    def play(self):
        print('WELCOME TO ROCK PAPER SCISSORS!\n')
        while True:
            self.round += 1
            user = self.user_choice()
            computer = self.computer_choice()
            result = self.game(computer, user)
            self.play_game(computer, user, result)

            play_again = input('Do you want to play again (YES/NO):\n').upper()
            if play_again != 'YES':
                print('\nTHANKS FOR PLAYING!\n')
                print(f'FINAL SCORES -> YOUR SCORE: {self.user_score} | COMPUTER SCORE: {self.computer_score}')
                break


# Start the game
game = RPS()
game.play()
