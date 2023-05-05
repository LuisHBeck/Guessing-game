import inquirer
from player import Player
from card import Card
from card_types import vehicles, country, people
from random import choice


def game_type():
    card_type = [
            inquirer.List('type',
                            message="Select your card type:",
                            choices=['Vehicles', 'Country', 'People'],
                            ),
            ]
    answers = inquirer.prompt(card_type)
    return answers['type']

def player():
    name = str(input('Input your name>> '))
    person = Player(name)

    mode = game_type()

    if mode == "Vehicles":
        card = choice(vehicles)
    elif mode == "Country":
        card = choice(country)
    elif mode == 'People':
        card = choice(people)

    person.card = card
    person.card.play(person.name, person.life)

        

