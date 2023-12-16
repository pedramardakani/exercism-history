class Luhn:
    def __init__(self, card_num: str):
        self.original = card_num
        tmp = card_num.replace(" ", "")
        self.clean = () if not tmp.isdigit() else tuple(int(c) for c in tmp)

    def valid(self) -> bool:
        if len(self.clean) < 2:
            return False
        res = (item + (index % 2 != 0)*(item-9*(item >= 5))
               for index, item in enumerate(reversed(self.clean)))
        return sum(res) % 10 == 0
