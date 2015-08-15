#script name: game.py
#author: Umut Orman
#created: 14th August 2015
#version: 1.0
#description: game engine script for duel based python game
from sys import exit
from random import randint
from chars import *
from skills import *
from effects import *

def Engine():

    #welcoming introduction and guide for character selection
    print """"Welcome Might & Magic Duel game. In this game you will fight with your opponent in
    a turn based duel engine.There are 6 characters currently you can pick.
    1. Paladin
    2. Demon Hunter
    3. Sorcerer
    4. Priest
    5. BladeMaster
    6. Wizard
    Choose wisely your character and kick your enemies' asses! May the force be with you !
"""

    #Character choosing mechanism
    pala_pala_rage = Effect(False, 0, 3)
    pala_untouchable = Effect (False, 0,  2)
    pala_dh_rain = Effect (False, 0, 3)
    pala_immobilize = Effect (False, 0, 2)
    pala_dark_rits = Effect(False, 0, 3)
    pala_sickness_lil = Effect (False, 0, 2)
    pala_pray_effect = Effect (False, 0, 3) 
    pala_fist_god = Effect (False, 0, 3)
    pala_ours_fury = Effect (False, 0, 2)
    
    dh_pala_rage = Effect(False, 0, 3)
    dh_untouchable = Effect (False, 0,  2)
    dh_dh_rain = Effect (False, 0, 3)
    dh_immobilize = Effect (False, 0, 2)
    dh_dark_rits = Effect(False, 0, 3)
    dh_sickness_lil = Effect (False, 0, 2)
    dh_pray_effect = Effect (False, 0, 3) 
    dh_fist_god = Effect (False, 0, 3)
    dh_ours_fury = Effect (False, 0, 2)
    
    sorc_pala_rage = Effect(False, 0, 3)
    sorc_untouchable = Effect (False, 0,  2)
    sorc_dh_rain = Effect (False, 0, 3)
    sorc_immobilize = Effect (False, 0, 2)
    sorc_dark_rits = Effect(False, 0, 3)
    sorc_sickness_lil = Effect (False, 0, 2)
    sorc_pray_effect = Effect (False, 0, 3) 
    sorc_fist_god = Effect (False, 0, 3)
    sorc_ours_fury = Effect (False, 0, 2)
    
    priest_pala_rage = Effect(False, 0, 3)
    priest_untouchable = Effect (False, 0,  2)
    priest_dh_rain = Effect (False, 0, 3)
    priest_immobilize = Effect (False, 0, 2)
    priest_dark_rits = Effect(False, 0, 3)
    priest_sickness_lil = Effect (False, 0, 2)
    priest_pray_effect = Effect (False, 0, 3) 
    priest_fist_god = Effect (False, 0, 3)
    priest_ours_fury = Effect (False, 0, 2)
    
    bm_pala_rage = Effect(False, 0, 3)
    bm_untouchable = Effect (False, 0,  2)
    bm_dh_rain = Effect (False, 0, 3)
    bm_immobilize = Effect (False, 0, 2)
    bm_dark_rits = Effect(False, 0, 3)
    bm_sickness_lil = Effect (False, 0, 2)
    bm_pray_effect = Effect (False, 0, 3) 
    bm_fist_god = Effect (False, 0, 3)
    bm_ours_fury = Effect (False, 0, 2)
    
    wizard_pala_rage = Effect(False, 0, 3)
    wizard_untouchable = Effect (False, 0,  2)
    wizard_dh_rain = Effect (False, 0, 3)
    wizard_immobilize = Effect (False, 0, 2)
    wizard_dark_rits = Effect(False, 0, 3)
    wizard_sickness_lil = Effect (False, 0, 2)
    wizard_pray_effect = Effect (False, 0, 3) 
    wizard_fist_god = Effect (False, 0, 3)
    wizard_ours_fury = Effect (False, 0, 2)
    
    pala = Paladin(2500, 1000, 1, 81, 101, pala_pala_rage , pala_untouchable, pala_dh_rain, pala_immobilize,  pala_dark_rits, pala_sickness_lil , pala_pray_effect, pala_fist_god, pala_ours_fury, 2500) 
    dh = DemonHunter(1500, 1000, 1, 112, 262 , dh_pala_rage ,dh_untouchable, dh_dh_rain, dh_immobilize,  dh_dark_rits, dh_sickness_lil , dh_pray_effect, dh_fist_god, dh_ours_fury, 1500)
    sorc = Sorcerer(1000, 2500, 1, 50, 147 , sorc_pala_rage ,sorc_untouchable, sorc_dh_rain, sorc_immobilize,  sorc_dark_rits, sorc_sickness_lil , sorc_pray_effect, sorc_fist_god, sorc_ours_fury, 1000)
    priest = Priest(1250, 2000, 1, 65, 117 , priest_pala_rage ,priest_untouchable, priest_dh_rain, priest_immobilize,  priest_dark_rits, priest_sickness_lil , priest_pray_effect, priest_fist_god, priest_ours_fury, 1250)
    bm = BladeMaster(1750, 750, 1, 135, 232 , bm_pala_rage ,bm_untouchable, bm_dh_rain, bm_immobilize,  bm_dark_rits, bm_sickness_lil , bm_pray_effect, bm_fist_god, bm_ours_fury, 1750)
    wizard = Wizard(1000 , 2500 , 1, 87 , 189 , wizard_pala_rage ,wizard_untouchable, wizard_dh_rain, wizard_immobilize,  wizard_dark_rits, wizard_sickness_lil , wizard_pray_effect, wizard_fist_god, wizard_ours_fury, 1000)
    characters = { 'wizard' : wizard ,
                   'blademaster': bm ,   
                   'priest' : priest ,
                   'paladin': pala ,
                   'demon hunter': dh ,
                   'sorcerer': sorc ,
                 }
    print "Pick your fighter now !"                 
    my_char_name = raw_input("> ")
    print "You chose %s !" % my_char_name                  
    my_char = characters.get(my_char_name)
    if (my_char == None):
        print "What an idiot you are !"
        exit(1)
    my_char.info()
    enemy_options = ['wizard',
                     'blademaster',
                     'priest',
                     'paladin',
                     'demon hunter',
                     'sorcerer' 
     ] 
    enemy_options.pop(enemy_options.index(my_char_name))
    enemy_no = randint(0, 4)
    enemy_char_name = enemy_options[enemy_no]
    print "Your opponent is %s !" % enemy_char_name
    enemy_char = characters.get(enemy_char_name)
    enemy_char.info()
    print "Let the fight begin Gods !"
    duel(my_char, enemy_char)
    
