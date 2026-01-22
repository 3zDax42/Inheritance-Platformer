import pygame
import random
pygame.display.set_caption("Platformer with Inheritance")
Game_Screen = pygame.display.set_mode((800, 800))

Clock = pygame.time.Clock()
Running = True

class Player():
    def __init__(self):
        self.X_Pos = 400
        self.Y_Pos = 700
        self.X_Vol = 0
        self.Y_Vol = 0
        self.Movement_Input = [False, False, False] # Left, Right, Up
    
    def Input(self, Key1, Key2, Key3):
        if event.type == pygame.KEYDOWN:
            if event.key == Key1:
                self.Movement_Input[0] = True
            elif event.key == Key2:
                self.Movement_Input[1] = True
            elif event.key == Key3:
                self.Movement_Input[2] = True
        elif event.type == pygame.KEYUP:
            if event.key == Key1:
                self.Movement_Input[0] = False
            elif event.key == Key2:
                self.Movement_Input[1] = False
            elif event.key == Key3:
                self.Movement_Input[2] = False

    def Physics(self):
        if self.Movement_Input[0] == True:
            self.X_Vol += 1
        elif self.Movement_Input[1] == True:
            self.X_Vol -= 1
        else:
            self.X_Vol = 0
        self.X_Pos += self.X_Vol

class Platform():
    def __init__(self, X_Pos=0, Y_Pos=0, Type=None):
        self.X_Pos = X_Pos
        self.Y_Pos = Y_Pos
        self.Type = Type

    def Move(self):
        pass

    def Draw(self):
        pygame.draw.rect(Game_Screen, (100, 50, 100), (self.X_Pos, self.Y_Pos, 80, 30))

class Moving_Platform(Platform):
    def __init__(self, X_Pos=0, Y_Pos=0, Type=None):
        self.X_Pos = X_Pos
        self.Y_Pos = Y_Pos
        self.Type = Type
        self.Start_X = self.X_Pos
        self.Start_Y = self.Y_Pos
        self.Direction = 1
    
    def Move(self):
        if self.Direction == 1:
            if self.X_Pos < self.Start_X:
                self.Direction *= -1
            else:
                self.X_Pos -= .1
        else:
            if self.X_Pos > self.Start_X +200:
                self.Direction *= -1
            else:
                self.X_Pos += .1

    def Draw(self):
        return super().Draw()

class Ice(Moving_Platform):
    def __init__(self, X_Pos=0, Y_Pos=0, Type=None):
        self.X_Pos = X_Pos
        self.Y_Pos = Y_Pos
        self.Type = Type
        self.Start_X = self.X_Pos
        self.Start_Y = self.Y_Pos
        self.Direction = 1

    def Move(self):
        if self.Type == "Dynamic:Ice":
            return super().Move()
        elif self.Type == "Static:Ice":
            pass
        else:
            print(self.Type)

    def Draw(self):
        return super().Draw()

class Trampoline(Moving_Platform):
    def __init__(self, X_Pos=0, Y_Pos=0, Type=None):
        self.X_Pos = X_Pos
        self.Y_Pos = Y_Pos
        self.Type = Type
        self.Start_X = self.X_Pos
        self.Start_Y = self.Y_Pos
        self.Direction = 1

    def Move(self):
        if self.Type == "Dynamic:Trampoline":
            return super().Move()
        elif self.Type == "Static:Trampoline":
            pass
        else:
            print(self.Type)

    def Draw(self):
        return super().Draw()

class Breakable(Moving_Platform):
    def __init__(self, X_Pos=0, Y_Pos=0, Type=None):
        self.X_Pos = X_Pos
        self.Y_Pos = Y_Pos
        self.Type = Type
        self.Start_X = self.X_Pos
        self.Start_Y = self.Y_Pos
        self.Direction = 1

    def Move(self):
        if self.Type == "Dynamic:Breakable":
            return super().Move()
        elif self.Type == "Static:Breakable":
            pass
        else:
            print(self.Type)

    def Draw(self):
        return super().Draw()

class Split(Platform):
    def __init__(self, X_Pos=0, Y_Pos=0, Type=None):
        self.X_Pos = X_Pos
        self.Y_Pos = Y_Pos
        self.Type = Type
        self.Space_Between = random.randrange(100, 400)

    def Move(self):
        if self.Type == "Static:Spit":
            return super().Move()
        else:
            print(self.Type)

    def Draw(self):
        pygame.draw.rect(Game_Screen, (100, 50, 100), (self.X_Pos, self.Y_Pos, 80, 30))
        pygame.draw.rect(Game_Screen, (100, 50, 100), (self.X_Pos + self.Space_Between, self.Y_Pos, 80, 30))


Platforms = []

for i in range(3, 5):
    Platforms.append(Platform(random.randrange(50, 700), random.randrange(50, 700), "Static:Simple"))
for i in range(1, 3):
    Platforms.append(Moving_Platform(random.randrange(50, 700), random.randrange(50, 500), "Dynamic:Simple"))

while Running == True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
    
    for i in Platforms:
        i.Move()
    
    
    Game_Screen.fill((0, 0, 0))
    
    for i in Platforms:
        i.Draw()

    pygame.display.flip()

pygame.quit()
