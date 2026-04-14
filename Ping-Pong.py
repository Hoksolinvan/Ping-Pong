import pygame
import random

random.seed()
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


ball_position_x = WIDTH//2
x_direction = 1
ball_position_y = HEIGHT//2
y_direction = 0

if random.random() < 0.5:
    x_direction *= -1



def AABB_collision(x_coordinate,y_coordinate,height,width,x2_coordinate,y2_coordinate,height2,width2):
    
    return(x_coordinate+width >x2_coordinate and
           x2_coordinate+width2 > x_coordinate and 
           y_coordinate+height > y2_coordinate and 
           y2_coordinate+height2 > y_coordinate)



user_speed = 5
ball_speed = 2

while main_loop:

  screen.fill((0,0,0))

  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          main_loop = False

  # 👇 continuous input (holding)
  keys = pygame.key.get_pressed()

  # Player 1 (W/S)
  if keys[pygame.K_w]:
      if first_position_y - user_speed >= 0:
          first_position_y -= user_speed

  if keys[pygame.K_s]:
      if first_position_y + user_speed + 100 <= HEIGHT:
          first_position_y += user_speed

  # Player 2 (UP/DOWN)
  if keys[pygame.K_UP]:
      if second_position_y - user_speed >= 0:
          second_position_y -= user_speed

  if keys[pygame.K_DOWN]:
      if second_position_y + user_speed + 100 <= HEIGHT:
          second_position_y += user_speed


  first_user = pygame.Rect(first_position_x,first_position_y,20,100)
  second_user = pygame.Rect(second_position_x,second_position_y,20,100)

  
  if x_direction <=-1:
    ball_position_x-=ball_speed
  else:
    ball_position_x+=ball_speed

  if y_direction ==0:
     ball_position_y+=0
  
  elif y_direction <=-1:
     ball_position_y-=ball_speed
  
  elif y_direction>=1:
     ball_position_y+=ball_speed
  

  if AABB_collision(ball_position_x,ball_position_y,10,10,first_position_x,first_position_y,100,20) or AABB_collision(ball_position_x,ball_position_y,10,10,second_position_x,second_position_y,100,20):
    
    x_direction*=-1

    if AABB_collision(ball_position_x,ball_position_y,10,10,first_position_x,first_position_y,100,20):
       paddle_center = first_position_y + 100//2
    else:
       paddle_center = second_position_y + 100//2

    ball_center = ball_position_y + 10//2

    if ball_center == paddle_center:
       y_direction = 0

    elif ball_center < paddle_center:
       y_direction = -1

    elif ball_center > paddle_center:
       y_direction = 1

  

  pygame.draw.rect(screen,(255,0,0),first_user)
  pygame.draw.rect(screen,(0,255,0),second_user)
  pygame.draw.circle(screen,(0,0,255),(ball_position_x,ball_position_y),10)

  
  if(ball_position_x<=0 or ball_position_x>=WIDTH):
    main_loop = False
  
  if(ball_position_y<=0 or ball_position_y>=HEIGHT):
     y_direction*=-1

     
  pygame.display.flip()

  clock.tick(FPS)

pygame.quit()
