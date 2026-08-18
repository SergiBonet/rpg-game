import random
import time

class Character:
    def __init__(self, name, level, health, attack, defence,velocity):
        self.name = name
        self.level = level
        self.health = health
        self.attack = attack
        self.defence = defence
        self.velocity = velocity
        
    def show_stats(self):
        print("Name:",self.name)
        print("Level:",self.level)
        print("Health: ",self.health)
        print("Attack: ",self.attack)
        print("Defence: ",self.defence)
        print("Velocity: ", self.velocity)

    def round_attack(first,second):
        damage=first.attack-second.defence
        if (damage<1):damage=1
        second.health=second.health-damage

        if (second.health<=0):
            print (second.name," is dead")
        else:
            damage=second.attack-first.defence
            if (damage<1):damage=1
            first.health=first.health-damage
        

class Enemy(Character):
    def __init__(self, name, level, health, attack, defence,velocity):
        super().__init__(name, level, health, attack, defence,velocity)

class Player(Character):
    def __init__(self, name, level, health, attack, defence,experience,velocity):
        super().__init__(name, level, health, attack, defence,velocity)
        self.experience = experience
    def show_stats(self):
        super().show_stats()
        print("Experience: ",self.experience)

def combat_round(player,enemy):
    print (("Combat START \n{} vs {}").format(player.name,enemy.name))
    if (player.velocity>enemy.velocity):
        print(player.name," attack first")
        Character.round_attack(player,enemy)

    elif(player.velocity==enemy.velocity):
        eleccion=random.choice([player,enemy])
        if eleccion==player:
            other=enemy
        else:
            other= player
        print(eleccion.name," attack first")
        Character.round_attack(eleccion,other)
    else:
        print(enemy.name," attack first")
        Character.round_attack(enemy,player)

robin = Player("Robin",1, 100, 10, 8,0,10)#LEVEL,HEALTH,ATTACK,DEFENCE,EXPERIENCE,SPEED
goblin = Enemy("Goblin",1,70,11,8,10)

print()
robin.show_stats()
print()
goblin.show_stats()
print()

print()
while ((robin.health>0)and(goblin.health>0)):
    combat_round(robin,goblin)
    print()
    robin.show_stats()
    print()
    goblin.show_stats()
    time.sleep(1)
if(robin.health<=0):
    winner= goblin.name
else:winner=robin.name
print()
print(winner," win the battle!!")