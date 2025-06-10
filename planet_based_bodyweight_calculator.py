# Input takes place in the terminal.

x = int(input("Enter weight (kg or lb): "))

def weight_planet():

    mercury = x * 0.378
    venus = x * 0.903
    earth = x * 1.0
    mars = x * 0.380
    jupiter = x * 2.640
    saturn = x * 1.140
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

# This script calculates the weight of a person on different planets using Eath's gravity as a reference.