from vpython import *
import json

def main():
    t = 0
    stars = {}
    
    with open('two_bodies') as data:   
        for i in json.loads(data.read()).items():
            stars.update(
                {i[0] : sphere(
                    pos = eval(i[1]['start']),
                    radius = float(i[1]['diameter'])/2,
                    mass = float(i[1]['mass']),
                    velocity = eval(i[1]['velocity']),
                    color = eval(i[1]['color']),
                    make_trail =True,
                    retain = 150
                    )})
        t = 0
        scene.follow(stars['star1'])
        while True:
            t += 1
            rate(15)
            stars['star1'].pos = stars['star1'].pos + stars['star1'].velocity
##            for i in stars.values():
##                acceleration = vec(0,0,0)
##                for j in stars.values():
##                    acceleration += mag(i.pos - j.pos)/(mag(i.pos))*norm(i.pos-j.pos)
##                    print(acceleration)
##                i.velocity = i.velocity + acceleration
##                print(i.velocity)
##                i.pos = i.pos + i.velocity 
##                print(i.pos)
        
if __name__ == '__main__':
    main()
