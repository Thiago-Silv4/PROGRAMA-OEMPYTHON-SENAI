import pygame
pygame.init()
tela  = pygame.display.set_mode((300,300))


tela.fill('blue')

         


#run = True         
#while run:
  #  for event in pygame.event.get():
   #     if event.type == pygame.QUIT:
    #        run  = False
  #          pygame.quit()
  #  tela.fill('green') 
   # pygame.draw.rect(tela,('red'),(100,100,70,70))
  #  pygame.display.flip() 
    
    
    # circle 
    
    # elipse
    

# import pygame
# pygame.init()
# tela  = pygame.display.set_mode((800,600))

# run = True         
# while run:
   # for event in pygame.event.get():
      #  if event.type == pygame.QUIT:
           # run  = False
          #  pygame.quit()
 #   tela.fill('black')
  #  pygame.draw.circle(tela,('red'),(500,100),(50))
  #  pygame.display.flip() 
  
  
import pygame
pygame.init()
tela  = pygame.display.set_mode((800,600))

run = True         
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run  = False
            pygame.quit()
    tela.fill('blue')
    pygame.draw.ellipse(tela,('white'),(500,100,200,50),(50))
    pygame.display.flip() 
  