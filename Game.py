import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600
SIZE = WIDTH, HEIGHT

screen = pygame.display.set_mode(SIZE)

TITLE = "Advanced Chrome Dino Game"

pygame.display.set_caption(TITLE)

up = False

gorund_size = 75
ground_rect = 0, HEIGHT - ground_size, WIDTH, HEIGHT

player = Player()

clock = pygame.time.Clock()

running = True
while running:
  mouse_pos = pygame.mouse.get_pos()
  
  for e in pygame.event.get():
    event = e.type
    
    if event == pygame.KEYDOWN:
      if e.key == pygame.K_UP or e.key == pygame.K_w:
        up = True
    
    if event == pygame.KEYUP:
      if e.key == pygame.K_UP or e.key == pygame.K_w:
        up = False
  
  if up:
    player.jump()
  
  player.gravity()
  player.react()
  
  screen.fill((100, 100, 100))
  screen.fill((100, 100, 100), ground_rect)
  
  pygame.display.flip()
  
  clock.tick(60)
  
