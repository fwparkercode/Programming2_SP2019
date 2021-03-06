'''
kivy card dealer
starter code for card game projects in kivy
'''


import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.size = [400, 600]
Window.clearcolor = [0,0,0,1]

class CardsApp(App):
    def build(self):
        return CardTable()

class Deck():
    def __init__(self):
        self.suits = ["s", "d", "h", "c"]
        self.cards = ["a", "k", "q", "j", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
        self.card_names = []
        for suit in self.suits:
            for card in self.cards:
                self.card_names.append(suit+card)

        print(len(self.card_names))






class CardTable(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.hand = ["" for x in range(5)]
        self.deck = Deck()
        self.cards = [self.card0, self.card1, self.card2, self.card3, self.card4]

    def deal_hand(self, number_cards):
        for card in self.cards:
            card.image_file = "pic/black.png"

        self.hand = ["" for x in range(5)]

        for i in range(number_cards):
            self.hand[i] = self.deck.card_names.pop(random.randrange(len(self.deck.card_names)))


        for i in range(number_cards):
            filename = "pic/"+self.hand[i]+".png"
            self.cards[i].image_file=filename
        print(self.hand)

    def hit_me(self):
        next_card = 5 - self.hand.count("")
        self.hand[next_card] = self.deck.card_names.pop(random.randrange(len(self.deck.card_names)))
        for i in range(next_card + 1):
            filename = "pic/"+self.hand[i]+".png"
            self.cards[i].image_file=filename
        print(self.hand)







if __name__ == "__main__":
    app = CardsApp()
    app.run()
