from Stats import health
from Stats import defense
from Stats import gold
from Stats import strength
from Stats import exp
from Stats import level
from Character import username
from Character import weapon
import pickle
from Character import load
from EnemyStats import *

save_file = input('Do you have a save file...yes/no: ')
if save_file == 'yes':
    save = load()
    character_name = save[6]
    print('Hello', character_name, ', welcome back, here are your stats.')
    time.sleep(.4)
    character_weapon = save[7]
    print('Weapon: ', character_weapon)
    time.sleep(.4)
    chac_health = save[0]
    print('Health: ', chac_health)
    time.sleep(.4)
    chac_defense = save[1]
    print('Defense: ', chac_defense)
    time.sleep(.4)
    chac_strength = save[2]
    print('Strength: ', chac_strength)
    time.sleep(.4)
    chac_gold = save[3]
    print('Gold: ', chac_gold)
    time.sleep(.4)
    chac_exp = save[4]
    print('Exp: ', chac_exp)
    time.sleep(.4)
    chac_lvl = save[5]
    print('Level: ', chac_lvl)
    time.sleep(.4)

else:
    name_one = (input('Enter username no longer than 8 characters: '))
    while len(name_one) > 8:
        print('Too many characters, try again')
        name_one = (input('Enter username no longer than 8 characters: '))

    weapon_one = input('Pick your weapon, sword, axe, bow: ')
    while weapon_one not in ['axe', 'sword', 'bow']:
        print("You didn't enter a weapon or spelled it wrong try again")
        weapon_one = (input('Pick your weapon, sword, axe, bow: '))

    character_name = username(name_one)
    character_weapon = weapon(weapon_one)
    weapon = character_weapon
    name = character_name
    ## printing stats and character names
    print('*', character_name, 'picked up the ', character_weapon, '*')
    time.sleep(2)
    stat_1 = health()
    chac_health = stat_1
    print('Health:', chac_health)
    time.sleep(1)
    stat_2 = defense()
    chac_defense = stat_2
    print('Defense:', chac_defense)
    time.sleep(1)
    stat_3 = strength()
    chac_strength = stat_3
    print('Strength:', chac_strength)
    time.sleep(1)
    stat_4 = gold()
    chac_gold = stat_4
    print('Gold:', chac_gold)
    time.sleep(1)
    stat_5 = exp()
    chac_exp = stat_5
    print('Exp:', chac_exp)
    time.sleep(1)
    stat_6 = level()
    chac_lvl = stat_6
    print('Level', chac_lvl)
    time.sleep(1)
print('Lets test out your fighting skills')
time.sleep(1)
chac_health, chac_defense, chac_exp, chac_strength, chac_gold, chac_lvl = ogre_low_level(chac_health, chac_defense,
                chac_gold, chac_strength, chac_exp, character_weapon, character_name, chac_lvl)
print('Hey you got some exp!! Leveling up increases your health and others stats!')
time.sleep(.5)
save_question = input('Do you want to save? yes/no : ')
if save_question == 'yes':
    save = []
    save.append(chac_health)
    save.append(chac_defense)
    save.append(chac_strength)
    save.append(chac_gold)
    save.append(chac_exp)
    save.append(chac_lvl)
    save.append(character_name)
    save.append(character_weapon)
    with open('save.pkl', 'wb') as f:
        pickle.dump(save, f)
    print('Saving')
    time.sleep(.4)
    print('.')
    time.sleep(.4)
    print('.')
    time.sleep(.4)
    print('.')
    time.sleep(.4)
    print('DONE!')





