import pygame
import sys
import easygui

class Ball(pygame.sprite.Sprite):
	def __init__(self, image_file, location, speed):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(image_file)
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = location
		self.speed = speed

	def move(self):
		if self.rect.left < 0 or self.rect.right > screen.get_width():
			self.speed[0] = -self.speed[0]
		if self.rect.top < 0:
			self.speed[1] = -self.speed[1]
		self.rect = self.rect.move(self.speed)

class Paddle(pygame.sprite.Sprite):
	def __init__(self, location = [0, 0]):
		pygame.sprite.Sprite.__init__(self)
		image_surface = pygame.surface.Surface([100, 20])
		image_surface.fill([0, 0, 0])
		self.image = image_surface.convert()
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = location

pygame.init()
screen = pygame.display.set_mode([640, 480])

clock = pygame.time.Clock()

ball = Ball(r'source\images\wackyball.bmp', [50, 50], [10, 5])
group = pygame.sprite.Group(ball)
paddle = Paddle([270, 400])

if __name__ == '__main__':
	while True:
		clock.tick(30)
		screen.fill([255,255, 255])
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.MOUSEMOTION:
				paddle.rect.centerx = event.pos[0]
		if pygame.sprite.spritecollide(paddle, group, False):
			ball.speed[1] = -ball.speed[1]
		ball.move()
		screen.blit(ball.image, ball.rect)
		screen.blit(paddle.image, paddle.rect)
		pygame.display.flip()

		if ball.rect.bottom >= screen.get_size()[1]:
			result = easygui.msgbox('You lost!')
			if result == 'OK':
				sys.exit()