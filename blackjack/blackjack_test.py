from blackjack import Card


def test_card_amounth():
    Card.create_pack()
    score = len(Card.packOfCards)
    assert score == 52
