class Player():
    def __init__(self, name) -> None:
        '''
        construtor da classe jogador
        :param name: nome do jogador
        '''
        self.__name = name
        self.__life = 5
        self.__card = None

    @property
    def name(self):
        '''
        retornar o nome do jogador
        :return: nome do jogador
        '''
        return self.__name
    
    @property
    def life(self):
        '''
        retornar vida
        :return: vida do jogador
        '''
        return self.__life

    @property
    def card(self):
        '''
        retornar o cartão
        :return: cartão sorteado
        '''
        return self.__card
    
    @card.setter
    def card(self, card):
        '''
        setter para o cortão
        :param card: o cartão sorteado
        :return: none
        '''
        self.__card = card
