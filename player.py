class Player():
    def __init__(self, name) -> None:
        self.__name = name
        self.__life = 5
        self.__card = None

    @property
    def name(self):
        return self.__name
    
    @property
    def life(self):
        return self.__life

    @property
    def card(self):
        return self.__card
    
    @card.setter
    def card(self, card):
        self.__card = card
