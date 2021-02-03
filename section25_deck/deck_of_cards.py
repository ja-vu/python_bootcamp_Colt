from random import choice, shuffle


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(value, suit) for suit in suits for value in values]

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def count(self):
        return len(self.cards)

    def _deal(self, num):
        if num > self.count():
            raise ValueError(f"All cards have been dealt")
        self.cards = self.cards[:-num]
        removed_cards = self.cards[-num::]
        return removed_cards

    def shuffle(self):
        if self.count() > 52:
            raise ValueError("Only full decks can be shuffled")
        return shuffle(self.cards)

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, num):
        return self._deal(num)


d = Deck()
print(d)
d.shuffle()
print(d)
#print(d.deal_card())
#print(deck.deal_card())