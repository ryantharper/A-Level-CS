# limited space in backpack

# kill zombie: 5pts, hit zombie: 1pt
# kill bear: 8pts, hit bear: 1pt
# kill orc: 15pts, hit orc: 2pts

import random, time
            # Gun Name: [ammo, fp]
gunList = {"Hand Gun": [40,1],
           "Rifle": [30,3],
           "Shotgun": [4,10],
           "Grenade": [1,20]}

monsterList = ["zombies", "bears", "orcs"]

class Player:
    def __init__(self, health, startGun, backpack, score):
        self.health = health
        self.guns = {gun:gunList[gun] for gun in [startGun]}
        self.backpack = backpack
        self.currentGun = startGun
        self.score = score

    # add gun
    def addGun(self, gun):
        self.guns[gun] = gunList[gun]

    # switch weapon method
    def switchWeapon(self):
        for i,v in enumerate(self.guns):
            print("{0}. {1} ammo: {2} firepower: {3}".format(i+1, player.guns[v][0], player.guns[v][1]))
            selection = int(input("Please select a gun: "))
            backpack.append(currentGun)
            currentGun = list(self.guns.keys())[selection-1]

    #remove weapon method

class Monster:
    def __init__(self, monsterType):
        self.monsterType = monsterType
        if monsterType == "zombies":
            self.attack = 1
            self.health = 5
        elif monsterType == "bears":
            self.attack = 3
            self.health = 15
        elif monsterType == "orcs":
            self.attack = 30
            self.health = 25

    def monsterAttack(self):
        numMonsters = random.randint(2,5)
        print()

def startText():
    print("Text Based Shooter!")
    print("This program is a simple game based on first person shooters where you can pick up and")
    print("store weapons and battle enemies...")
    print()
    print()
    anyKey = input("Please press any key to start...")
    print()

def monsterAttack(player):
    monster = random.choice(monsterList)
    numMonsters = random.randint(2,5)
    print("There are " + str(numMonsters) + " " + str(monster) + " in front of you...")
    print()
    monsters = [Monster(monster) for i in range(numMonsters)]

    while len(monsters) > 0 and player.health > 0:
        print("You are equipped with the {0} ammo:{1}".format(player.currentGun, gunList[player.currentGun][0]))
        if len(player.guns) > 1:
            switch = input("Do you wish to switch gun (Y/N)?: ")
            print()
            if switch.lower() == "y":
                player.switchWeapon()

        gunFp = player.guns[player.currentGun][1]
        gunAmmo = player.guns[player.currentGun][0]
        print("You bravely battle the " + monster)
        for count in range(len(monsters)):
            if gunAmmo > 0:
                # attack monster
                hitMonster = random.randint(1,100)
                if hitMonster % 9 != 0:
                    print("You shot "+monster+str(count+1)+"!")
                    monsters[count].health -= gunFp
                else:
                    print("You missed "+monster+str(count+1)+"!")
                gunAmmo-=1
            else:
                print("This gun is out of ammo!")
            time.sleep(1)
        player.guns[player.currentGun][0] = gunAmmo
        monsters = [m for m in monsters if m.health > 0]
        
        if len(monsters) > 0:
            print("There is still " + str(len(monsters)) + " " + monster + " after you!")
            time.sleep(2)
            for i in monsters:
                hitPlayer = random.randint(1,50)
                if hitPlayer % 3 == 0:
                    print("The " + monster + " shot you!")
                    player.health -= i.attack
                    print("Current Health: " + str(player.health))
                else:
                    print("The " + monster + " missed!")
                time.sleep(1)
        if len(monsters)>1:
            print("The " +  monster + " are still coming after you")
        elif len(monsters)==1:
            print("There is only one " + monster + " left")
        else:
            print("The "+monster+" are dead...")
            print("Your health is now {0}".format(player.health))
            break
        print()
        print()
        if player.health<=0:
            print("You died!")
            break
        anyKey = str(input("Press R to run OR any letter to continue fighting"))
        if anyKey.lower().startswith("r"):
            break
        else:
            pass

    return


def main():
    startText()
    player = Player(30,"Hand Gun", [],0)
    
    while player.health > 0:    
        time.sleep(0.5)
        randNum = 1 #random.randint(1,10)
        print("asd")
        if randNum == 1:
            monsterAttack(player)
            
main()
    
        
