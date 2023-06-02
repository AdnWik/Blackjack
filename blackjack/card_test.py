from card import Card


def test_set_score_5():
    """
    Check value for Card(5, hearts)
    """
    card_5 = Card(5, 'hearts')
    score = card_5.set_score()
    assert score == 5


def test_set_score_j():
    """
    Check value for Card(Jack, spades)
    """
    card_J = Card('Jack', 'spades')
    score = card_J.set_score()
    assert score == 10


def test_set_score_q():
    """
    Check value for Card(Queen, clubs)
    """
    card_Q = Card('Queen', 'clubs')
    score = card_Q.set_score()
    assert score == 10


def test_set_score_k():
    """
    Check value for Card(King, diamonds)
    """
    card_K = Card('King', 'diamonds')
    score = card_K.set_score()
    assert score == 10


def test_set_score_a():
    """
    Check value for Card(Ace, hearts)
    """
    card_A = Card('Ace', 'hearts')
    score = card_A.set_score()
    assert score == 1
