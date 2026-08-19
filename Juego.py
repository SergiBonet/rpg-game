import random
import time

class Character:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.health = 100
        self.attack = 10
        self.defence = 10
        self.velocity = 10
        
    def show_stats(self):
        print("Name:",self.name)
        print("Level:",self.level)
        print("Health: ",self.health)
        print("Attack: ",self.attack)
        print("Defence: ",self.defence)
        print("Velocity: ", self.velocity)

    def round_attack(self,target):
        damage=self.attack-target.defence
        if (damage<1):damage=1
        target.health=target.health-damage

        if (target.health<=0):
            print (target.name," is dead")
        else:
            damage=target.attack-self.defence
            if (damage<1):damage=1
            self.health=self.health-damage
        

class Enemy(Character):
    def __init__(self, name):
        super().__init__(name)
        self.level *= 1
        self.health *= 2
        self.attack *= 2
        self.defence *= 1
        self.velocity *= 2
        self.experience = 0
        self.experience_reward = 50

class Player(Character):
    def __init__(self, name):
        super().__init__(name)
        self.level *= 1
        self.health *= 2
        self.attack *= 3
        self.defence *= 2
        self.velocity *= 2
        self.experience = 0
        self.next_exp = 40 + (self.level * 10)


    
    def show_stats(self):
        super().show_stats()
        print("Experience: ",self.experience)
        print("For the next level: ",self.experience,"/", self.next_exp)

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

robin = Player("Robin")
goblin = Enemy("Goblin")

print()
robin.show_stats()
print()
goblin.show_stats()
print()

print()
while ((robin.health>0)and(goblin.health>0)):
    print()
    combat_round(robin,goblin)
    print()
    robin.show_stats()
    print()
    goblin.show_stats()
    time.sleep(0)
if(robin.health<=0):
    winner= goblin.name
else:
    winner=robin.name
    robin.experience= robin.experience+goblin.experience_reward
    print()
    print("And win ", goblin.experience_reward," exp points")
    print()
    if (robin.experience>=robin.next_exp):
        robin.level+=1
        robin.experience=0
        print(robin.name," has leveled up")
        print()
        robin.next_exp = 40 + (robin.level * 10)
        robin.health = round(robin.health*1.1)
        robin.attack = round(robin.attack*1.1)
        robin.defence = round(robin.defence*1.1)
        robin.velocity = round(robin.velocity*1.1)
robin.show_stats()
print()
print(winner," win the battle!!")
