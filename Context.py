import Fuck

def combat():
    #while(Character.health > 0 or Skeleton.health > 0):
        if Fuck.Character.hit_succ():
            if not Fuck.Skeleton.dodge_succ():
                Fuck.Skeleton.health -= Fuck.Character.attack

        if Fuck.Skelton.hit_succ():
            if not Fuck.Character.dodge_succ():
                Fuck.Character.health -= Fuck.Skeleton.attack

while(Fuck.Character.health > 0 or Fuck.Skeleton.health > 0):
    print("There is a skeleton in front of you do you attack or run?")
    choose=int(input("Press 1 to attack. Press 2 to run."))
    if choose == 1:
        combat()
