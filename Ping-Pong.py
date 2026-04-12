import pygame

pygame.init()
FPS = 60
WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Ping-Pong game")

main_loop = True
clock = pygame.time.Clock()

first_user = pygame.Rect(0,HEIGHT//2,20,100)
second_user = pygame.Rect(WIDTH-20,HEIGHT//2,20,100)

user_speed = 10

while main_loop:

  screen.fill((0,0,0))

  for event in pygame.event.get():
    if event == pygame.QUIT:
      main_loop = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_w:
        pass

      if event.key == pygame.K_s:
        pass


      if event.key == pygame.K_UP:
        pass

      if event.key == pygame.K_DOWN:
        pass

  

  pygame.display.flip()

  clock.tick(FPS)

pygame.quit()
