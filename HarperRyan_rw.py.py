'''Resident Weevil
Simple FPS without using functions'''

import random,time

guns = []   # empty list
health = 30
killed = [] # empty list
#equip with handgun
currentgun = ["Hand Gun",50] 
enemies = ["zombies", "bears", "orcs"]

print("Text Based Shooter!")
print("This program is a simple game based on first person shooters where you can pick up and")
print("store weapons and battle enemies...")
print()
print()
anyKey = input("Please press any key to start...")
print()

while health > 0:
    time.sleep(0.5)
    randomNo = random.randint(1,10) # generate random integer between 1 and 10
    print()
    if randomNo == 1:
        monster = random.choice(enemies)
        numMonsters = random.randint(2,5)

        print("There are " + str(numMonsters) + " " + str(monster) + " in front of you...")
        
        



        
        print("There are two zombies in front of you...")
        print()
        #create zombies (two zombies with 5 health each)
        zombies = [5,5]
        #battle the zombies
        while len(zombies) > 0 and health > 0:
            #current weapon
            print("You are equiped with the {0} ammo:{1}.".format(currentgun[0],currentgun[1]))
            print("There are {0} other guns in your pack.".format(len(guns)))
            print()
            print()
            if len(guns) > 0:
                switch = input("Do you wish to switch gun (Y/N)?: ")
                print()
                #switch gun
                if switch.lower() = "y":
                #display list of guns
                    for item in range(len(guns)):
                      print("{0}. {1} ammo: {2}".format(item+1,guns[item][0],guns[item][1]))
                    selection = int(input("Please select a gun: "))
                    #put current gun in pack - uses append to add item to list
                    if currentgun[1] > 0:
                        guns.append(currentgun)
                    else:
                        print("your {0} was out of ammo, so you have dropped it.".format(currentgun[0]))
                    #get the selected gun - uses pop to remove item from list 
                    currentgun = guns.pop(selection - 1)
                    print("you are now equiped with the {0}".format(currentgun[0]))
                    print()
                    print()
            #firepower of weapon
            if currentgun[0] == "Hand Gun":
                firepower = 1
            elif currentgun[0] == "Rifle":
                firepower = 3
            elif currentgun [0] == "Shotgun":
                firepower = 10
            elif currentgun == "Grenade":
                firepower = 20
            print("You bravely battle the zombies...")
            print()
            for count in range(len(zombies)):
              if currentgun[1] > 0:
                  #attack zombie
                  hitzombie = random.randint(1,100)
                  if (hitzombie % 9) != 0:
                      print("you shot zombie"+str(count)+"!")
                      zombies[count] = zombies[count] - firepower
                  else:
                      print("your shot missed...")
                  #decrease ammo
                  currentgun[1] = currentgun[1] - 1
              else:
                   print("You are out of ammo for this gun!!!")
            #remove dead zombies - this is basic list comprehension
            zombies = [each for each in zombies if each > 0]
            #zombies shoot you if there are any left
            if len(zombies) > 0:
                print("There are still",len(zombies),"zombie(s) after you!")
              #each zombie gets a chance to shoot
              for each in zombies:
                  hitYou = random.randint(1,50)
                  if (hitYou % 3) == 0:
                      print("the zombie shot you...")
                      health = health - 1
                  else:
                      print("the zombie missed you...")
            if len(zombies) > 1:
                print("The zombies are still coming for you...")
            elif len(zombies) == 1:
                print("there is only one zombie left...")
            elif len(zombies) == 0:
                print("the zombies are dead...")
                print("your health is now {0}.".format(health))
            print()
            print()
            anyKey = input("Press any key to continue")
    #only allows further action if random number is 7. This could be improved.
    elif randomNo == 2:
        print("A Guard notices you...")
    elif randomNo == 3:
        print("A pack of hell hounds are bounding towards you")
    elif randomNo == 4:
        print("You have encountered a Giant Weevil, beware!")
    elif randomNo == 5:
        print("There is a health pack to your left")
    elif randomNo == 6:
        print("There is a box of ammo on a shelf")
    elif randomNo == 7:
        print("A shotgun is lying on the floor")
        pickUp = input("Do you want to pick up the shotgun? (Y/N): ")
        if pickUp == 'Y':
            guns.append(["Shotgun",2])
    elif randomNo == 8:
        print("A grenade is over on the table")
        # do you want to pick it up
    elif randomNo == 9:
        print("You have found a rifle")
        # do you want to pick it up


    '''
    Starter functions - use and adapt these and add the others you need for your game:
    
    def initialSetUp():
    guns = []
    health = 50
    killed = []
    #equip with handgun
    currentgun = ["Hand Gun",50]
    return guns,health,killed,currentgun

    def selectGun(guns,currentgun):
    displayGuns(guns)
    selection = int(input("Please select a gun: "))
    #put current gun in pack
    if currentgun[1] > 0:
        guns.pop(currentgun)
    else:
        print("your {0} was out of ammo, so you have dropped it.".format(currentgun[0]))
    #get the selected gun
    currentgun = guns.remove(selection - 1)
    print("you are now equiped with the {0}".format(currentgun[0]))
    print()
    print()
    return currentgun
    '''
