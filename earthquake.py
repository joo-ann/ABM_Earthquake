import random
import math

city = []
struct = []
wear = []

for i in range(10):
    temp1 = []
    temp2 = []
    temp3 = []

    for j in range(10):
        temp1.append('🏢')
        x = random.randint(1, 100)
        temp2.append(x/100)
        temp3.append(1)

    city.append(temp1)
    struct.append(temp2)
    wear.append(temp3)


def earthquake():
    epicenter1, epicenter2 = random.randint(0, 9), random.randint(0, 9)
    magnitude = random.randint(1, 8)
    
    print('MAGNITUDE:', magnitude)
    print(f'EPICENTER: [{epicenter1}, {epicenter2}]')

    for i in range(len(city)):
        for j in range(len(city)):
            if i == epicenter1 and j == epicenter2:
                damage = (1-struct[i][j])*(magnitude)
                wear[i][j] = wear[i][j] - damage

            else:
                distance = math.sqrt((i-epicenter1)**2 + (j - epicenter2)**2)
                damage = (1/distance)*(1-struct[i][j])*(magnitude)
                wear[i][j] = wear[i][j] - damage

                

    for i in range(len(wear)):
        for j in range(len(wear)):
            if wear[i][j] <= 0:
                wear[i][j] = 0
                city[i][j] = '🪦'
                struct[i][j] = 0            

    print(*city, sep='\n')


earthquake()

days = 10
e_chance = 0.3
for i in range(days):
    x = random.randint(1, 100)/100
    if x < e_chance:
        print('- - - - - - - - - - EMERGENCY: EARTHQUAKE - - - - - - - - - -')

        earthquake()
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')

