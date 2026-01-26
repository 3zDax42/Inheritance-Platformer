import pygame
import random
pygame.display.set_caption("Platformer with Inheritance")
Game_Screen = pygame.display.set_mode((800, 800))

Clock = pygame.time.Clock()
Running = True

class Player():
    def __init__(self):
        self.X_Pos = 400
        self.Y_Pos = 600
        self.X_Vol = 0
        self.Y_Vol = 0
        self.OnGround = True
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
        if (self.Movement_Input[0] == True) and (self.OnGround == True) and (self.X_Vol < 5):
            self.X_Vol += 1
        elif (self.Movement_Input[0] == False) and (self.OnGround == True) and (self.X_Vol > 0):
            if (self.OnType == "Static:Ice") or (self.OnType == "Dynamic:Ice"):
                pass
            else:
                self.X_Vol = 0
        elif (self.Movement_Input[1] == True) and (self.OnGround == True) and (self.X_Vol > -5):
            self.X_Vol -= 1
        else:
            self.X_Vol = 0
        self.X_Pos += self.X_Vol
        if (self.OnGround == True) and (self.Movement_Input[2] == True):
            if (self.OnType == "Static:Ice") or (self.OnType == "Dynamic:Ice"):
                self.Y_Vol = -1
            else:
                self.Y_Vol = -2
        if (self.OnGround == False) and (self.X_Vol <= 0):
            self.Y_Vol += .5
        self.Y_Pos += self.Y_Vol
        print(f"The player is at {self.X_Pos} and {self.Y_Pos} and is moving {self.Y_Vol} per loop")
    
    def Colision(self, Type, X, Y):
        if (X < self.X_Pos < X + 80) and ( Y < self.Y_Pos < Y + 30):
            self.PlatformColide = True
            self.OnGround = True
        else:
            self.PlatformColide = False
            self.OnGround = False
        if self.PlatformColide == True:
            self.OnType = Type
        else:
            self.OnType = None

    def Draw(self):
        pygame.draw.rect(Game_Screen, (180, 100, 200), (self.X_Pos, self.Y_Pos, 32, 32))

player1 = Player()

class Platform():
    def __init__(self, X_Pos=0, Y_Pos=0, Type=None):
        self.X_Pos = X_Pos
        self.Y_Pos = Y_Pos
        self.Type = Type

    def Move(self):
        pass

    def ReturnHitBox(self, XorY):
        if XorY == "X":
            return self.X_Pos
        elif XorY == "Y":
            return self.Y_Pos
        else:
            print("Error in ReturnHitBox function")

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

    def ReturnHitBox(self, XorY):
        return super().ReturnHitBox(XorY)

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

    def ReturnHitBox(self, XorY):
        return super().ReturnHitBox(XorY)

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

    def ReturnHitBox(self, XorY):
        return super().ReturnHitBox(XorY)
    
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
        self.Living = True

    def Move(self):
        if self.Type == "Dynamic:Breakable":
            return super().Move()
        elif self.Type == "Static:Breakable":
            pass
        else:
            print(self.Type)

    def ReturnHitBox(self, XorY):
        return super().ReturnHitBox(XorY)

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

    def ReturnHitBox(self, XorY):
        return super().ReturnHitBox(XorY)
    
    def Draw(self):
        pygame.draw.rect(Game_Screen, (100, 50, 100), (self.X_Pos, self.Y_Pos, 80, 30))
        pygame.draw.rect(Game_Screen, (100, 50, 100), (self.X_Pos + self.Space_Between, self.Y_Pos, 80, 30))


PlatformType = ["Simple", "Ice", "Trampoline", "Breakable", "Split"]

Platforms = []
Platforms.append(Platform(360, 600, "Static:Simple"))
for i in range(random.randrange(3, 5)):
    Platforms.append(Platform(random.randrange(50, 700), random.randrange(50, 700), "Static:Simple"))
for i in range(random.randrange(1, 3)):
    Platforms.append(Moving_Platform(random.randrange(50, 500), random.randrange(50, 700), "Dynamic:Simple"))

while Running == True:
    Clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
        player1.Input(pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP)
    
    for i in Platforms:
        i.Move()
        player1.Colision(i.Type, i.ReturnHitBox("X"), i.ReturnHitBox("Y"))

    player1.Physics()
    
    Game_Screen.fill((0, 0, 0))
    
    for i in Platforms:
        i.Draw()

    player1.Draw()

    pygame.display.flip()

pygame.quit()
