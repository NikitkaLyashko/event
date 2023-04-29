import random
import time, pygame
from pygame import event
from pygame import display
pygame.init()
window = display.set_mode([800, 600])

text = pygame.font.SysFont("arial", 30, False, True)

a=pygame.event.custom_type()

pygame.time.set_timer(a,3000,1)

while True:
    time.sleep(1/60)

    x=random.randint(10,800)
    y=random.randint(10,600)



    cobibtie_list = event.get()
    for cobibtie in cobibtie_list:

        if cobibtie.type==a:
            window.fill([211,219,5])
            pygame.time.set_timer(a, random.randint(500,3000), 1)

        if cobibtie.type==pygame.QUIT:
            text_on_wind=text.render("НЕ закроюсь",True,[134,213,42])
            window.blit(text_on_wind,[220,300])

        if cobibtie.type==pygame.KEYDOWN and cobibtie.key==32:
            space=text.render("Пробел",True,[134,213,42])
            window.blit(space,[x,y])

        if cobibtie.type==pygame.KEYDOWN and cobibtie.key!=32:
            key=text.render("клавиша  "+str(cobibtie.key),True,[152,111,100])
            window.blit(key,[x,y])

        if cobibtie.type==pygame.MOUSEBUTTONDOWN:
            if cobibtie.button==pygame.BUTTON_LEFT:
                mouse_1=text.render(str(cobibtie.pos),True,[54,200,211])

            if cobibtie.button == pygame.BUTTON_RIGHT:
                mouse_1 = text.render(str(cobibtie.pos), True, [250, 0, 2])

            if cobibtie.button == pygame.BUTTON_MIDDLE:
                mouse_1 = text.render(str(cobibtie.pos), True, [250,184, 2])

            window.blit(mouse_1, [cobibtie.pos[0], cobibtie.pos[1]])


        if cobibtie.type==pygame.MOUSEMOTION and cobibtie.buttons[0]==1:
            pygame.draw.circle(window, [225, 0, 0],cobibtie.pos, 10, 3)

        elif cobibtie.type==pygame.MOUSEMOTION and cobibtie.buttons[1]==1:
            pygame.draw.circle(window, [0,225, 0],cobibtie.pos, 10, 3)

        elif cobibtie.type==pygame.MOUSEMOTION and cobibtie.buttons[2]==1:
            pygame.draw.circle(window, [0,0, 225], cobibtie.pos, 10, 3)

        elif cobibtie.type==pygame.MOUSEMOTION:
            pygame.draw.circle(window, [145, 23, 72],cobibtie.pos, 1, 1 )



















    display.flip()
        # print(cobibtie)

