import random

#Variable setup
gamerun = True 
player_HP = 2000
CPU_HP = 2000
player_dmg = 0
CPU_dmg = 0 

print('''============
    Welcome to the RPG test!
    The game will end if you or the CPU's health reaches 0.
    To make your move, answer the game's prompt with "attack" or "defend"
    ============''' )
if player_HP == 0 or CPU_HP == 0:
        gamerun = False
elif gamerun == True:
    while gamerun:
        print('''        MENU
       -------
       ATTACK
       DEFEND''')
        player_input = input("Enter your next move: ")
        CPU_input = random.randrange(0,2,1)
#######IF THE PLAYER IS ATTACKING
        if player_input.upper() == "ATTACK" and CPU_input == 0:
            player_dmg = random.randrange(10,500,5)
            CPU_dmg = random.randrange(10,500,5)
            if player_dmg > CPU_dmg:
                CPU_HP = CPU_HP - (player_dmg - CPU_dmg)
                print("The player's damage is: ", player_dmg, ". The CPU's damage is: ", CPU_dmg, ". The CPU's HP is: ", CPU_HP)
            elif player_dmg < CPU_dmg:
                player_HP = player_HP - (CPU_dmg - player_dmg)
                print("The player's damage is: ", player_dmg, ". The CPU's damage is: ", CPU_dmg, ". The players's HP is: ", player_HP)
        elif player_input.upper() == "ATTACK" and CPU_input ==1:
            player_dmg = random.randrange(10, 500, 5)
            CPU_def = random.randrange(10, 500, 5)
            print("The player's attack damage is: ", player_dmg, "! ", "The CPU's defense is: ", CPU_def, "!")
            if player_dmg > CPU_def:
                player_dmg = player_dmg - CPU_def
                CPU_HP = CPU_HP - player_dmg
                print('The CPU takes ', player_dmg, "damage! The CPU's health is now: ", CPU_HP)
            elif player_dmg < CPU_def:
                print("The CPU's defense is: ", CPU_def, ". The player's attack damage is: ", player_dmg, ". The CPU takes no damage.")
            else:
                print("Attack and defense values are the same, no damage.")
    ########IF THE PLAYER IS DEFENDING
        elif player_input.upper() == "DEFEND" and CPU_input == 0:
            player_def = random.randrange(10, 500, 5)
            CPU_dmg = random.randrange(10, 500, 5)
            if player_def > CPU_dmg:
                print("The player's defense is: ", player_def, ". The CPU's attack damage is: ", CPU_dmg, ". The player takes no damage.")
            elif player_def < CPU_dmg:
                CPU_dmg = CPU_dmg - player_def
                player_HP = player_HP - CPU_dmg
                print ("The CPU's attack damage is: ", CPU_dmg, ". The player's defense is: ", player_def, " The player's HP is now: ", player_HP)
            else:
                print("Attack and defense values are are equal, no damage.")
        elif player_input.upper() == "DEFEND" and CPU_input == 1:
            print("Both players defended.")
        if player_HP <=0:
            print("The player has run out of health, the CPU wins!")
        elif CPU_HP <=0:
            print("The CPU's health has run out, the player wins!")