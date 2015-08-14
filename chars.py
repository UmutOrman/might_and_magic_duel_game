from random import randint
from skills import *
class Char(object):
    def __init__(self, health, mana, attack_power, x, y, pala_rage, untouchable, dh_rain, immobilize,  dark_rits, sickness_lil , pray_effect, fist_god, ours_fury , initial_hp): 
        self.health = health
        self.mana = mana
        self.x = x
        self.y = y
        self.attack_power = attack_power
        self.pala_rage = pala_rage
        self.untouchable = untouchable
        self.dh_rain = dh_rain
        self.immobilize = immobilize
        self.dark_rits = dark_rits
        self.sickness_lil = sickness_lil
        self.pray_effect = pray_effect
        self.fist_god = fist_god
        self.ours_fury = ours_fury
        self.initial_hp = initial_hp
        
    def attack(self, enemy, is_enemy):
        if (is_enemy == True):
            print "Enemy attacks you!"
        else:
            print "You attack to enemy!"    
        self.attack_power = randint(self.x , self.y)
        enemy.health -= self.attack_power
        
class Paladin(Char):
        
    def info(self):
        print """"
        Greetings my lord, what a decent job you made by picking me ! I fight for 
        the lord of the light !
        Let's bring light to all those bastards who do not bend knee! 
        Siggmaaaaarrrrrrr !
        My skills are :
        1. Holy Strike
        2. Wise Rage
        3. Divine Protection
    """
    def firstskill(self, enemy, is_enemy):
        holy_strike(self,enemy, is_enemy)

    def secondskill(self, enemy, is_enemy):
        wise_rage(self, enemy, is_enemy)
        
    def thirdskill(self, enemy, is_enemy):
        divine_protection(self, enemy, is_enemy)
        
class DemonHunter(Char):
    def info(self):
        print """
        Well, I think you need to burn down some heretics or kick some asses! 
        Let's burn all the witches and bitches ! 
        My skills are:
        1. Rain of the Old Legion
        2. Tail of Samael
        3. Killing Blow
        """
    def firstskill(self, enemy, is_enemy):
        rain_of_the_old_legion(self, enemy, is_enemy)
    
    def secondskill(self, enemy, is_enemy):
        tail_of_samael(self, enemy, is_enemy)
        
    def thirdskill(self, enemy, is_enemy):
        killing_blow(self, enemy, is_enemy)
        
class Sorcerer(Char):
    def info(self):
        print """
        If you're looking for some real magic, you are at right place.
        Let's see what can my darkest spells do !
        My skills are:
        1. Dark Rituals     
        2. Sickness of Lilith
        3. Frostnova
        """
    def firstskill(self, enemy, is_enemy):
        dark_rituals(self,enemy, is_enemy)
    
    def secondskill(self, enemy, is_enemy):
        sickness_of_lilith(self, enemy, is_enemy)
        
    def thirdskill(self, enemy, is_enemy):
        frostnova(self,enemy, is_enemy)
        
class Priest(Char):
    def info(self):
        print """
        Raise the God, let Thy the shine above them, they may find peace at the end.
        Surrender me, surrender the world, God will forgive!
        My skills are:
        1. Pray     
        2. Healing Wounds
        3. I'm God's Fist!
        """
    def firstskill(self, enemy, is_enemy):
        pray(self, enemy, is_enemy)

    def secondskill(self, enemy, is_enemy):
        healing_wounds(self, enemy, is_enemy)
    
    def thirdskill (self, enemy, is_enemy):
        god_fist(self, enemy, is_enemy)
        
class BladeMaster(Char):
    def info(self):
        print """
        Just show me the target, or go away, I don't have time for bullshit.
        Mastering blades is an ancient art.People shouldn't mess with that...
        My skills are:
        1. Twin Blades
        2. Reaper's Harvest
        3. Ours is the fury!
        """
        
    def firstskill(self, enemy, is_enemy):
        twin_blades(self, enemy, is_enemy)
        
    def secondskill(self, enemy, is_enemy):
        reaper_harvest(self, enemy, is_enemy)
        
    def thirdskill(self, enemy, is_enemy):
        our_is_the_fury(self, enemy, is_enemy)
        
class Wizard(Char):
    def info(self):
        print """
        Burn baby burn, till your blood boils.
        Real magic is fire, come and test me !
        My skills are:
        1. Fireball
        2. Fire Shield
        3. Polymorph
        """
    def firstskill(self, enemy, is_enemy):
        fireball(self, enemy, is_enemy)
        
    def secondskill(self, enemy, is_enemy):
        fire_shield(self, enemy, is_enemy)
        
    def thirdskill(self, enemy, is_enemy):
        polymorph(self, enemy ,is_enemy)

    
