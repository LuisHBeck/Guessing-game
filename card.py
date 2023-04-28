import os
# import json
# from random import shuffle

class Card():
    def __init__(self, name, tip1, tip2, tip3, tip4, tip5) -> None:
        self._name = name
        self._tips = [tip1, tip2, tip3, tip4, tip5]
        self._life = 5

    @property
    def name(self):
        return self._name

    @property
    def tips(self):
        return self._tips
    
    # def select_card(self):
    #     JSON_PATH = 'card_types.py'
    #     all_cards = []
    #     with open(JSON_PATH, 'r', encoding='utf8') as archive:
    #         cards = json.load(archive)
    #         for options in cards:
    #             all_cards.append(options)
    #         shuffle(all_cards)
    #     print(all_cards) 
            
    def print_tips(self, z):
        # tips = selected_card.tips
        tips = self.tips
        os.system("cls")
        print(f'Type #{z+1}: {tips[z]}')
        
    def verify_answer(self, answer):
        if answer == self.name:
            print("Congrats buddy!! You won!")
            quit()
        else:
            self._life -= 1

    def lose(self):
        if self._life == 0:
            print('You lose!')
            quit
            
    def play(self):
        z = 0
        while self._life > 0:
            self.print_tips(z)
            z += 1
            answer = str(input("Input your answer>> ")).capitalize()
            self.verify_answer(answer)
            self.lose()
