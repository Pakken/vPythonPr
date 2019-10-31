#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8
import cgi,sys,os,cgitb, datetime, json
import vpython as vp
from math import cos,sin
#from myvpython import earth_sat_func

cgitb.enable()

def get_data(planet_file,moon_file):
	'''Функция для получения данных с формы, загрузки данных из переданных файлов
	 и пепедачи для дайльнейшей работы'''
	color = vp.color
	try:
		os.chdir('/home/pakke/Documents/Python3_projects/vPythonPr/cgi-bin')
		tplanet = form.getvalue('tplanet')
		planets = {}
		moons = {}
		with open(planet_file) as planet_data:
			for i in json.loads(planet_data.read()).items():
				planets.update(
					{i[0] : vp.sphere(
					pos = vp.vec(0,0,0),
					radius = float(i[1]['diameter'])/2,
					mass = float(i[1]['mass']),
					orbita = float(i[1]['orb_rad']),
					period = 1/float(i[1]['period']),
					moons = eval(i[1]['moons']),
					color = eval(i[1]['color']),
					make_trail =True,
					retain = 100
					)})
		with open(moon_file) as moon_data:
			for i in json.loads(moon_data.read()).items():
				moons.update(
					{i[0]: vp.sphere(
						pos = vp.vec(0,0,0),
						radius = float(i[1]['diameter'])/2,
						mass = float(i[1]['mass']),
						orbita = float(i[1]['orb_rad']),
						period = 1/float(i[1]['period']),
						color = eval(i[1]['color']),
						make_trail =True,
						retain = 100
					)})
		if tplanet not in planets: tplanet = 'earth'
	except KeyError:
		htmlerror = '''
		<html>
		<title>ERROR IN DATA</title>
		<body>
		<form method=POST action="solar_system_scene.py">
	    <table>
	    	<tr><th><b>Solar system (please type real planet)</b></th></tr>
	    	<tr><th>Input your the most liked planet (like Mars or Pluto): <td><input type="text" name="tplanet"></td></th></tr>
	    </table>
	    <input type="submit" value="Real" name="action">
	    <input type="submit" value="Visual" name="action">
		</body></html>
		'''
		print(htmlerror)
		return None
	else:
		return tplanet,planets,moons

def processing(val):
	tplanet,planets,moons = val
	t=0
	vp.scene.camera.follow(planets[tplanet])
	while True:
		t += 0.01
		vp.rate(30)
		for i in planets.values():
			i.pos = vp.vec(
				i.orbita*cos(i.period*t),
				i.orbita*sin(i.period*t),
				0)
			for j in i.moons:
				moons[j].pos = vp.vec(
					i.orbita*cos(i.period*t) + moons[j].orbita*cos(moons[j].period*t),
					i.orbita*sin(i.period*t) + moons[j].orbita*sin(moons[j].period*t),
					0)

def main():
	global form
	a = None
	form = cgi.FieldStorage()	
	action = form['action'].value if 'action' in form else None
	if action == 'Real':
		processing(get_data('solar_system_real_data_planets','solar_system_real_data_moons'))
	if action == 'Visual':
		processing(get_data('solar_system_visual_data_planets','solar_system_visual_data_moons'))
if __name__ == '__main__':
	main()