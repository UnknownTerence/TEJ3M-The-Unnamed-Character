# Terence Nguyen
# 11/23/2022
# Programming Project
# This is a game created with what we have learned in python

# Notes for me and whoever reads this
# Text-based RPG which includes weapons, coins, shops, enemies and maybe drops
# Player will start in the shop with a selection of different weapons
# They can choose, have their choice randomized or they can go unarmed
# Each weapon will have an advantage and disadvantage
# Coins (and maybe drops) will be dropped after an enemy has been slain
# If you die, the game ends and you have to restart to play again

# IDEAS *for me*
# HAVE A BOSS THAT USES A FOR LOOP?

# How will things be used
# While loops
# - used for battles
# - spending too much in the shop
# For loops
# - amount of enemies to fight before final boss
# RNG
# - Randomize weapon choice
# - Coin drops
# - Maybe a rare item drop
# If statements
# - Decisions for RNG
# - Battles
# - Shop

from colorama import Fore, Back, Style
import random
from time import sleep # creates to ability to delay prints using the sleep() function

coins = 100 # in game currency
coinsDrop = 0 # coin drops
cost = 10000 # cost of weapons and items
pHP = 20 # health points for player
eHP = 0 # health points for enemy
pAtk = 0 # The attack stat for the player
eAtk = 0 # The attack stat for the enemies
weapon = 0 # indicates which weapon the player chooses
choice = 0 # players choices throughout the 
loopCounter = 0 # counts if the player made an invalid input
dblHit = 0 # This is the double hit feature for the daggers, rng 1 - 2, if 2 then 2 hits, else single hit
dodge = 0 # if player chooses to dodge, rng 1 - 10 if # is <= 8 ten successful dodge
geeseAtk = 0 # value for how many times the geese will attack
bkAtk = 0 # counter for when The Burger King uses his special attack
eDodge = 0 # dodge rate for enemies (if they have one)
smallPotion = 0 # restores 3 hp, determines how many potions the player has
mediumPotion = 0 # restores 5 hp, determines how many potions the player has
largePotion = 0 # restores 10 hp, determines how many potions the player has

print(Fore.YELLOW)
print("===========================================================")
print(Fore.WHITE)
print("                   The Unnamed Character                   ")
print(Fore.YELLOW)
print("===========================================================")
sleep(1)
print(Fore.YELLOW)
print("===========================================================")
print(Fore.WHITE)
print("Hello Player! This is an RPG game where you are playing as")
print("an unnamed character in a Fantasy World with only swords")
print("and potions! The premise of the game is to defeat the")
print("enemies you encounter on your journey. These enemies will")
print("drop various amounts of coins to help purchase new items.")
print("The longer you go on, the harder it will get. All enemies")
print("will have unique attack and health stats and some will even")
print("have unique attack patterns.")
print()
print("You start off with 100 coins where you can pick your")
print("starter weapon. You have 20 HP, if this value reaches zero,")
print("that's GAME OVER and you have to start from the beginning.")
print()
print("Good luck on your journey!")
print("Tip: The game will load after 5 seconds")
print(Fore.YELLOW)
print("===========================================================")
sleep(5)

print()
print(Fore.MAGENTA+"You walk into the shop with 100 coins") # game text
print() # spacer

# SHOP
while (weapon!=1 and weapon!=2 and weapon!=3 and weapon!=4): # Makes sure the player chooses one of the choices
  if (loopCounter > 0):
    print()
    print(Fore.RED+"Invalid Choice")
    sleep(1)
    print(Style.RESET_ALL)
  print(Fore.YELLOW+"===========================================================") # I found out I could use triple quotes for multiple lines, but I already have the game half done
  print(Fore.WHITE+"               Select your weapon of choice                ")
  print(Fore.YELLOW+"-----------------------------------------------------------")
  print(Fore.GREEN+"Balance: "+str(coins)+" coins")
  print(Fore.WHITE+"1. Sword") # item
  print("     100 coins: A basic sword, grants 5 attack") # desc
  print() # spacer
  print("2. Daggers") # item
  print("     100 coins: 2 daggers, grants 3 attack but a 50% chance")
  print("to attack twice") # desc
  print() # spacer
  print("3. Unarmed") # item
  print("     0 coins: Your trusty fists, grants 1 attack") # desc
  print() # spacer
  print("4. Randomize")
  print("     It seems you don't know what to choose") # desc
  print() # spacer
  print(Fore.YELLOW+"===========================================================")
  print()
  weapon=int(input(Fore.BLUE+"Enter the number corresponding to your choice: "))
  print() # spacer
  print(Fore.YELLOW+"===========================================================")
  loopCounter += 1

loopCounter = 0 # Resets loop counter
print() # spacer
if (weapon==4): # if the player chose to randomize their choice
  weapon = random.randint(1,3)
if (weapon==1):
  print(Fore.MAGENTA+"You have chosen the sword as your weapon")
  coins -= 100
  print(Fore.GREEN+"Balance: "+str(coins)+" coins")
  pAtk = 5
elif (weapon==2):
  print(Fore.MAGENTA+"You have chosen the daggers as your weapon")
  coins -= 100
  print(Fore.GREEN+"Balance: "+str(coins)+" coins")
  pAtk = 3
elif (weapon==3):
  print(Fore.MAGENTA+"You have chosen unarmed as your weapon")
  print(Fore.GREEN+"Balance: "+str(coins)+" coins")
  pAtk = 1

print() # spacer
print(Fore.MAGENTA+"You exit the shop") # game text
print() # spacer
while (choice != 1 and choice != 2):
  if (loopCounter > 0):
    print()
    print(Fore.RED+"Invalid Choice")
    sleep(1)
    print(Style.RESET_ALL)
  print(Fore.YELLOW+"===========================================================")
  print(Fore.WHITE+"                Where would you like to go?                 ")
  print(Fore.YELLOW+"-----------------------------------------------------------")
  print()
  print(Fore.WHITE+"1. The Forest")
  print("2. The Mountains")
  print() # spacer
  print(Fore.YELLOW+"===========================================================")
  print() # spacer
  choice=int(input(Fore.BLUE+"Enter the number corresponding to your choice: "))
  print() # spacer
  print(Fore.YELLOW+"===========================================================")
  loopCounter += 1

