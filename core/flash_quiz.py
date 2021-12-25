import sys,os
import csv
import pygame
from pygame.locals import QUIT
import random

def import_csv_file(select_directory = None, select_file = None):
    cwd = os.getcwd()
    file_path = os.path.dirname(cwd) 
    file_path = os.path.join(file_path,"csv")
    files = os.listdir(file_path)
    files_file = [f for f in files]
    files = []
    print("---------file/directory list-------")
    for file_name in files_file:
        files.append(file_name)
        if os.path.isfile(os.path.join(file_path, file_name)):
            csv_file = open(file_path + "\\" + file_name, "r", encoding="utf-8", errors="", newline="" )
            
            f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
            count = 0
            for i in f:
                count += 1
            print("file_num:",len(files) - 1 ,file_name,count)
        else:
            print("file_num:",len(files) - 1 ,file_name)
    print("-----------------------------------")

    if select_directory == None:
        print("input file or directory num",end=":")
        selected_file = input()
        selected_file = int(selected_file)

    if not selected_file in range(len(files)):
        raise ValueError("This file doesn't exist.")
    
    file_path = os.path.join(file_path,files[selected_file])
    
    if os.path.isdir(file_path):
        print("---------file/directory list-------")
        files = os.listdir(file_path)
        files_file = [f for f in files]
        files = []
        for file_name in files_file:
            files.append(file_name)
            assert os.path.isfile(os.path.join(file_path, file_name))
            csv_file = open(file_path + "\\" + file_name, "r", encoding="utf-8", errors="", newline="" )
            
            f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
            count = 0
            for i in f:
                count += 1
            print("file_num:",len(files) - 1 ,file_name,count)
            
        print("-----------------------------------")
        if select_directory == None:
            print("input file_num",end=":")
            selected_file = input()
            selected_file = int(selected_file)
            
        if not selected_file in range(len(files)):
            raise ValueError("This file doesn't exist.")
    
        file_path = os.path.join(file_path, files[selected_file])
    
    return file_path

def make_question_list(file_path,is_shuffle=True):
    
    csv_file = open(file_path, "r", encoding="utf-8", errors="", newline="" )
    f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

    question_list = []
    for i in f:
        question_list.append(i)
    if is_shuffle == True:
        random.shuffle(question_list)
        
    return question_list

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
        self.surface.fill((88, 90, 100))
        pygame.display.flip()
        
    def draw(self,list):
        for print_question in list:
            #desplay question
            self.desplay_text(print_question[0])
            pygame.display.update()
            sleeped_time = int((len(print_question[0]) // 5 +1 ) * 1.0)
            pygame.time.delay(sleeped_time * 1000)
            #desplay answer
            self.desplay_text(print_question[1])
            pygame.display.update()
            sleeped_time = int((len(print_question[1]) // 5 + 1 ) * 1.0)
            pygame.time.delay(sleeped_time * 1000)

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
            
        print(print_text)
        for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
        #textpos:(左上のx座標,y座標,文字の幅,文字の高さ)

if __name__ == '__main__':
    file_path = import_csv_file()
    question_list = make_question_list(file_path)
    gui = GUI((800,400))
    gui.draw(question_list)

