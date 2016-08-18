#!/usr/bin/env Env_Python34_Quandl289

#### Quandl 2.8.9

import numpy as np
import pandas as pd
import sqlite3
import Quandl
from hidden import quandl_ticker_get_df 
import datetime
import random
import time
import sys

# activate Env_Python34_Quandl289

SNAKES_LADDERS = {
    1: 38, 4: 14, 9: 31,
    16: 6,
    21: 42, 28: 84,
    36: 44,
    48: 26, 49: 11,
    51: 67, 56: 53,
    62: 19, 64: 60,
    71: 91, 80: 100,
    87: 24,
    93: 73, 95: 75, 98: 78,
}

MAX_SQUARE = 100
MAX_MOVES = 100000

def play_one():
    """Play one game and return the number of moves it took."""
    square = 0
    for num_moves in range(1, MAX_MOVES + 1):
        dice_roll = random.randrange(1, 7)
        square += dice_roll
        # It allows you to provide a default value if the key is missing. 
        # Give the get funtion the var - square if not in dict then return square.
        square = SNAKES_LADDERS.get(square,square)  
        if square >= MAX_SQUARE:
            return num_moves
    return MAX_MOVES


def play_all(num_rounds):
    """Play num_rounds games and return tuple of (total, max, time)."""
    start_time = time.time()

    total_moves = 0
    max_moves = 0
    # the _ in "for _ in" is a it's just a variable like any other, 
    # but by convention it means that you don't intend to use that value, just read it and ignore it.
    for _ in range(num_rounds):
        num_moves = play_one()
        total_moves += num_moves # number of moves for the game to complete.
        max_moves = max(max_moves, num_moves) # max number between max moves from previous round and current round.

    elapsed_time = time.time() - start_time

    return (total_moves, max_moves, elapsed_time)

#print(play_all(100))


## argparse is the recommended command-line parsing module.
## Allows you to run
## eg. python ScrapTests.py -n 1000
## OR python ScrapTests.py --help
if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--num-rounds', type=int, default=10000,
                        help='number of rounds (games) to play')
    args = parser.parse_args()

    total_moves, max_moves, elapsed_time = play_all(args.num_rounds)
    print('Played {} rounds, averaged {} moves, max {} moves, took {:.3f}s'.format(
        args.num_rounds,
        total_moves / args.num_rounds,
        max_moves,
        elapsed_time,
    ))






