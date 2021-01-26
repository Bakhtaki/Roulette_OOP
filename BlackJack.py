import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
Playing = True


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + self.suit


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        Head = self.deck.pop()
        return Head


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:
    def __init__(self):
        self.Total = 100
        self.bet = 0

    def win(self):
        self.Total += self.bet

    def lost(self):
        self.Total -= self.bet

    def charge(self, Amount):
        self.Total += Amount


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("Please Enter Your Bet : "))
        except ValueError:
            print('Bet must be an Integer')
        else:
            if chips.bet > chips.Total or chips.bet <= 0:
                print("Invalid Bet ,Please bet between 0 and ", chips.Total)
            else:
                break


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust()


def decision(deck, hand):
    global Playing
    while True:
        x = input("Please press 1 for his or 0 to Stand!!!!")
        if x.lower() == '1':
            hit(deck, hand)
        elif x.lower() == '0':
            print("Dealer now Playing")
        else:
            print("unknown Command")
            continue
        break


def Partial_Show(player, dealer):
    print("\n Dealer Hand: ")
    print("Hidden card")
    print("", dealer.cards[1])
    print(" \n Your Hand : ", player.cards, sep='\n')


def Show_all(player, dealer):
    print("\n Dealer Hand: ", dealer.cards, sep='\n')
    print("Dealer hand : ", dealer.value)
    print("\n Your Hand : ", player.cards, sep='\n')
    print("Player Hand", player.value, sep='\n')


def player_bust(player, dealer, chips):
    print('You are busted')
    chips.lost()


def player_win(player, dealer, chips):
    print("You won ")
    chips.win()


def dealer_bust(player, dealer, chips):
    print("Dealer Boosts")
    chips.win()


def dealer_win(player, dealer, chips):
    print('dealer Wins')
    chips.lost()


def draw(player, dealer):
    print("The match is drawn")


Credit = Chips()

while True:
    deck1 = Deck()
    deck1.shuffle()

    Player_hand = Hand()
    Player_hand.add_card(deck1.deal())
    Player_hand.add_card(deck1.deal())

    Dealer_Hand = Hand()
    Dealer_Hand.add_card(deck1.deal())
    Dealer_Hand.add_card(deck1.deal())

    take_bet(Credit)
    Partial_Show(Player_hand, Dealer_Hand)

    while Playing:
        hit(deck1, Player_hand)
        Partial_Show(Player_hand, Dealer_Hand)
        if Player_hand.value > 21:
            player_bust(Player_hand, Dealer_Hand, Credit)
            break
        if Player_hand.value <= 21:
            while Dealer_Hand.value < 17:
                hit(deck1, Dealer_Hand)
            Show_all(Player_hand, Dealer_Hand)

            if Dealer_Hand.value > 21:
                dealer_bust(Player_hand, Dealer_Hand, Credit)
            elif Dealer_Hand.value > Player_hand.value:
                dealer_win(Player_hand, Dealer_Hand, Credit)
            elif Dealer_Hand.value < Player_hand.value:
                player_win(Player_hand, Dealer_Hand, Credit)
            else:
                draw(Player_hand, Dealer_Hand)
    print("Your Balance  is: ", Credit.Total)
    if Credit.Total > 0:
        Answer = input("Continue ? ")
        if Answer.lower() == '1':
            Playing = True
            continue
        else:
            print("Your Balance  is : ", Credit.Total)
    else:
        print("You lost all your Money")
