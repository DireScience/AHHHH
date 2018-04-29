import Entities
import time
import Items

def rand_enc():
    s_enc = Entities.Skeleton.get_enc()
    g_enc = Entities.Goblin.get_enc()
    a_enc = Entities.Ant.get_enc()
    b_enc = Entities.Bear.get_enc()
    enc_array = [s_enc, g_enc, a_enc, b_enc]
    global great_index = 0
    great_value = 0
    for x in range(0,3):
        if enc_array[x] > great_value:
            great_index = x
            great_value = enc_array[x]


    global charac_int = Entities.Character.intiative()

    if great_index == 0:
        Entities.Skeleton.health = 25
        global skele_int = Entities.Skeleton.intiative()
        if charac_int >= skele_int:
            print("You notice a skeleton and swing at it!")
            time.sleep(2)

        else:
            print("Out of nowhere a skeleton pops out and swings at you!")
            time.sleep(2)

        skelton_combat()

    elif great_index == 1:
        Entities.Goblin.health = 20
        global gob_int = Entities.Goblin.intiative()
        if charac_int >= gob_int:
            print("You notice a goblin and take a swing!")
            time.sleep(2)

        else:
            print("A goblin jumps out from behind a rock and stabs at you!")
            time.sleep(2)

        goblin_combat()

    elif great_index == 2:
        Entities.Ant.health = 1
        global ant_int = Entities.Ant.intiative()
        if charac_int >= ant_int:
            print("You almost step on an ant!")
            time.sleep(2)

        else:
            print("You're walking and notice a small ant. You say to yourself 'Oh fuck...'")
            time.sleep(2)

        ant_combat()

    else:
        Entities.Bear.health = 30
        global bear_int = Entities.Bear.intiative()
        if charac_int >= bear_int:
            print("You see a bear and try to chop it's head off!")
            time.sleep(2)

        else:
            print("You see a bear in the distance and it charges at you!")
            time.sleep(2)

        bear_combat()

def skeleton_combat():
    if charc_int >= skele_int:

        if Entities.Character.hit_succ():
            if not Entities.Skeleton.dodge_succ():
                Entities.Skeleton.health -= Entities.Character.attack
                print("You hit the skeleton!")
                time.sleep(2)

            else:
                print("You missed the skeleton!")
                time.sleep(2)

        else:
            print("You missed the skeleton!")
            time.sleep(2)


        if Entities.Skeleton.health == 0:
            print("You killed the skeleton and have completed your quest!")
            time.sleep(2)
            exit()

        if Entities.Skeleton.hit_succ():
            if not Entities.Character.dodge_succ():
                Entities.Character.health -= Entities.Skeleton.attack
                print("You were hit!")
                time.sleep(2)

            else:
                print("The skeleton missed!")
                time.sleep(2)

        else:
            print("The skeleton missed!")
            time.sleep(2)

        if Entities.Character.health == 0:
            print("You died!")
            time.sleep(2)
            exit()

    else:
        if Entities.Skeleton.hit_succ():
            if not Entities.Character.dodge_succ():
                Entities.Character.health -= Entities.Skeleton.attack
                print("You were hit!")
                time.sleep(2)

            else:
                print("The skeleton missed!")
                time.sleep(2)

        else:
            print("The skeleton missed!")
            time.sleep(2)

        if Entities.Character.health == 0:
            print("You died!")
            time.sleep(2)
            exit()

        if Entities.Character.hit_succ():
            if not Entities.Skeleton.dodge_succ():
                Entities.Skeleton.health -= Entities.Character.attack
                print("You hit the skeleton!")
                time.sleep(2)

            else:
                print("You missed the skeleton!")
                time.sleep(2)

        else:
            print("You missed the skeleton!")
            time.sleep(2)


        if Entities.Skeleton.health == 0:
            print("You killed the skeleton and have completed your quest!")
            time.sleep(2)
            exit()

def ant_combat():
    if Echarac_int >= ant_int:

        if Entities.Character.hit_succ():
            if not Entities.Ant.dodge_succ():
                Entities.Ant.health -= Entities.Character.attack
                print("You hit the ant!")
                time.sleep(2)

            else:
                print("You missed the ant!")
                time.sleep(2)

        else:
            print("You missed the ant!")
            time.sleep(2)


        if Entities.Skeleton.health == 0:
            print("You killed the ant!")
            time.sleep(2)
            print("Would you like to use a health potion?")
            time.sleep(2)
            pot = int(input("Press 1 to use a health potion. Press 2 to save it."))
            if pot == 1:
                Entities.Character.health += get_heal()

            elif pot == 2:
                rand_enc()
            rand_enc()

        if Entities.Ant.hit_succ():
            if not Entities.Ant.dodge_succ():
                Entities.Character.health -= Entities.Ant.attack
                print("You were hit!")
                time.sleep(2)

            else:
                print("The ant missed!")
                time.sleep(2)

        else:
            print("The ant missed!")
            time.sleep(2)

        if Entities.Character.health == 0:
            print("You died!")
            time.sleep(2)
            exit()

    else:
        if Entities.Ant.hit_succ():
            if not Entities.Character.dodge_succ():
                Entities.Character.health -= Entities.Ant.attack
                print("You were hit!")
                time.sleep(2)

            else:
                print("The ant missed!")
                time.sleep(2)

        else:
            print("The ant missed!")
            time.sleep(2)

        if Entities.Character.health == 0:
            print("You died!")
            time.sleep(2)
            exit()

        if Entities.Character.hit_succ():
            if not Entities.Ant.dodge_succ():
                Entities.Ant.health -= Entities.Character.attack
                print("You hit the ant!")
                time.sleep(2)

            else:
                print("You missed the ant!")
                time.sleep(2)

        else:
            print("You missed the ant!")
            time.sleep(2)


        if Entities.Skeleton.health == 0:
            print("You killed the ant!")
            time.sleep(2)
            print("Would you like to use a health potion?")
            time.sleep(2)
            pot = int(input("Press 1 to use a health potion. Press 2 to save it."))
            if pot == 1:
                Entities.Character.health += get_heal()

            elif pot == 2:
                rand_enc()
            rand_enc()

