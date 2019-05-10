import random
import time
from kivy.clock import Clock

from kivy.animation import Animation
from kivy.app import App
from kivy.graphics import Rectangle, Color
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.uix.listview import ListItemButton
from kivy.uix.listview import ListView
from kivy.uix.button import Button


Window.size = [320, 568]
Window.clearcolor = [0,0,0,0]

class YachtApp(App):
    def build(self):
        return YachtLayout()

class ScoreCard(ListItemButton):
    pass

class YachtLayout(BoxLayout):
    rolls = 3
    current_hand = [0,0,0,0,0]
    gutter = 20
    started = False
    score_labels = ["Ones", "Twos", "Threes", "Fours", "Fives", "Sixes", "Chance", "Three of a Kind", "Four of a Kind", "Full House", "Small Straight", "Large Straight", "Five of a Kind"]
    hand_scores = [0 for x in score_labels]  # scores for THIS hand
    score = [x for x in hand_scores]  # scores for scorecard
    used = [False for x in hand_scores]
    total_score = 0

    def enable_all_buttons(self):
        self.button_ones.disabled = False
        self.button_twos.disabled = False
        self.button_threes.disabled = False
        self.button_fours.disabled = False
        self.button_fives.disabled = False
        self.button_sixes.disabled = False
        self.button_chance.disabled = False
        self.button_3kind.disabled = False
        self.button_4kind.disabled = False
        self.button_full.disabled = False
        self.button_small.disabled = False
        self.button_large.disabled = False

    def update_buttons(self):
        self.single_button_update(self.button_ones, 0)
        self.single_button_update(self.button_twos, 1)
        self.single_button_update(self.button_threes, 2)
        self.single_button_update(self.button_fours, 3)
        self.single_button_update(self.button_fives, 4)
        self.single_button_update(self.button_sixes, 5)

        self.single_button_update(self.button_chance, 6)
        self.single_button_update(self.button_3kind, 7)
        self.single_button_update(self.button_4kind, 8)
        self.single_button_update(self.button_full, 9)
        self.single_button_update(self.button_small, 10)
        self.single_button_update(self.button_large, 11)
        self.single_button_update(self.button_5kind, 12)

    def single_button_update(self, button, i):
        if self.score[i] == 0 and self.used[i] == False:
            button.disabled = False
            if self.hand_scores[i] == 0:
                button.background_color = [0.5, 0.5, 0.5, 1]
            else:
                button.background_color = [0, 0.5, 0, 1]
        else:
            button.disabled = True
            button.background_color = [0,0,0,1]

    def enter_score(self, i):
        if self.score[i] == 0 and self.used[i] == False:
            self.used[i] = True
            self.score[i] = self.hand_scores[i]
            self.roll_button.text = "Roll Dice!"
            self.roll_button.disabled = False
        self.update_total_score()
        self.update_board()
        if self.used.count(False) == 0:
            self.roll_button.disabled = True
            self.roll_button.color = [0,0,0,1]
            self.message_text.text = "Final Score: " + str(self.total_score)


    def new_roll(self):
        if self.used.count(False) > 0:
            self.message_text.text = ""
        self.enable_all_buttons()
        self.rolls = 3
        self.rolls_text.color = [1, 1, 1, 1]

        for i in range(len(self.hand_scores)):
            self.hand_scores[i] = 0
        for i in range(len(self.current_hand)):
            self.current_hand[i] = 0
        self.rolls_text.text = "Rolls Remaining: " + str(self.rolls)

        self.die1.die_source = "images/black.png"
        self.die2.die_source = "images/black.png"
        self.die3.die_source = "images/black.png"
        self.die4.die_source = "images/black.png"
        self.die5.die_source = "images/black.png"

        self.die1.value = 0
        self.die2.value = 0
        self.die3.value = 0
        self.die4.value = 0
        self.die5.value = 0

        self.die1.locked = False
        self.die2.locked = False
        self.die3.locked = False
        self.die4.locked = False
        self.die5.locked = False

        self.die1.box_alpha = 1
        self.die2.box_alpha = 1
        self.die3.box_alpha = 1
        self.die4.box_alpha = 1
        self.die5.box_alpha = 1



        self.update_buttons()

    def score_hand(self):
        if self.rolls > 0:
            self.rolls -= 1
            self.rolls_text.text = "Rolls Remaining: " + str(self.rolls)
            self.rolls_text.color = [1, 1, 1, 1]

            if self.rolls == 0:
                self.rolls_text.color = [1,0,0,1]
                self.rolls_text.text = "Rolls Remaining: " + str(self.rolls)
                self.roll_button.text = ""
                self.roll_button.disabled = True
            else:
                self.roll_button.text = "Roll Dice!"
                self.roll_button.disabled = False

        self.hand_scores = []
        self.current_hand = [self.die1.value, self.die2.value, self.die3.value, self.die4.value, self.die5.value]
        for i in range(1, 7):
            self.hand_scores.append(self.current_hand.count(i) * i)

        self.hand_scores.append(self.chance_check())
        self.hand_scores.append(self.three_kind_check()) # 3 of kind
        self.hand_scores.append(self.four_kind_check()) # 4 of kind
        self.hand_scores.append(self.full_house_check()) # full house
        self.hand_scores.append(self.small_straight_check())
        self.hand_scores.append(self.large_straight_check())
        self.hand_scores.append(self.yacht_check())
        self.update_total_score()

        #self.print_my_hand()  # for troubleshooting
        self.update_board()
        self.update_buttons()

    def update_total_score(self):
        self.total_score = sum(self.score)
        self.score_text.text = "Your Score: " + str(self.total_score)


    def update_board(self):
        self.hand_ones.text = str(self.hand_scores[0])
        self.hand_twos.text = str(self.hand_scores[1])
        self.hand_threes.text = str(self.hand_scores[2])
        self.hand_fours.text = str(self.hand_scores[3])
        self.hand_fives.text = str(self.hand_scores[4])
        self.hand_sixes.text = str(self.hand_scores[5])
        self.hand_chance.text = str(self.hand_scores[6])
        self.hand_3kind.text = str(self.hand_scores[7])
        self.hand_4kind.text = str(self.hand_scores[8])
        self.hand_full.text = str(self.hand_scores[9])
        self.hand_small.text = str(self.hand_scores[10])
        self.hand_large.text = str(self.hand_scores[11])
        self.hand_5kind.text = str(self.hand_scores[12])

        self.score_ones.text = str(self.score[0])
        self.score_twos.text = str(self.score[1])
        self.score_threes.text = str(self.score[2])
        self.score_fours.text = str(self.score[3])
        self.score_fives.text = str(self.score[4])
        self.score_sixes.text = str(self.score[5])
        self.score_chance.text = str(self.score[6])
        self.score_3kind.text = str(self.score[7])
        self.score_4kind.text = str(self.score[8])
        self.score_full.text = str(self.score[9])
        self.score_small.text = str(self.score[10])
        self.score_large.text = str(self.score[11])
        self.score_5kind.text = str(self.score[12])
        self.update_total_score()

    def print_my_hand(self):
        print("\n" * 20)
        for i in range(len(self.score_labels)):
            print("{0}:{1}".format(self.score_labels[i], self.hand_scores[i]))

    def bonus_check(self):
        total = 0
        for i in range(6):
            total += self.score[i]
        if total >= 63:
            return 35
        return 0

    def chance_check(self):
        total = 0
        for i in range(6):
            total += self.hand_scores[i]
        return total

    def small_straight_check(self):
        small_straight1 = True  # 1,2,3,4
        small_straight2 = True  # 2,3,4,5
        small_straight3 = True  # 3,4,5,6

        # check for small_straight_1
        for i in range(4):
            if self.hand_scores[i] < 1:
                small_straight1 = False

        # check for small_straight_2
        for i in range(1,5):
            if self.hand_scores[i] < 1:
                small_straight2 = False

        # check for small_straight_3
        for i in range(2,6):
            if self.hand_scores[i] < 1:
                small_straight3 = False

        if small_straight1 or small_straight2 or small_straight3:
            return 30
        return 0

    def large_straight_check(self):
        large_straight1 = True # 1,2,3,4,5
        large_straight2 = True # 2,3,4,5,6

        # check for large_straight1
        for i in range(5):
            if self.hand_scores[i] < 1:
                large_straight1 = False

        # check for large_straight2
        for i in range(1,6):
            if self.hand_scores[i] < 1:
                large_straight2 = False


        if large_straight1 or large_straight2:
            if self.score[-2] == 0:
                self.message_text.text = "LARGE STRAIGHT!"
            return 40
        return 0
    def yacht_check(self):
        yacht = False
        # check for large_straight1
        for i in range(6):
            if self.hand_scores[i] == (i+1) * 5:
                self.message_text.text = "5 OF A KIND!"
                return 50
        return 0

    def three_kind_check(self):
        for i in range(6):
            if self.hand_scores[i] >= (i+1) * 3:
                return self.chance_check()
        return 0

    def four_kind_check(self):
        for i in range(6):
            if self.hand_scores[i] >= (i+1) * 4:
                return self.chance_check()
        return 0

    def full_house_check(self):
        three = False
        two = False
        for i in range(6):
            if self.hand_scores[i] == (i+1) * 3:
                three = True
            if self.hand_scores[i] == (i+1) * 2:
                two = True
        if three and two:
            return 25
        return 0

