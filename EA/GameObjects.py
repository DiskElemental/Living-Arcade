import random

#TODO
# 1. Figure out what the action set looks like for this project.

class Game(object):
    Fitness = None
    Score = 0

    #Basic Properties to create a game, everything else will be generated later
    def __init__(self, OffScreenEffect, NumActionButtons, Score):
        self.ID = random.randint(0,2**(128)) #Sample Space so big collisions aren't a concern
        self.OffScreenEffect = OffScreenEffect
        self.NumActionButtons = NumActionButtons
        self.Score = Score

    #We don't pass individual objects into the Game
    #We define rules for entire classes of objects, as shown below
    #Tmp = [GameObject, (locations_of_object)]
    #This allows us to tweak individual object spawn rates
    #And ensures all objects sharing a sprite have consistent properties.
    def SetObjectLogs(self, objList):
        self.objList = objList
        self.Player = objList[-1]    #Player

    def SetFitness(self,fitness):
        self.Fitness = fitness


class GameObject(object):
    Fitness = 0

    #All buttons saved as variables with an empty action set
    Up = []
    Left = []
    Down = []
    Right = []
    A1 = []
    A2 = []
    A3 = []
    A4 = []
    CollisionReactions = []

    def __init__(self, Name, HP, Shape, Color, Opacity, NumActionButtons):
        self.Name = Name
        self.HP = HP
        self.Shape = Shape
        self.Color = Color
        self.Opacity = Opacity

    def GenerateReactions(self, NumAct, objList):
        #List of all buttons
        #ButtonValues = [Up, Left, Down, Right, A1, A2, A3, A4]
        ButtonReactions = [None, None, None, None, None, None, None, None]

        # VVV THIS IS THE PRIORITY VVV
        ActionSet = [["Game.Score += " + str(random.randint(0,10))], ["Self.Destroy()"]]
        # ^^^ NEED TO FIGURE OUT WHAT THE ACTION SET LOOKS LIKE ^^^

        #While loop which ensures we pick different values each time
        prev = -1
        for i in range(NumAct):
            k = prev
            while(k == prev):
                k = random.randint(0,len(ButtonReactions)-1)
            j = random.choice(ActionSet)
            ButtonReactions[k] = j
            prev = k

        self.Up, self.Left, self.Down, self.Right, self.A1, self.A2, self.A3, self.A4 = ButtonReactions

        #total number of reactions in range [1, 8]
        i = random.randint(1,8)

        #Picks a random Collision Type and a Random action
        #Then adds the action to the collision's action set
        #There may be some actions without a reaction, and some with multiple reactions
        tmp = []
        for j in range(i):
            k = random.choice(objList)[0].Name
            l = random.choice(ActionSet)
            tmp.append((k,l))
        self.CollisionReactions = tmp

    def SetFitness(self, fitness):
        self.Fitness = fitness








