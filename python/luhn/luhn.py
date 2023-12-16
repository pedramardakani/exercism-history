class Luhn:
    def __init__(self, card_num: str):
        self.original = card_num
        tmp = card_num.replace(" ", "")
        self.clean = () if not tmp.isdigit() else tuple(int(c) for c in tmp)

    def valid(self) -> bool:
        if len(self.clean) < 2:
            return False
        rev = reversed(self.clean)
        tmp = (x + (i % 2 != 0)*(x-9*(x >= 5)) for i, x in enumerate(rev))
        return sum(tmp) % 10 == 0
