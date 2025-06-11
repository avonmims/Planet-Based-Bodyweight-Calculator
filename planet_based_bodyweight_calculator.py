import pandas as pd

# Input takes place in the terminal.

x = int(input("Enter weight (number only): "))

def weight_planet():

    mercury = round(x * 0.378, 3)
    
    venus = round(x * 0.903, 3)
    
    earth = round(x * 1.000, 3)
    moon = round(x * 0.165, 3)
    
    mars = round(x * 0.380, 3)
    
    jupiter = round(x * 2.640, 3)
    io = round(x * 0.183, 3)
    europe = round(x * 0.134, 3)
    ganymede = round(x * 0.146, 3)
    callisto = round(x * 0.1259, 3)
    
    saturn = round(x * 1.140, 3)
    titan = round(x * 0.138, 3)
    iapetus = round(x * 0.022, 3)
    mimas = round(x * 0.006, 3)
    enceladus = round(x * 0.011, 3)
    tethys = round(x * 0.015, 3)
    dione = round(x * 0.024, 3)
    rhea = round(x * 0.027, 3)
    
    uranus = round(x * 0.918, 3)
    miranda = round(x * 0.008, 3)
    ariel = round(x * 0.028, 3)
    umbriel = round(x * 0.023, 3)
    titania = round(x * 0.040, 3)
    oberon = round(x * 0.036, 3)

    neptune = round(x * 1.150, 3)
    triton = round(x * 0.080, 3)
    
    pluto = round(x * 0.063, 3)
    charon = round(x * 0.029, 3)

    results = pd.DataFrame({
        'Planet' : ['Mercury', 'Venus', 'Earth', 'Earth', 'Mars', 'Jupiter',
                    'Jupiter', 'Jupiter', 'Jupiter', 'Jupiter','Saturn',
                    'Saturn', 'Saturn', 'Saturn', 'Saturn', 'Saturn',
                    'Saturn', 'Saturn', 'Uranus', 'Uranus', 'Uranus',
                    'Uranus', 'Uranus', 'Uranus','Neptune', 'Neptune',
                    'Pluto', 'Pluto'],
        'Celestial Body': ['Mercury', 'Venus', 'Earth', 'Moon', 'Mars',
                           'Jupiter', 'Io', 'Europa', 'Ganymede', 'Callisto',
                           'Saturn', 'Titan', 'Iapetus', 'Mimas', 'Enceladus',
                           'Tethys', 'Dione', 'Rhea',
                           'Uranus', 'Miranda', 'Ariel', 'Umbriel',
                           'Titania', 'Oberon',
                           'Neptune', 'Triton',
                           'Pluto', 'Charon'],
        'Weight': [mercury, venus, earth, moon, mars,
                   jupiter, io, europe, ganymede, callisto,
                   saturn, titan, iapetus, mimas, enceladus,
                   tethys, dione, rhea,
                   uranus, miranda, ariel, umbriel,
                   titania, oberon,
                   neptune, triton,
                   pluto, charon],
    })

    print(results)
    
weight_planet()

# This script calculates the weight of a person on different celestial
# bodies in our solar system, using Eath's gravity as a reference.