def gen_steps(array: list[str], x: int, y: int):
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            if dy == dx == 0:
                continue
            if x+dx < 0 or y+dy < 0:
                continue
            if x+dx >= len(array) or y+dy >= len(array[0]):
                continue
            yield (x+dx, y+dy)

def annotate(minefield):
    annotated = [
        [col == "*" for col in row] for row in minefield
    ]
    for x, row in enumerate(minefield):
        if len(row) != len(minefield[0]):
            raise ValueError("The board is invalid with current input.")
        for y, col in enumerate(row):
            steps = gen_steps(minefield, x, y)
            if minefield[x][y] not in (" ", "*"):
                raise ValueError("The board is invalid with current input.")
            adjacent_mines = "*" if minefield[x][y] == "*" else sum(minefield[dx][dy] == "*" for (dx,dy) in steps)
            annotated[x][y] = str(adjacent_mines) if adjacent_mines else " "

    result = [
        "".join(row) for row in annotated
    ]
    return result



