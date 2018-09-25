import pickle
def username(name):
    print('Hello', name, ',welcome to games name now!\n\n')
    return name


def weapon(starting_weapon):
    if starting_weapon == 'axe':
        print('You have chosen the axe')
    elif starting_weapon == 'sword':
            print('you have chosen sword')
    elif starting_weapon == 'bow':
        print('you have chosen bow')
    print('Now to begin.')
    return starting_weapon


def save(health, defense, strength, gold, exp, level, name, weapon):
    #save.append(health)
    #save.append(defense)
    #save.append(strength)
    #save.append(gold)
    #save.append(exp)
    #save.append(level)
    #save.append(name)
    #save.append(weapon)
    with open('save.pkl', 'wb') as f:
        pickle.dump([health, defense, strength, gold, exp, level, name, weapon], f)



def load():
    with open('save.pkl', 'rb') as f:
        save_test = pickle.load(f)
        health = save_test[0]
        defense = save_test[1]
        strength = save_test[2]
        gold = save_test[3]
        exp = save_test[4]
        level = save_test[5]
        name = save_test[6]
        weapon = save_test[7]
        return health, defense, strength, gold, exp, level, name, weapon