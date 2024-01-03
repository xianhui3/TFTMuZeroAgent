# Description: This script will verify the drop rate of a shop 
# by running the simulator 100000 times and counting the number of times
# each champion is chosen.

from Simulator.player import Player
from Simulator.pool import pool
from Simulator.champion import champion
from Simulator.pool import COST_1, COST_2, COST_3, COST_4, COST_5

# Verify shop drop rates for each cost are correct

# Correct drop rates of each cost by level for set 4
CORRECT_DROP_RATES = [
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [0.75, 0.25, 0, 0, 0],
    [0.55, 0.30, 0.15, 0, 0],
    [0.45, 0.33, 0.20, 0.02, 0],
    [0.25, 0.40, 0.30, 0.05, 0],
    [0.20, 0.30, 0.35, 0.14, 0.01],
    [0.15, 0.20, 0.35, 0.25, 0.05],
    [0.10, 0.15, 0.30, 0.30, 0.15],
]
#Correct chosen drop rates of each cost by level for set 4
#TODO: Test if chosen drop rates are correct
CHOSEN_DROP_RATES = [
    [1   , 0   , 0   , 0   , 0   ],
    [1   , 0   , 0   , 0   , 0   ],
    [1   , 0   , 0   , 0   , 0   ],
    [0.8 , 0.2 , 0   , 0   , 0   ],
    [0.4 , 0.55, 0.05, 0   , 0   ],
    [0   , 0.6 , 0.4 , 0   , 0   ],
    [0   , 0.4 , 0.58, 0.02, 0   ],
    [0   , 0   , 0.6 , 0.4 , 0   ],
    [0   , 0   , 0   , 0.6 , 0.4 ]
]
def setup_function():
    global pool1
    global player1
    pool1 = pool()
    player1 = Player(pool_pointer=pool1, player_num=1)

#Can potentially consolidate tests
def test_level_one():
    level_test(1)   

def test_level_two():
    level_test(2)

def test_level_three():
    level_test(3)

def test_level_four():
    level_test(4)

def test_level_five():
    level_test(5)

def test_level_six():
    level_test(6)

def test_level_seven():
    level_test(7)

def test_level_eight():
    level_test(8)

def test_level_nine():
    level_test(9)

#Checks if the cost drop rates are correct at a certain level
def level_test(level_to_test):
    cost_checker(1, level_to_test)
    cost_checker(2, level_to_test)
    cost_checker(3, level_to_test)
    cost_checker(4, level_to_test)
    cost_checker(5, level_to_test)

#Tests a certain cost's drop rates are correct at a certain level
def cost_checker(cost_num, player_level):
    player1.level = player_level
    costs = verify(pool1, player1)
    total_costs = 0
    for i in range(len(costs[cost_num - 1])):
        total_costs += costs[cost_num - 1][list(costs[cost_num - 1])[i]]
    
    assert (CORRECT_DROP_RATES[player_level - 1][cost_num-1] - 0.01) <= total_costs / 100000 <= (
                    CORRECT_DROP_RATES[player_level - 1][cost_num-1] + 0.01), \
            f"{cost_num} Cost Champion drop rate at level {player_level} is significantly incorrect! Control: " \
            f"{CORRECT_DROP_RATES[player_level - 1][cost_num-1]} Sample: {total_costs / 100000}"

def verify(_pool, _player):
    shop = pool.sample(self=_pool, player=_player, num=100000, idx=-1)
    # a dictionary to store the number of times each cost is chosen

    cost_1 = {}
    cost_2 = {}
    cost_3 = {}
    cost_4 = {}
    cost_5 = {}

    # the number of times each cost is chosen
    for i in range(len(shop)):
        if shop[i] in COST_1:
            if shop[i] in cost_1:
                cost_1[shop[i]] += 1
            else:
                cost_1[shop[i]] = 1
        elif shop[i] in COST_2:
            if shop[i] in cost_2:
                cost_2[shop[i]] += 1
            else:
                cost_2[shop[i]] = 1
        elif shop[i] in COST_3:
            if shop[i] in cost_3:
                cost_3[shop[i]] += 1
            else:
                cost_3[shop[i]] = 1
        elif shop[i] in COST_4:
            if shop[i] in cost_4:
                cost_4[shop[i]] += 1
            else:
                cost_4[shop[i]] = 1
        elif shop[i] in COST_5:
            if shop[i] in cost_5:
                cost_5[shop[i]] += 1
            else:
                cost_5[shop[i]] = 1
        else:
            pass

    return cost_1, cost_2, cost_3, cost_4, cost_5
