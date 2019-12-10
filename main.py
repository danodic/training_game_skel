import pygame # Pygame is our SDL wrapper
import constants # This module carries the file names and static values

from state import GameController # Will control the overall state of the game

# Some globals
screen = None
game_controller = None

def setup():
    global screen, game_controller

    # Initializes pygame
    pygame.init()

    # Initializes the game controllers
    game_controller = GameController()

    # Initializes the screen
    screen = pygame.display.set_mode(constants.SCREEN_SIZE, pygame.DOUBLEBUF)

def game_loop():
    global screen, game_controller

    # Enter the main game loop
    while not game_controller.done:

        # Paint the background
        screen.fill((255,255,0))

        # Check events and look for the exit event
        input()

        # Do the debug
        debug()

        # Update the screen
        pygame.display.flip()


def input():
    global game_controller

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_controller.done = True

def debug():
    print("It works!")


# Run the game setup
setup()

# This is where the game starts
game_loop()