loopCounter = 0 # Resets loop counter
if (choice == 1): # Forest route
  choice = 0
  print()
  print(Fore.MAGENTA+"You head into the forest")
  print()
  for x in range(0,2,1):
    if (x == 0): # copy and paste 3 other times my friend (slime, tomato juice man, big boi beef aka triple b, duolingo the bird)
      eHP = 10
      eAtk = 2
      sleep(1)
      print("You have encountered a slime!")
      sleep(1)
      print("The slime challenges you to a battle!")
      print()
      sleep(1)
      while (pHP > 0 and eHP > 0):
        while (choice != 1 and choice != 2):
          if (loopCounter > 0):
            print()
            print(Fore.RED+"Invalid Choice")
            sleep(1)
            print(Style.RESET_ALL)
          print(Fore.YELLOW+"===========================================================")
          print()
          print(Fore.MAGENTA+"You have "+str(pHP)+" HP")
          print("The slime has "+str(eHP)+" HP")
          print()
          sleep(1)
          print(Fore.YELLOW+"===========================================================")
          print(Fore.WHITE+"                Choose which action to take                ")
          print(Fore.YELLOW+"-----------------------------------------------------------")
          print()
          print(Fore.WHITE+"1. Attack | "+str(pAtk)+" Dmg")
          print("2. Dodge  | 80% Chance")
          print() # spacer
          print(Fore.YELLOW+"===========================================================")
          print()
          choice=int(input(Fore.BLUE+"Enter the number corresponding to your choice: "))
          print() # spacer
          print(Fore.YELLOW+"===========================================================")
          print(Fore.MAGENTA)
          loopCounter += 1
        if (choice == 1):
          if (weapon == 1 or weapon == 3):
            eHP -= pAtk
            print("You attacked the slime")
            sleep(1)
            print("You did "+str(pAtk)+" Dmg")
            sleep(1)
            print("The slime has "+str(eHP)+" HP left")
          elif (weapon == 2): # sees if the player has daggers to calculate the 50% chance to attack twice
            dblHit = random.randint(1,2)
            if (dblHit == 1): # 1 is a single hit
              eHP -= pAtk
              print("You attacked the slime")
              sleep(1)
              print("You did "+str(pAtk)+" Dmg")
              print("You attacked once")
              sleep(1)
              print("The slime has "+str(eHP)+" HP left")
            elif (dblHit == 2): # 2 is a double hit
              eHP -= pAtk*2
              print("You attacked the slime")
              sleep(1)
              print("You did "+str(pAtk*2)+" Dmg")
              print("You attacked twice")
              sleep(1)
              print("The slime has "+str(eHP)+" HP left")
          if (eHP > 0):
            pHP -= eAtk
            print()
            print("The slime did "+str(eAtk)+" Dmg")
        elif (choice == 2):
          dodge = random.randint(1,10)
          if (dodge <= 8):
            print("Dodge Successful")
          else:
            pHP -= eAtk
            print("You failed to dodge!")
            sleep(1)
            print("The slime did "+str(eAtk)+" Dmg")
            sleep(1)
            print("You have "+str(pHP)+" HP left")
        choice = 0
        loopCounter = 0
        sleep(1)
      if (pHP <= 0):
        exit("You Died")
      elif (eHP <= 0):
        print()
        print(Fore.YELLOW+"===========================================================")
        print(Fore.MAGENTA)
        print("You have slain the slime")
        coinsDrop = random.randint(5,20) # makes slime drop from 5 - 20 coins
        coins += coinsDrop
        print("The slime dropped "+str(coinsDrop)+" coins")
        print(Fore.GREEN+"Balance: "+str(coins)+" coins")
        print()
      choice = 0 # resets players choice
      loopCounter = 0 # Resets loop counter
      while (choice != 1 and choice != 2):
        if (loopCounter > 0):
          print()
          print(Fore.RED+"Invalid Choice")
          sleep(1)
          print(Style.RESET_ALL)
        print(Fore.YELLOW+"===========================================================")
        print(Fore.WHITE+"             Do you want to return to the shop?             ")
        print(Fore.YELLOW+"-----------------------------------------------------------")
        print(Fore.WHITE)
        print("Tip: There might be new things")
        print("1. Yes")
        print("2. No")
        print()
        print(Fore.YELLOW+"===========================================================")
        print()
        choice=int(input(Fore.BLUE+"Enter the number corresponding to your choice: "))
        print()
        loopCounter += 1
      if (choice == 1):
        choice = 0
        loopCounter = 0 # Resets loop counter
        while (choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5 and cost > coins):
          if (loopCounter > 0):
            print()
            print(Fore.RED+"Invalid Choice")
            sleep(1)
            print(Style.RESET_ALL)
          print(Fore.YELLOW+"===========================================================") # I found out I could use triple quotes for multiple lines, but I already have the game half done
          print(Fore.WHITE+"                      Page 1: Weapons                      ")
          print(Fore.YELLOW+"-----------------------------------------------------------")
          print(Fore.GREEN+"Balance: "+str(coins)+" coins")
          print(Fore.WHITE+"1. Sword") # item
          print("     100 coins: A basic sword, grants 5 attack") # desc
          print() # spacer
          print("2. Daggers") # item
          print("     100 coins: 2 daggers, grants 3 attack but a 50% chance")
          print("to attack twice") # desc
          print() # spacer
          print("3. Unarmed") # item
          print("     0 coins: Your trusty fists, grants 1 attack") # desc
          print() # spacer
          print("4. Page 2")
          print("     Potions")
          print() # spacer
          print("5. Exit")
          print() # spacer
          print(Fore.YELLOW+"===========================================================")
          print()
          choice=int(input(Fore.BLUE+"Enter the number corresponding to your choice: "))
          print()
          print(Fore.YELLOW+"===========================================================")
          loopCounter += 1
          if (choice == 1):
            choice = 0
            cost = 100
            if (cost > coins):
              print(Fore.RED+"You cannot afford this!")
              choice = 0
              loopCounter = 0
            elif (cost <= coins):
              print("You have purchased the sword for 100 coins")
              print(Fore.GREEN+"Balance: "+str(coins)+" coins")
              weapon = 1
              cost = 1000
          elif (choice == 2):
            choice = 0
            cost = 100
            if (cost > coins):
              print(Fore.RED+"You cannot afford this!")
              choice = 0
              loopCounter = 0
            elif (cost <= coins):
              print("You have purchased the daggers for 100 coins")
              print(Fore.GREEN+"Balance: "+str(coins)+" coins")
              weapon = 2
              cost = 1000
          elif (choice == 3):
            choice = 0
            cost = 0
            if (cost <= coins):
              print("You have purchased unarmed for 0 coins")
              print(Fore.GREEN+"Balance: "+str(coins)+" coins")
              weapon = 3
              cost = 1000
          elif (choice == 4):
            choice = 0
            loopCounter = 0
            while (choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5 and cost > coins):
              if (loopCounter > 0):
                print()
                print(Fore.RED+"Invalid Choice")
                sleep(1)
                print(Style.RESET_ALL)
              print(Fore.WHITE+"                      Page 2: Potions                      ")
              print(Fore.YELLOW+"-----------------------------------------------------------")
              print(Fore.GREEN+"Balance: "+str(coins)+" coins")
              print(Fore.WHITE+"1. Small HP Potion") # item
              print("     10 Coins: Restores 3 HP") # desc
              print() # spacer
              print("2. Medium HP Potion") # item
              print("     15 Coins: Restores 5 HP") # desc
              print() # spacer
              print("3. Large HP Potion") # item
              print("     25 Coins: Restores 10 HP, Best Deal!") # desc
              print() # spacer
              print("4. Page 1")
              print("     Weapons")
              print() # spacer
              print("5. Exit")
              print() # spacer
              print(Fore.YELLOW+"===========================================================")
              print()
              choice=int(input(Fore.BLUE+"Enter the number corresponding to your choice: "))
              print()
              print(Fore.YELLOW+"===========================================================")
              if (choice == 1): # SMALL POTION
                choice = 0
                cost = 10
                if (cost > coins):
                  print(Fore.RED+"You cannot afford this!")
                  choice = 0
                  loopCounter = 0
                elif (cost <= coins):
                  coins -= cost
                  print(Fore.MAGENTA)
                  print("You have purchased the Small HP Potion for 10 Coins")
                  print(Fore.GREEN+"Balance: "+str(coins)+" coins")
                  print()
                  print(Fore.YELLOW+"===========================================================")
                  smallPotion += 1
                  cost = 1000
              elif (choice == 2): # MEDIUM POTION
                choice = 0
                cost = 15
                if (cost > coins):
                  print(Fore.RED+"You cannot afford this!")
                  choice = 0
                  loopCounter = 0
                elif (cost <= coins):
                  coins -= cost
                  print(Fore.MAGENTA)
                  print("You have purchased the Medium HP Potion for 15 Coins")
                  print(Fore.GREEN+"Balance: "+str(coins)+" coins")
                  print()
                  print(Fore.YELLOW+"===========================================================")
                  mediumPotion += 1
                  cost = 1000
              elif (choice == 3): # LARGE POTION
                choice = 0
                cost = 25
                if (cost > coins):
                  print(Fore.RED+"You cannot afford this!")
                  choice = 0
                  loopCounter = 0
                elif (cost <= coins):
                  coins -= cost
                  print(Fore.MAGENTA)
                  print("You have purchased the Large HP Potion for 25 Coins")
                  print(Fore.GREEN+"Balance: "+str(coins)+" coins")
                  print()
                  print(Fore.YELLOW+"===========================================================")
                  largePotion += 1
                  cost = 1000
              elif (choice == 4):
                loopCounter = 0
              cost = 1000
            choice = 0
        print(Fore.MAGENTA+("You exit the shop and further explore the forest"))
        print()
      elif (choice == 2):
        print()
        print(Fore.YELLOW+"===========================================================")
        print(Fore.MAGENTA)
        print("You travel further into the forest")
        choice = 0
      loopCounter = 0 # Resets loop counter
    if (x == 1): # second mob/enemy Tomato Man -----------------------------------------------------------------------------
      eHP = 12
      eAtk = 5
      sleep(1)
      print(Fore.MAGENTA+"You have encountered a Tomato Man!")
      sleep(1)
      print("The Tomato Man challenges you to a battle!")
      sleep(1)
      print("Tip: Don't take too many moves! Potions count as a move")
      print("but can be used with a dodge or attack")
      print()
      sleep(1)
      while (pHP > 0 and eHP > 0):
        while (choice != 1 and choice != 2 and choice != 3):
          if (loopCounter > 0):
            print()
            print(Fore.RED+"Invalid Choice")
            sleep(1)
            print(Style.RESET_ALL)
          print()
          print(Fore.MAGENTA+"You have "+str(pHP)+" HP")
          print("The Tomato Man has "+str(eHP)+" HP")
          print()
          sleep(1)
          print(Fore.YELLOW+"===========================================================")
          print(Fore.WHITE+"                Choose which action to take                ")
          print(Fore.YELLOW+"-----------------------------------------------------------")
          print(Fore.WHITE+"1. Attack | "+str(pAtk)+" Dmg")
          print("2. Dodge  | 80% Chance")
          print("3. Potion | Heal your HP (no HP limit)")
          print() # spacer
          print(Fore.YELLOW+"===========================================================")
          print()
          choice=int(input(Fore.BLUE+"Enter the number corresponding to your choice: "))
          print() # spacer
          print(Fore.YELLOW+"===========================================================")
          print(Fore.MAGENTA)
          loopCounter += 1
        if (choice == 3):
          choice = 0
          loopCounter = 0
          if (smallPotion <= 0 and mediumPotion <= 0 and largePotion <= 0): # checks to see if the player has potions
            print("You do not have any potions!")
            while (choice != 1 and choice != 2):
              if (loopCounter > 0):
                print()
                print(Fore.RED+"Invalid Choice")
                sleep(1)
                print(Style.RESET_ALL)
              print(Fore.YELLOW+"===========================================================")
              print(Fore.WHITE+"                Choose which action to take                ")
              print(Fore.YELLOW+"-----------------------------------------------------------")
              print("1. Attack | "+str(pAtk)+" Dmg")
              print("2. Dodge  | 80% Chance")
              print() # spacer
              print(Fore.YELLOW+"===========================================================")
              print()
              choice=int(input(Fore.BLUE+"Enter the number corresponding to your choice: "))
              print() # spacer
              print(Fore.YELLOW+"===========================================================")
              loopCounter += 1
          while (choice != 1 and choice != 2 and choice != 3): # which potion they want to use
            if (loopCounter > 0):
              print()
              print(Fore.RED+"Invalid Choice")
              sleep(1)
              print(Style.RESET_ALL)
            print("Choose which action to take")
            print("1. Small Potion  | ( "+str(smallPotion)+" ) 3 HP")
            print("2. Medium Potion | ( "+str(mediumPotion)+" ) 5 HP")
            print("3. Large Potion  | ( "+str(largePotion)+" ) 10 HP")
            choice=int(input("Enter the number corresponding to your choice: "))
            loopCounter += 1
          if (choice == 1):
            if (smallPotion <= 0): # checks to see if the player has potions
              while (choice != 1 and choice != 2):
                if (loopCounter > 0):
                  print()
                  print(Fore.RED+"Invalid Choice")
                  sleep(1)
                  print(Style.RESET_ALL)
                print("Choose which action to take")
                print("1. Medium Potion | ( "+str(mediumPotion)+" ) 5 HP")
                print("2. Large Potion  | ( "+str(largePotion)+" ) 10 HP")
                choice=int(input("Enter the number corresponding to your choice: "))
                loopCounter += 1
              if (choice == 1):
                mediumPotion -= 1
                pHP += 5
                print("You used a Medium Potion")
                print("You have "+str(mediumPotion)+" Medium Potions left")
                print("You gained 5 HP")
              elif (choice == 2):
                largePotion -= 1
                pHP += 10
                print("You used a Large Potion")
                print("You have "+str(largePotion)+" Large Potions left")
                print("You gained 10 HP")
            if (smallPotion > 0): # checks to see if the player has potions
              smallPotion -= 1
              pHP += 3
              print("You used a Small Potion")
              print("You have "+str(smallPotion)+" Small Potions left")
              print("You gained 3 HP")
          elif (choice == 2):
            if (mediumPotion <= 0): # checks to see if the player has potions
              while (choice != 1 and choice != 2):
                if (loopCounter > 0):
                  print()
                  print(Fore.RED+"Invalid Choice")
                  sleep(1)
                  print(Style.RESET_ALL)
                print("Choose which action to take")
                print("1. Small Potion | ( "+str(smallPotion)+" ) 3 HP")
                print("2. Large Potion  | ( "+str(largePotion)+" ) 10 HP")
                choice=int(input("Enter the number corresponding to your choice: "))
                loopCounter += 1
            if (mediumPotion > 0): # checks to see if the player has potions
              mediumPotion -= 1
              pHP += 5
              print("You used a Medium Potion")
              print("You have "+str(mediumPotion)+" Medium Potions left")
              print("You gained 5 HP")
          elif (choice == 3):
            if (largePotion <= 0): # checks to see if the player has potions
              while (choice != 1 and choice != 2):
                if (loopCounter > 0):
                  print()
                  print(Fore.RED+"Invalid Choice")
                  sleep(1)
                  print(Style.RESET_ALL)
                print("Choose which action to take")
                print("1. Small Potion | ( "+str(smallPotion)+" ) 3 HP")
                print("2. Medium Potion  | ( "+str(mediumPotion)+" ) 5 HP")
                choice=int(input("Enter the number corresponding to your choice: "))
                loopCounter += 1
            if (largePotion > 0): # checks to see if the player has potions
              largePotion -= 1
              pHP += 10
              print("You used a Large Potion")
              print("You have "+str(largePotion)+" Large Potions left")
              print("You gained 10 HP")
          choice = 0
        if (choice == 1):
          if (weapon == 1 or weapon == 3):
            eHP -= pAtk
            print("You attacked the Tomato Man")
            sleep(0.5)
            print("You did "+str(pAtk)+" Dmg")
            sleep(0.5)
            print("The Tomato Man has "+str(eHP)+" HP left")
          elif (weapon == 2): # sees if the player has daggers to calculate the 50% chance to attack twice
            dblHit = random.randint(1,2)
            if (dblHit == 1): # 1 is a single hit
              eHP -= pAtk
              print("You attacked the Tomato Man")
              sleep(0.5)
              print("You did "+str(pAtk)+" Dmg")
              print("You attacked once")
              sleep(0.5)
              print("The Tomato Man has "+str(eHP)+" HP left")
            elif (dblHit == 2): # 2 is a double hit
              eHP -= pAtk*2
              print("You attacked the Tomato Man")
              sleep(0.5)
              print("You did "+str(pAtk*2)+" Dmg")
              print("You attacked twice")
              sleep(0.5)
              print("The Tomato Man has "+str(eHP)+" HP left")
          if (eHP > 0):
            pHP -= eAtk
            print("The Tomato Man did "+str(eAtk)+" Dmg")
        elif (choice == 2):
          dodge = random.randint(1,10)
          if (dodge <= 8):
            print("Dodge Successful")
          else:
            pHP -= eAtk
            print("You failed to dodge!")
            sleep(0.5)
            print("The Tomato Man did "+str(eAtk)+" Dmg")
            sleep(0.5)
            print("You have "+str(pHP)+" HP left")
        eAtk += 1 # each round, tomato man gets 1 more atk stat
        choice = 0
        loopCounter = 0
        sleep(0.5)
      if (pHP <= 0):
        exit("You Died")
      elif (eHP <= 0):
        print("You have slain the Tomato Man")
        coinsDrop = random.randint(20,40) # makes Tomato Man drop from 20 - 40 coins
        coins += coinsDrop
        print("The Tomato Man dropped "+str(coinsDrop)+" coins")
        print(Fore.GREEN+"Balance: "+str(coins)+" coins")
      choice = 0 # resets players choice
      loopCounter = 0 # Resets loop counter
      while (choice != 1 and choice != 2):
        if (loopCounter > 0):
          print()
          print(Fore.RED+"Invalid Choice")
          sleep(1)
          print(Style.RESET_ALL)
        print(Fore.YELLOW+"===========================================================")
        print(Fore.WHITE+"             Do you want to return to the shop?             ")
        print(Fore.YELLOW+"-----------------------------------------------------------")
        print(Fore.WHITE)
        print("Tip: There might be new things")
        print("1. Yes")
        print("2. No")
        print()
        print(Fore.YELLOW+"===========================================================")
        print()
        choice=int(input(Fore.BLUE+"Enter the number corresponding to your choice: "))
        print()
        loopCounter += 1
      if (choice == 1):
        choice = 0
        loopCounter = 0 # Resets loop counter
        while (choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5 and cost > coins):
          if (loopCounter > 0):
            print()
            print(Fore.RED+"Invalid Choice")
            sleep(1)
            print(Style.RESET_ALL)
          print(Fore.YELLOW+"===========================================================") # I found out I could use triple quotes for multiple lines, but I already have the game half done
          print(Fore.WHITE+"                      Page 1: Weapons                      ")
          print(Fore.YELLOW+"-----------------------------------------------------------")
          print("Balance: "+str(coins)+" coins")
          print(Fore.WHITE+"1. Sword") # item
          print("     100 coins: A basic sword, grants 5 attack") # desc
          print() # spacer
          print("2. Daggers") # item
          print("     100 coins: 2 daggers, grants 3 attack but a 50% chance")
          print("to attack twice") # desc
          print() # spacer
          print("3. Unarmed") # item
          print("     0 coins: Your trusty fists, grants 1 attack") # desc
          print() # spacer
          print("4. Page 2")
          print("     Potions")
          print() # spacer
          print("5. Exit")
          print() # spacer
          print(Fore.YELLOW+"===========================================================")
          print()
          choice=int(input(Fore.BLUE+"Enter the number corresponding to your choice: "))
          print()
          print(Fore.YELLOW+"===========================================================")
          loopCounter += 1
          if (choice == 1):
            choice = 0
            cost = 100
            if (cost > coins):
              print(Fore.RED+"You cannot afford this!")
              choice = 0
              loopCounter = 0
            elif (cost <= coins):
              print("You have purchased the sword for 100 coins")
              print("Balance: "+str(coins)+" coins")
              weapon = 1
              cost = 1000
          elif (choice == 2):
            choice = 0
            cost = 100
            if (cost > coins):
              print(Fore.RED+"You cannot afford this!")
              choice = 0
              loopCounter = 0
            elif (cost <= coins):
              print("You have purchased the daggers for 100 coins")
              print("Balance: "+str(coins)+" coins")
              weapon = 2
              cost = 1000
          elif (choice == 3):
            choice = 0
            cost = 0
            if (cost <= coins):
              print("You have purchased unarmed for 0 coins")
              print("Balance: "+str(coins)+" coins")
              weapon = 3
              cost = 1000
          elif (choice == 4):
            choice = 0
            loopCounter = 0
            while (choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5 and cost > coins):
              if (loopCounter > 0):
                print()
                print(Fore.RED+"Invalid Choice")
                sleep(1)
                print(Style.RESET_ALL)
              print(Fore.WHITE+"                      Page 2: Potions                      ")
              print(Fore.YELLOW+"-----------------------------------------------------------")
              print("Balance: "+str(coins)+" coins")
              print(Fore.WHITE+"1. Small HP Potion") # item
              print("     10 Coins: Restores 3 HP") # desc
              print() # spacer
              print("2. Medium HP Potion") # item
              print("     15 Coins: Restores 5 HP") # desc
              print() # spacer
              print("3. Large HP Potion") # item
              print("     25 Coins: Restores 10 HP, Best Deal!") # desc
              print() # spacer
              print("4. Page 1")
              print("     Weapons")
              print() # spacer
              print("5. Exit")
              print() # spacer
              print(Fore.YELLOW+"===========================================================")
              print()
              choice=int(input(Fore.BLUE+"Enter the number corresponding to your choice: "))
              print()
              print(Fore.YELLOW+"===========================================================")
              if (choice == 1): # SMALL POTION
                choice = 0
                cost = 10
                if (cost > coins):
                  print(Fore.RED+"You cannot afford this!")
                  choice = 0
                  loopCounter = 0
                elif (cost <= coins):
                  coins -= cost
                  print(Fore.MAGENTA)
                  print("You have purchased the Small HP Potion for 10 Coins")
                  print(Fore.GREEN+"Balance: "+str(coins)+" coins")
                  print()
                  print(Fore.YELLOW+"===========================================================")
                  smallPotion += 1
                  cost = 1000
              elif (choice == 2): # MEDIUM POTION
                choice = 0
                cost = 15
                if (cost > coins):
                  print(Fore.RED+"You cannot afford this!")
                  choice = 0
                  loopCounter = 0
                elif (cost <= coins):
                  coins -= cost
                  print(Fore.MAGENTA)
                  print("You have purchased the Medium HP Potion for 15 Coins")
                  print(Fore.GREEN+"Balance: "+str(coins)+" coins")
                  print()
                  print(Fore.YELLOW+"===========================================================")
                  mediumPotion += 1
                  cost = 1000
              elif (choice == 3): # LARGE POTION
                choice = 0
                cost = 25
                if (cost > coins):
                  print(Fore.RED+"You cannot afford this!")
                  choice = 0
                  loopCounter = 0
                elif (cost <= coins):
                  coins -= cost
                  print(Fore.MAGENTA)
                  print("You have purchased the Large HP Potion for 25 Coins")
                  print(Fore.GREEN+"Balance: "+str(coins)+" coins")
                  print()
                  print(Fore.YELLOW+"===========================================================")
                  largePotion += 1
                  cost = 1000
              elif (choice == 4):
                loopCounter = 0
            choice = 0
      elif (choice == 2):
        print()
        print(Fore.YELLOW+"===========================================================")
        print(Fore.MAGENTA)
        print("You reach the other side of the forest where there is also a mountain")
        choice = 0
      loopCounter = 0 # Resets loop counter
