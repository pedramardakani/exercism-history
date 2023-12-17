class Luhn:
    def __init__(self, card_num: str):
        self.original = card_num
        tmp = card_num.replace(" ", "")
        self.clean = () if not tmp.isdigit() else tuple(int(c) for c in tmp)

    def valid(self) -> bool:
        return len(self.clean) > 1 and sum(
            item + (index % 2 != 0) * (item - 9 * (item >= 5))
            for index, item in enumerate(reversed(self.clean))
        ) % 10 == 0
