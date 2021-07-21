class Money:
    def __init__(self, name= None, symbol= None ):
        self.kind = ''
        self.name = name
        self.symbol = symbol

    def __str__(self) -> str:
        return f'The {self.name} is {self.kind} money and has symbol {self.symbol}'

    def money_type(self):
        return self.kind

    
    def get_dollars(self):
        ask = input('Do you want change some euros? yes/no ')
        if ask == 'yes':
            change= float(input('How much euro? '))
            return f'The {change} euros equals {change *1.17} dollars'
    


class Paper(Money):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.kind = 'paper'


class Coin(Money):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.kind = 'metal'

    def coin_to_banknote(self):
        x= float(input('How many coins do you want to change? '))
        return f'The {x} equals {x * 0.01} paper money'


euro = Paper(name= 'Euro', symbol= '€' )
euro_cent = Coin(name= 'Euro cent', symbol= '€')
dollar = Paper(name= 'Dollar', symbol= '$' )
cent = Coin(name= 'Cent', symbol= '$' )

print(euro)
print(euro_cent)
print(dollar)
print(cent)

print(euro.money_type())
print(euro_cent.money_type())

print(Paper.get_dollars(euro))
print(Coin.coin_to_banknote(euro_cent))

