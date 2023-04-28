import os
import json
from random import shuffle

class Card():
    def __init__(self, name, *tips) -> None:
        self._name = name
        self._tips = [*tips]
        # self._life = 5

    @property
    def name(self):
        return self._name

    @property
    def tips(self):
        return self._tips
    
    def selec_card(self):
        JSON_PATH = 'card_types.py'
        all_cards = []
        with open(JSON_PATH, 'r', encoding='utf8') as archive:
            cards = json.load(archive)
            for options in cards:
                all_cards.append(options)
            shuffle(all_cards)
        return all_cards[-1] 
            
    def print_tips(selected_card, z):
        tips = selected_card.tips
        os.system("cls")
        print(f'Type #{z+1}: {tips[0][z]}')
        
    def verify_answer(self, answer, life):
        if answer == self.name:
            print("Congrats buddy!! You won!")
            quit()
        else:
            life -= 1
            
    def play(self):
        z = 0
        life = 5
        while life > 0:
            self.print_tips(z)
            z += 1
            answer = str(input("Input your answer>> ")).capitalize()
            self.verify_answer(answer, life)