def bear_combat():
    if charac_int >= bear_int:

        if Entities.Character.hit_succ():
            if not Entities.Bear.dodge_succ():
                Entities.Bear.health -= Entities.Character.attack
                print("You hit the bear!")
                time.sleep(2)

            else:
                print("You missed the bear!")
                time.sleep(2)

        else:
            print("You missed the bear!")
            time.sleep(2)


        if Entities.Bear.health == 0:
            print("You killed the bear!")
            time.sleep(2)
            print("Would you like to use a health potion?")
            time.sleep(2)
            pot = int(input("Press 1 to use a health potion. Press 2 to save it."))
            if pot == 1:
                Entities.Character.health += get_heal()

            elif pot == 2:
                rand_enc()
            rand_enc()

        if Entities.Bear.hit_succ():
            if not Entities.Character.dodge_succ():
                Entities.Character.health -= Entities.Bear.attack
                print("You were hit!")
                time.sleep(2)

            else:
                print("The bear missed!")
                time.sleep(2)

        else:
            print("The Bear missed!")
            time.sleep(2)

        if Entities.Character.health == 0:
            print("You died!")
            time.sleep(2)
            exit()

    else:
        if Entities.Bear.hit_succ():
            if not Entities.Character.dodge_succ():
                Entities.Character.health -= Entities.Bear.attack
                print("You were hit!")
                time.sleep(2)

            else:
                print("The bear missed!")
                time.sleep(2)

        else:
            print("The bear missed!")
            time.sleep(2)

        if Entities.Character.health == 0:
            print("You died!")
            time.sleep(2)
            exit()

        if Entities.Character.hit_succ():
            if not Entities.Bear.dodge_succ():
                Entities.Bear.health -= Entities.Character.attack
                print("You hit the bear!")
                time.sleep(2)

            else:
                print("You missed the bear!")
                time.sleep(2)

        else:
            print("You missed the bear!")
            time.sleep(2)


        if Entities.Bear.health == 0:
            print("You killed the bear!")
            time.sleep(2)
            print("Would you like to use a health potion?")
            time.sleep(2)
            pot = int(input("Press 1 to use a health potion. Press 2 to save it."))
            if pot == 1:
                Entities.Character.health += get_heal()

            elif pot == 2:
                rand_enc()
            rand_enc()

def goblin_combat():
    if charac_int >= =gob_int:

        if Entities.Character.hit_succ():
            if not Entities.Goblin.dodge_succ():
                Entities.Goblin.health -= Entities.Character.attack
                print("You hit the goblin!")
                time.sleep(2)

            else:
                print("You missed the goblin!")
                time.sleep(2)

        else:
            print("You missed the goblin!")
            time.sleep(2)


        if Entities.Goblin.health == 0:
            print("You killed the goblin!")
            time.sleep(2)
            print("Would you like to use a health potion?")
            time.sleep(2)
            pot = int(input("Press 1 to use a health potion. Press 2 to save it."))
            if pot == 1:
                Entities.Character.health += get_heal()

            elif pot == 2:
                rand_enc()
            rand_enc()

        if Entities.Goblin.hit_succ():
            if not Entities.Character.dodge_succ():
                Entities.Character.health -= Entities.Goblin.attack
                print("You were hit!")
                time.sleep(2)

            else:
                print("The goblin missed!")
                time.sleep(2)

        else:
            print("The goblin missed!")
            time.sleep(2)

        if Entities.Character.health == 0:
            print("You died!")
            time.sleep(2)
            exit()

    else:
        if Entities.Goblin.hit_succ():
            if not Entities.Character.dodge_succ():
                Entities.Character.health -= Entities.Goblin.attack
                print("You were hit!")
                time.sleep(2)

            else:
                print("The goblin missed!")
                time.sleep(2)

        else:
            print("The goblin missed!")
            time.sleep(2)

        if Entities.Character.health == 0:
            print("You died!")
            time.sleep(2)
            exit()

        if Entities.Character.hit_succ():
            if not Entities.Goblin.dodge_succ():
                Entities.Goblin.health -= Entities.Character.attack
                print("You hit the goblin!")
                time.sleep(2)

            else:
                print("You missed the goblin!")
                time.sleep(2)

        else:
            print("You missed the goblin!")
            time.sleep(2)


        if Entities.goblin.health == 0:
            print("You killed the goblin!")
            time.sleep(2)
            print("Would you like to use a health potion?")
            time.sleep(2)
            pot = int(input("Press 1 to use a health potion. Press 2 to save it."))
            if pot == 1:
                Entities.Character.health += get_heal()

            elif pot == 2:
                rand_enc()
            rand_enc()

print("You are a brave knight who is on an adventure to kill one singular skeleton!")
time.sleep(2)
print("While on your journey you walk into a dark cavern.")
time.sleep(2)
rand_enc()

while(Entities.Character.health > 0):
    print("Do you wish to attack or run?")
    time.sleep(2)
    choose = int(input("Press 1 to attack. Press 2 to run."))
    if choose == 1:
        if great_index == 0:
            skeleton_combat()

        elif great_index == 1 :
            goblin_combat()

        elif great_index == 2:
            ant_combat()

        else:
            bear_combat()

    elif choose == 2:
        print("You run away like the 'brave' knight you are. You may have failed your quest, but at least you're alive.")
        time.sleep(2)
        exit()
