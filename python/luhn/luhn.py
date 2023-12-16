class Luhn:
    def __init__(self, card_num: str):
        self.original = card_num
        tmp = card_num.replace(" ", "")
        self.clean = [] if not tmp.isdigit() else [int(c) for c in tmp]

    def valid(self) -> bool:
        # Must use a shallow copy so that the 'self.clean' is not mutated
        cleaned = self.clean.copy()
        length = len(cleaned)
        if length < 2:
            return False
        for i in range(length-2, -1, -2):
            doubled = 2*cleaned[i]
            cleaned[i] = doubled-9 if doubled > 9 else doubled
        return sum(cleaned) % 10 == 0