def duel(char1, char2):
    #decide who will have the first turn
    first_turn = randint(1, 10)
    player, cpu = False, False
    skill_used = False 
    if ( 6 > first_turn > 1):
        player = True
    else:
        cpu = True
    #while loop for turn based fighting till someone gets died
    while (char1.health > 0 and char2.health > 0):
        
        #while loop for player for single turn
        while ( player == True  and cpu == False ):
        
            if (char1.pala_rage.under_effect == True ):
                if (char1.pala_rage.counter == char1.pala_rage.effect_time):
                    char1.pala_rage.counter = 0
                    char1.pala_rage.under_effect = False
                    char1.x = char1.x / 135 * 100
                    char1.y = char1.y / 135 * 100
                else:
                    char1.pala_rage.counter += 1
                    
            if (char2.untouchable.under_effect == True):
                if (char2.untouchable.counter == char2.untouchable.effect_time):
                    char2.untouchable.counter = 0
                    char2.untouchable.under_effect = False
                else:
                    char2.untouchable.counter += 1
                    print "Enemy is protected by forces ! Can't touch this!"
                    player = False
                    cpu = True
                    break
                    
            if (char1.dh_rain.under_effect == True ):
                if (char1.dh_rain.counter == char1.dh_rain.effect_time):
                    char1.dh_rain.counter = 0
                    char1.dh_rain.under_effect = False
                    char1.x = char1.x / 125 * 100
                    char1.y = char1.y / 125 * 100
                else:
                    char1.dh_rain.counter += 1
            
            if (char1.immobilize.under_effect == True):
                if (char1.immobilize.counter == char1.immobilize.effect_time):
                    char1.immobilize.counter = 0
                    char1.immobilize.under_effect = False
                else:
                    char1.immobilize.counter += 1
                    print "You can't do any shit, hahaha !"
                    player = False
                    cpu = True
                    break
                    
            if (char1.dark_rits.under_effect == True):
                if (char1.dark_rits.counter == char1.dark_rits.effect_time):
                    char1.dark_rits.counter = 0
                    char1.dark_rits.under_effect = False
                    char1.health -= char1.health / 5 
                    char2.health += char2.health / 3
                else:
                    char1.dark_rits.counter += 1
            
            if (char1.sickness_lil.under_effect == True):
                if (char1.sickness_lil.counter == char1.sickness_lil.effect_time):
                    char1.sickness_lil.counter = 0
                    char1.sickness_lil.under_effect = False
                    char1.x *= 2
                    char1.y *= 2
                else:
                    char2.sickness_lil.counter += 1
         
            if (char1.pray_effect.under_effect == True):
                if (char1.pray_effect.counter == char1.pray_effect.effect_time):
                    char1.pray_effect.counter = 0
                    char1.pray_effect.under_effect = False
                    char1.health -= 1000
                else:
                    char1.pray_effect.counter += 1                  
             
            if (char1.fist_god.under_effect == True):
                if (char1.fist_god.counter == char1.fist_god.effect_time):
                    char1.fist_god.counter = 0
                    char1.fist_god.under_effect = False
                    char1.x /= 4
                    char1.y /= 4
                else:
                    char1.fist_god.counter += 1
                    
            if (char1.ours_fury.under_effect == True):
                if(char1.ours_fury.counter == char1.ours_fury.effect_time):
                    char1.ours_fury.counter = 0
                    char1.ours_fury.under_effect = False
                    char1.x = 2 / 3 * char1.x
                    char1.y = 2 / 3 * char1.y
                else:
                    char1.ours_fury.counter += 1                                                                                     
                                 
            print "It's your turn now !"
            move = raw_input("> ")
            if ( move == 'attack' ):
                char1.attack(char2, False)
                print_after_skill(char1, char2, False)
                player = False
                cpu = True
                if (char2.health <= 0):
                    print "Congratulations! You win !"
                    exit(1)
                elif (char1.health <= 0):
                    print "You lost! Did you die with your honour?"
                    exit(1)
                break
          
            elif ( move == '1' ):
                if (skill_used == False):
                    char1.firstskill(char2, False)
                    skill_used = True
                else:
                    print "What a bitch, you already used your skill on this turn!" 
                           
            elif ( move == '2'):
                if (skill_used == False):
                    char1.secondskill(char2, False)
                    skill_used = True
                else:
                    print "What a bitch, you already used your skill on this turn!"      
                      
            elif ( move == '3'):
                if (skill_used == False):
                    char1.thirdskill(char2, False)
                    skill_used = True
                else:
                    print "What a bitch, you already used your skill on this turn!"
                
            else: 
                print "That move is not valid at all bastard!"
                
        #check if someone is  already got wounded badly
            if (char2.health <= 0):
                print "Congratulations! You win !"
                exit(1)
            elif (char1.health <= 0):
                print "You lost! Did you die with your honour?"
                exit(1)
        
        
        #while loop for cpu        
        while (player == False and cpu == True ):
        
            if (char2.pala_rage.under_effect == True ):
                if (char2.pala_rage.counter == char2.pala_rage.effect_time):
                    char2.pala_rage.counter = 0
                    char2.pala_rage.under_effect = False
                    char2.x = char2.x / 135 * 100
                    char2.y = char2.y / 135 * 100
                else:
                    char2.pala_rage.counter += 1
                    
            if (char1.untouchable.under_effect == True):
                if (char1.untouchable.counter == char1.untouchable.effect_time):
                    char1.untouchable.counter = 0
                    char1.untouchable.under_effect = False
                else:
                    char1.untouchable.counter += 1
                    print "You are protected by forces ! Enemy Can't touch this!"
                    player = True
                    cpu = False
                    break
                    
            if (char2.dh_rain.under_effect == True ):
                if (char2.dh_rain.counter == char2.dh_rain.effect_time):
                    char2.dh_rain.counter = 0
                    char2.dh_rain.under_effect = False
                    char2.x = char2.x / 125 * 100
                    char2.y = char2.y / 125 * 100
                else:
                    char2.dh_rain.counter += 1
            
            if (char2.immobilize.under_effect == True):
                if (char2.immobilize.counter == char2.immobilize.effect_time):
                    char2.immobilize.counter = 0
                    char2.immobilize.under_effect = False
                else:
                    char2.immobilize.counter += 1
                    print "Enemy can't do any shit to you, hahaha ! "
                    player = True
                    cpu = False
                    break
                    
            if (char2.dark_rits.under_effect == True):
                if (char2.dark_rits.counter == char1.dark_rits.effect_time):
                    char2.dark_rits.counter = 0
                    char2.dark_rits.under_effect = False
                    char2.health -= char1.health / 5 
                    char1.health += char2.health / 3
                else:
                    char2.dark_rits.counter += 1
            
            if (char2.sickness_lil.under_effect == True):
                if (char2.sickness_lil.counter == char2.sickness_lil.effect_time):
                    char2.sickness_lil.counter = 0
                    char2.sickness_lil.under_effect = False
                    char2.x *= 2
                    char2.y *= 2
                else:
                    char2.sickness_lil.counter += 1
         
            if (char2.pray_effect.under_effect == True):
                if (char2.pray_effect.counter == char2.pray_effect.effect_time):
                    char2.pray_effect.counter = 0
                    char2.pray_effect.under_effect = False
                    char2.health -= 1000
                else:
                    char2.pray_effect.counter += 1                  
             
            if (char2.fist_god.under_effect == True):
                if (char2.fist_god.counter == char2.fist_god.effect_time):
                    char2.fist_god.counter = 0
                    char2.fist_god.under_effect = False
                    char2.x /= 4
                    char2.y /= 4
                else:
                    char2.fist_god.counter += 1
                    
            if (char2.ours_fury.under_effect == True):
                if(char2.ours_fury.counter == char2.ours_fury.effect_time):
                    char2.ours_fury.counter = 0
                    char2.ours_fury.under_effect = False
                    char2.x = 2 / 3 * char2.x
                    char2.y = 2 / 3 * char2.y
                else:
                    char2.ours_fury.counter += 1 
        
            move = randint(1, 3)
            if (move == 1 ):
                char2.firstskill(char1, True)
            elif (move == 2):
                char2.secondskill(char1, True)
            elif(move == 3):
                char2.thirdskill(char1, True)
            char2.attack(char1, True)
            print_after_skill(char2, char1, True)
            cpu = False
            player = True
            
            skill_used = False         
                 
            if (char2.health <= 0):
                print "Congratulations! You win !"
                exit(1)
            elif (char1.health <= 0):
                print "You lost motherfucker, next time work harder! "
                exit(1)
            
Engine()            
