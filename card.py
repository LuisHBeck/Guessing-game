class Card():
    def __init__(self, name) -> None:
        self._name = name
        self._tips = []
        self._life = 5

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def tips(self):
        return self._tips
    
    def add_tips(self, *tips):
        for tip in tips:
            self._tips.append(tip)

    def lose_file(self, value=1):
        return self._life - value

    def play(self):
        z = 0
        while self._life > 0:
            print(f'Type #{5-z}: {self.tips[z]}')
            z += 1
            print()
            x = str(input("Input your answer>> ")).capitalize()
            if x == self.name:
                print("You won!")
                break
            else:
                self._life -= 1