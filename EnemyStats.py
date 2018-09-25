import random
import winsound
import time


def ogre_low_level(chealth, cdefense, cgold, cstrength, cexp, cweapon, cname, clevel):
    name = 'ogre'
    health = 50
    strength = 15
    defense = 2
    gold = random.randrange(10, 20)
    level = clevel
    exp = 100 #random.randrange(10, 20)
    print('You have encountered an', name, 'with', health, ' health !!!')
    chealth, cdefense, cexp, cstrength, cgold, clevel = fight(health, chealth, name, strength, cdefense, cweapon, defense, exp, gold, clevel,
          cexp, cstrength, cgold)

    return chealth, cdefense, cgold, cstrength, cexp, clevel


    #elif weapon == 'sword':



    #elif weapon == 'axe'
    #print(health, strength, defense, gold)



def ogre_mid_level(self):
        health = 85
        strength = 35
        defense = 12
        gold = random.randrange(20, 50)

def ogre_high_level(self):
        health = 180
        strength = 55
        defense = 25
        gold = random.randrange(50, 80)

def ogre_king(self):
        health = 280
        strength = 80
        defense = 25
        gold = random.randrange(100, 150)


def fight(health, chealth, name, strength, cdefense, cweapon, defense, exp, gold, clevel,
          cexp, cstrength, cgold):
    # setting up hp to fight variable so it doesnt change actually hp
    fight_health = chealth
    if cweapon == 'bow':
        enemy_attack = ['Hit', 'Miss', 'Hit', 'Miss', 'Hit']
        chac_attack = ['Hit', 'Miss', 'Hit', 'Hit', 'Hit', 'Miss', 'Miss', 'Hit']
        while health > 0 and chealth > 0:
            # critical chances
            enemy_crit = random.randrange(1, 25)
            chac_crit = random.randrange(1, 20)
            enemy_result = random.choice(enemy_attack)
            player_result = random.choice(chac_attack)
            if enemy_result == 'Hit':
                print('The', name, 'hit you!!')
                time.sleep(.5)
                if enemy_crit == 5:
                    strength *= 1.5
                    print('The', name, 'crit you')
                attack_strength = random.uniform((strength+5)-strength, strength)
                damage = attack_strength - cdefense
                if damage > 0:
                    print('The', name, 'did', round(damage), 'damage!!')
                    time.sleep(.5)
                    fight_health -= damage
                    print('You have', round(fight_health), 'health')
                    choice = input('Do you want to punch or use your ' + str(cweapon) + '?:')
                    time.sleep(.5)
                    while choice not in [cweapon, 'punch']:
                        choice = input('You can only punch or use: ' + cweapon + ': ')
                        time.sleep(.5)
                    if choice == cweapon:
                        if player_result == 'Hit':
                            if chac_crit == 7:
                                cstrength *=1.5
                                print('You crit the', name)
                            damage = cstrength - defense
                            if damage > 0:
                                print('You hit the ogre and did', round(damage), 'damage')
                                time.sleep(.5)
                                health -= damage
                                print('The ogre has', round(health), 'health\n\n')
                                time.sleep(.5)
                            else:
                                print('You did no damage.\n\n')
                                time.sleep(.5)
                        else:
                            print('You missed!\n\n')
                    elif choice == 'punch':
                        if player_result == 'Hit':
                            if chac_crit == 7:
                                cstrength *= 1.5
                                print('You crit the', name)
                                time.sleep(.5)
                            damage = (cstrength - 1) - defense
                            if damage > 0:
                                print('You hit the ogre with', choice, 'and did', round(damage), 'damage')
                                time.sleep(.5)
                                health -= damage
                                print('The ogre has', round(health), 'health\n\n')
                            else:
                                print('You did no damage.\n\n')
                                time.sleep(.5)
                        else:
                            print('You missed!\n\n')
                else:
                    print('It did no damage!\n\n')
                    choice = input('Do you want to punch or use your ' + str(cweapon) + '?:')
                    time.sleep(.5)
                    while choice not in [cweapon, 'punch']:
                        choice = input('You can only punch or use: ' + cweapon + ': ')
                        time.sleep(.5)
                    if choice == cweapon:
                        if player_result == 'Hit':
                            if chac_crit == 7:
                                cstrength *= 1.5
                                print('You crit the', name)
                            damage = cstrength - defense
                            if damage > 0:
                                print('You hit the ogre and did', round(damage), 'damage')
                                time.sleep(.5)
                                health -= damage
                                print('The ogre has', round(health), 'health\n\n')
                                time.sleep(.5)
                            else:
                                print('You did no damage.\n\n')
                                time.sleep(.5)
                        else:
                            print('You missed!\n\n')
                    elif choice == 'punch':
                        if player_result == 'Hit':
                            if chac_crit == 7:
                                cstrength *= 1.5
                                print('You crit the', name)
                                time.sleep(.5)
                            damage = (cstrength - 1) - defense
                            if damage > 0:
                                print('You hit the ogre with', choice, 'and did', round(damage), 'damage')
                                time.sleep(.5)
                                health -= damage
                                print('The ogre has', round(health), 'health\n\n')
                            else:
                                print('You did no damage.\n\n')
                                time.sleep(.5)
                        else:
                            print('You missed!\n\n')
            else:
                print('The', name, 'missed!')
                choice = input('Do you want to punch or use your ' + str(cweapon) + '?:')
                while choice not in [cweapon, 'punch']:
                    choice = input('You can only punch or use the ' + cweapon + ' :')
                    time.sleep(.5)
                if choice == cweapon:
                    if player_result == 'Hit':
                        if chac_crit == 7:
                            cstrength *= 1.5
                            print('You crit the', name)
                            time.sleep(.5)
                        damage = cstrength - defense
                        if damage > 0:
                            print('You hit the ogre and did', round(damage), 'damage')
                            time.sleep(.5)
                            health -= damage
                            print('The ogre has', round(health), 'health\n\n')
                        else:
                            print('You did no damage.\n\n')
                            time.sleep(.5)
                    else:
                        print('You missed!\n\n')
                elif choice == 'punch':
                    if player_result == 'Hit':
                        if chac_crit == 7:
                            cstrength *= 1.5
                            print('You crit the', name)
                            time.sleep(.5)
                        damage = (cstrength - 1) - defense
                        if damage > 0:
                            print('You hit the ogre with', choice, 'and did', round(damage), 'damage')
                            health -= damage
                            print('The ogre has', round(health), 'health\n\n')
                            time.sleep(.5)
                        else:
                            print('You did no damage.\n\n')
                            time.sleep(.5)
                    else:
                        print('You missed!\n\n')
        if health > 0 and chealth <= 0:
            print('You have died.....',time.sleep(.5),'\nReturning Home')
            time.sleep(.5)
        else:

            print('You have won!')
            time.sleep(1.5)
            print('You have earned', gold, 'gold and', exp, 'exp')
            time.sleep(1)
            cexp += exp
            cgold += gold
            if clevel == 1 and exp >= 100:
                clevel += 1
                chealth *= 1.2
                cstrength *= 1.2
                cdefense *= 1.2
                chealth = round(chealth)
                cdefense = round(cdefense)
                cstrength = round(cstrength)
                # alert for level up
                duration = 200  # millisecond
                freq = 500  # Hz
                counter = 1
                print('You are now level', clevel, '!!')
                print(' Health-->', chealth, '\n','Strength-->', cstrength, '\n','Defense-->', cdefense)
                while counter <= 3:
                    winsound.Beep(freq, duration)
                    counter += 1

        print('Health:',chealth)
        print('Defense:',cdefense)
        print('Exp:',cexp)
        print('Strength:',cstrength)
        print('Gold:',cgold)
        print('Level:',clevel)
        return chealth, cdefense, cexp, cstrength, cgold, clevel
            #return cexp, cgold, chealth,cstrength,cdefense

