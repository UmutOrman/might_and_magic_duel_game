#script name: skills.py
#author: Umut Orman
#created: 14th August 2015
#version: 1.0
#description: skills are defined in this script in terms of functions
def print_after_skill(player, enemy, is_enemy):
    if (is_enemy == False):
        print "Your health is : %d  , your mana is %d " % (player.health , player.mana)
        print "Enemy's health is: %d , enemy's mana is %d " % (enemy.health, enemy.mana)
    else:
        print "Enemy's health is : %d  , enemy's mana is %d " % (player.health, player.mana)
        print "Your health is: %d , your mana is: %d " % (enemy.health, enemy.mana)
        
#Pala skill1        
def holy_strike(player, enemy, is_enemy):
    if (player.mana >= 200):
        print "Holy Strike!BOOM!A holy light comes from above, heals paladin and "
        print "strikes the enemy..."
        player.health += 300
        enemy.health -= 200
        player.mana -= 200
        print_after_skill(player, enemy, is_enemy)
    else:
        print "Insufficient mana!"      

#pala skill2
def wise_rage(player,enemy, is_enemy ):
    if (player.mana >= 300 and player.pala_rage.under_effect == False):       
        print "Wise Rage is active!Paladin fills himself with rage of wise light lord !"
        player.health -= player.health / 4
        player.x += player.x * 2
        player.y += player.y * 2
        player.mana -= 300
        player.pala_rage.under_effect = True
        print_after_skill(player, enemy, is_enemy)
    else:
        print "Insufficient mana!"     
    
#pala skill3    
def divine_protection(player, enemy, is_enemy):
    if (player.mana >= 400):    
        print "Divine Protection is active !No one can't hurt the protected ones... "
        player.untouchable.under_effect = True
        player.pala_rage.counter += 1 
        player.mana -= 400
        print_after_skill(player, enemy, is_enemy)   
    else:
        print "Insufficient mana!"       

#dh skill1
def rain_of_the_old_legion(player, enemy, is_enemy ):
    if (player.mana >= 300 and player.dh_rain.under_effect == False):
        print "Rain of the Old Legion! Fire arrows rains from sky, this grants Demon "
        print "Hunter some extra power!"
        player.x *= 2
        player.y *= 2
        enemy.health -= 250
        player.dh_rain.under_effect = True
        player.dh_rain.counter = 1
        player.mana -= 300 
        print_after_skill(player, enemy, is_enemy)
    else:
        print "Insufficient mana!"
        
#dh skill2
def tail_of_samael(player, enemy, is_enemy):
    if (player.mana >= 300):
        print "Tail of Samael! This ancient artifact from might Samael makes enemies worried..."
        player.mana -= 300
        enemy.immobilize.under_effect = True
        print_after_skill(player, enemy, is_enemy)
    else:
        print "Insufficient mana!"
        
#dh skill3
def killing_blow(player, enemy, is_enemy):
    if (player.mana >= 400):
        print "Killing Blow! Sounds like someone is gonna get killed! Big gunz are out! "  
        player.mana -= 400
        if (enemy.health <= enemy.initial_hp / 4):
            enemy.health -= enemy.initial_hp / 4
        else:
            enemy.health -= 200                     
        print_after_skill(player, enemy, is_enemy)      
    else:
        print "Insufficient mana!"
          
#sorc skill1
def dark_rituals(player, enemy, is_enemy ):
    if (player.mana >= 500 and player.dark_rits.under_effect == False):
        print "Dark Rituals! Dark magic surrounds everywhere, sickening enemies and "
        print "giving power to sorcerer..."
        player.mana -= 500
        player.health += player.health / 4
        enemy.health -= enemy.health / 4
        player.dark_rits.under_effect = True
        player.dark_rits.counter = 1
        print_after_skill(player, enemy, is_enemy)
    else:
        print "Insufficient mana!"

#sorc skill2
def sickness_of_lilith(player, enemy, is_enemy ):
    if (player.mana >= 500 and enemy.sickness_lil.under_effect == False):    
        print "Sickness of Lilith! You have no power against dark Gods !"
        player.mana -= 500
        enemy.x -= int(enemy.x / 1.5)
        enemy.y -= int(enemy.y / 1.5)
        enemy.sickness_lil.under_effect = True
        print_after_skill(player, enemy, is_enemy)
    else:
        print "Insufficient mana!"
        
