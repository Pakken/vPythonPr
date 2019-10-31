#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8
import cgi,sys,os,cgitb, datetime
#from myvpython import earth_sat_func

cgitb.enable()

fields = (('fsat_mass',
		  'fsat_orb',
		  'fsat_vel'),
		  ('ssat_mass',
		  'ssat_orb',
		  'ssat_vel'),
		  ('lsat_mass',
		  'lsat_axel',
		  'lsat_fuel'))

def get_data():
	try:
		sats_data = {}
		for i in fields:
			vals = (form.getvalue(i[0]),
					  form.getvalue(i[1]),
					  form.getvalue(i[2]))
			if None in vals: raise KeyError
			sats_data[i[0].split('_')[0]] = {i[0]: float(vals[0]),
										i[1]: float(vals[1]),
										i[2]: float(vals[2])}
	except KeyError:
		htmlerror = '''
		<html>
		<title>ERROR IN DATA</title>
		<body>
		<form method=POST action="earth_sat_scene.py">
    		<table>
		    	<tr><th><b>Earth satellites</b></th></tr>
		    	<tr><th>First sat mass (417000) <td><input type="text" name='fsat_mass'></td></th></tr>
		  		<tr><th>First sat orbit radius (6700000)<td><input type="text" name="fsat_orb"></td></th></tr>
		  		<tr><th>First sat velocity (7746 km) <td><input type="text" name="fsat_vel"></td></th></tr>
				<tr><th>Second sat mass (3000)<td><input type="text" name="ssat_mass"></td></th></tr>
		  		<tr><th>Second sat orbit radius (42171000)<td><input type="text" name="ssat_orb"></td></th></tr>
		  		<tr><th>Second sat velocity (3074) <td><input type="text" name="ssat_vel"></td></th></tr>
		  		<tr><th>Launching sat mass (4000)<td><input type="text" name="lsat_mass"></td></th></tr>
		  		<tr><th>Launching sat acceleartion (100)<td><input type="text" name="lsat_axel"></td></th></tr>
		  		<tr><th>Launching sat fuel (30)<td><input type="text" name="lsat_fuel"></td></th></tr>
		    </table>
    		<input type="submit" value="Poehali!" name="action">
		</form>
		</body></html>
		'''
		print(htmlerror)
		return None
	else:
		return sats_data

def processing(sats_data):
	import vpython as vp
	from math import sin,cos,pi

	def gravi_force(obj):
	    difference = earth.pos - obj.pos
	    acceleration = (const_g/(vp.mag(difference)**2))*vp.norm(difference)
	    return acceleration

	def collision(obj):
		difference = obj.pos - earth.pos
		if vp.mag(difference) <= earth.radius:
			obj.visible = False
			obj.vel = vp.vec(0,0,0)



	earth_mass = 6*10**24
	G = 6.7*10**-11
	const_g = earth_mass*G
	earth_rad = 6371000
	t=0
	earth = vp.sphere(pos = vp.vec(0,0,0),
					  radius = earth_rad,
					  mass = earth_mass,
					  color = vp.vec(0,1,0)
					  )
	sats = {}
	sats['fsat'] = vp.cone(pos = vp.vec(sats_data['fsat']['fsat_orb'],0,0),
					    mass = sats_data['fsat']['fsat_mass'],
					    #vel = vp.vec(0,0,0),
					    vel = vp.vec(0,sats_data['fsat']['fsat_vel'],0),
						radius = 100,
						make_trail = True,
						retain = 500,
						color = vp.vec(1,0,0)
					    )
	sats['ssat'] = vp.cone(pos = vp.vec(-sats_data['ssat']['ssat_orb'],0,0),
					    mass = sats_data['ssat']['ssat_mass'],
					    #vel = vp.vec(0,0,0),
					    vel = vp.vec(0,sats_data['ssat']['ssat_vel'],0),
						radius = 100,
						make_trail = True,
						retain = 500,
						color = vp.vec(0,0,1)
					    )
	sats['lsat'] = vp.cone(pos = vp.vec(0,earth_rad+10000,0),
					  	mass = sats_data['lsat']['lsat_mass'],
					  	acceleration = sats_data['lsat']['lsat_axel']*vp.vec(0,0.7,0.7),
					  	fuel = sats_data['lsat']['lsat_fuel'],
					  	vel = vp.vec(0,0,0),
						radius = 5000,
						make_trail = True,
						retain = 500,
						color = vp.vec(1,1,1)
						)
	# vp.scene.follow(sats['lsat'])
	while True:
		vp.rate(24)
		for i in sats.values():
			collision(i)
			i.pos += i.vel
			if 'fuel' in i.__dict__:
				if i.fuel != 0:
					i.fuel -= 1
					i.vel += i.acceleration
			i.vel += gravi_force(i)

def htmlize(adict):
	new = adict.copy()
	for field in fieldnames:
		value = new[field]
		new[field] = cgi.escape(repr(value))
	return new

def main():
	global form
	a = None
	form = cgi.FieldStorage()
	action = form['action'].value if 'action' in form else None
	if action == 'Poehali!':
		a = get_data()
	if a  != None:
		processing(a)
	# processing(get_data())
	#print(replyhtml % htmlize(fields))

if __name__ == '__main__':
	main()