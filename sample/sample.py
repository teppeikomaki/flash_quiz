import sys
import pygame
import time
from pygame.locals import QUIT
 
def main():
    pygame.init()
    surface = pygame.display.set_mode((400, 200))
    print(surface.get_rect().width)
    print(surface.get_rect().height)
 
    jfont = pygame.font.SysFont('meiryo', 20)   # フォントファイルのパス
 
    # (テキスト, アンチエイリアス, カラー)を指定
    list = ["1234567890","1234567890123456789012345678901234567890","123456789012345678901234567890123456789012345678901234567890"]
    for print_text in list:
        
        text = jfont.render(print_text, True, (0x88, 0xC0, 0xEF)) 
        textpos = text.get_rect()
    
        textpos.centerx = surface.get_rect().centerx  # X座標
        textpos.centery = surface.get_rect().centery   # Y座標
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        surface.fill((88, 90, 100))
        surface.blit(text, textpos)
        pygame.display.update()
        time.sleep(2)
 
 
if __name__ == '__main__':
    main()