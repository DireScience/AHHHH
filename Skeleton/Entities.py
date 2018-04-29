import random

class Character:
    attack = 5
    health = 20
    dodge = 20  #Out of hundred
    hit = 80 #Out of hundred

    def intiative():
        roll = random.randint(1,21)
        return roll

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

class Skeleton:
    attack = 4
    health = 25
    dodge = 50
    hit = 35

    def intiative():
        roll = random.randint(1,21)
        return roll

    def dodge_succ():
        rand_d = random.randint(1,101)
        if rand_d <= Skeleton.dodge:
            return True
        return False

    def hit_succ():
        rand_h = random.randint(1,101)
        if rand_h <= Skeleton.hit:
            return True
        return False

     def get_enc():
         enc = random.randint(1,21)
         return enc

class Bear:
    attack = 7
    health = 30
    dodge = 5
    hit = 40

    def intiative():
        roll = random.randint(1,21)
        return roll

    def dodge_succ():
        rand_d = random.randint(1,101)
        if rand_d <= Skeleton.dodge:
            return True
        return False

    def hit_succ():
        rand_h = random.randint(1,101)
        if rand_h <= Skeleton.hit:
            return True
        return False

    def get_enc():
        enc = random.randint(1,21)
        return enc

class Ant:
    attack = 15
    health = 1
    dodge = 99
    hit = 75

    def intiative():
        roll = random.randint(1,21)
        return roll

    def dodge_succ():
        rand_d = random.randint(1,101)
        if rand_d <= Skeleton.dodge:
            return True
        return False

    def hit_succ():
        rand_h = random.randint(1,101)
        if rand_h <= Skeleton.hit:
            return True
        return False

    def get_enc():
        enc = random.randint(1,21)
        return enc

class Goblin:
    attack = 5
    health = 20
    dodge = 20
    hit = 60

    def intiative():
        roll = random.randint(1,21)
        return roll

    def dodge_succ():
        rand_d = random.randint(1,101)
        if rand_d <= Skeleton.dodge:
            return True
        return False

    def hit_succ():
        rand_h = random.randint(1,101)
        if rand_h <= Skeleton.hit:
            return True
        return False

    def get_enc():
        enc = random.randint(1,21)
        return enc
