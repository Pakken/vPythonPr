from vpython import *
import json

def main():
    t=0
    planets = {}
    moons = {}
    
    with open('com_planets') as planet_data:
        for i in json.loads(planet_data.read()).items():
            planets.update(
                {i[0] : sphere(
                    pos = vec(0,0,0),
                    radius = float(i[1]['diameter'])/2,
                    mass = float(i[1]['mass']),
                    orbita = float(i[1]['orb_rad']),
                    period = 1/float(i[1]['period']),
                    moons = eval(i[1]['moons']),
                    color = eval(i[1]['color']),
                    make_trail =True,
                    retain = 150
                    )})
    with open('com_moons') as moon_data:
        for i in json.loads(moon_data.read()).items():
            moons.update(
                {i[0]: sphere(
                    pos = vec(0,0,0),
                    radius = float(i[1]['diameter'])/2,
                    mass = float(i[1]['mass']),
                    orbita = float(i[1]['orb_rad']),
                    period = 1/float(i[1]['period']),
                    color = eval(i[1]['color']),
                    make_trail =True,
                    retain = 160
                    )})
            
    while True:
        scene.camera.follow(planets['jupiter'])
        t += 0.01
        rate(30)
        for i in planets.values():
            i.pos = vec(
                i.orbita*cos(i.period*t),
                i.orbita*sin(i.period*t),
                0)
            for j in i.moons:
                moons[j].pos = vec(
                    i.orbita*cos(i.period*t) + moons[j].orbita*cos(moons[j].period*t),
                    i.orbita*sin(i.period*t) + moons[j].orbita*sin(moons[j].period*t),
                    0)

if __name__ == '__main__':
    main()
