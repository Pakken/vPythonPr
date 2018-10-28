from vpython import *

def create_obj():
    planets = {
        'sun' : {
            'radius' : 10/2,
            'volume' : 1303781,
            'mass' : 100,
            'color' : color.yellow},
        'planet1' : {
            'radius' : 2/2,
            'volume' : 0.0562,
            'mass' : 10,
            'color' : color.green},
        'planet2' : {
            'radius' : 1/2,
            'volume' : 0.0562,
            'mass' : 15,
            'color' : color.blue}
        }

    for i in planets.items():
        sky_bodies.update({i[0] :
                           sphere(
                               pos = vec(0,0,0),
                               radius = i[1]['radius'],
                               color = i[1]['color'])})

def main():
    global sky_bodies
    sky_bodies = {}

    create_obj()

    for i in sky_bodies:
            print(i)
                      
    t = 0
    sky_bodies['sun'].pos = vec(0,0,0)
    
    while True:
        t += 0.01
        rate(24)
        sky_bodies['planet1'].pos = vec(
            15*cos(10*t)+7.5 + sin(t),
            10*sin(10*t) + cos(t),
            0)
        sky_bodies['planet2'].pos = vec(
            25*cos(5*t)+12.5,
            15*sin(5*t),0)
    
        
if __name__ == '__main__':
    main()
