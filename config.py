import numpy as np

# IMPORTANT: Change this value to the number of cpu cores you want to use (recommended 80% of cpu)
NUM_CPUS = 16
GPU_SIZE_PER_WORKER = 0.16
STORAGE_GPU_SIZE = 0.1
BUFFER_GPU_SIZE = 0.01
TRAINER_GPU_SIZE = 0.2
# NUM_CPUS = 8
# GPU_SIZE_PER_WORKER = 0.0
# STORAGE_GPU_SIZE = 0.0

DEVICE = "cuda"
IMITATION = False
CHAMP_DECIDER = False

# AI RELATED VALUES START HERE

#### MODEL SET UP ####
HIDDEN_STATE_SIZE = 256
NUM_RNN_CELLS = 2
LSTM_SIZE = int(HIDDEN_STATE_SIZE / (NUM_RNN_CELLS * 2))
RNN_SIZES = [LSTM_SIZE] * NUM_RNN_CELLS
LAYER_HIDDEN_SIZE = 256
ROOT_DIRICHLET_ALPHA = 1.0
ROOT_EXPLORATION_FRACTION = 0.25
VISIT_TEMPERATURE = 1.0
MINIMUM_REWARD = -300.0
MAXIMUM_REWARD = 300.0
PB_C_BASE = 19652
PB_C_INIT = 1.25
DISCOUNT = 0.997
TRAINING_STEPS = 1e10
OBSERVATION_SIZE = 10432
OBSERVATION_TIME_STEPS = 4
OBSERVATION_TIME_STEP_INTERVAL = 5
INPUT_TENSOR_SHAPE = np.array([OBSERVATION_SIZE])
ACTION_ENCODING_SIZE = 1045
ACTION_CONCAT_SIZE = 81
ACTION_DIM = [7, 37, 10]
# 57 is the number of champions in set 4. Don't want to add an import to the STATS in the simulator in a config file
CHAMPION_ACTION_DIM = [5 for _ in range(58)]
CHAMPION_LIST_DIM = [2 for _ in range(58)]
ITEM_CHOICE_DIM = [3 for _ in range(10)]
CHAMP_DECIDER_ACTION_DIM = CHAMPION_ACTION_DIM + [2] + ITEM_CHOICE_DIM

# Number of categories for each trait tier. Emperor for example has 2, no emperors or 1.
TEAM_TIERS_VECTOR = [4, 5, 4, 4, 4, 3, 3, 3, 2, 4, 4, 4, 5, 3, 5, 2, 3, 5, 4, 4, 3, 4, 4, 4, 2, 5]
TIERS_FLATTEN_LENGTH = 97
CHANCE_BUFFER_SEND = 1
GLOBAL_BUFFER_SIZE = 20000
ITEM_POSITIONING_BUFFER_SIZE = 2000
MINIMUM_POP_AMOUNT = 100

# INPUT SIZES
SHOP_INPUT_SIZE = 45
BOARD_INPUT_SIZE = 728
BENCH_INPUT_SIZE = 234
STATE_INPUT_SIZE = 85
COMP_INPUT_SIZE = 102
OTHER_PLAYER_INPUT_SIZE = 5180
OTHER_PLAYER_ITEM_POS_SIZE = 5920

OBSERVATION_LABELS = ["shop", "board", "bench", "states", "game_comp", "other_players"]
POLICY_HEAD_SIZES = [7, 5, 630, 370, 9]  # [7 types, shop, movement, item, sell/item loc]
NEEDS_2ND_DIM = [1, 2, 3, 4]

# ACTION_DIM = 10
ENCODER_NUM_STEPS = 601
SELECTED_SAMPLES = True
MAX_GRAD_NORM = 5

N_HEAD_HIDDEN_LAYERS = 2

### TIME RELATED VALUES ###
ACTIONS_PER_TURN = 15
CONCURRENT_GAMES = 1
NUM_PLAYERS = 8 
NUM_SAMPLES = 30
NUM_SIMULATIONS = 50

# Set to -1 to turn off.
TD_STEPS = -1 
# This should be 1000 + because we want to be sampling everything when using priority.
# To change, look into the code in replay_muzero_buffer
SAMPLES_PER_PLAYER = 1000
# For default agent, this needs to be low because there often isn't many samples per game.
UNROLL_STEPS = 5

### TRAINING ###
BATCH_SIZE = 1024
INIT_LEARNING_RATE = 0.01
LEARNING_RATE_DECAY = int(350e3)
LR_DECAY_FUNCTION = 0.1
WEIGHT_DECAY = 1e-5
REWARD_LOSS_SCALING = 1
POLICY_LOSS_SCALING = 1
VALUE_LOSS_SCALING = 1
GAME_METRICS_SCALING = 0.2

AUTO_BATTLER_PERCENTAGE = 0

# Putting this here so that we don't scale the policy by a multiple of 5
# Because we calculate the loss for each of the 5 dimensions.
# I'll add a mathematical way of generating these numbers later.
DEBUG = True
CHECKPOINT_STEPS = 100

#### TESTING ####
RUN_UNIT_TEST = False
RUN_PLAYER_TESTS = False
RUN_MINION_TESTS = False
RUN_DROP_TESTS = False
RUN_MCTS_TESTS = False
RUN_MAPPING_TESTS = False
RUN_CHECKPOINT_TESTS = True
LOG_COMBAT = False
ke