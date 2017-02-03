from GameObjects import *
import random, json

def InitializePopulation(Pop_Size, Score, OffScreenEffect, NumObjectTypes, NumObjects, MaxX, MaxY, HP):
    population = []


    for i in range(Pop_Size):
        #Pick the number of used buttons, and initialize GameObject
        NumActionButtons = random.randint(2,4)
        Player = GenerateGameObj(NumActionButtons,HP)
        NewGame = Game(OffScreenEffect, NumActionButtons, Score)
        objectList = []

        #Randomize the size of each object population
        for j in range(NumObjects):
            objectList.append([GenerateGameObj(NumActionButtons,HP),(random.uniform(0,MaxX),random.uniform(0,MaxY))])

        objectList.append([Player,(random.uniform(0,MaxX),random.uniform(0,MaxY))]) #player is always at index '-1'

        #Put all the information together, and insert into the Population

        print(len(objectList))

        for i in objectList:
            i[0].GenerateReactions(NumActionButtons,objectList)
        NewGame.SetObjectLogs(objectList)
        population.append(NewGame)

    return population

def GenerateGameObj(NumActionButtons, HP):
    Shape = random.choice(["triangle", "circle", "cross", "square"])
    Color = random.randint(0,999) #TODO: Color Generating Code
    Opacity = random.uniform(0,100) #Opacity Percentage
    NewObj = GameObject(Shape+str(Color),HP,Shape,Color,Opacity, NumActionButtons)
    return NewObj


def dumper(obj):
    return obj.__dict__

def ToJson(CurrentGame):
    with open("JsonTest.txt", "w+") as myfile:
        json.dump(CurrentGame,myfile,default=dumper,indent=4)


def main():
    pop = InitializePopulation(10,0,None,3,5,100,100,1)
    ToJson(pop[0])

if __name__ == '__main__':
    main()
