from vpython import *

def create_solar_system():
    mer_dist, mer_year = '120', '1/0.241'
    ven_dist, ven_year = '200', '1/0.66'
    ear_dist, ear_year = '400', '1'
    moon_dist, moon_year = '20', '1/0.07'
    mar_dist, mar_year = '600', '1/1.88'
    jup_dist, jup_year = '800', '1/11'
    sat_dist, sat_year = '950', '1/29'
    ura_dist, ura_year = '1100', '1/84'
    nep_dist, nep_year = '1250', '1/164'
    plu_dist, plu_year = '1500', '1/248'
    solar_system = {
        'sun' : {
            'radius' : 109.245/2,
            'volume' : 1303781,
            'mass' : 332837,
            'color' : color.yellow,
            'law' : 'vec(0,0,0)'},
        'mercury': {
            'radius' : 0.383/2,
            'volume' : 0.0562,
            'mass' : 0.0553,
            'color' : color.green,
            'law' : 'vec({0}*cos({1}*t),{0}*sin({1}*t),0)'.format(mer_dist,mer_year)},
        'venus' : {
            'radius' : 0.950/2,
            'volume' : 0.857,
            'mass' : 0.815,
            'period' : 1,
            'color' : color.white,
            'law' : 'vec({0}*cos({1}*t),{0}*sin({1}*t),0)'.format(ven_dist,ven_year)},
        'earth' : {
            'radius' : 1/2,
            'mass' : 1,
            'color'  : color.blue,
            'law' : 'vec({0}*cos({1}*t),{0}*sin({1}*t),0)'.format(ear_dist,ear_year)},
        'moon' : {
            'radius' : 0.2727,
            'volume' : 0.0203,
            'mass' : 0.0123,
            'color' : color.gray(0.5),
            'law' : 'vec({0}*cos({1}*t) + {2}*cos({3}*t),{0}*sin({1}*t) +{2}*sin({3}*t) ,0)'.format(ear_dist,ear_year,moon_dist,moon_year)},
        'mars' : {
            'radius' : 0.532/2,
            'volume' : 0.151,
            'mass' : 0.107,
            'color' : color.red,
            'law' : 'vec({0}*cos({1}*t),{0}*sin({1}*t),0)'.format(mar_dist,mar_year)},
        'jupiter' : {
            'radius' : 10.973/2,
            'volume' : 1321,
            'mass' : 317.83,
            'color' : color.red,
            'law' : 'vec({0}*cos({1}*t),{0}*sin({1}*t),0)'.format(jup_dist,jup_year)},
        'saturn' : {
            'radius' : 9.14/2,
            'volume' : 764,
            'mass' : 95.159,
            'color' : color.yellow,
            'law' : 'vec({0}*cos({1}*t),{0}*sin({1}*t),0)'.format(sat_dist,sat_year)},
        'uranus' : {
            'radius' : 3.981/2,
            'volume' : 63.1,
            'mass' : 14.536,
            'color' : color.green,
            'law' : 'vec({0}*cos({1}*t),{0}*sin({1}*t),0)'.format(ura_dist,ura_year)},
        'neptun' : {
            'radius' : 3.865/2,
            'volume' : 57.7,
            'mass' : 17.147,
            'color' : color.blue,
            'law' : 'vec({0}*cos({1}*t),{0}*sin({1}*t),0)'.format(nep_dist,nep_year)},
        'pluto' : {
            'radius' : 0.181/2,
            'volume' : 0.0066,
            'mass' : 0.0022,
            'color' : color.white,
            'law' : 'vec({0}*cos({1}*t),{0}*sin({1}*t),0)'.format(plu_dist,plu_year)}
        }
    return(solar_system)

def main():
    t=0
    sky_bodies = {}
    solar_system = create_solar_system()

    for i in solar_system.items():
        sky_bodies.update({i[0] :
                           sphere(
                               pos = eval(i[1]['law']),
                               radius = i[1]['radius'],
                               color = i[1]['color'],
                               make_trail = True,
                               retain = 100)})
    

    while True:
        scene.camera.follow(sky_bodies['earth'])
        t += 0.01
        rate(30)
        
        for i in sky_bodies.items():
            i[1].pos = eval(solar_system[i[0]]['law'])
        
if __name__ == '__main__':
    main()
