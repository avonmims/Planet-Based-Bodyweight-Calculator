# Input takes place in the terminal.

x = int(input("Enter weight (number only): "))

def weight_planet():

    mercury = x * 0.378
    
    venus = x * 0.903
    
    earth = x * 1.0
    moon = x * 0.165
    
    mars = x * 0.380
    
    jupiter = x * 2.640
    io = x * 0.183
    europe = x * 0.134
    ganymede = x * 0.146
    callisto = x * 0.1259
    
    saturn = x * 1.140
    titan = x * 0.138
    iapetus = x * 0.022
    mimas = x * 0.006
    enceladus = x * 0.011
    tethys = x * 0.015
    dione = x * 0.024
    rhea = x * 0.027
    
    uranus = x * 0.918
    
    neptune = x * 1.15
    
    pluto = x * .063

    print(f'Your weight on each planet:''\n',
          f'Mercury: {mercury}''\n',
          f'Venus: {venus}''\n',
          f'Earth: {earth}''\n',
          f'Mars: {mars}''\n',
          f'Jupiter: {jupiter}''\n',
          f'Saturn: {saturn}''\n',
          f'Uranus: {uranus}''\n',
          f'Neptune: {neptune}''\n',
          f'Pluto: {pluto}'
          )
    
weight_planet()

# This script calculates the weight of a person on different celestial
# bodies in our solar system, using Eath's gravity as a reference.