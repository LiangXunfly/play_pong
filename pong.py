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
		global points
		if self.rect.left < 0 or self.rect.right > screen.get_width():
			self.speed[0] = -self.speed[0]
		if self.rect.top < 0:
			points = points + 1
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

#version2 add
points = 0
lives = 3

if __name__ == '__main__':
	while True:
		clock.tick(30)
		screen.fill([255,255, 255])

		#version2 add
		font = pygame.font.Font(None, 50)
		score_text = font.render(str(points), 1, (0, 0, 0))
		textpos = (10, 10)

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

		#version2 add
		screen.blit(score_text, textpos)
		#for i in range(lives):
		for i in range(lives - 1):
			screen.blit(ball.image, (screen.get_width() - 30 * i - 20, 20))

		pygame.display.flip()

		if ball.rect.bottom >= screen.get_rect().bottom:
			if lives == 1:
				result = easygui.msgbox('Your score is %d!' % points)
				sys.exit()
			else:
				lives = lives - 1
				pygame.time.delay(2000)
				ball.rect.topleft = [50, 50]