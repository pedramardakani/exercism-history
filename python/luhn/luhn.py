import itertools as it


class Luhn:
    def __init__(self, card_num: str):
        self.original = card_num
        tmp = card_num.replace(" ", "")
        self.clean = () if not tmp.isdigit() else tuple(int(c) for c in tmp)

    def odd_operation(self, x):
        """Operation that should be done on odd indices"""
        return x

    def even_operation(self, x):
        """Operation that should be done on even indices"""
        return x * 2 - 9 * (x > 4)

    def valid(self) -> bool:
        odd_even = it.cycle((self.odd_operation, self.even_operation))
        return len(self.clean) > 1 and sum(
            map(lambda i: next(odd_even)(i), reversed(self.clean))
        ) % 10 == 0
