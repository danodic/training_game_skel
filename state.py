"""
This module handles the state of the game. Things like the Game or the input
state.
"""

import pygame

class GameController:
    """
    This class stores the game state.
    """
    def __init__(self):
        self.done = False
        