#sorc skill3
def frostnova(player, enemy, is_enemy):
    if (player.mana >= 500):
        print "Frostnova ! Chill chill chill baby!!It's more than chilling :D "
        player.mana -= 500
        enemy.health -= 350
        enemy.immobilize.under_effect = True
        print_after_skill(player, enemy, is_enemy)
    else:
        print "Insufficient mana!"

#priest skill1

def pray(player, enemy, is_enemy ):
    if (player.mana >= 500 and player.pray_effect.under_effect == False):
        print "Pray! Priest prays his ancient God and grants his strentgh!"
        player.health += 1000
        player.mana -= 500
        player.pray_effect.under_effect = True
        player.pray_effect.counter = 1
        print_after_skill(player, enemy, is_enemy)
    else:
        print "Insufficient mana!"
    
#priest skill2
def healing_wounds(player, enemy, is_enemy):
    if (player.mana >= 500):
        print "Healing Wounds! Priest heals his fatal wounds and prevents diseases."
        player.health += player.health / 4
        player.mana -= 500
        print_after_skill(player, enemy, is_enemy)
    else:
        print "Insufficient mana!" 
   
#priest skill3    
def god_fist (player, enemy, is_enemy):
    if (player.mana >= 500 and player.fist_god.under_effect == False):
        print "I'm God's Fist ! ARRRRRGGGHHH! ALL ENEMIES SHOULD DIE !"
        player.health /= 2
        player.mana -= 500
        player.x += int(4 * player.x)
        player.y += int(4 * player.y)
        player.fist_god.under_effect = True
        player.fist_god.counter = 1
        print_after_skill(player, enemy, is_enemy)
    else:
        print "Insufficient mana!"

#bm skill1
def twin_blades (player, enemy, is_enemy):
    if (player.mana >= 250):
        print "Twin Blades ! Bladmaster slashes his enemy with his two blades ! Ouch !"
        enemy.health -= 300
        player.mana -= 250
        enemy.immobilize.under_effect = True
        print_after_skill(player, enemy, is_enemy)
    else:
        print "Insufficient mana!"

#bm skill2
def reaper_harvest (player, enemy, is_enemy):
    if (player.mana >= 250):
        print "Reaper's Harvest! Taste Reaper's Scythe through your heart !"
        enemy.health -= enemy.health * 0.4
        player.mana -= 250
        print_after_skill(player, enemy, is_enemy)                         
    else:
        print "Insufficient mana!"
    
#bm skill3
def our_is_the_fury (player, enemy, is_enemy):
    if (player.mana >= 250 and player.ours_fury.under_effect == False):
        print "Ours is the Fury ! ARRRRGGGHHHH, let's slay them all! "
        player.mana -= 250
        player.x = int(player.x * 1.5)
        player.y = int(player.y * 1.5)
        player.ours_fury.under_effect = True
        player.ours_fury.counter = 1
        print_after_skill(player, enemy, is_enemy)
    else:
        print "Insufficient mana!"
        
#wizard skill1
def fireball(player, enemy, is_enemy):
    if (player.mana >= 500):
        print "Fireball! Fireballs are sexy to hurl  enemies !"
        player.mana -= 500
        enemy.health -= 400
        print_after_skill(player, enemy, is_enemy)    
    else:
        print "Insufficient mana!"

#wizard skill2
def fire_shield (player, enemy, is_enemy):
    if (player.mana >= 500):  
        print "Fire Shield ! You had better watch out the wizard when he has" 
        print "his fucking fire shield..."       
        player.mana -= 500
        player.untouchable.under_effect = True
        print_after_skill(player, enemy, is_enemy)
    else:
        print "Insufficient mana!"
        
#wizard skill3
def polymorph(player, enemy, is_enemy):
    if (player.mana >= 500):   
        print "Polymorphism ! Who's that sheep looking to me, HAHAHAHA! "
        enemy.immobilize.under_effect = True
        player.mana -= 500
        print_after_skill(player, enemy, is_enemy)    
    else:
        print "Insufficient mana!"  
    