class Die(Widget):
    number = ObjectProperty()
    image_name = ObjectProperty()
    value = ObjectProperty()
    locked = ObjectProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.update, 1/10)
        self.size = [50,50]
        self.start_x, self.start_y = self.pos
        self.animate_me = False
        self.die_source_list = ["images/dieWhite" + str(x) + ".png" for x in range(1, 7)]


    def update(self, *args):
        if self.animate_me:
            self.die_source = random.choice(self.die_source_list)

    def stop_animation(self, widget, item):
        self.animate_me = False
        self.die_source = "images/dieWhite" + str(self.value) + ".png"

    def roll(self):
        roll = random.randrange(1, 7)
        Animation.cancel_all(self)

        anim = Animation(center_y=150, size=[50,50], duration=random.random()/2 + 0.5, t="out_bounce")
        if not self.locked:
            size = random.randrange(60, 100)
            self.size = [size,size]
            self.center_y = 150
            Animation.cancel_all(self)
            self.animate_me = True
            anim.start(self)
            self.value = roll

            anim.bind(on_complete=self.stop_animation)


    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):

            if self.locked:
                self.locked = False
                self.box_alpha = 1
            else:
                self.locked = True
                self.box_alpha = 0.5




if __name__ == "__main__":
    demo = YachtApp()
    demo.run()
