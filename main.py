# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *


def main():
	pygame.init()
	time_clock = pygame.time.Clock()
	dt = 0
	print("Starting asteroids!")
	print(f'Screen width: {SCREEN_WIDTH}')
	print(f'Screen height: {SCREEN_HEIGHT}')
	screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill('black')

		player.draw(screen)
		player.update(dt)
		pygame.display.flip()
		dt = (time_clock.tick() / 1000)


if __name__ == "__main__":
	main()
