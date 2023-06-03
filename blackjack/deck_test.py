from deck import Deck


#def test_test():
#    given

#    when

#    then


def test_card_amount():
    """
    Check generated 52 unique cards in 3 packs
    """
    number_of_packs = 3
    Deck.create_pack(number_of_packs)
    score = len({(card.value, card.color) for card in Deck.packOfCards})
    assert score == 52
