class Luhn:
    def __init__(self, card_num: str):
        self.original = card_num
        tmp = card_num.replace(" ", "")
        # Use a tuple so that 'clean' is not mutated unintentionally
        self.clean = () if not tmp.isdigit() else tuple(int(c) for c in tmp)

    def valid(self) -> bool:
        cleaned = list(self.clean)
        length = len(cleaned)
        if length < 2:
            return False
        for i in range(length-2, -1, -2):
            doubled = 2*cleaned[i]
            cleaned[i] = doubled-9 if doubled > 9 else doubled
        return sum(cleaned) % 10 == 0