elif (choice == 2): #MOUNTAIN ROUTE, CODE IS THE SAME EXCEPT FOR SOME TWEAKS WITH ATTACKS, HEALTH AN TEXT-------------------
  choice = 0
  print()
  print(Fore.MAGENTA+"You head up into the mountains")
  print()
  for x in range(0,2,1):
    if (x == 0):
      eHP = 20
      eAtk = 1
      sleep(1)
      print("You have encountered a guy named Horace!")
      sleep(1)
      print("The guy named Horace challenges you to a battle!")
      sleep(1)
      print("Tip: It seems he is unarmed")
      print()
      sleep(1)
      while (pHP > 0 and eHP > 0):
        while (choice != 1 and choice != 2):
          if (loopCounter > 0):
            print()
            print(Fore.RED+"Invalid Choice")
            sleep(1)
            print(Style.RESET_ALL)
          print(Fore.YELLOW+"===========================================================")
          print()
          print(Fore.MAGENTA+"You have "+str(pHP)+" HP")
          print("The guy named Horace has "+str(eHP)+" HP")
          print()
          sleep(1)
          print(Fore.YELLOW+"===========================================================")
          print(Fore.WHITE+"                Choose which action to take                ")
          print(Fore.YELLOW+"-----------------------------------------------------------")
          print()
          print(Fore.WHITE+"1. Attack | "+str(pAtk)+" Dmg")
          print("2. Dodge  | 80% Chance")
          print() # spacer
          print(Fore.YELLOW+"===========================================================")
          print()
          choice=int(input(Fore.BLUE+"Enter the number corresponding to your choice: "))
          print() # spacer
          print(Fore.YELLOW+"===========================================================")
          print(Fore.MAGENTA)
          loopCounter += 1
        if (choice == 1):
          if (weapon == 1 or weapon == 3):
            eHP -= pAtk
            print("You attacked the guy named Horace")
            sleep(1)
            print("You did "+str(pAtk)+" Dmg")
            sleep(1)
            print("The guy named Horace has "+str(eHP)+" HP left")
          elif (weapon == 2): # sees if the player has daggers to calculate the 50% chance to attack twice
            dblHit = random.randint(1,2)
            if (dblHit == 1): # 1 is a single hit
              eHP -= pAtk
              print("You attacked the guy named Horace")
              sleep(1)
              print("You did "+str(pAtk)+" Dmg")
              print("You attacked once")
              sleep(1)
              print("The guy named Horace has "+str(eHP)+" HP left")
            elif (dblHit == 2): # 2 is a double hit
              eHP -= pAtk*2
              print("You attacked the guy named Horace")
              sleep(1)
              print("You did "+str(pAtk*2)+" Dmg")
              print("You attacked twice")
              sleep(1)
              print("The guy named Horace has "+str(eHP)+" HP left")
          if (eHP > 0):
            pHP -= eAtk
            print()
            print("The guy named Horace did "+str(eAtk)+" Dmg")
        elif (choice == 2):
          dodge = random.randint(1,10)
          if (dodge <= 8):
            print("Dodge Successful")
          else:
            pHP -= eAtk
            print("You failed to dodge!")
            sleep(1)
            print("The guy named Horace did "+str(eAtk)+" Dmg")
            sleep(1)
            print("You have "+str(pHP)+" HP left")
        choice = 0
        loopCounter = 0
        sleep(1)
      if (pHP <= 0):
        exit("You Died")
      elif (eHP <= 0):
        print()
        print(Fore.YELLOW+"===========================================================")
        print(Fore.MAGENTA)
        print("You have slain the guy named Horace")
        coinsDrop = random.randint(5,20) # makes guy named Horace drop from 5 - 20 coins
        coins += coinsDrop
        print("The guy named Horace dropped "+str(coinsDrop)+" coins")
        print(Fore.GREEN+"Balance: "+str(coins)+" coins")
        print()
      choice = 0 # resets players choice
      loopCounter = 0 # Resets loop counter
      while (choice != 1 and choice != 2):
        if (loopCounter > 0):
          print()
          print(Fore.RED+"Invalid Choice")
          sleep(1)
          print(Style.RESET_ALL)
        print(Fore.YELLOW+"===========================================================")
        print(Fore.WHITE+"             Do you want to return to the shop?             ")
        print(Fore.YELLOW+"-----------------------------------------------------------")
        print(Fore.WHITE)
        print("Tip: There might be new things")
        print("1. Yes")
        print("2. No")
        print()
        print(Fore.YELLOW+"===========================================================")
        print()
        choice=int(input(Fore.BLUE+"Enter the number corresponding to your choice: "))
        print()
        loopCounter += 1
      if (choice == 1):
        choice = 0
        loopCounter = 0 # Resets loop counter
        while (choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5 and cost > coins):
          if (loopCounter > 0):
            print()
            print(Fore.RED+"Invalid Choice")
            sleep(1)
            print(Style.RESET_ALL)
          print(Fore.YELLOW+"===========================================================") # I found out I could use triple quotes for multiple lines, but I already have the game half done
          print(Fore.WHITE+"                      Page 1: Weapons                      ")
          print(Fore.YELLOW+"-----------------------------------------------------------")
          print(Fore.GREEN+"Balance: "+str(coins)+" coins")
          print(Fore.WHITE+"1. Sword") # item
          print("     100 coins: A basic sword, grants 5 attack") # desc
          print() # spacer
          print("2. Daggers") # item
          print("     100 coins: 2 daggers, grants 3 attack but a 50% chance")
          print("to attack twice") # desc
          print() # spacer
          print("3. Unarmed") # item
          print("     0 coins: Your trusty fists, grants 1 attack") # desc
          print() # spacer
          print("4. Page 2")
          print("     Potions")
          print() # spacer
          print("5. Exit")
          print() # spacer
          print(Fore.YELLOW+"===========================================================")
          print()
          choice=int(input(Fore.BLUE+"Enter the number corresponding to your choice: "))
          print()
          print(Fore.YELLOW+"===========================================================")
          loopCounter += 1
          if (choice == 1):
            choice = 0
            cost = 100
            if (cost > coins):
              print(Fore.RED+"You cannot afford this!")
              choice = 0
              loopCounter = 0
            elif (cost <= coins):
              print("You have purchased the sword for 100 coins")
              print(Fore.GREEN+"Balance: "+str(coins)+" coins")
              weapon = 1
              cost = 1000
          elif (choice == 2):
            choice = 0
            cost = 100
            if (cost > coins):
              print(Fore.RED+"You cannot afford this!")
              choice = 0
              loopCounter = 0
            elif (cost <= coins):
              print("You have purchased the daggers for 100 coins")
              print(Fore.GREEN+"Balance: "+str(coins)+" coins")
              weapon = 2
              cost = 1000
          elif (choice == 3):
            choice = 0
            cost = 0
            if (cost <= coins):
              print("You have purchased unarmed for 0 coins")
              print(Fore.GREEN+"Balance: "+str(coins)+" coins")
              weapon = 3
              cost = 1000
          elif (choice == 4):
            choice = 0
            loopCounter = 0
            while (choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5 and cost > coins):
              if (loopCounter > 0):
                print()
                print(Fore.RED+"Invalid Choice")
                sleep(1)
                print(Style.RESET_ALL)
              print(Fore.WHITE+"                      Page 2: Potions                      ")
              print(Fore.YELLOW+"-----------------------------------------------------------")
              print(Fore.GREEN+"Balance: "+str(coins)+" coins")
              print(Fore.WHITE+"1. Small HP Potion") # item
              print("     10 Coins: Restores 3 HP") # desc
              print() # spacer
              print("2. Medium HP Potion") # item
              print("     15 Coins: Restores 5 HP") # desc
              print() # spacer
              print("3. Large HP Potion") # item
              print("     25 Coins: Restores 10 HP, Best Deal!") # desc
              print() # spacer
              print("4. Page 1")
              print("     Weapons")
              print() # spacer
              print("5. Exit")
              print() # spacer
              print(Fore.YELLOW+"===========================================================")
              print()
              choice=int(input(Fore.BLUE+"Enter the number corresponding to your choice: "))
              print()
              print(Fore.YELLOW+"===========================================================")
              if (choice == 1): # SMALL POTION
                choice = 0
                cost = 10
                if (cost > coins):
                  print(Fore.RED+"You cannot afford this!")
                  choice = 0
                  loopCounter = 0
                elif (cost <= coins):
                  coins -= cost
                  print(Fore.MAGENTA)
                  print("You have purchased the Small HP Potion for 10 Coins")
                  print(Fore.GREEN+"Balance: "+str(coins)+" coins")
                  print()
                  print(Fore.YELLOW+"===========================================================")
                  smallPotion += 1
                  cost = 1000
              elif (choice == 2): # MEDIUM POTION
                choice = 0
                cost = 15
                if (cost > coins):
                  print(Fore.RED+"You cannot afford this!")
                  choice = 0
                  loopCounter = 0
                elif (cost <= coins):
                  coins -= cost
                  print(Fore.MAGENTA)
                  print("You have purchased the Medium HP Potion for 15 Coins")
                  print(Fore.GREEN+"Balance: "+str(coins)+" coins")
                  print()
                  print(Fore.YELLOW+"===========================================================")
                  mediumPotion += 1
                  cost = 1000
              elif (choice == 3): # LARGE POTION
                choice = 0
                cost = 25
                if (cost > coins):
                  print(Fore.RED+"You cannot afford this!")
                  choice = 0
                  loopCounter = 0
                elif (cost <= coins):
                  coins -= cost
                  print(Fore.MAGENTA)
                  print("You have purchased the Large HP Potion for 25 Coins")
                  print(Fore.GREEN+"Balance: "+str(coins)+" coins")
                  print()
                  print(Fore.YELLOW+"===========================================================")
                  largePotion += 1
                  cost = 1000
              elif (choice == 4):
                loopCounter = 0
              cost = 1000
            choice = 0
        print(Fore.MAGENTA+("You exit the shop and further explore the mountains"))
        print()
      elif (choice == 2):
        print()
        print(Fore.YELLOW+"===========================================================")
        print(Fore.MAGENTA)
        print("You travel further up the mountains")
        choice = 0
      loopCounter = 0 # Resets loop counter
    if (x == 1): # second mob/enemy Flock of Geese -------------------------------------------------------------------------
      eHP = 10
      eAtk = 2
      sleep(1)
      print(Fore.MAGENTA+"You have encountered a Flock of Geese!")
      sleep(1)
      print("The Flock of Geese challenges you to a battle!")
      sleep(1)
      print("Tip: There's more than one!")
      print()
      sleep(1)
      while (pHP > 0 and eHP > 0):
        while (choice != 1 and choice != 2 and choice != 3):
          if (loopCounter > 0):
            print()
            print(Fore.RED+"Invalid Choice")
            sleep(1)
            print(Style.RESET_ALL)
          print(Fore.MAGENTA+"You have "+str(pHP)+" HP")
          print("The Flock of Geese has "+str(eHP)+" HP")
          print()
          sleep(1)
          print(Fore.YELLOW+"===========================================================")
          print(Fore.WHITE+"                Choose which action to take                ")
          print(Fore.YELLOW+"-----------------------------------------------------------")
          print(Fore.WHITE+"1. Attack | "+str(pAtk)+" Dmg")
          print("2. Dodge  | 80% Chance")
          print("3. Potion | Heal your HP (no HP limit)")
          print() # spacer
          print(Fore.YELLOW+"===========================================================")
          print()
          choice=int(input(Fore.BLUE+"Enter the number corresponding to your choice: "))
          print() # spacer
          print(Fore.YELLOW+"===========================================================")
          print(Fore.MAGENTA)
          loopCounter += 1
        if (choice == 3):
          choice = 0
          loopCounter = 0
          if (smallPotion <= 0 and mediumPotion <= 0 and largePotion <= 0): # checks to see if the player has potions
            print("You do not have any potions!")
            while (choice != 1 and choice != 2):
              if (loopCounter > 0):
                print()
                print(Fore.RED+"Invalid Choice")
                sleep(1)
                print(Style.RESET_ALL)
              print(Fore.YELLOW+"===========================================================")
              print(Fore.WHITE+"                Choose which action to take                ")
              print(Fore.YELLOW+"-----------------------------------------------------------")
              print("1. Attack | "+str(pAtk)+" Dmg")
              print("2. Dodge  | 80% Chance")
              print() # spacer
              print(Fore.YELLOW+"===========================================================")
              print()
              choice=int(input(Fore.BLUE+"Enter the number corresponding to your choice: "))
              print() # spacer
              print(Fore.YELLOW+"===========================================================")
              loopCounter += 1
          while (choice != 1 and choice != 2 and choice != 3): # which potion they want to use
            if (loopCounter > 0):
              print()
              print(Fore.RED+"Invalid Choice")
              sleep(1)
              print(Style.RESET_ALL)
            print("Choose which action to take")
            print("1. Small Potion  | ( "+str(smallPotion)+" ) 3 HP")
            print("2. Medium Potion | ( "+str(mediumPotion)+" ) 5 HP")
            print("3. Large Potion  | ( "+str(largePotion)+" ) 10 HP")
            choice=int(input("Enter the number corresponding to your choice: "))
            loopCounter += 1
          if (choice == 1):
            if (smallPotion <= 0): # checks to see if the player has potions
              while (choice != 1 and choice != 2):
                if (loopCounter > 0):
                  print()
                  print(Fore.RED+"Invalid Choice")
                  sleep(1)
                  print(Style.RESET_ALL)
                print("Choose which action to take")
                print("1. Medium Potion | ( "+str(mediumPotion)+" ) 5 HP")
                print("2. Large Potion  | ( "+str(largePotion)+" ) 10 HP")
                choice=int(input("Enter the number corresponding to your choice: "))
                loopCounter += 1
              if (choice == 1):
                mediumPotion -= 1
                pHP += 5
                print("You used a Medium Potion")
                print("You have "+str(mediumPotion)+" Medium Potions left")
                print("You gained 5 HP")
              elif (choice == 2):
                largePotion -= 1
                pHP += 10
                print("You used a Large Potion")
                print("You have "+str(largePotion)+" Large Potions left")
                print("You gained 10 HP")
            if (smallPotion > 0): # checks to see if the player has potions
              smallPotion -= 1
              pHP += 3
              print("You used a Small Potion")
              print("You have "+str(smallPotion)+" Small Potions left")
              print("You gained 3 HP")
          elif (choice == 2):
            if (mediumPotion <= 0): # checks to see if the player has potions
              while (choice != 1 and choice != 2):
                if (loopCounter > 0):
                  print()
                  print(Fore.RED+"Invalid Choice")
                  sleep(1)
                  print(Style.RESET_ALL)
                print("Choose which action to take")
                print("1. Small Potion | ( "+str(smallPotion)+" ) 3 HP")
                print("2. Large Potion  | ( "+str(largePotion)+" ) 10 HP")
                choice=int(input("Enter the number corresponding to your choice: "))
                loopCounter += 1
            if (mediumPotion > 0): # checks to see if the player has potions
              mediumPotion -= 1
              pHP += 5
              print("You used a Medium Potion")
              print("You have "+str(mediumPotion)+" Medium Potions left")
              print("You gained 5 HP")
          elif (choice == 3):
            if (largePotion <= 0): # checks to see if the player has potions
              while (choice != 1 and choice != 2):
                if (loopCounter > 0):
                  print()
                  print(Fore.RED+"Invalid Choice")
                  sleep(1)
                  print(Style.RESET_ALL)
                print("Choose which action to take")
                print("1. Small Potion | ( "+str(smallPotion)+" ) 3 HP")
                print("2. Medium Potion  | ( "+str(mediumPotion)+" ) 5 HP")
                choice=int(input("Enter the number corresponding to your choice: "))
                loopCounter += 1
            if (largePotion > 0): # checks to see if the player has potions
              largePotion -= 1
              pHP += 10
              print("You used a Large Potion")
              print("You have "+str(largePotion)+" Large Potions left")
              print("You gained 10 HP")
          choice = 0
        if (choice == 1):
          if (weapon == 1 or weapon == 3):
            eHP -= pAtk
            print("You attacked the Flock of Geese")
            sleep(0.5)
            print("You did "+str(pAtk)+" Dmg")
            sleep(0.5)
            print("The Flock of Geese has "+str(eHP)+" HP left")
          elif (weapon == 2): # sees if the player has daggers to calculate the 50% chance to attack twice
            dblHit = random.randint(1,2)
            if (dblHit == 1): # 1 is a single hit
              eHP -= pAtk
              print("You attacked the Flock of Geese")
              sleep(0.5)
              print("You did "+str(pAtk)+" Dmg")
              print("You attacked once")
              sleep(0.5)
              print("The Flock of Geese has "+str(eHP)+" HP left")
            elif (dblHit == 2): # 2 is a double hit
              eHP -= pAtk*2
              print("You attacked the Flock of Geese")
              sleep(0.5)
              print("You did "+str(pAtk*2)+" Dmg")
              print("You attacked twice")
              sleep(0.5)
              print("The Flock of Geese has "+str(eHP)+" HP left")
          if (eHP > 0):
            geeseAtk = random.randint(1,5)
            pHP -= eAtk*geeseAtk
            print()
            sleep(0.5)
            print("The Flock of Geese attacked "+str(geeseAtk)+" times")
            sleep(0.5)
            print("The Flock of Geese did "+str(eAtk*geeseAtk)+" Dmg")
            sleep(0.5)
        elif (choice == 2):
          dodge = random.randint(1,10)
          if (dodge <= 8):
            print("Dodge Successful")
          else:
            print("You failed to dodge!")
            sleep(0.5)
            geeseAtk = random.randint(1,5)
            pHP -= eAtk*geeseAtk
            print()
            print("The Flock of Geese attacked "+str(geeseAtk)+" times")
            sleep(0.5)
            print("The Flock of Geese did "+str(eAtk*geeseAtk)+" Dmg")
            sleep(0.5)
            print("You have "+str(pHP)+" HP left")
        choice = 0
        loopCounter = 0
        sleep(0.5)
      if (pHP <= 0):
        exit("You Died")
      elif (eHP <= 0):
        print("You have slain the Flock of Geese")
        coinsDrop = random.randint(20,40)
        coins += coinsDrop
        print("The Flock of Geese dropped "+str(coinsDrop)+" coins")
        print(Fore.GREEN+"Balance: "+str(coins)+" coins")
      choice = 0 # resets players choice
      loopCounter = 0 # Resets loop counter
      while (choice != 1 and choice != 2):
        if (loopCounter > 0):
          print()
          print(Fore.RED+"Invalid Choice")
          sleep(1)
          print(Style.RESET_ALL)
        print(Fore.YELLOW+"===========================================================")
        print(Fore.WHITE+"             Do you want to return to the shop?             ")
        print(Fore.YELLOW+"-----------------------------------------------------------")
        print(Fore.WHITE)
        print("Tip: There might be new things")
        print("1. Yes")
        print("2. No")
        print()
        print(Fore.YELLOW+"===========================================================")
        print()
        choice=int(input(Fore.BLUE+"Enter the number corresponding to your choice: "))
        print()
        loopCounter += 1
      if (choice == 1):
        choice = 0
        loopCounter = 0 # Resets loop counter
        while (choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5 and cost > coins):
          if (loopCounter > 0):
            print()
            print(Fore.RED+"Invalid Choice")
            sleep(1)
            print(Style.RESET_ALL)
          print(Fore.YELLOW+"===========================================================") # I found out I could use triple quotes for multiple lines, but I already have the game half done
          print(Fore.WHITE+"                      Page 1: Weapons                      ")
          print(Fore.YELLOW+"-----------------------------------------------------------")
          print(Fore.GREEN+"Balance: "+str(coins)+" coins")
          print(Fore.WHITE+"1. Sword") # item
          print("     100 coins: A basic sword, grants 5 attack") # desc
          print() # spacer
          print("2. Daggers") # item
          print("     100 coins: 2 daggers, grants 3 attack but a 50% chance")
          print("to attack twice") # desc
          print() # spacer
          print("3. Unarmed") # item
          print("     0 coins: Your trusty fists, grants 1 attack") # desc
          print() # spacer
          print("4. Page 2")
          print("     Potions")
          print() # spacer
          print("5. Exit")
          print() # spacer
          print(Fore.YELLOW+"===========================================================")
          print()
          choice=int(input(Fore.BLUE+"Enter the number corresponding to your choice: "))
          print()
          print(Fore.YELLOW+"===========================================================")
          loopCounter += 1
          if (choice == 1):
            choice = 0
            cost = 100
            if (cost > coins):
              print(Fore.RED+"You cannot afford this!")
              choice = 0
              loopCounter = 0
            elif (cost <= coins):
              print("You have purchased the sword for 100 coins")
              print(Fore.GREEN+"Balance: "+str(coins)+" coins")
              weapon = 1
              cost = 1000
          elif (choice == 2):
            choice = 0
            cost = 100
            if (cost > coins):
              print(Fore.RED+"You cannot afford this!")
              choice = 0
              loopCounter = 0
            elif (cost <= coins):
              print("You have purchased the daggers for 100 coins")
              print(Fore.GREEN+"Balance: "+str(coins)+" coins")
              weapon = 2
              cost = 1000
          elif (choice == 3):
            choice = 0
            cost = 0
            if (cost <= coins):
              print("You have purchased unarmed for 0 coins")
              print(Fore.GREEN+"Balance: "+str(coins)+" coins")
              weapon = 3
              cost = 1000
          elif (choice == 4):
            choice = 0
            loopCounter = 0
            while (choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5 and cost > coins):
              if (loopCounter > 0):
                print()
                print(Fore.RED+"Invalid Choice")
                sleep(1)
                print(Style.RESET_ALL)
              print(Fore.WHITE+"                      Page 2: Potions                      ")
              print(Fore.YELLOW+"-----------------------------------------------------------")
              print(Fore.GREEN+"Balance: "+str(coins)+" coins")
              print(Fore.WHITE+"1. Small HP Potion") # item
              print("     10 Coins: Restores 3 HP") # desc
              print() # spacer
              print("2. Medium HP Potion") # item
              print("     15 Coins: Restores 5 HP") # desc
              print() # spacer
              print("3. Large HP Potion") # item
              print("     25 Coins: Restores 10 HP, Best Deal!") # desc
              print() # spacer
              print("4. Page 1")
              print("     Weapons")
              print() # spacer
              print("5. Exit")
              print() # spacer
              print(Fore.YELLOW+"===========================================================")
              print()
              choice=int(input(Fore.BLUE+"Enter the number corresponding to your choice: "))
              print()
              print(Fore.YELLOW+"===========================================================")
              if (choice == 1): # SMALL POTION
                choice = 0
                cost = 10
                if (cost > coins):
                  print(Fore.RED+"You cannot afford this!")
                  choice = 0
                  loopCounter = 0
                elif (cost <= coins):
                  coins -= cost
                  print(Fore.MAGENTA)
                  print("You have purchased the Small HP Potion for 10 Coins")
                  print(Fore.GREEN+"Balance: "+str(coins)+" coins")
                  print()
                  print(Fore.YELLOW+"===========================================================")
                  smallPotion += 1
                  cost = 1000
              elif (choice == 2): # MEDIUM POTION
                choice = 0
                cost = 15
                if (cost > coins):
                  print(Fore.RED+"You cannot afford this!")
                  choice = 0
                  loopCounter = 0
                elif (cost <= coins):
                  coins -= cost
                  print(Fore.MAGENTA)
                  print("You have purchased the Medium HP Potion for 15 Coins")
                  print(Fore.GREEN+"Balance: "+str(coins)+" coins")
                  print()
                  print(Fore.YELLOW+"===========================================================")
                  mediumPotion += 1
                  cost = 1000
              elif (choice == 3): # LARGE POTION
                choice = 0
                cost = 25
                if (cost > coins):
                  print(Fore.RED+"You cannot afford this!")
                  choice = 0
                  loopCounter = 0
                elif (cost <= coins):
                  coins -= cost
                  print(Fore.MAGENTA)
                  print("You have purchased the Large HP Potion for 25 Coins")
                  print(Fore.GREEN+"Balance: "+str(coins)+" coins")
                  print()
                  print(Fore.YELLOW+"===========================================================")
                  largePotion += 1
                  cost = 1000
              elif (choice == 4):
                loopCounter = 0
            choice = 0
      elif (choice == 2):
        print()
        print(Fore.YELLOW+"===========================================================")
        print(Fore.MAGENTA)
        print("The mountain trail connects to the entrance of a forest")
        choice = 0
      loopCounter = 0 # Resets loop counter
  # Cat of the mountain, dog of wisdom, just some guy named Horace, flock of geese (rng for attacks aka fury swipes)
