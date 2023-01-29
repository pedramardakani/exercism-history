"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card: str) -> int:
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    match card:
        case 'A':
            return 1
        case 'J' | 'Q' | 'K':
            return 10
        case _:
            return int(card)


def higher_card(card_one: str, card_two: str) -> str | tuple[str, str]:
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    match [value_of_card(card_one), value_of_card(card_two)]:
        case [a, b] if a > b:
            return card_one
        case [a, b] if a < b:
            return card_two
        case _:
            return (card_one, card_two)


def value_of_ace(card_one: str, card_two: str) -> int:
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    if 'A' in (card_one, card_two) or value_of_card(card_one) + value_of_card(card_two) > 10:
        # In case the ace is already in hand, the second ace must be 1 or
        # the player goes "bust". On the other hand, if the sum of cards is
        # more than 10, the new ace must be 1 or the player would go "bust".
        return 1
    # No ace in hand and the sum is low enough so that setting the new ace to
    # 11 would still prevent the player from going 'bust'.
    return 11


def is_blackjack(card_one: str, card_two: str) -> bool:
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    if 'A' in [card_one, card_two] and value_of_card(card_one) + value_of_card(card_two) == 11:
        # There is an ace in the hand and we know that 'value_of_card'
        # returns '1' for the ace. So, if the other card has the value '10',
        # the sum must be '11' and the hand is a blackjack!
        return True
    return False


def can_split_pairs(card_one: str, card_two: str) -> bool:
    """Determine if a player can split their hand into two hands.

    If the players first two cards are of the same value, such as two sixes,
    or a `Q` and `K` a player may choose to treat them as two separate hands.
    This is known as "splitting pairs".

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """
    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    return 9 <= value_of_card(card_one) + value_of_card(card_two) <= 11
