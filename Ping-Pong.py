import pygame

pygame.init()
FPS = 60
WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Ping-Pong game")

main_loop = True
clock = pygame.time.Clock()

first_position_x = 0
first_position_y = HEIGHT//2

second_position_x = WIDTH-20
second_position_y = HEIGHT//2



user_speed = 10

while main_loop:

  screen.fill((0,0,0))

  for event in pygame.event.get():
    if event == pygame.QUIT:
      main_loop = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_w:

        if first_position_y-user_speed >=0:
          first_position_y-=user_spped

      if event.key == pygame.K_s:

        if first_position_y+user_speed+100<=HEIGHT:
          first_position_y+=user_speed

      if event.key == pygame.K_UP:

        if second_position_y-user_speed >=0:
          second_position_y-=user_speed
        
      if event.key == pygame.K_DOWN:
        if second_position_y+user_speed+100<=HEIGHT:
          second_position_y+=user_speed



  first_user = pygame.Rect(first_position_x,first_position_y,20,100)
  second_user = pygame.Rect(second_position_x,second_position_y,20,100)

  
  
  pygame.display.flip()

  clock.tick(FPS)

pygame.quit()
