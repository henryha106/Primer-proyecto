import random


def play():
    user = input("Escoge una!, 'r' para roca, 'p' para papel, y 't' para tijeras: ")
    pc = random.choice(['r', 'p', 't'])

    if user == pc:
        return 'es un empate'

    # r > t, t > p, p > r
    if is_win(user, pc):
        return 'Ganaste!'
    if is_win(pc, user):
        return 'Perdiste :('
def is_win(player, opponent):
    # r > t, t > p, p > r
    if (player == 'r' and opponent == 't') or (player == 't' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
print(play())
