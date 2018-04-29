import Entities
import time

def combat():
    if Entities.Character.roll >= Entities.Skeleton.roll:

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
            print("You killed the skeleton!")
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
            print("You killed the skeleton!")
            time.sleep(2)
            exit()

Entities.Character.roll
Entities.Skeleton.roll

print("You are a brave knight who is on an adventure to kill one singular skeleton!")
time.sleep(2)
print("While on your journey you walk into a dark cavern.")
time.sleep(2)

if Entities.Character.roll >= Entities.Skeleton.roll:
    print("You notice a skelton in the darkness and swing at it!")
    time.sleep(2)

else:
    print("Out of nowhere a skeleton surprises you and swings its sword at you!")
    time.sleep(2)

combat()

while(Entities.Character.health > 0 and Entities.Skeleton.health > 0):
    print("Do you wish to attack or run?")
    time.sleep(2)
    choose = int(input("Press 1 to attack. Press 2 to run."))
    if choose == 1:
        combat()

    if choose == 2:
        print("You run away like the 'brave' knight you are. You may have failed your quest, but at least you're alive.")
        time.sleep(2)
        exit()
