from time import sleep
from random import randint
baboos=[]
kingdoms=[]
kol_vo=0
day=0

class Kingdom:
    def __init__(self, name):
        self.wood=0
        self.stone=0
        self.food=0
        self.name=name
    def day(self):
        if self.food>10:
            new(self.name, 0)
            self.food-=5
            print("New people!")
        print(f"Wood: {self.wood}")
        print(f"Stone: {self.stone}")
        print(f"Food: {self.food}")


class Baboo:
    def __init__(self, health, wood, stone, food, strenght, ID, kingdom):
        self.health=health
        self.age=0
        self.wood=wood/100
        self.stone=stone/100
        self.food=food/100
        self.strenght=strenght/100
        self.ID=ID
        self.warrior=False
        self.kingdom=kingdom
        if self.strenght >= 1.3:
            self.warrior=True
            print("New Warrior!")
    def day(self):
        self.age += 1
        if self.warrior==False:
            if self.wood>self.stone and self.wood>self.food:
                return self.wood
            elif self.stone>self.wood and self.stone>self.food:
                return self.stone
            elif self.food>self.wood and self.food>self.stone:
                return self.food
        return 0



def new(kingdom, starter=0):
    global kol_vo
    kol_vo+=1
    if starter == 0:
        baboos.append(
        Baboo(randint(70, 100), randint(25, 200), randint(25, 200), randint(25, 200), randint(25, 200), kol_vo,
        kingdom))
    else:
        baboos.append(
        Baboo(randint(70, 100), 0, 0, randint(25, 200), 0, kol_vo,
        kingdom))

def death():
    global kol_vo
    for i, j in enumerate(baboos):
        if baboos[i].age>60:
            baboos.pop(i)

def new_k(kingdom="Patapons"):
    kingdoms.append(Kingdom(kingdom))
    new(kingdom, 1)

new_k()

while True:
    a=0
    day+=1
    vivod = f"Day {day}"
    print(f"{vivod:=^50}")
    for i, j in enumerate(baboos):
        a=baboos[i].day()
        for l, y in enumerate(kingdoms):
            if kingdoms[l].name==baboos[i].kingdom:
                if baboos[i].wood > baboos[i].stone or baboos[i].wood > baboos[i].food:
                    kingdoms[l].wood+=a
                elif baboos[i].stone > baboos[i].wood or baboos[i].stone > baboos[i].food:
                    kingdoms[l].stone += a
                elif baboos[i].food > baboos[i].wood or baboos[i].food > baboos[i].stone:
                    kingdoms[l].food += a
        sleep(0.2)
        death()
    for i, j in enumerate(kingdoms):
        kingdoms[i].day()
    if len(baboos)<1:
        break

