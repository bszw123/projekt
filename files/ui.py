import pygame
from settings import *

class UI:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.font = pygame.font.Font(FONT,FONT_SIZE)

        #paski i statystyki
        bar_x = 8
        bar_y = 685
        self.health_bar = pygame.Rect(bar_x,bar_y-17,BAR_WIDTH,BAR_HEIGHT)
        self.mana_bar = pygame.Rect(bar_x,bar_y,BAR_WIDTH,BAR_HEIGHT)

    def controls(self):
        text_surface = self.font.render(str('Sterowanie:                     '),False,COLOUR_TEXT)
        text_surface2 = self.font.render(str('poruszanie sie - strzalki    '),False,COLOUR_TEXT)
        text_surface3 = self.font.render(str('magia - w                        '),False,COLOUR_TEXT)        
        text_surface4 = self.font.render(str('zmiana magii - d  '),False,COLOUR_TEXT)        
        text_surface5 = self.font.render(str('menu ulepszen - lewy shift'),False,COLOUR_TEXT)
        #na oko wyliczone                
        x=1045
        y=545
        text_rectangle = text_surface.get_rect(topleft = (x,y))
        text_rectangle2 = text_surface2.get_rect(topleft = (x,y+38))
        text_rectangle3 = text_surface3.get_rect(topleft = (x,y+76))
        text_rectangle4 = text_surface4.get_rect(topleft = (x,y+114))
        text_rectangle5 = text_surface5.get_rect(topleft = (x,y+152))

        pygame.draw.rect(self.screen,COLOUR_UI_BG,text_rectangle.inflate(20,20))
        self.screen.blit(text_surface,text_rectangle)

        pygame.draw.rect(self.screen,COLOUR_UI_BG,text_rectangle2.inflate(20,20))
        self.screen.blit(text_surface2,text_rectangle2)

        pygame.draw.rect(self.screen,COLOUR_UI_BG,text_rectangle3.inflate(20,20))
        self.screen.blit(text_surface3,text_rectangle3)

        pygame.draw.rect(self.screen,COLOUR_UI_BG,text_rectangle4.inflate(20,20))
        self.screen.blit(text_surface4,text_rectangle4)

        pygame.draw.rect(self.screen,COLOUR_UI_BG,text_rectangle5.inflate(20,20))
        self.screen.blit(text_surface5,text_rectangle5)



    def xp(self,xp):
        surface = self.font.render("xp: "+str(int(xp)),False,COLOUR_TEXT)
        rectangle = surface.get_rect(topleft = (18,638))
        pygame.draw.rect(self.screen,COLOUR_UI_BG,rectangle.inflate(20,20))
        self.screen.blit(surface,rectangle)


    def bar(self,froggo):

        #życie
        pygame.draw.rect(self.screen,COLOUR_UI_BG,self.health_bar)
        width1 = self.health_bar.width * (froggo.hp/froggo.stats['hp']) #pasek 200px*1 ratio =200px (wiec caly pasek jest wypelniony zyciem)
        rectangle1 = self.health_bar.copy() #juz wiekszosc info jest w health_bar wiec to kopiuje po prostu
        rectangle1.width = width1
        pygame.draw.rect(self.screen,COLOUR_HEALTH,rectangle1)
        pygame.draw.rect(self.screen,COLOUR_UI_BORDER,self.health_bar,4)

        #mana
        pygame.draw.rect(self.screen,COLOUR_UI_BG,self.mana_bar)
        current_width2 = self.mana_bar.width * (froggo.mana/froggo.stats['mana'])
        current_rectangle2 = self.mana_bar.copy()
        current_rectangle2.width = current_width2
        pygame.draw.rect(self.screen,COLOUR_MANA,current_rectangle2)
        pygame.draw.rect(self.screen,COLOUR_UI_BORDER,self.mana_bar,4)



    def display(self,froggo):
        self.controls()
        self.xp(froggo.xp)
        self.bar(froggo)