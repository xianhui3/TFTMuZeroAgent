from Simulator.player import Player
from Simulator.pool import pool
from Simulator.champion import champion
from Simulator import minion

# contains the list of round numbers where unique PVE rounds occur
rounds = [0,1,2,8,14,20,26,33]

def create_player() -> Player:
    """Creates fresh player and pool"""
    base_pool = pool()
    player1 = Player(base_pool, 0)
    return player1

# Check health calculation from minion combat
def test_combat():
    p1 = create_player()
    p1.gold = 10000
    p1.max_units = 100
    minion.minion_combat(p1, minion.FirstMinion(), 0, [None for _ in range(2)])

    assert p1.health < 100, "I didn't lose any health from losing a PVE round!"

# test if each round is dropping rewards for the player
def test_rewards():
    p1 = create_player()
    # add 3* zilean and yone to board for combat
    p1.board[0][0] = champion("zilean", None, 0, 0, 3, None, None, None, False)
    p1.board[0][1] = champion("yone", None, 0, 0, 3, None, None, None, False)

    # PVE rounds can drop champions, gold, or items, but not nothing
    for r in rounds:
        p1.gold = 0
        p1.bench = [None for _ in range(9)]
        p1.item_bench = [None for _ in range(10)]
        
        minion.minion_round(p1, r, [None for _ in range(2)])

        assert not len(p1.item_bench) == 0 \
            or len(p1.bench) == 0 \
            or not p1.gold == 0, "I didn't get anything from the PVE round!"