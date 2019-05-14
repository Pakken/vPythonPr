from vpython import *

def create_solar_system():
    solar_system = {
        'sun' : {
            'radius' : 10.245/2,
            'volume' : 1303781,
            'mass' : 332837,
            'color' : color.yellow},
        'mercury': {
            'radius' : 0.383/2,
            'volume' : 0.0562,
            'period' : 1,
            'color' : color.green},
        'venus' : {
            'radius' : 0.950/2,
            'volume' : 0.857,
            'mass' : 0.815,
            'period' : 1,
            'color' : color.white},
        'earth' : {
            'radius' : 1/2,
            'mass' : 1,
            'color'  : color.blue},
        'moon' : {
            'radius' : 0.2727,
            'volume' : 0.0203,
            'mass' : 0.0123,
            'color' : color.gray(0.5)},
        'mars' : {
            'radius' : 0.532/2,
            'volume' : 0.151,
            'mass' : 0.107,
            'color' : color.red}
        }

    for i in solar_system.items():
        sky_bodies.update({i[0] :
                           sphere(
                               pos = vec(0,0,0),
                               radius = i[1]['radius'],
                               color = i[1]['color'])})

def main():
    global sky_bodies
    sky_bodies = {}

    create_solar_system()

    for i in sky_bodies:
            print(i)
                      
    t = 0
    sky_bodies['sun'] = vec (0,0,0)
    while True:
        t += 0.01
        rate(24)
        sky_bodies['mercury'].pos = vec(15*cos(10*t),10*sin(10*t),0)
        sky_bodies['venus'].pos = vec(25*cos(5*t),15*sin(5*t),0)
        sky_bodies['earth'].pos = vec(35*cos(3*t),20*sin(3*t),0)
        sky_bodies['moon'].pos = vec(35*cos(3*t) + 1.5*cos(20*t),20*sin(3*t) +1*sin(20*t) ,0)
        sky_bodies['mars'].pos = vec(40*cos(2*t),25*sin(2*t),0)
    
        
if __name__ == '__main__':
    main()
