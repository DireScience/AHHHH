import random
class Character:
    attack = 5
    health = 20
    dodge = 10  #Out of hundred
    hit = 80 #Out of hundred

    def dodge_succ():
        rand_d = random.randint(1,101)
        if rand_d <= Character.dodge:
            return True
        return False

    def hit_succ():
        rand_h = random.randint(1,101)
        if rand_h <= Character.hit:
            return True
        return False

class Skelton:
    attack = 4
    health = 25
    dodge = 50
    hit = 30

    def dodge_succ():
        rand_d = random.randint(1,101)
        if rand_d <= Skeleton.dodge:
            return True
        return False

    def hit_succ():
        rand_h = random.randint(1,101)
        if rand_h <= Skelton.hit:
            return True
        return False
