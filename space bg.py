import pygame
import random
h = 450+500
w = 750+500

pygame.init()

colors = [(255,255,255),(0,255,0),(255,0,0),(255,255,0)]
x = []
y = []
times = 150
for i in range(times):
    x.append(random.randint(10,w-50))
    y.append(random.randint(10,h-50))
pygame.display.set_caption("pygame")

c = pygame.time.Clock()
dis = pygame.display.set_mode([w,h])

fl = True
while fl:


   for ev in pygame.event.get():
       if ev.type == pygame.QUIT:
           fl = False

   for i in range(times):
       if y[i] > h:
          y[i] = 0

       y[i]+=1   

   dis.fill((0,0,0))
   for i in range(times):
       pygame.draw.circle(dis, colors[random.randint(0,len(colors)-1)],(x[i],y[i]), 1)
         
   pygame.display.update()
   c.tick(120)
pygame.quit()
quit()
