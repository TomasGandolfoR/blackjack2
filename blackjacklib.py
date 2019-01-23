import random
from dictionaries import symbolsCounting


symbolsConversions = {    #NOTA: cada key debe ser unica#"Jan" is the key and "January" is the value
    "As": 11,
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: 10,
    "J": 10,
    "Q": 10,
    "K": 10,
}


class Card:
    def __init__(self, symbol, suit):
        self.symbol = symbol
        self.suit = suit


class PokerDeck:
    def __init__(self, num_of_decks):
        self.isError = 0
        self.deck_in_game = []
        self.num_of_cards = 0
        self.num_of_decks = num_of_decks
        self.symbols = ["As", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

        for i in range(0, num_of_decks):
            self.Generate_Poker_Deck(self.deck_in_game, i)

    def Shuffle_Deck(self):
        disorder = []
        self.isError = self.num_ordered_array(len(self.deck_in_game) - 1, disorder, 0)

        if self.isError != 1:
            random.shuffle(disorder)
            deck_aux = self.deck_in_game.copy()

            # for x in range(0, len(self.deck_in_game)):
            for x in range(0, len(self.deck_in_game) - 1):
                aux = disorder[x]
                self.deck_in_game[x] = deck_aux[aux]

    def num_ordered_array(self, length, array, init):
        if init >= 0:
            for i in range(init, length + init):
                array.append(i)
            return 0
        else:
            return 1

    def Generate_Poker_Deck(self, deck_of_cards, deck_number):
        for i in range(0, 4):
            for j in range(0, 13):
                deck_of_cards.append(j)
        for x in range(0, 4):
            for y in range(0, 13):
                if x == 0:
                    deck_of_cards[deck_number * 52 + y] = Card(self.symbols[y], "spades")
                if x == 1:
                    deck_of_cards[deck_number * 52 + (13 + y)] = Card(self.symbols[y], "hearts")
                if x == 2:
                    deck_of_cards[deck_number * 52 + (26 + y)] = Card(self.symbols[y], "clubs")
                if x == 3:
                    deck_of_cards[deck_number * 52 + (39 + y)] = Card(self.symbols[y], "diamonds")


class Person:
    def __init__(self):
        self.cards = []
        self.num = 0
        self.flagAs = 0

    def general_hit(self, card):
        self.cards.append(Card(card.symbol, card.suit))
        self.num = self.num + symbolsConversions[card.symbol]
        if card.symbol == "As":
            self.flagAs += 1

    def general_new_round(self):
        self.num = 0
        self.flagAs = 0


class Crupier(Person):
    def __init__(self):
        self.hand = "Crupier: "
        Person.__init__(self)

    def hit(self, card):
        self.hand = self.hand + " | " + str(card.symbol) + " | "
        self.general_hit(card)

    def new_round(self):
        self.hand = "Crupier: "
        self.general_new_round()


class Player(Person):
    def __init__(self):
        self.hand = "You: "
        Person.__init__(self)

    def hit(self, card):
        self.hand = self.hand + " | " + str(card.symbol) + " | "
        self.general_hit(card)

    def new_round(self):
        self.hand = "You: "
        self.general_new_round()


class Blackjack:

    @staticmethod
    def begin_round(crupier, players, poker_deck, count):

        for player in players:
            card = poker_deck.deck_in_game.pop()
            player.hit(card)
            count = count + symbolsCounting[card.symbol]

        card = poker_deck.deck_in_game.pop()
        crupier.hit(card)
        count = count + symbolsCounting[card.symbol]

        for player in players:
            card = poker_deck.deck_in_game.pop()
            player.hit(card)
            count = count + symbolsCounting[card.symbol]

        card = poker_deck.deck_in_game.pop()
        crupier.hit(card)
        count = count + symbolsCounting[card.symbol]

        return count

    @staticmethod
    def players_turn(players, poker_deck, count):
        for player in players:
            answer = "h"
            while (answer == "h" or answer == "d") and (player.num < 21):
                answer = input("Do you hit (h), stand (s) or double (d) ? \n")
                if answer == "h":
                    card = poker_deck.deck_in_game.pop()
                    player.hit(card)
                    count = count + symbolsCounting[card.symbol]

                    if player.flagAs > 0 and player.num > 21:
                        # for value in range(1, flagAsC):
                        player.num = player.num - 10
                        player.flagAs = 0

                    print(player.hand + "\n")
                    print("The COUNT is: " + str(count) + "\n")
                # elif answer == "d":
        return count

    @staticmethod
    def who_wins(player, crupier):
        if crupier.num < player.num and player.num <= 21:
            return 2
        elif crupier.num > player.num and crupier.num <= 21:
            return 0
        elif crupier.num == player.num and crupier.num <= 21:
            return 1
        elif crupier.num > 21 and player.num <= 21:
            return 2
        elif player.num > 21 and crupier.num <= 21:
            return 0

