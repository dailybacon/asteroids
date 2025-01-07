# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
import sys


def main():
	pygame.init()
	time_clock = pygame.time.Clock()
	dt = 0
	print("Starting asteroids!")
	print(f'Screen width: {SCREEN_WIDTH}')
	print(f'Screen height: {SCREEN_HEIGHT}')
	screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
	
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	Shot.containers = (shots, updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = updatable
	asteroidfield = AsteroidField()


	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		screen.fill('black')

		for thing in updatable:
			thing.update(dt)
		
		for asteroid in asteroids:
			for shot in shots:
				if shot.collide(asteroid):
					shot.kill()
					asteroid.split()

		for thing in drawable:
			thing.draw(screen)

			
			



		for asteroid in asteroids:
			if(player.collide(asteroid)):
				print("Game Over!")
				sys.exit()

		pygame.display.flip()
		dt = (time_clock.tick() / 1000)


if __name__ == "__main__":
	main()
