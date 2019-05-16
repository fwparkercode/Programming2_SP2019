'''
kivy card dealer
starter code for card game projects in kivy
'''


import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.core.window import Window

Window.size = [400, 600]
Window.clearcolor = [0,0,0,1]

class PokerApp(App):
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
        self.dealt = False

        # pairjack, high_pair, two_pair, three_kind, straight, flush, full_house, four_kind, straight_flush, royal
        self.wins = [False for x in range(10)]


    def deal_hand(self):
        for card in self.cards:
            card.image_file = "pic/black.png"


        for i in range(5):
            if not self.cards[i].locked:
                self.hand[i] = self.deck.card_names.pop(random.randrange(len(self.deck.card_names)))
            filename = "pic/" + self.hand[i] + ".png"
            self.cards[i].image_file = filename

        # check for wins
        self.check_hand()
        print(self.wins)




    def hit_me(self):
        next_card = 5 - self.hand.count("")
        self.hand[next_card] = self.deck.card_names.pop(random.randrange(len(self.deck.card_names)))
        for i in range(next_card + 1):
            filename = "pic/"+self.hand[i]+".png"
            self.cards[i].image_file=filename
        print(self.hand)

    def check_hand(self):
        self.wins = [False for x in range(9)]

        suitless = [x[1:] for x in self.hand]
        suitsonly = [x[0] for x in self.hand]
        possible_wins = ["Jacks or Better", "Two Pair", "Three of a Kind", "Straight", "Flush", "Full House", "Four of a Kind", "Straight Flush", "Royal Flush"]
        # pair check
        for val in self.deck.cards[:4]:
            # only check first 4 AKQJ
            if suitless.count(val) == 2:
                self.wins[0] = True    # PAIR JACKS OR HIGHER

        # two pair check
        pairs = 0
        three_kind = False
        for val in self.deck.cards:
            if suitless.count(val) == 2:
                pairs +=1
            if suitless.count(val) == 3:
                self.wins[2] = True     # THREE OF A KIND
            if suitless.count(val) == 4:
                self.wins[6] = True      # 4 OF A KIND

        if pairs == 2:
            self.wins[1] = True    # TWO PAIR

        if pairs == 1 and self.wins[2]:
            self.wins[5] = True  # FULL HOUSE (pair and 3 kind)

        for suit in suitsonly[1:]:
            if suit != suitsonly[0]:
                break
        else:
             self.wins[4] = True   # FLUSH

        # straight check
        print(suitless)
        hand_pos = []
        for card in suitless:
            hand_pos.append(self.deck.cards.index(card))

        hand_pos.sort()
        print(hand_pos)

        if pairs == 0 and not self.wins[2] and not self.wins[6] and (max(hand_pos) - min(hand_pos) == 4):
            # if there are no pairs, no 3kind, no 4kind and top - bottom is 4
            self.wins[3] = True # STRAIGHT!

        if self.wins[3] and self.wins[4]:
            self.wins[8] = True

        for i in range(len(self.wins)):
            if self.wins[i]:
                self.win_text = possible_wins[i]




        


class Card(Widget):

   def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            if self.locked:
                self.locked = False
                self.lock_color = 1
            else:
                self.locked = True
                self.lock_color = 0.5






if __name__ == "__main__":
    app = PokerApp()
    app.run()
