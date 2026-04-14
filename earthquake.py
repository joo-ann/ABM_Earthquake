import random
import math

'''
Here, we declare three variables that go into a building: location (city), struct (structural integrity/resistance to earthquakes), and wear (how worn down/old the building is).
For city, I append an emoji for every slot in a 10x10 grid. For struct, I scale it from 0 to 1. For wear, everything starts as 1.
'''

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


'''
Here, I define the earthquake() function, which essentially takes into account the structural integrity and wear of the building in relation to magnitude and distance from epicenter to calculate overall damage.

For distance, I used an inverse function (1/x), where the best possible distance is near 0 (i.e. 1/200), and the worst possible distance is 1 (1/1)/
For structural integrity, I subtracted the struct score from 1 to calculate the percentage of damage dealt.
I took both of those and multiplied them by the magnitude, then subtracted that from the wear to calculate whether or not the building is still standing.
'''

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


'''
Here, we simulate earthquake occurences over the course of 10 days, where the chance of an earthquake in this case is 30% (very high, insurance must cost a lot). 
Every loop, we check to see if there is an earthquake, then output the magnitude, epicenter, and the remaining buildings
'''

days = 10
e_chance = 0.3
for i in range(days):
    x = random.randint(1, 100)/100
    if x < e_chance:
        print('- - - - - - - - - - EMERGENCY: EARTHQUAKE - - - - - - - - - -')
        earthquake()
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')

