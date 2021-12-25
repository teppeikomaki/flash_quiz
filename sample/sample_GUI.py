import sys
import pygame
import time
from pygame.locals import QUIT


class GUI:
    def __init__(self, display_size = (400,200), font_size = 40):
        pygame.init()
        self.WIDTH = display_size[0]
        self.HEIGHT = display_size[1]
        self.FONT_SIZE = font_size #font_hight = font_size * 1.5
        self.surface = pygame.display.set_mode(display_size)
        self.jfont = pygame.font.SysFont('meiryo', self.FONT_SIZE)
        print(self.surface.get_rect().width)
        print(self.surface.get_rect().height)
        
    def draw(self,list):
        for print_text in list:
            self.desplay_text(print_text)
            pygame.display.update()
            time.sleep(2)

    def desplay_text(self,print_text):
        self.surface.fill((88, 90, 100))
        text = self.jfont.render(print_text, True, (0x88, 0xC0, 0xEF))
        textpos = text.get_rect()
        row_num = textpos.w // self.WIDTH + 1
        len_of_row = len(print_text) // row_num + 1
        print_list =  [print_text[idx:idx + len_of_row] for idx in range(0,len(print_text),len_of_row)]
        for i in range(row_num):
            printed_text = print_list[i]
            text = self.jfont.render(printed_text, True, (0x88, 0xC0, 0xEF)) 
            textpos = text.get_rect()
            height = (row_num - 2*i - 1) * self.FONT_SIZE * 1.5 / 2.0
            textpos.centerx = self.surface.get_rect().centerx  # X座標
            textpos.centery = self.surface.get_rect().centery - height   # Y座標
            self.surface.blit(text, textpos)
            
        #self.desplay_text(print_text)
        #self.desplay_text(print_text[len(print_text)//2:])
            
        print(textpos,textpos.w,textpos.h)
        for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
        #textpos:(左上のx座標,y座標,文字の幅,文字の高さ)
def main():
    gui = GUI((800,400))
    list = ["12345678901234567890","1234567890123456789009876543210987654321","123456789012345678901234567890123456789012345678901234567890"]
    gui.draw(list)
    
        
        
        
    
        
        
        

        
        
 
 
if __name__ == '__main__':
    main()