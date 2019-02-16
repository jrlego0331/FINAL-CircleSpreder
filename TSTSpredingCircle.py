import pygame
import os
import sys
import random as r
import math
import time

class circleCal():
    def __init__(self):
        self.dotNum = 10
        self.midAng = 360 / self.dotNum
        self.growRate = 5

    def AcutalMathCal(self):
        for n in range(len(the.Circle)):
            MPOSX = the.Circle[n][0]
            MPOSY = the.Circle[n][1]
            currentRad = the.Circle[n][2] + self.growRate

            for mid in range(self.dotNum):
                currentMidAng = mid * self.midAng
                SINVAL = math.sin(math.radians(currentMidAng))
                COSVAL = math.cos(math.radians(currentMidAng))
                print("SINVAL: ", SINVAL, " COSVAL: ", COSVAL)
                
                hight = SINVAL * currentRad
                length = currentRad * COSVAL

                instantX = round(MPOSX  + length)
                instantY = round(MPOSY + hight)
                the.dots.append([instantX, instantY])
                
            the.Circle[n][2] += self.growRate
            
        

class MainGameOperator():
    def __init__(self):
        self.screenx = 700
        self.screeny = 700
        self.screen = pygame.display.set_mode((self.screenx, self.screeny))
        pygame.display.set_caption("Spreding Circle")

        self.gameStatus = True
        self.BGCol = (30, 30, 30)
        self.gameSet()

    def gameSet(self):
        self.Circle = []
    
    def loopMain(self):
        while self.gameStatus == True:
            self.inputControl()
            for n in range((len(self.Circle))):
                print(n, "th Cicle is ", self.Circle[n])
            self.dots = []
            self.updateToCal()
            self.draw()

            pygame.display.update()
            

    def inputControl(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(event.type)
                self.gameStatus = True
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.gameStatus = False
                    print("Esc Key Pressed")
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                print(pos)
                x = pos[0]
                y = pos[1]
                self.Circle.append([x, y, 0])
                print("M1 preseed")


    
    def updateToCal(self):
        blacklist = []
        for n in range(len(self.Circle)):
            if self.Circle[n][2] > 800:
                blacklist.append(n)
       
        for x in range(len(blacklist)):
            self.Circle.pop(blacklist[x])
            
        cal = circleCal()
        cal.AcutalMathCal()
        print("# of Dots: ", len(self.dots))
        
    
    def draw(self):
        self.screen.fill(self.BGCol)

        for n in range(len(self.dots)):
            #randCol = (r.randint(0, 255), r.randint(0, 255), r.randint(0, 255))
            curntpos = self.dots[n]
            pygame.draw.circle(self.screen, (255, 255, 255), curntpos, 4)

if __name__ == '__main__':
    the = MainGameOperator()
    the.loopMain()