# NOTE FOR SELF - START OFF WITH THE FOREST ROUTE, IF YOU HAVE ENOUGH TIME, DO THE MOUNTAIN ROUTE
# THE BURGER KING SHALL BE THE FINAL BOSS FOR BOTH ROUTES

# STARTING THE BURGER KING FIGHT
# The boss can be defeated, it requires some luck, but you just need to dodge his special, and heal
print(Fore.MAGENTA)
eAtk = 5
eHP = 25
sleep(1)
print("You spot something in the distance")
sleep(1)
print("It seems to be wearing a crown")
sleep(1)
print("You have encountered The Burger King!")
sleep(1)
print("Tip: Every other attack he uses a special ability!")
while (pHP > 0 and eHP > 0):
  while (choice != 1 and choice != 2 and choice != 3):
    if (loopCounter > 0):
      print()
      print(Fore.RED+"Invalid Choice")
      sleep(1)
      print(Style.RESET_ALL)
    print(Fore.MAGENTA+"You have "+str(pHP)+" HP")
    print("The Burger King has "+str(eHP)+" HP")
    print()
    sleep(1)
    print(Fore.YELLOW+"===========================================================")
    print(Fore.WHITE+"                Choose which action to take                ")
    print(Fore.YELLOW+"-----------------------------------------------------------")
    print(Fore.WHITE+"1. Attack | "+str(pAtk)+" Dmg")
    print("2. Dodge  | 80% Chance")
    print("3. Potion | Heal your HP (no HP limit)")
    print() # spacer
    print(Fore.YELLOW+"===========================================================")
    print()
    choice=int(input(Fore.BLUE+"Enter the number corresponding to your choice: "))
    print() # spacer
    print(Fore.YELLOW+"===========================================================")
    print(Fore.MAGENTA)
    loopCounter += 1
  if (choice == 3):
    choice = 0
    loopCounter = 0
    if (smallPotion <= 0 and mediumPotion <= 0 and largePotion <= 0): # checks to see if the player has potions
      print("You do not have any potions!")
      while (choice != 1 and choice != 2):
        if (loopCounter > 0):
          print()
          print(Fore.RED+"Invalid Choice")
          sleep(1)
          print(Style.RESET_ALL)
        print(Fore.YELLOW+"===========================================================")
        print(Fore.WHITE+"                Choose which action to take                ")
        print(Fore.YELLOW+"-----------------------------------------------------------")
        print("1. Attack | "+str(pAtk)+" Dmg")
        print("2. Dodge  | 80% Chance")
        print() # spacer
        print(Fore.YELLOW+"===========================================================")
        print()
        choice=int(input(Fore.BLUE+"Enter the number corresponding to your choice: "))
        print() # spacer
        print(Fore.YELLOW+"===========================================================")
        loopCounter += 1
    while (choice != 1 and choice != 2 and choice != 3): # which potion they want to use
      if (loopCounter > 0):
        print()
        print(Fore.RED+"Invalid Choice")
        sleep(1)
        print(Style.RESET_ALL)
      print("Choose which action to take")
      print("1. Small Potion  | ( "+str(smallPotion)+" ) 3 HP")
      print("2. Medium Potion | ( "+str(mediumPotion)+" ) 5 HP")
      print("3. Large Potion  | ( "+str(largePotion)+" ) 10 HP")
      choice=int(input("Enter the number corresponding to your choice: "))
      loopCounter += 1
    if (choice == 1):
      if (smallPotion <= 0): # checks to see if the player has potions
        while (choice != 1 and choice != 2):
          if (loopCounter > 0):
            print()
            print(Fore.RED+"Invalid Choice")
            sleep(1)
            print(Style.RESET_ALL)
          print("Choose which action to take")
          print("1. Medium Potion | ( "+str(mediumPotion)+" ) 5 HP")
          print("2. Large Potion  | ( "+str(largePotion)+" ) 10 HP")
          choice=int(input("Enter the number corresponding to your choice: "))
          loopCounter += 1
        if (choice == 1):
          mediumPotion -= 1
          pHP += 5
          print("You used a Medium Potion")
          print("You have "+str(mediumPotion)+" Medium Potions left")
          print("You gained 5 HP")
        elif (choice == 2):
          largePotion -= 1
          pHP += 10
          print("You used a Large Potion")
          print("You have "+str(largePotion)+" Large Potions left")
          print("You gained 10 HP")
      if (smallPotion > 0): # checks to see if the player has potions
        smallPotion -= 1
        pHP += 3
        print("You used a Small Potion")
        print("You have "+str(smallPotion)+" Small Potions left")
        print("You gained 3 HP")
    elif (choice == 2):
      if (mediumPotion <= 0): # checks to see if the player has potions
        while (choice != 1 and choice != 2):
          if (loopCounter > 0):
            print()
            print(Fore.RED+"Invalid Choice")
            sleep(1)
            print(Style.RESET_ALL)
          print("Choose which action to take")
          print("1. Small Potion | ( "+str(smallPotion)+" ) 3 HP")
          print("2. Large Potion  | ( "+str(largePotion)+" ) 10 HP")
          choice=int(input("Enter the number corresponding to your choice: "))
          loopCounter += 1
      if (mediumPotion > 0): # checks to see if the player has potions
        mediumPotion -= 1
        pHP += 5
        print("You used a Medium Potion")
        print("You have "+str(mediumPotion)+" Medium Potions left")
        print("You gained 5 HP")
    elif (choice == 3):
      if (largePotion <= 0): # checks to see if the player has potions
        while (choice != 1 and choice != 2):
          if (loopCounter > 0):
            print()
            print(Fore.RED+"Invalid Choice")
            sleep(1)
            print(Style.RESET_ALL)
          print("Choose which action to take")
          print("1. Small Potion | ( "+str(smallPotion)+" ) 3 HP")
          print("2. Medium Potion  | ( "+str(mediumPotion)+" ) 5 HP")
          choice=int(input("Enter the number corresponding to your choice: "))
          loopCounter += 1
      if (largePotion > 0): # checks to see if the player has potions
        largePotion -= 1
        pHP += 10
        print("You used a Large Potion")
        print("You have "+str(largePotion)+" Large Potions left")
        print("You gained 10 HP")
    choice = 0
  if (choice == 1):
    if (weapon == 1 or weapon == 3):
      eHP -= pAtk
      print("You attacked the Burger King")
      sleep(0.5)
      print("You did "+str(pAtk)+" Dmg")
      sleep(0.5)
      print("The Burger King has "+str(eHP)+" HP left")
    elif (weapon == 2): # sees if the player has daggers to calculate the 50% chance to attack twice
      dblHit = random.randint(1,2)
      if (dblHit == 1): # 1 is a single hit
        eHP -= pAtk
        print("You attacked the Burger King")
        sleep(0.5)
        print("You did "+str(pAtk)+" Dmg")
        print("You attacked once")
        sleep(0.5)
        print("The Burger King has "+str(eHP)+" HP left")
      elif (dblHit == 2): # 2 is a double hit
        eHP -= pAtk*2
        print("You attacked the Burger King")
        sleep(0.5)
        print("You did "+str(pAtk*2)+" Dmg")
        print("You attacked twice")
        sleep(0.5)
        print("The Burger King has "+str(eHP)+" HP left")
    if (eHP > 0):
      if (bkAtk == 0):
        pHP -= eAtk
        print("The Burger King attacks")
        sleep(0.5)
        print("The Burger King did "+str(eAtk)+" Dmg")
        sleep(0.5)
        bkAtk += 1
      elif (bkAtk == 1):
        pHP -= eAtk*2
        print("The Burger King activates his special ability")
        sleep(1)
        print("* * * * * * * *")
        print("W H O P P E R !")
        print("* * * * * * * *")
        sleep(0.5)
        print("The Burger King did "+str(eAtk*2)+" Dmg")
        sleep(0.5)
        bkAtk = 0
  elif (choice == 2):
    dodge = random.randint(1,10)
    if (dodge <= 8):
      if (bkAtk == 0):
        print("The Burger King attacks")
        bkAtk += 1
      elif (bkAtk == 1):
        print("The Burger King activates his special ability")
        sleep(1)
        print("* * * * * * * *")
        print("W H O P P E R !")
        print("* * * * * * * *")
        sleep(0.5)
        bkAtk = 0
      print("Dodge Successful")
    else:
      print("You failed to dodge!")
      sleep(0.5)
      if (bkAtk == 0):
        pHP -= eAtk
        print("The Burger King attacks")
        sleep(0.5)
        print("The Burger King did "+str(eAtk)+" Dmg")
        sleep(0.5)
        bkAtk += 1
      elif (bkAtk == 1):
        pHP -= eAtk*2
        print("The Burger King activates his special ability")
        sleep(1)
        print("* * * * * * * *")
        print("W H O P P E R !")
        print("* * * * * * * *")
        sleep(0.5)
        print("The Burger King did "+str(eAtk*2)+" Dmg")
        sleep(0.5)
        print("You have "+str(pHP)+" HP left")
        bkAtk = 0
  choice = 0
  loopCounter = 0
  sleep(0.5)
if (pHP <= 0):
  exit("You Died")
elif (eHP <= 0):
  print(Fore.MAGENTA)
  print("You have slain the Burger King")
  sleep(1)
  print("You pick up his crown")
  sleep(1)
  print("You put it on")
  sleep(1)
  print("Everything goes black")
  sleep(1)
  print(".")
  sleep(1)
  print(".")
  sleep(1)
  print(".")
  sleep(1)
  print("You wake up and see someone in the distance")
  sleep(1)
  print("It seems they want to battle you")
  sleep(1)
  print()
  print(Fore.CYAN+"===========================================================")
  print(Fore.WHITE+"                          THE END                          ")
  print(Fore.CYAN+"===========================================================")