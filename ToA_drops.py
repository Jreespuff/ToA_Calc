import random
dice = 0
unique = 0
times = 0
shadow = 0

while dice != 1:
    dice = random.randint(1,10)
    times += 1

    if dice == 1:
        while unique != 24:
            unique == random.randint(1,24)
            if unique == 24:
                break
            else:
                shadow +=1
        unique = 0



print('It took ' + str(times) + ' raids to get a purple.')
print('It took ' + str(shadow) + ' times to get a shadow.')






    