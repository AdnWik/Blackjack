from blackjack import Deck


def test_card_amounth():
    Deck.create_pack()
    score = len(Deck.packOfCards)
    assert score == 52
