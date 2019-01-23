
from dictionaries import symbolsCounting
from blackjacklib import PokerDeck, Crupier, Player, symbolsConversions, Blackjack

blackjack = Blackjack()

number_of_players = int(input("how many players do you want to play?"))
number_of_decks = int(input("how many decks do you want to play?"))

poker_deck = PokerDeck(number_of_decks)
poker_deck.Shuffle_Deck()

#=======================================================================
#INICIO JUEGO

crupier = Crupier()
players = list()
for i in range(0, number_of_players):
    players.append(Player())

i = 1

count = 0

while i != 0:

    crupier.new_round()
    for player in players:
        player.new_round()

    #   BEGIN ROUND

    count = blackjack.begin_round(crupier, players, poker_deck, count)

    print(crupier.hand)
    for player in players:
        print(player.hand + "\n")
    print("The COUNT is: " + str(count) + "\n")

    blackjack.players_turn(players, poker_deck, count)

    for player in players:
        if player.num > 21:
            winner = 0
        else:
            while crupier.num < 17:
                card = poker_deck.deck_in_game.pop()
                crupier.hit(card)
                count = count + symbolsCounting[card.symbol]
                if crupier.flagAs > 0 and crupier.num > 21:
                    crupier.num = crupier.num - 10
                    crupier.flagAs = 0

                print(crupier.hand)
                print("The COUNT is: " + str(count) + "\n")

            winner = blackjack.who_wins(player, crupier)

        if winner == 0:
            print("\nthe house wins\n")
        elif winner == 1:
            print("\ntie\n")
        else:
            print("\nYou win\n")

    answer = input("Do you want to continue? yes (y) / no (n) \n")
    if answer == "n" or len(poker_deck.deck_in_game) <= 20:
        print(len(poker_deck.deck_in_game))
        i = 0
    else:
        i = 1



