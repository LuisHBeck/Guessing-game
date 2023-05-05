import os

class Card():
    def __init__(self, name) -> None:
        '''
        construtor
        :param name: nome da carta
        '''
        self._name = name
        self._tips = []
        self._life = 5

    @property
    def name(self):
        '''
        retorna o nome da carta
        :return: carta selecionada
        '''
        return self._name

    @property
    def tips(self):
        '''
        retorna as dicas
        :return: dicas de cada carta
        '''
        return self._tips
    
    def add_tips(self, *tips):
        '''
        adicionar as dicas
        :param tips: todas as dicas
        :return: none
        '''
        for tip in tips:
            self._tips.append(tip)

    def play(self, name, life):
        z = 0
        while life > 0:
            os.system("cls")
            print(f'Type #{z+1}: {self.tips[z]}')
            z += 1
            x = str(input("Input your answer>> ")).capitalize()
            if x == self.name:
                print("Congrats buddy!! You won!")
                print()
                break
            else:
                life -= 1
                if life == 0:
                    print(f"Unfortunately you lost, {name}!")
                    print()
                    break
            
            