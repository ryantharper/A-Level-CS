# limited space in backpack

# kill zombie: 5pts, hit zombie: 1pt
# kill bear: 8pts, hit bear: 1pt
# kill orc: 15pts, hit orc: 2pts

# use health/ammo pack --> gets removed from bp

import random, time, sys
            # Gun Name: [ammo, fp]
gunList = {"Hand Gun": [40,1],
           "Rifle": [30,3],
           "Shotgun": [4,10],
           "Grenade": [1,20]}

monsterList = ["zombies", "bears", "giant weevils"]

class Player:
    def __init__(self, health, startGun):
        self.health = health
        self.guns = {gun:gunList[gun] for gun in [startGun]}
        self.backpack = [] # limit of 7 items
        self.currentGun = startGun
        self.points = 0

    def addItemBp(self,item):
        if len(self.backpack) >= 7:
            print("There is not enough room in your backpack. Would you like to remove an item? (Y/N)")
            remove = str(input(">>> "))
            if remove.lower() == "y":
                self.removeItemBp()
                if item in gunList:
                    self.addGun(item)
                else:
                    self.backpack.append(item)
            else:
                print("Okay. Returning.")
                return
        else:
            if item in gunList:
                self.addGun(item)
            else:
                self.backpack.append(item)

    def removeItemBp(self):
        for i,v in enumerate(self.backpack):
            print(str(i+1)+": "+v)

        itemToRemove = 10
        while itemToRemove > 7:
            print("Please enter the number of the item you wish to remove: ")
            itemToRemove = int(input(">>> "))

        self.backpack.pop(itemToRemove-1)

    def useBpItem(self, item, itemIndex):
        if item == "Ammo Pack":
            if len(self.guns) > 1:
                gunList_Temp = [] # gun list so player can select
                for index, item in enumerate(self.guns):
                    print(index+1,": "+item+" -- Ammo:", self.guns[item][0], "Firepower: ", self.guns[item][1])
                    gunList_Temp.append(item)

                gunToLoad = len(self.guns)+1
                while gunToLoad > len(self.guns):
                    print("Which gun would you like to add ammo to? Please enter the number that corresponds to the gun: ")
                    gunToLoad = int(input(">>> "))

                if gunList_Temp[gunToLoad-1] == "Grenade":
                    self.guns["Grenade"][0] += 1
                elif gunList_Temp[gunToLoad-1] == "Shotgun":
                    self.guns["Shotgun"][0] += 4
                else:
                    self.guns[gunList_Temp[gunToLoad-1]][0] += 30

            else:
                if self.guns[list(self.guns.keys())[0]] == "Grenade":
                    self.guns["Grenade"][0] += 1
                elif self.guns[list(self.guns.keys())[0]] == "Shotgun":
                    self.guns["Shotgun"][0] += 4
                else:
                    self.guns[list(self.guns.keys())[0]][0] += 30

        else:
            self.health += 15

        self.backpack.pop(itemIndex)



    def pointInc(self, monster, killed):
        if killed == True:
            if monster == "zombies":
                self.points += 5
                print("+5 PTS")
            elif monster == "bears":
                self.points += 8
                print("+8 PTS")
            elif monster == "giant weevils":
                self.points += 15
                print("+15 PTS")
        else:
            if monster == "zombies":
                self.points += 1
                print("+1 PTS")
            elif monster == "bears":
                self.points += 2
                print("+2 PTS")
            elif monster == "giant weevils":
                self.points += 3
                print("+3 PTS")

        print("Current Points:",self.points)

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
        elif monsterType == "giant weevils":
            self.attack = 8
            self.health = 25

    """
    def monsterAttack(self):
        numMonsters = random.randint(2,5)
        print()
    """


def startText():
    print("Text Based Shooter!")
    print("This program is a simple game based on first person shooters where you can pick up and")
    print("store weapons and battle enemies...")
    print()
    print()
    anyKey = input("Please press any key to start...")
    print()

def pickUp(item, player):
    puList = ["A "+item+" is lying on the floor.", "There is a "+item+" to your left.", "There is a "+item+" to your right.", "There is a "+item+" on a shelf."]
    print(random.choice(puList))
    print("Do you want to pick it up? (Y/N)")
    pickupYN = str(input(">>> "))
    if pickupYN.lower() == "y":
        player.addItemBp(item)



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

        time.sleep(0.5)

        gunFp = player.guns[player.currentGun][1]
        gunAmmo = player.guns[player.currentGun][0]
        print("You bravely battle the " + monster)

        time.sleep(0.5)

        previousMonsterNum = len(monsters)
        for count in range(len(monsters)):
            if gunAmmo > 0:
                # attack monster
                hitMonster = random.randint(1,100)
                if hitMonster % 9 != 0:
                    print("You shot "+monster+str(count+1)+"!")
                    monsters[count].health -= gunFp
                    player.pointInc(monster, False)
                else:
                    print("You missed "+monster+str(count+1)+"!")
                gunAmmo-=1
            else:
                print("This gun is out of ammo!")
            time.sleep(1)
        player.guns[player.currentGun][0] = gunAmmo
        monsters = [m for m in monsters if m.health > 0]

        # Determine how many monsters were killed and calculate points from that
        monstersKilled = previousMonsterNum - len(monsters)
        for i in range(monstersKilled):
            player.pointInc(monster, True)

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
            print("The "+monster+" are all dead...")
            print("Your health is now {0}".format(player.health))
            break
        print()
        print()
        if player.health<=0:
            print("You died!")
            dead()
        anyKey = str(input("Press R to run OR any letter to continue fighting"))
        if anyKey.lower().startswith("r"):
            break
        else:
            pass

    return

def dead():
    print("You are dead!\nWould you like to restart? Y/N")
    restart = str(input(">>> "))
    if restart.lower().startswith("y"):
        main()
    else:
        sys.exit()

def main():
    startText()
    player = Player(30,"Hand Gun")

    while player.health > 0:
        time.sleep(1)

        print("Would you like to:\n1 - Explore\n2 - Open Backpack\n3 - Open Gun Pack")
        firstOpt = int(input("Please enter the number corresponding to the option you wish to pick: "))
        print()

        time.sleep(1)

        if firstOpt == 1:
            randNum = random.randint(1,2) #random.randint(1,50)

            if randNum == 1:
                pickUp("Ammo Pack", player)
            elif randNum == 2:
                pickUp("Health Pack", player)
            elif randNum == 3:
                pickUp("Grenade", player)

            """
            if randNum in range(1,2):
                monsterAttack(player)
            elif randNum in range(2,26):
                pickUp("Health Pack", player)
            elif randNum in range(26,31):
                pickUp("Shotgun", player)
            elif randNum in range(31,35):
                pickUp("Rifle", player)
            elif randNum in range(35,39):
                pickUp("Grenade", player)
            elif randNum in range(39,45):
                print("A Guard notices you.")
                #guard notices func
            elif randNum in range(45,49):
                pickUp("Ammo Pack", player)
            else:
                print("A Giant Weevil snuck up behind you and hurt you! -10HP")
                player.health -= 10
            """
        elif firstOpt == 2:
            for index, item in enumerate(player.backpack):
                print(index+1,": "+item)
            print("If you would like to use an item in the backpack, enter its number. Else, enter 0: ")
            bpChoice = int(input(">>> "))
            player.useBpItem(player.backpack[bpChoice-1], bpChoice-1)


        elif firstOpt == 3:
            for index, item in enumerate(player.guns):
                print(index,": "+item+" -- Ammo:", player.guns[item][0], "Firepower: ", player.guns[item][1])



main()
