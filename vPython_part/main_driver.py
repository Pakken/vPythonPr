from vpython import *
import json

start_vec = (vec(0,0,0),vec(1500,1500,0))
radius = (20,300)
mass = (150,1000)
velocity = (vec(0,1,0), vec(0,0,0))
color = [vec(1,0,0), vec(0,0,1)]

def gravi_force(*,another_mass,myvec,another_vec):
    difference = myvec - another_vec

    acceleration = (another_mass/(mag(difference)**2))*norm(-difference)

    print('\t','ax = ', acceleration)
    print('\t', 'diff = ', difference)
    print('\t', 'mag = ', mag(difference))
    return acceleration

def collision(*, obj0, obj1):
    difference = obj0.pos - obj1.pos
    if mag(difference) < obj0.radius + obj1.radius:
        obj0.velocity = mag(obj0.velocity) * norm(difference + obj0.velocity)
        obj1.velocity = mag(obj1.velocity) * norm(-difference - obj1.velocity)



def main():
    t = 0
    stars = []
    for i in zip(start_vec,radius,mass,velocity,color):
        stars.append(sphere(
            pos = i[0],
            radius = i[1],
            mass = i[2],
            velocity = i[3],
            color = i[4],
            make_trail = True,
            retain = 1000))

    while True:
        t += 1
        rate(20)
        scene.follow(stars[1])
        print('Star0')
        # if mag(stars[0].pos - stars[1].pos) < stars[0].radius + stars[1].radius:
        #     stars[0].velocity = -stars[0].velocity
        #     stars[1].velocity = - stars[1].velocity
        collision(obj0 = stars[0], obj1 = stars[1])
        stars[0].velocity = stars[0].velocity + gravi_force(another_mass = stars[1].mass,
                                                            myvec = stars[0].pos,
                                                            another_vec = stars[1].pos)
        print('Star1')
        stars[1].velocity = stars[1].velocity + gravi_force(another_mass = stars[0].mass,
                                                            myvec = stars[1].pos,
                                                            another_vec = stars[0].pos)
        for i in stars:
            i.pos += i.velocity
    # t = 0
    # stars = {}
    
    # with open('two_bodies') as data:   
    #     for i in json.loads(data.read()).items():
    #         stars.update(
    #             {i[0] : sphere(
    #                 pos = eval(i[1]['start']),
    #                 radius = float(i[1]['diameter'])/2,
    #                 mass = float(i[1]['mass']),
    #                 velocity = eval(i[1]['velocity']),
    #                 color = eval(i[1]['color']),
    #                 make_trail =True,
    #                 retain = 150
    #                 )})
    #     t = 0
    #     scene.follow(stars['star1'])
    #     while True:
    #         t += 1
    #         rate(15)
    #         stars['star1'].pos = stars['star1'].pos + stars['star1'].velocity
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