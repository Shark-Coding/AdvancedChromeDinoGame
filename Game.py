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


class Player:
  player_pos = 50
  def __init__(self, color=(0, 0, 0)):
    self.color = color
    self.width = 30
    self.height = 100
    self.x = player_pos
    self.y = HEIGHT - ground_size - self.height
    self.speed = 0
    self.jump_power = 15
    self._gravity = 1
  
  @property
  def pos(self):
    return self.x, self.y
  
  @pos.setter
  def pos(self, p):
    self.x, self.y = p
  
  def jump(self):
    self.speed = self.jump_power
  
  def gravity(self):
    self.speed -= self._gravity
  
  def react(self):
    self.y -= self.speed
    if self.y < HEIGHT - ground_size - self.height:
      self.y = HEIGHT - ground_size - self.height
      self.speed = 0
  
  def draw(self, surf):
    rect = self.x, self.y, self.width, self.height
    surf.blit(self.color, rect)


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
  
